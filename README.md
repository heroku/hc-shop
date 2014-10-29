Heroku Connect Django Shop
=============================

A sample Django application that intergrates with Heroku Connect and Salesforce.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=)

  1. Add your app to connect, you *MUST* use the public schema and *not* salesforce
  2. Configure Connect using connect_cfg.yml, this ensures you have mappings for all the Django salesforce models.
  3. Enable read/write and evented on all mappings
  4. In SFDC create a new ExternalId field on Account
  5. Go to your [Store](http://yourapp.herokuapp.com/shop) and buy something fun, using any random values for checkout

Bonus, log into [Admin](http://yourapp.herokuapp.com/admin/salesforce) with username `admin` and password `default`

If you didn't use the Deploy button before setting up connect, you will need to

 1. heroku apps:create [name]
 2. heroku addons:add heroku-postgresql
 3. heroku config:set SECRET_KEY=$(cat /dev/urandom | env LC_CTYPE=C tr -cd 'a-f0-9' | head -c 64)
 4. git push heroku
 5. heroku run postdeploy.sh
