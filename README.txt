Heroku Connect Django Shop
=============================

A sample Django application that intergrates with Heroku Connect and Salesforce.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=)

  1. Add your app to connect, you *MUST* use the public schema and *not* salesforce
  2. Configure Connect using connect_cfg.yml, this ensures you have mappings for all the Django salesforce models.
  3. Enable read/write and evented on all mappings
  4. In SFDC create a new ExternalId field on Account
  5. Go to your (Store)[http://yourapp.herokuapps.com/shop] and buy something fun, using any random values for checkout

Bonus, log into (Admin)[http://yourapp.herokuapps.com/admin/salesforce] with username `admin` and password `default`
