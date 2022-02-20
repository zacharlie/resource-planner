from django.contrib import admin
from rp.resource.models import Resource
from reversion.admin import VersionAdmin


@admin.register(Resource)
class ResourceAdmin(VersionAdmin):
    list_display = (
        "id",
        "name",
        "surname",
        "comment",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "surname",
    )
