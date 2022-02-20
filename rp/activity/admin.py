from django.contrib import admin
from rp.activity.models import Activity
from reversion.admin import VersionAdmin


@admin.register(Activity)
class ActivityAdmin(VersionAdmin):
    list_display = (
        "name",
        "code",
        "description",
        "start_date_pretty",
        "end_date_pretty",
    )
    list_filter = ("start_date", "end_date")
    search_fields = ("name",)
