import datetime

import pytz
from django.conf import settings
from django.db.models import Q
from django_ical.views import ICalFeed

from RIGS import models


class CalendarICS(ICalFeed):
    """
    A simple event calender
    """
    # Metadata which is passed on to clients
    product_id = 'RIGS'
    title = 'RIGS Calendar'
    timezone = settings.TIME_ZONE
    file_name = "rigs.ics"

    # Cancelled = 'cancelled' = False
    # Dry Hire = 'dry-hire' = True
    # Non Rig = 'non-rig' = True
    # Rig = 'rig' = True
    # Provisional = 'provisional' = True
    # Confirmed/Booked = 'confirmed' = True

    def get_object(self, request, *args, **kwargs):
        params = {}

        params['dry-hire'] = request.GET.get('dry-hire', 'true') == 'true'
        params['non-rig'] = request.GET.get('non-rig', 'true') == 'true'
        params['rig'] = request.GET.get('rig', 'true') == 'true'

        params['cancelled'] = request.GET.get('cancelled', 'false') == 'true'
        params['provisional'] = request.GET.get('provisional', 'true') == 'true'
        params['confirmed'] = request.GET.get('confirmed', 'true') == 'true'

        return params

    def description(self, params):
        desc = "Calendar generated by RIGS system. This includes event types: " + ('Rig, ' if params['rig'] else '') + (
            'Non-rig, ' if params['non-rig'] else '') + ('Dry Hire ' if params['dry-hire'] else '') + '\n'
        desc = desc + "Includes events with status: " + ('Cancelled, ' if params['cancelled'] else '') + (
            'Provisional, ' if params['provisional'] else '') + ('Confirmed/Booked, ' if params['confirmed'] else '')

        return desc

    def items(self, params):
        # include events from up to 1 year ago
        start = datetime.datetime.now() - datetime.timedelta(days=365)
        filter = Q(start_date__gte=start)

        typeFilters = Q(pk=None)  # Need something that is false for every entry

        if params['dry-hire']:
            typeFilters = typeFilters | Q(dry_hire=True, is_rig=True)

        if params['non-rig']:
            typeFilters = typeFilters | Q(is_rig=False)

        if params['rig']:
            typeFilters = typeFilters | Q(is_rig=True, dry_hire=False)

        statusFilters = Q(pk=None)  # Need something that is false for every entry

        if params['cancelled']:
            statusFilters = statusFilters | Q(status=models.Event.CANCELLED)
        if params['provisional']:
            statusFilters = statusFilters | Q(status=models.Event.PROVISIONAL)
        if params['confirmed']:
            statusFilters = statusFilters | Q(status=models.Event.CONFIRMED) | Q(status=models.Event.BOOKED)

        filter = filter & typeFilters & statusFilters

        return models.Event.objects.filter(filter).order_by('-start_date').select_related('person', 'organisation',
                                                                                          'venue', 'mic')

    def item_title(self, item):
        title = ''

        # Prefix title with status (if it's a critical status)
        if item.cancelled:
            title += 'CANCELLED: '

        if not item.is_rig:
            title += 'NON-RIG: '

        if item.dry_hire:
            title += 'DRY HIRE: '

        # Add the rig name
        title += item.name

        # Add the status
        title += f' ({item.get_status_display()})'

        return title

    def item_start_datetime(self, item):
        return item.earliest_time

    def item_end_datetime(self, item):
        # if isinstance(item.latest_time, datetime.date):  # Ical end_datetime is non-inclusive, so add a day
        #    return item.latest_time + datetime.timedelta(days=1)
        return item.latest_time

    def item_location(self, item):
        return item.venue

    def item_description(self, item):
        # Create a nice information-rich description
        # note: only making use of information available to "non-keyholders"

        tz = pytz.timezone(self.timezone)

        desc = f'Rig ID = {item.display_id}\n'
        desc += f'Event = {item.name}\n'
        desc += 'Venue = ' + (item.venue.name if item.venue else '---') + '\n'
        if item.is_rig and item.person:
            desc += 'Client = ' + item.person.name + (
                (' for ' + item.organisation.name) if item.organisation else '') + '\n'
        desc += f'Status = {item.get_status_display()}\n'
        desc += 'MIC = ' + (item.mic.name if item.mic else '---') + '\n'

        desc += '\n'
        if item.meet_at:
            desc += 'Crew Meet = ' + (
                item.meet_at.astimezone(tz).strftime('%Y-%m-%d %H:%M') if item.meet_at else '---') + '\n'
        if item.access_at:
            desc += 'Access At = ' + (
                item.access_at.astimezone(tz).strftime('%Y-%m-%d %H:%M') if item.access_at else '---') + '\n'
        if item.start_date:
            desc += 'Event Start = ' + item.start_date.strftime('%Y-%m-%d') + (
                (' ' + item.start_time.strftime('%H:%M')) if item.has_start_time else '') + '\n'
        if item.end_date:
            desc += 'Event End = ' + item.end_date.strftime('%Y-%m-%d') + (
                (' ' + item.end_time.strftime('%H:%M')) if item.has_end_time else '') + '\n'

        desc += '\n'
        if item.description:
            desc += f'Event Description:\n{item.description}\n\n'
        # if item.notes:  // Need to add proper keyholder checks before this gets put back
        #     desc += 'Notes:\n'+item.notes+'\n\n'

        desc += f'URL = https://rigs.nottinghamtec.co.uk{item.get_absolute_url()}'

        return desc

    def item_link(self, item):
        # Make a link to the event in the web interface
        return item.get_absolute_url()

    def item_updated(self, item):  # some ical clients will display this
        return item.last_edited_at

    def item_guid(self, item):  # use the rig-id as the ical unique event identifier
        return item.pk
