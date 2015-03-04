Heroku Connect Django Shop
=============================

A sample Django application that intergrates with Heroku Connect and Salesforce.

# Setup


Deploy with the Heroku Button -
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=)

  1. heroku run python manage.py createsuperuser
  1. Go to /admin/shop/products/add/ to create your first product


## Salesforce Intergration

  1. In SFDC create a new ExternalId field on Account
  2. Add your app to connect, you *MUST* use the public schema and *not* salesforce
  3. Configure Connect using connect_cfg.yml, this ensures you have mappings for all the Django salesforce models.
  4. Enable read/write and evented on all mappings
  5. Go to your [Store](http://yourapp.herokuapp.com/shop) and buy something fun, using any random values for checkout

Bonus, log into [Admin](http://yourapp.herokuapp.com/admin/salesforce) with username `admin` and password `default`
