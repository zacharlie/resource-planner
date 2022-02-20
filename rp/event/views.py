from django.shortcuts import render
from django.http import HttpResponse
from rp.activity.models import Activity
from rp.event.models import Event
from rp.resource.models import Resource
from django.views.generic import ListView, TemplateView
from datetime import date, timedelta, datetime
from json import dumps


class EventView(ListView):
    model = Event


class AvailabilityView(TemplateView):
    template_name = "visavail.html"

    # def get_context_data(self, request, *args, **kwargs):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.filter(resource=self.kwargs["resource_id"])
        resource = Resource.objects.filter(pk=self.kwargs["resource_id"])

        context["name"] = str(resource.values_list("name")[0][0]).title()

        activity_list = set(events.values_list("activity"))

        dataDictionary = {}

        for activity_pk in activity_list:
            activity_id = int(activity_pk[0])
            activity_name = Activity.objects.get(id=activity_id).name
            dict_element = {}
            dict_element["measure"] = activity_name
            dict_element["interval_s"] = 24 * 60 * 60
            entries = []
            for event in events.filter(activity=activity_id):
                start = event.start_date
                end = start + timedelta(hours=24)
                entry = [
                    start.strftime("%Y-%m-%d"),
                    1,
                    end.strftime("%Y-%m-%d"),
                ]
                entries.append(entry)
            dict_element["data"] = entries
            dataDictionary[activity_name] = dict_element

        dataArray = []

        for i in dataDictionary:
            dataArray.append(dataDictionary[i])

        context["data"] = dataArray

        # dataJSON = dumps(dataDictionary)
        # context["data"] = dataJSON

        # datetime.today()

        return context
