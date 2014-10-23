from django.contrib import admin

from . import models


class LeadAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
admin.site.register(models.Lead, LeadAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(models.Account, AccountAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')

admin.site.register(models.Contact, ContactAdmin)
