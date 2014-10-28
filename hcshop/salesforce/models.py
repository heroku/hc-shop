from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from cartridge.shop.models import Order


class TriggerLog(models.Model):
    id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=40, blank=True)
    field_c5_source = models.CharField(db_column='_c5_source', max_length=40, blank=True)
    action = models.CharField(max_length=7, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    record_id = models.IntegerField(blank=True, null=True)
    values = models.CharField(max_length=16384, blank=True)
    state = models.CharField(max_length=8, blank=True)
    sf_result = models.IntegerField(blank=True, null=True)
    sf_message = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = '_trigger_log'


class Lead(models.Model):
    id = models.AutoField(primary_key=True)
    field_c5_source = models.CharField(db_column='_c5_source', max_length=18, blank=True)
    firstname = models.CharField(max_length=40, blank=True)
    lastmodifieddate = models.DateTimeField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=False)
    createddate = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=80, blank=True)
    lastname = models.CharField(max_length=80, blank=False)
    sfid = models.CharField(unique=True, max_length=18, blank=True, default=None)
    isdeleted = models.NullBooleanField()

    def __unicode__(self):
        return '{} - {}/{}'.format(self.email, self.id, self.sfid)

    @property
    def name(self):
        return ' '.join(self.firstname, self.lastname)

    class Meta:
        managed = False
        db_table = 'lead'


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    field_c5_source = models.CharField(db_column='_c5_source', max_length=18, blank=True)
    name = models.CharField(max_length=255, blank=False)
    accountnumber = models.CharField(max_length=40, blank=True)
    lastmodifieddate = models.DateTimeField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    sfid = models.CharField(unique=True, max_length=18, blank=True, default=None)
    isdeleted = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'account'

    def __unicode__(self):
        return '{} - {}/{}'.format(self.name, self.id, self.sfid)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    field_c5_source = models.CharField(db_column='_c5_source', max_length=18, blank=True)
    lastmodifieddate = models.DateTimeField(blank=True, null=True)
    firstname = models.CharField(max_length=40, blank=True)
    lastname = models.CharField(max_length=80, blank=False)
    email = models.CharField(max_length=80, blank=True)
    createddate = models.DateTimeField(blank=True, null=True)
    sfid = models.CharField(unique=True, max_length=18, blank=True, default=None)
    isdeleted = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'contact'

    def __unicode__(self):
        return '{} - {}/{}'.format(self.email, self.id, self.sfid)

    @property
    def name(self):
        return ' '.join(self.firstname, self.lastname)


@receiver(post_save, sender=Order, dispatch_uid='salesforce_order_post_save')
def order_post_save(sender, **kwargs):
    """ Anytime we get a new order lets create new SFDC objects too
    """
    order = kwargs.get('instance')
    email = order.billing_detail_email
    account, _ = Account.objects.get_or_create(name=email)

    # XXX link contact to account
    contact, _ = Contact.objects.get_or_create(email=email)

    return account, contact
