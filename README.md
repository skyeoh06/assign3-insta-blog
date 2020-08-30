
# Code Institute Data Centric Development with Python
# **Insta-Blog-assign3**

## **Project Objectives**
1. As the idea of app to serve the community, gives me the inspiration to create an Insta-Blog app.
2. Insta- Blog is a short form for Instagram Blogs.
3. Mobile devices become an important assets for community/society nowadays, and what connect between us is the social networking platform
   such as Instagram, Facebook, Twitter,and etc.
4. Upload photo to the social networking with a thought summary about it has become a habits among the community/society.
5. This app is a platform for sharing an insta-blog from the users with other users among the community.
6. The main purpose of this platform is to bring a warm and positive inspiration energy among the community by sharing user inspiration
   thought from the photo that shared.
7. Impact of social media is so deeply mark into our daily life and mindset.
8. With an beautiful image and meaningful/inspiration blog will bring change/courage to the users to face the
   difficulties in life sometimes.

## **Deployed Link**

The process of deployed of this project was done with a new herokuapp. As the past deployed website was 
disconnect from github for an unknown cause.
Link to the working deployed website on heroku [here](https://sky-instablogs.herokuapp.com/).


## **UX/UI**
## **Overview and Color**
1. An image was choosen to be background of all page bring the idea that this is an Insta website.(Photo mainly).
2. The Navbar was created with closed(toggle in) or open(toggle out) effect from javascript for user able to view a wide and clear navigation bar in any mobile device and 
   Electronic devices.
3. The Register and login features is placed on the right top of each page that can be easy access by user regardless which page they currently browsing at.
4. Google font Playfair+Display was choosen as it's large size font effect will be view clear from small to large screens devices by users.
5. Color was choose based compability effect to have attractive effect for user browsing.

## **User Stories**
1. The User, as a Insta-blog inspirator, would like to create his/her inspiration Insta-Blog start with register an account in the webpage.
2. The User will be able to register an account on this website.
3. As logged in Users, he/she can create /update or delete the Insta-Blog with his/her own user account.
4. The User with /without register account, will be able to browse through all the list of Insta-Blog in the webpage.
5. The User with /without register account, can look for title of Insta-blog that wish to browse by search with a keyword.
6. The User wwith /without register account, can view the details of selected Insta-Blog.

## **Wireframes**
The wireframes was created with the use of AdobeXD and it can be view [here](https://github.com/skyeoh06/assign3-insta-blog/blob/master/document/assign3-insta-blog.pdf).

## **Features**
## **Index/Home Page**
1. Features that draws the User Attention.
* The background was placed with a full page image as a bright spot to attract user attention.
* Two Clear Idea of What is Insta-Blog was placed in the Home/Index page for user understanding.

2. Features that allow user easily navigate to other page in the website.
* A full wide navbar with toggle in / out effect was placed on the left side of the webpage.
* Register, Login/Logout and User email Info was placed in easy spot by user area which is right top of each page.

3. Features for user Notifcations.
* A flash message will be prompt to user upon success of process such as "create blog successfully, logged In successfully,
  etc.
* Info about total of posted Insta-Blog will be shown on the Top of HomePage.


## **Create Page**
1. User Creation features
* As a login user, he/she can create a new Insta-Blog with her own account by fill in all the field of the form and click on submit
  to upload the Insta-Blog to the database.
* User that do not login in this website first, will be redirect to the login page. A Login button was placed for user with existing account can login
 to the website while register button is for new user to register their accounts.

## **View Page**
1. User browsing features
*  User with or without logged in first, can view all the current posted Insta-Blog in the website.
*  User with or without logged in first, can view the thought content of the Insta-Blog by click on the Details link.
*  As a login Userm, he/she can edit/delete his own posted Insta-Blog.


## **Search Page**
1. User Search features
* User with or without logged in first, can search the Insta-Blog with fill in the keyword for the title of the Insta-Blog.
* Upon User successfully submit the form, he/she will be redirect to a results page with a scroll down list of Insta-Blog that matched.
* User will be notify with total of matched Insta-Blog on top of the Results page.

## **Register Page**
1. User Registration features
* User will be redirect to "Register" form page when clicking on the register button.
* User required to fill in correct format of info of each field for successfully submit register form.

## **Login/Logout Page**
1. User Login features
* With an valid user account in the webite, user can login to the website by clicking on the login form.
* As a registered user, he/she required to fill in matching email and password for login form submission.
* As a login user, he/she will able to see their email id and logout button on top right of the Website.

## **Technologies Used**
The technologie that involved in this project are:
The technologies used for this project are:
1. [Flask (Release 1.1.2)](https://flask.palletsprojects.com/en/1.1.x/)  
Flask is the microweb framework that supports and serves the web applications (services). It provides the logic and controls the database access,
view templates and session management to the client. Flask is written in python and it is the main project requirement.
2. [Python (Release 3.8.3)](https://www.python.org/downloads/release/python-383/)  
Python is the programming language used in Flask.
3. [HTML5](https://html.spec.whatwg.org/)  
HTML is the markup language that structures the webpage documents.
4. [CSS3](https://www.w3.org/TR/2001/WD-css3-roadmap-20010523/)  
CSS is the style sheet language that supports the presentation of document written in HTML.
5. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)  
Jinja is leveraged by Flask as its template engine. Although HTML is still needed to structure the web documents, Jinja dynamizes the web documents.
6. [Javascript and JQuery](https://developer.oracle.com/sg/javascript/)  
Javascript and Jquery is used primarily to do DOM manipulation and it is the main engine to serve interactivity and event handling to the webpages. 
7. [Gitpod](https://www.gitpod.io/)  
Gitpod is an online IDE that can be launched in Github. It is used to develope and write the code for this project.
8. [Git and Github](https://github.com/)  
Github is an online hosting service for software development that utilizes Git for version control.
9. [PYMongo Release 3.10.1](https://pymongo.readthedocs.io/en/stable/)  
Pymongo is a Python driver for MongoDB. It is the engine that allows Flask to interface to MongoDB.
10. [Cloudinary](https://cloudinary.com/)
Cloudinary is used for its cloud-based image and video management platform to enhance user experience in this project's profile registration process.
11. [Google Fonts](https://fonts.google.com/)
Google Font Playfair+Display is used as the content font in the HTML documents in this projects. 
12. [Bootstrap](https://www.bootstrapcdn.com/) is used for create, update process form.

## **Database**
* MongoDB is the database that used for this project. It is a cross platform document oriented database program.
* MongoDB is classified as a NoSQL (non relational) database that stored data in JSON-like format.
* MongoDB has a complete managed cloud database service named MongoDB Atlas.
* This project is based on MongoAtlas services.

## **Database**
* A simple ERD diagram of data structure illustration is [here](https://github.com/skyeoh06/assign3-insta-blog/blob/master/document/assign3-ERD.pdf).
* The explanation of the database structure is [here](https://github.com/skyeoh06/assign3-insta-blog/blob/master/database_structure.md).
https://materializecss.com/getting-started.html /) The project uses the materializecss for search form format.


## **Testing**
Testing result as [testing](https://github.com/skyeoh06/assign3-insta-blog/blob/master/tests.md)

## **Deployment**
Running the project locally
This project is build using Gitpod. The steps I went through to run the project locally are as follows:

1. Sign up for a MongoDB Atlas account here
2. Follow the steps to creating an Atlas cluster here
3. Install the gitpod extensions for the local machine browser.
4. Sign up for a github account and login.
5. Sign up for a gitpod account and link it to github account.
6. Go to the own github account page and start a new repository using the Code Institute Gitpod Full Template
7. The project folder will be available on the personal github page repository.
8. At the top right of the personal repository, you will be able to see the green coloured Gitpod button.
9. Click on the Gitpod link to open up the development environment for this project in Gitpod.
10. Once the project has fully loaded in the browser, a Visual Studio Code-like editor with a terminal will be seen.
11. In the terminal, type in the below command to install the dependencies.
$ pip3 -r requirements.txt 
12. In the main directory of the gitpod project, an .env file have to be created. In the .env file the following environment variables have to be setup.
a. MONGO_URI = mongodb+srv://[database_root_username]:[database_root_user_password]@[cluster_name].mongodb.net/[database_name]?retryWrites=true&w=majority
The above is just an example mongodb connection string. The string can be found in the mongodb atlas connection in each project folder created.
b. SECRET_KEY = a random string generated from any random key generator sites
c. CLOUD_NAME = cloudinary name provided when signed up for cloudinary account.
d. UPLOAD_PRESET = cloudinary upload preset.
e. API_SECRET = api secret provided by cloudinary.
f. API_KEY = api key provided by cloudinary.

13. Finally, run the app on the terminal / command line interface by typing the below into the terminal like so:
$ python3 app.py

## **Deployment on Heroku**

The steps taken to deploy this project on Heroku are as follows:

1. Sign up for Heroku account
2. Install Heroku CLI in the gitpod terminal if it hasn't been installed
3. Upon success installed, access heroku login as below
$ heroku login
4. Login Heroku via the opened browser. If browser window is not able to display, open the site in a new window and login heroku.
5. Type in the below to create a heroku app, where <the_name_of_the_project> is the name of the project to be deployed.
$ heroku create <name_of_the_project>
6. Create a remote repository by typing in
$ git remote -v
7. Install gunicorn with pip3
$ pip3 install gunicorn
8. Create a Procfile with the content "web gunicorn <name of the project>:app"
9. Freeze all project dependencies by keying in to the terminal
$ pip3 freeze --local > requirements.txt 
10. Commit the project to github again
11. Finally push the project to git as below:
$ git push heroku master
12. Before opening the deployed project url, the same environment variables like the local deployment have to be set up. To do that, in the terminal, type the following (the empty strings have to be filled in with the appropriate variable):
$ heroku config:set MONGODB_URI='mongodb+srv://...'
$ heroku config:set SECRET_KEY=''
$ heroku config:set CLOUD_NAME=''
$ heroku config:set API_KEY=''
$ heroku config:set API_SECRET=''
$ heroku config:set UPLOAD_PRESET=''
13. Finally, the deployed url can be accessed from Heroku dashboard in their website : https://dashboard.heroku.com/apps/projectname where the [project name] is the name of the deployed project via an 'Open App" button on the dashboard, else the deployed link can also be found in the terminal message just right after executing step 11.

## **Credits**
**(1) Content**

Info on [cloudinary] https://cloudinary.com/

Info on [mongodb]https://www.mongodb.com/



**(2) Media**
The image was search from [google](http://www.google.com )

**(3) Acknowledgements**
Get the idea of how platform look likes from Instagram #dailywebdesing
Some code info from 

[codexworld]https://www.codexworld.com/ 

[w3schools]https://www.w3schools.com/
