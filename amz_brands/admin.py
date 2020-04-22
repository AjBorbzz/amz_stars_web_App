from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Brand


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    pass
