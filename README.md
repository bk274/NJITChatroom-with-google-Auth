

                                                                           
1.	Install packages
a.	`pip install python-dotenv`
b.	`pip install flask-sqlalchemy`
c.	`pip install requests`
d.	`pip install psycopg2`
e.	`pip install flask-socketio`
f.	`pip install eventlet`
g.	`npm install`
h.	`pip install flask-socketio`    
i.	`npm install -g webpack`   
j.	`npm install --save-dev webpack`    
k.	`npm install socket.io-client –save`
l.	
 If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install` like in step 2 

2.      Setting up  PSQL
a.	Update yum: 
i.	    `sudo yum update`
        enter yes to all prompts    
b.	Upgrade pip:
i.	`sudo /usr/local/bin/pip install --upgrade pip`
c.	Get psycopg2: 
i.	`sudo /usr/local/bin/pip install psycopg2-binary`   
d.	Get SQLAlchemy: 
i.	`sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1`
e.	Install PostGreSQL: 
i.	`sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`    
Enter yes to all prompts.    
f.	Initialize PSQL database: 
i.	`sudo service postgresql initdb`
g.	Start PSQL: 
i.	`sudo service postgresql start`
h.	Make a new superuser: 
i.	`sudo -u postgres createuser --superuser $USER `
:warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
i.	Make a new database: 
i.	`sudo -u postgres createdb $USER`
:warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:        

        6. Make sure your user shows up:   
 a) `psql`     
 b) `\du` look for ec2-user as a user      
 c) `\l` look for ec2-user as a database    
Make a new user:    
   type `psql` 
(if you already quit out of psql)  
k.	   `create user [some_username_here] superuser password '[some_unique_new_password_here]';``  


	     `\q` to quit out of sql  
	     
3.	Enabling read/write from SQLAlchemy  
a.	Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`
	If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  
b.	Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
c.	 After changing those lines, run `sudo service postgresql restart`  
d.	Run sudo service postgresql start
e.	Ensure that `sql.env` has the username/password of the superuser you created


            4.	Run your awesome code 
                
a.	Make sure you are in the correct Directory cd/nameofdirectory
b.	`npm run watch`
c.	`python app.py`
d.  `sudo service postgresql start`
g.	go to browser http://localhost:8082


            5. Update the API key in the env file along with your username and password for yourdatabase
   a. Go to "https://rapidapi.com/KishCom/api/covid-19-coronavirus-statistics"
   b. Sign up and you will granted an API key
   c. copy and paste that key in sql.env
   d. Go to https://console.developers.google.com/ and create new project --> under credientials 
   e. Go to chatHeader.jsx and replace X with your own client id from google ||  this.clientId = "XXXXXXXXXXXXXXX"

6.	Deployment on Heroku

    a.	heroku login -i
                -  `heroku create`
    b.  `heroku addons:create heroku-postgresql:hobby-dev`
    c.	`heroku pg:wait`
                 `PGUSER=databasename heroku pg:push username DATABASE_URL`
                 `heroku pg:psql`
                 `DATABASE=> SELECT * FROM postgres;``
    e.	`psql`
    f.	`ALTER DATABASE postgres OWNER TO username2020`
    g.	``\du` 
    h.	`PGUSER=username2020`
    i.	`PGUSER=username2020 heroku pg:push postgres DATABASE_URL`
    j.	`heroku pg:psql`
    
    k.	`pip freeze > requirements.txt`
    
    l.	`create a procfile with web:python app.py`
    
    m.	Make sure to go in Heroku and add all the values from your env file 
    n.  `git push heroku master (if doesnt work try this a and b)``
    a.	`git checkout – masterbranch`
    b.	` git push heroku masterbranch`


    

Issues i Experienced during this project
1. Experienced an issue with my database where some of the files were not getting installed and i had to do the project in a different aws environment
2. Had an issue with when i signed into the app from another browser instead of it showing another user chat box, it displayed the same. I fixed that issue by adding {info[2]== setUser() && } which adds a new user everytime the page is loaded
3. I had an issue with scrolling down. Everytime a new message was entered the chat would not scroll to the buttom. Fixed that by adding in content.jsx file "this.ref= reactRef();" and "thiss.ref.currebt.scrolltop = this.ref.current.scrollHeight"
4. Had an issue with cross compatiblity with the styling from the css file that i had already and how i wanted the new google chatbot looking so i redid the styling.
5. Experienced an issue with heroku databse not loading, the fix for that issue was reseting dyno
6. Experienced an issue with my database not updating, i earased the user and added again, that fix the databases from not loading
7. With milestone i realized that when i do force push it deleted all of my previous commits and it will make it seem like i did not commit anything. Fix for that issue is never use force push
8. Experience issues with importing userame and password from env file because i had DATABASE_URL in the incorrect form. EXAMPLE  (DATABASE_URL='databasename://username:password@localhost/databasename')

python -m unittest tests.mocked_unit_tests tests.unmocked_unit_tests
coverage run -m unittest tests.unmocked_unit_tests tests.mocked_unit_tests -v
coverage report -m