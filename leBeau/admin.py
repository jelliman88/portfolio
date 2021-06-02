
from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('item','purchase_date',)
    search_fields = ('item', 'purchase_price', 'purchase_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()




admin.site.register(Transaction, TransactionAdmin)


