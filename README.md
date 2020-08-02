
# **Insta-Blog-assign3**

### Data Centric Development Project

By: Seok Khim Yeoh

## **Demo**

Link to the project demo on heroku [here](https://insta-blogs.herokuapp.com/).

![Desktop image](https://github.com/skyeoh06/assign3-insta-blog/blob/master/testing/responsive.jpg)

## **Objective**

This project started with from the idea of webpage for community target purpose.As the tools for taking for photos become much
and much easy access with phone users nowadays. I would like create webpage for user to share their photo and their thought of their sharing photos.


## **UX**
Easy access to camera make user use it almost to replace paper as tools for the daily activities such as taking notes, sharing, and save. 
* Register - for new user to this webpage to register an account for create, edit or delete process in this website.
* Login - Upon sucess register, User can CUD(create, Update and delete) the insta  blog after success log in and it limit to their own post only.
* Home - A home page to demonstrate what is the idea and use of this webpage about.
* Create - A form platform for create an insta-blog with necessary attribute to be fill in.
* view - A page for all users to view idea or sharing that being created by other users so far. A details link for thought attributes enable users to view more clear the info in a
new page.Edit (update) and delete button is individually placed in each blog for user carried those process separately on selected post only.
* Search - A form which can search the current exit blog by dropdown of the title available.
* Logout - To exit from your account on this webpage.
An indicator about current login user email is able to be see on each page on right top below the register and login button.



## **UI**
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
