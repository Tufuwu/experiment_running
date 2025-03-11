#!/usr/bin/env python3

# Copyright 2021 Google LLC
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
"""Executable and reusable sample for cancelling a retrohunt.

API reference:
https://cloud.google.com/chronicle/docs/reference/detection-engine-api#cancelretrohunt
"""

import argparse

from google.auth.transport import requests

from common import chronicle_auth
from common import regions

CHRONICLE_API_BASE_URL = "https://backstory.googleapis.com"


def cancel_retrohunt(http_session: requests.AuthorizedSession, version_id: str,
                     retrohunt_id: str):
  """Cancel a specific retrohunt.

  Args:
    http_session: Authorized session for HTTP requests.
    version_id: Unique ID of the detection rule to cancel a retrohunt for
      ("ru_<UUID>" or "ru_<UUID>@v_<seconds>_<nanoseconds>"). If a version
      suffix isn't specified we use the rule's latest version.
    retrohunt_id: Id of the retrohunt to cancel.

  Raises:
    requests.exceptions.HTTPError: HTTP request resulted in an error
      (response.status_code >= 400).
  """
  url = f"{CHRONICLE_API_BASE_URL}/v2/detect/rules/{version_id}/retrohunts/{retrohunt_id}:cancelRetrohunt"

  response = http_session.request("POST", url)
  # Expected server response:
  # {}

  if response.status_code >= 400:
    print(response.text)
  response.raise_for_status()


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  chronicle_auth.add_argument_credentials_file(parser)
  regions.add_argument_region(parser)
  parser.add_argument(
      "-vi",
      "--version_id",
      type=str,
      required=True,
      help="version ID ('ru_<UUID>[@v_<seconds>_<nanoseconds>]')")
  parser.add_argument(
      "-ri",
      "--retrohunt_id",
      type=str,
      required=True,
      help="retrohunt ID (for Retrohunts: 'oh_<UUID>')")

  args = parser.parse_args()
  CHRONICLE_API_BASE_URL = regions.url(CHRONICLE_API_BASE_URL, args.region)
  session = chronicle_auth.initialize_http_session(args.credentials_file)
  cancel_retrohunt(session, args.version_id, args.retrohunt_id)
