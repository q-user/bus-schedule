import json
import requests
import itertools
import datetime

from django.urls import reverse
from django.views.generic import TemplateView


class DestinationsView(TemplateView):
    template_name = 'bus_schedule/destinations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open('../stations.json', 'r') as f:
            data = json.load(f)

        points = [item['point'] for item in data['stations']]
        p2p = set(itertools.combinations(points, 2))

        urls = [
            reverse(
                'bus_schedule:station-destination',
                kwargs={'station': str(x), 'destination': str(y)}
            )
            for x, y in p2p
        ]

        context.update({
            'urls': urls
        })
        return context


class StationDestinationView(TemplateView):
    template_name = 'bus_schedule/station-destination.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open('../stations.json', 'r') as f:
            data = json.load(f)
        point1 = kwargs.get('station')
        point2 = kwargs.get('destination')
        item = {}
        for i in data['stations']:
            if point1 == i['point']:
                item = i
                break

        page = requests.get(item['link'])
        j = json.loads(page.text)
        current_destination = []
        for i in j['data']:
            if point2 == i['allSegment']['destination']['point']['id']:
                current_destination.append(i['allSegment'])
        context.update({
            'current_destination': current_destination
        })
        return context
