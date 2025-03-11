# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Unit tests for the "update_collector" module."""

import unittest
from unittest import mock

from google.auth.transport import requests

from . import update_collector


class UpdateCollectorTest(unittest.TestCase):

  @mock.patch.object(requests, "AuthorizedSession", autospec=True)
  @mock.patch.object(requests.requests, "Response", autospec=True)
  def test_http_error(self, mock_response, mock_session):
    mock_session.request.return_value = mock_response
    type(mock_response).status_code = mock.PropertyMock(return_value=400)
    mock_response.raise_for_status.side_effect = (
        requests.requests.exceptions.HTTPError())

    with self.assertRaises(requests.requests.exceptions.HTTPError):
      update_collector.update_collector(mock_session, "collector name")

  @mock.patch.object(requests, "AuthorizedSession", autospec=True)
  @mock.patch.object(requests.requests, "Response", autospec=True)
  def test_happy_path(self, mock_response, mock_session):
    mock_session.request.return_value = mock_response
    type(mock_response).status_code = mock.PropertyMock(return_value=200)
    expected_collector = {
        "name": "forwarders/{forwarderUUID}/collectors/{collectorUUID}",
        "displayName": "UpdatedCollector",
        "config": {
            "logType": "WINDOWS_DHCP",
            "maxSecondsPerBatch": 10,
            "maxBytesPerBatch": "1048576",
            "fileSettings": {
                "filePath": "/new/path/to/file.txt"
            }
        },
        "state": "ACTIVE"
    }

    mock_response.json.return_value = expected_collector

    actual_collector = update_collector.update_collector(
        mock_session, "collector name")
    self.assertEqual(actual_collector, expected_collector)


if __name__ == "__main__":
  unittest.main()
