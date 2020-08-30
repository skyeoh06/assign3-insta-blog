# Insta-Blog - Testing #

The deployed project 'Insta-Blog' is on [Heroku](https://sky-instablogs.herokuapp.com/)

[**Main README.md file**](https://github.com/skyeoh06/assign3-insta-blog/blob/master/README.md)

## Automated Testing

### Validating Code

Validation services were used to ensure that the respective codes were valid used to develop the website.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to test HTML code to ensure it was valid code. Errors were shown where there were Jinja codes and this was expected as the latter are not html codes. Aside from these there were no other errors.

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test CSS code to ensure it was valid code. No errors were found.

## Manual Testing

A number of manual tests were done on each page to confirm that the website functioned well.

This website was tested on different web browsers and on different devices. Different user from friends and collegues test on 
using the features of this website to detect any error.

## Responsive

Responsive of this website to different mobile and electronic devices was tested on [Am i Responsive](http://ami.responsivedesign.is/?url=#).

## Manual Testing
## 1. Home Page

I ensured that:
* The reponsed of navbar work according to closeNav and openNav function.
* The number of posted blog updated correctly from the code.
* The navigation to each back working correspondingly.
* The register and login button working correspondingly.

## 2. Create Insta-Blog page

I ensured that:
* form valid for submission all of field data from user.
* access to the create Insta-Blog form only from login user.
* redirect with flash message of suceess to Index/home page.

## 3. View Insta-Blog page 

I ensured that:
- All the posted Insta-Blogs in the database was listed in the view page with symmetric alignment.
- All the data of Insta-Blogs was reflect correctly.
- Updated /deleted Insta-Blogs only by owner of login user.
- Details redirect Url for the Insta-Blog accessible by user with/ without login first.
- Info of total posted Insta-Blog in correct amount.
- No listing working according with the total of Insta-Blogs.

## 4. Search Blog page

I ensured that:
- The title keyword for matching Insta-Blog will be reflected in the Result page.

## 5. Register Page
I ensured that:
- The user fill in info was in correct type of format before submission.
* redirect with flash message of suceess to Login page.

## 6. Login page

I ensured that:
- Registered user fills in valid and matching info in the form before submission.
* redirect with flash message of suceess to Index/home page.

## 7. Edit Insta-Blog page

I ensured that:
- form fill with correct data of selected Insta-Blog.
- form valid for submission all of field data from user.
* access to the edit selected Insta-Blog form only from Insta-Blog owner login user.
redirect with flash message of suceess to Index/home page.

## 8. Delete page

I ensured that:
- The Selected Insta-Blog was deleted by Insta-Blog owner login user.

## Bugs 

1. Search ramen flavour:
This was my initial code for users to search for ramen flavours. It worked for a few weeks and one day, it stopped working. An error message saying '1 attribute is expected but 2 were given' was displayed.
```
@app.route('/search_ramen')
def search_ramen():
    orig_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    print(query)
    results=mongo.db.ramens.find({'flavour': query})
    
    ramen = []
    for result in results:
        ramen.append(result)
    
    return render_template('ramen_search.html', title="Search Results", query=orig_query, ramen_search=ramen)
```

  I narrowed the bug down to the line 
```
query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
```
and if i removed the `$options` key-pair values, the code would work but doesn't not allow search on both upper and lower cases of the same search text input.

  I changed the search codes to this and it worked again:
```
@app.route('/search_ramen/', methods=["GET", "POST"])
def search_ramen():
    post_request = request.args['query']
    return render_template("ramen_search.html",
                            title="Search Results",
                            query=post_request,
                            ramen_search=mongo.db.ramens.find({"flavour" : {"$regex": post_request, "$options": "i"}}),
                            ramen_count=mongo.db.ramens.find({"flavour" : {"$regex": post_request, "$options": "i"}}).count())
```

2. Ramen cards:
Initially, the images overflow and overspill out of the placeholder of the card. They appeared stretched at different screen sizes and were hard to manage. Also, I gave a very long text input for the 'flavour' field to see how the card would look and the card adjusted to the number of characters. This made the cards unbalanced and of different height sizes. To force the cards to look identical I set the image height to a fixed pixel, set the max-height of the card-content to a fixed pixel and gave a scroll function should the text content overflows from the height. Here are the code fix:
```
.card .card-image img {
  height: 214px;
}
.index-page-card .card .card-content {
  overflow-y: scroll;
  max-height: 144px;
}
``` 
    
## Further Testing
- In the future, I would like to implement unit testing while building a website of this kind
- A special acknowledgement and thanks to family and friends for their time to test this website on their device and their invaluable feedback.