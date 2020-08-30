## **Database Structure**
* This database name for this project is insta-blogger and is consists of 2 collections.
* These collection are setup with PyMongo in app.py file.
* As the reference to the ERD.pdf diagram, each field in the collection represents the attribute in the entity.

1. Pictures Collections.
* Each collection will be defines with each own unique _id/Object Id.
* The fields instances for this are:
- Title
- Categories
- Create_date/date
- thoughts
- uploaded_file_url/image url
- user_email

2. User Collections
* Each collection will be defines with each own unique _id/Object Id.
* The fields instances for this are:
- Username
- email
- password