from django.contrib import admin
from django.db.models import Count
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from UI.models import System, Event, Node, Contract, Spread


# Register your models here.

@admin.register(System)
class SystemAdmin(ImportExportModelAdmin): ## << This is required in order to enable import/export in django admin
    pass

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin): ## << This is required in order to enable import/export in django admin
    pass

@admin.register(Contract)
class ContractAdmin(ImportExportModelAdmin): ## << This is required in order to enable import/export in django admin
    pass

@admin.register(Node)
class NodeAdmin(ImportExportModelAdmin): ## << This is required in order to enable import/export in django admin
    pass

@admin.register(Spread)
class SpreadAdmin(ImportExportModelAdmin): ## << This is required in order to enable import/export in django admin
    pass

admin.site.index_title = "Default Admin"
admin.site.site_header = "The Default Admin"
admin.site.site_title = "Default Site Title"
# admin.site.


# admin.site.register(Contract)
# admin.site.register(Node)
# admin.site.register(Spread)

# Admin site Attributes
# https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#adminsite-objects
# Admin Site Methods
# https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#adminsite-methods