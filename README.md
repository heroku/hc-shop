Heroku Connect Django Shop
=============================

A sample Django application that intergrates with Heroku Connect and Salesforce.

# Deploy

Deploy with the Heroku Button -
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=)

## Salesforce Intergration
Once deployed you will need to setup Heroku Connect to talk to your Salesforce Org

  1. Use an existing Org or [setup a new Developer Org](https://developer.salesforce.com/signup)
  1. In SFDC create a new ExternalId field on Account
  2. Add your app to connect, you *MUST* use the public schema and *not* salesforce
  3. Configure Connect using connect_cfg.yml, this ensures you have mappings for all the Django salesforce models.
  4. Enable read/write and evented on all mappings
  5. Go to your [Store](http://yourapp.herokuapp.com/shop) and buy something fun, using any random values for checkout

Bonus, log into [Admin](http://yourapp.herokuapp.com/admin/salesforce) with username `admin` and password `default`


## Local Development

  1. mkvirtualenv env
  1. pip install -r requirements.txt
  1. cp env.example .env
  1. foreman run ./setup.sh
  1. foreman start
