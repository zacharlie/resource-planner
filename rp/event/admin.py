from django.contrib import admin
from rp.event.models import Event
from reversion.admin import VersionAdmin


@admin.register(Event)
class EventAdmin(VersionAdmin):
    list_display = (
        "name",
        "resource",
        "activity",
        "commit",
        "start_date_pretty",
        "end_date_pretty",
    )
    list_filter = ("start_date", "end_date")
    search_fields = ("name",)
