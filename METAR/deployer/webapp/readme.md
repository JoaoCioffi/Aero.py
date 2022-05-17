# Deployment on Heroku

At this point, you have a functioning web app running on your local machine. However, it is hard to share this — your machine might be behind a firewall, your IP address might change often or the machine isn’t always on. Luckily, it’s possible to deploy flask apps to an online platform that will make it much easier for people to access your app.

* Sign up for a free Heroku account at https://signup.heroku.com/signup/dc
* Make sure you have git installed, to push your app to Heroku.
* Install the Heroku CLI tool (https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

## Make a git repository for your web app
Inside the webapp folder, run the following to create a new repository.
```
git init
```

## Authenticate with Heroku
Once this is done, you can log into your Heroku account using the CLI
```
heroku login
```

## Create a new Heroku app
```
heroku create
```

By default, this will make an app with a random name. If you want to choose your own name, simply pass it as an argument. For example:
```
heroku create bike-model
```

## Create the required Heroku files
You will need two files, placed inside the webapp folder.

1- requirements.txt - this tells Heroku which packages to install for your web app. It should look like this:
- flask
- pandas
- gunicorn
- xgboost
