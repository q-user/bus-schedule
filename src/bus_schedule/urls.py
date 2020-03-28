from django.urls import path
from bus_schedule.views import StationDestinationView

app_name = 'bus_schedule'

urlpatterns = [
    path('<slug:station>--<slug:destination>', StationDestinationView.as_view(), name='station-destination')
]