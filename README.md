
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
2. The Navbar was created with closed(toggle in) or open(toggle out) effect for user able to view a wide and clear navigation bar in any mobile device and 
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

1.Project Strategy
* The Navigation is responsive for different sizes of screen with uses of bootstrap cdn. 
* For the navbar,a side bar with toggle effect(with javascript) were choose for easy view in regardless of screen size.
* Each success activities such as login, update and etc will be indicated on a flash message on top of page.
* Google [fonts] (https://fonts.google.com/specimen/Playfair+Display?selection.family=Playfair+Display) were chosen for this website. This is choose for easy view for the users.
* The page use blur effect, webgradient image background for each page presentation.
* The [Home](https://insta-blogs.herokuapp.com/), a brief introduction of webpage ideas, register and login access button and current login user email info displayed in right top of the webpage.
* The [Register](https://insta-blogs.herokuapp.com/register), uses of a form format for register attribute displays.
* The [Login](https://insta-blogs.herokuapp.com/login), uses of a form format for login attribute displays (email and password).
* The [Create](https://insta-blogs.herokuapp.com/create), uses of a form format and cloudinary tools for an insta blog required attributes fill in.
* The [View](https://insta-blogs.herokuapp.com/view), uses of card format  for display all current viewable blog, a sorted listing idea for tidy of blog display and info about total current that can viewable.
* The blog details of each blog thoughts, update/edit and delete button is placed on each card of individual blog. Once access, a link end with current blod id will display on the link as this
  - details (https://insta-blogs.herokuapp.com/details/5f101e874d280d2a23320028)
  - update (https://insta-blogs.herokuapp.com/update/5f101e874d280d2a23320028)
  - delete (https://insta-blogs.herokuapp.com/delete/5f101e874d280d2a23320028).
* The [Search](https://insta-blogs.herokuapp.com/search), use of dropdown with all the available title to be select for view.
* The logout on the navbar is a click access button, it activate once click on it.
* Upload photo uses the cloudinary - upload widget (javascript) to store the upload photo.
* The blog was stored in the MONGODB database with collection named pictures and photo in cloudinary with its link in the MONGODB database.
* The users account that register in this blog was stored in MONGODB database  with collection named users.
* jinja code involved in database data access process.


2.Scope of the project
* Register , login - A user account required for create, update and delete an insta-blog in the webpage.
* Create - List of attributes about an insta blog and required to fill in for sucess created.
* View - Info about the blog collection on this page such as total number of blog, access to read by all users, while update and delete only accessible by user who created it.
* Search - The blog can be search by title of dropdown and viewable with and without login account.
* logout - Access via upon on click it from nacbar.
* Flash - uses for acknowledgement that process of edit, create and etc was success.
* relationships of database collection - between two collection of database, user emaill attribute was used for the connection.


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
