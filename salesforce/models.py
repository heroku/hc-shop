# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.


from __future__ import unicode_literals

from django.db import models

class TriggerLog(models.Model):
    id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=40, blank=True)
    field_c5_source = models.CharField(db_column='_c5_source', max_length=40, blank=True) # Field renamed because it started with '_'.
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
    field_c5_source = models.CharField(db_column='_c5_source', max_length=18, blank=True) # Field renamed because it started with '_'.
    firstname = models.CharField(max_length=40, blank=True)
    lastmodifieddate = models.DateTimeField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True)
    createddate = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=80, blank=True)
    lastname = models.CharField(max_length=80, blank=True)
    sfid = models.CharField(unique=True, max_length=18, blank=True)
    id = models.IntegerField(primary_key=True)
    isdeleted = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'lead'


class Account(models.Model):
    field_c5_source = models.CharField(db_column='_c5_source', max_length=18, blank=True) # Field renamed because it started with '_'.
    name = models.CharField(max_length=255, blank=True)
    accountnumber = models.CharField(max_length=40, blank=True)
    lastmodifieddate = models.DateTimeField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    sfid = models.CharField(unique=True, max_length=18, blank=True)
    id = models.IntegerField(primary_key=True)
    isdeleted = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'account'


class Contact(models.Model):
    field_c5_source = models.CharField(db_column='_c5_source', max_length=18, blank=True) # Field renamed because it started with '_'.
    lastmodifieddate = models.DateTimeField(blank=True, null=True)
    firstname = models.CharField(max_length=40, blank=True)
    lastname = models.CharField(max_length=80, blank=True)
    email = models.CharField(max_length=80, blank=True)
    createddate = models.DateTimeField(blank=True, null=True)
    sfid = models.CharField(unique=True, max_length=18, blank=True)
    id = models.IntegerField(primary_key=True)
    isdeleted = models.NullBooleanField()
    class Meta:
        managed = False
        db_table = 'contact'

