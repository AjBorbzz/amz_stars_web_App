from django.contrib import admin

from .models import FeedbackRemoval


class FeedbackRemovalAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'product_name', 'case_id',
                    'order_id', 'reason_for_removal', 'created_date', 'updated_date', 'username')
    display_links = ('brand_name', 'case_id')
    search_fields = ('reason_for_removal', 'case_id', 'order_id')


admin.site.register(FeedbackRemoval, FeedbackRemovalAdmin)
