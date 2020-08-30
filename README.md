
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
The wireframes was created with the use of AdobeXD and it can be view [here].

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
* The explanation of the database structure is [here].
3.Layout Draft
The Draft of layout and ER diagram for relationships collection of database can be view in this folder link:
[layout](https://github.com/skyeoh06/assign3-insta-blog/tree/master/static/draft)

## **Features**
1.Existing Features
* Button click function
* Form
* Flash
* The webpage is mobile-friendly and reponsive.

2.Additional Features to be implemented in the future.
*searcable with different attribute.

## **Technologies Used**
## **Technologies Used**
1. HTML5 (https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5): The project uses HTML5 to structure the layout of the website.

2. CSS (https://developer.mozilla.org/en-US/docs/Web/CSS): The project uses CSS to add the stylistic designs to the webpages.

3. Bootstrap (https://getbootstrap.com/docs/4.3/getting-started/introduction/): The project uses the Bootstrap framework to make structuring and styling of the webpages easier

4. GoogleFonts (https://fonts.google.com/) The project uses GoogleFonts to style the typography used in the heading, paragraphs and buttons of the website.

5. Color Picker (https://www.google.com/search?q=color+picker) The Project uses Color picker to style the background image and font color for comfortable view.

6. JQuery (https://code.jquery.com/) The Projects uses Jquery library for toggle effect of navbar.

7. Materialize (https://materializecss.com/getting-started.html /) The project uses the materializecss for search form format.

8. Jinja (https://jinja.palletsprojects.com/en/2.11.x/) The project uses jinja code for data access with MONGO database.

9. Upload -widget cloudinary (https://widget.cloudinary.com/) The project uses this features for photo database and CRUD.

10. MONGODD (https://www.mongodb.com/) The database platform for this project.

11. Python (https://www.python.org/) The project uses features of python language for each features of the webpage.

12. Heroku (https://www.heroku.com/) The project uses heroku for webpage deployment.

## **Testing**
Testing result as below folder:
[testing](https://github.com/skyeoh06/assign3-insta-blog/tree/master/testing)

## **Deployment**
This site is hosted using GitHub pages, editing in gitpod. Github link [here](https://github.com/skyeoh06/assign3-insta-blog)

It is deploy in herokuapp. 

There is not difference for deployment version and development version.

## **Credits**
**(1) Content**

Info on cloudinary from https://cloudinary.com/

Info on mongodb from https://www.mongodb.com/

Info on materializecss from https://materializecss.com/getting-started.html/

**(2) Media**
The image was search from http://www.goole.com 

**(3) Acknowledgements**
Get the idea of how platform look likes from Instagram #dailywebdesing
Some code info from 

https://www.codexworld.com/ 

https://www.w3schools.com/
