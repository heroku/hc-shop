from django.contrib import admin

from . import models


class TriggerLogAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'state', 'table_name', 'action', 'values')
    search_fields = ('table_name', 'values')
    list_filter = ('state', 'action')
admin.site.register(models.TriggerLog, TriggerLogAdmin)


class LeadAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
    search_fields = ('firstname', 'lastname', 'email')
admin.site.register(models.Lead, LeadAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'accountnumber')
    search_fields = ('name', 'accountnumber')
admin.site.register(models.Account, AccountAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
    search_fields = ('firstname', 'lastname', 'email')
admin.site.register(models.Contact, ContactAdmin)
