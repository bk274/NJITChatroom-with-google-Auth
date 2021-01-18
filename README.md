NJIT ChatRoom
---
[Click here for a live deployment of the NJIT Chatrooom !](https://njit-chatroom.herokuapp.com/)
![Screenshot](screenshot.JPG)



s. To launch the app run the command `npm run build` to update your script.js and then run `python app.py` in order to run the app. If running `npm run build` asks you if you want to install `webpack-CLI` respond 'yes'.

# Installations and Technologies.
Before running this app, make sure you have all of the dependencies installed. All the dependencies are in the `requirements.txt` file, but all of these packages are not necessary.
1. Use the command `pip install` to install flask, coverage, pylint, pytz, black, tweepy, pyopenstates, and flask-socketio.
2. Use `npm` to install the heroku package, `npm install -g heroku`
3. It's recommended that you use the `Git CLI` in order to keep your code up to date.

## Database Setup
This web application uses `psql` as the database to provide persistence with the bulletin boards. In order to get psql to work with python, run the following commands:
1. `sudo yum update`, say yes for all the prompts.
2. `sudo pip install --upgrade pip`
3. `sudo pip install psycopg2-binary`
4. `sudo pip install Flask-SQLAlchemy==2.1`

If you have not already created a psql database, follow these steps in order to initialize one.

1. `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`, Enter yes to all prompts.    
2. `sudo service postgresql initdb`  
3. `sudo service postgresql start`    
4. Make a new superuser: `sudo -u postgres createuser --superuser $USER` 
5. Make a new database: `sudo -u postgres createdb $USER`   
6. Make sure your user shows up and make a new one:    
	1. `psql`    
	2. `\du` look for yourself as a user    
	3. `\l` look for yourself as a database 
	4. `create user [some_username_here] superuser password '[password]';` 
	5. Make sure you remember the quotes around password and the semicolon. 
		1. Check `\du` to ensure it worked.
	6. `\q` to quit out of psql

## API Keys
In order to get the modules to work correctly, you will need to register and obtain a few API Keys.


Create a file named `.env` and set it up as the following:
```

DATABASE_URL=<URL to your psql database>

```

Note: Do not include quotes or the `<>` characters in the `.env` file.\
Optional, but you can run the command `source .env` to ensure the system has read the API Key variables.

## Setting up the clientside
There are a few commands you must run in order to ensure that the clientside will run properly.
1. `npm install`
3. `npm install -g webpack`
4. `npm install webpack@next --dev`
5. `npm install --save-dev webpack`




## Setting up testcases
If you wish to utilize test cases, enter the following commands to ensure you have the correct modules:
1. `pip install unittest`
2. `pip install requests_mock`

In order to run these tests, run `python unmocked_unit_tests.py` and `python mocked_unit_tests.py` to test the test cases in those files.

In order to view the code coverage, run the following commands in the directory:
1. `coverage run -m --source=. unittest tests/*.py`
2. `coverage html`
3. In the future, you can simply run ``coverage run -m --source=. unittest tests/*.py && coverage html`` to run both of these commands at the same time.

### Linting
If you wish to check the linting on this project, execute the following commands.
1. `pip install pylint`
2. `pip install black`
3. `npm install -g eslint`
4. `eslint --init`, select the following options.
	1. "To check syntax, find problems, and enforce code style"
	2. "Javascript modules (import/export)"
	3. "React"
	4. "No"
	5. "Browser"
	6. "Use a popular style guide"
	7. "Airbnb"
	8. "Javascript"
	9. When asked if you want to install dependencies with npm, say "Yes"
5. Run `eslint scripts/[FILE]` on any of the `.js/.jsx`  files in the scripts directory.
	1.  Run `eslint --fix scripts/[FILE]` in order to automatically fix some of the linting errors
6. Run `pylint [FILE]` on any of the python files.

### Heroku Deployment
   If you wish to deploy to heroku, log into heroku on your command line and run the 
      following commands to move your database over:
        0. If you do not already have a heroku project: `heroku create` and add your 
          keys to the config variables.
        1. `heroku addons:create heroku-postgresql:hobby-dev`
        2. `heroku pg:wait`
        3. `heroku pg:push postgres DATABASE_URL`
        4. `git push heroku master`


	1. Edit Proposal
	2. Establish and continuously update Kanban Board
	3. Work on the style of the site.
	4. Add content to the landing page.
	5. Find bugs and report them to the person who's work it applies to.
	6. Lint and test one anothers code.

## Technical Issues and Solutions
	1. Experienced an issue with my database where some of the files were not getting installed and i had to do the project in a different aws environment
	2. Had an issue with when i signed into the app from another browser instead of it showing another user chat box, it displayed the same. I fixed that issue by adding {info[2]== setUser() && } which adds a new user everytime the page is loaded
	3. I had an issue with scrolling down. Everytime a new message was entered the chat would not scroll to the buttom. Fixed that by adding in content.jsx file "this.ref= reactRef();" and "thiss.ref.currebt.scrolltop = this.ref.current.scrollHeight"
	4. Had an issue with cross compatiblity with the styling from the css file that i had already and how i wanted the new google chatbot looking so i redid the styling.
	5. Experienced an issue with heroku databse not loading, the fix for that issue was reseting dyno
	6. Experienced an issue with my database not updating, i earased the user and added again, that fix the databases from not loading
	7. With milestone i realized that when i do force push it deleted all of my previous commits and it will make it seem like i did not commit anything. Fix for that issue is never use force push
	8. Experience issues with importing userame and password from env file because i had DATABASE_URL in the incorrect form. EXAMPLE  (DATABASE_URL='databasename://username:password@localhost/databasename')
	9. Issues with mocking database, i was able to get around it by app.db.session.execute", self.mocked_session_execute



