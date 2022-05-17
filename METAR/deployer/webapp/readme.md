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
heroku create your-model-name
```

## Create the required Heroku files
You will need two files, placed inside the webapp folder.

1. requirements.txt - this tells Heroku which packages to install for your web app. It should look like this:
- flask
- pandas
- gunicorn
- xgboost

2. Procfile - this tells Heroku what kind of app you are running and how to serve it to users. It is a single line and should look like this:
```
web: gunicorn app:app
```
Your web app folder should now look like this:
```
webapp/
    ├── model/
    │   └── your_model.pkl
    ├── templates/
    │   └── main.html
    ├── requirements.txt
    ├── Procfile
    └── app.py
```

## Add files to repository
While in the webapp folder, use the following command to add all your web app's files to the git repository:
```
git add .
git commit -m "First commit!"
```

## Set the remote destination for pushing from git to Heroku

This command makes it easier to push your local web app to Heroku, using git. You should change bike-model to whatever you named your Heroku app when you created it.

```
heroku git:remote -a your-model-name
```

## Push your app to the web

Just one more command and your web app will be online. During this process, Heroku will upload your app files, install the packages it needs and start the app running.

```
git push heroku master
```

If everything goes as expected, you’ll see output showing things being installed and uploaded.
