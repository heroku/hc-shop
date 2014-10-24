class SalesforceRouter(object):
    """
    A router to control all database operations on models in the
    salesforce application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read salesforce models go to salesforce.
        """
        if model._meta.app_label == 'salesforce':
            return 'salesforce'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write salesforce models go to salesforce.
        """
        if model._meta.app_label == 'salesforce':
            return 'salesforce'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the salesforce app is involved.
        """
        if obj1._meta.app_label == 'salesforce' or \
           obj2._meta.app_label == 'salesforce':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the salesforce app only appears in the 'salesforce'
        database.
        """
        if db == 'salesforce':
            return model._meta.app_label == 'salesforce'
        elif model._meta.app_label == 'salesforce':
            return False
        return None
