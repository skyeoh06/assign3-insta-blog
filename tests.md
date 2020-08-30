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
- The title keyword for matching Insta-Blog will be reflected in the Search Result page.

## 5. Register Page
I ensured that:
- The user fill in info was in correct type of format before submission.
* Able to redirect with flash message of suceess to Login page.

## 6. Login page

I ensured that:
- Registered user fills in valid and matching info in the form before submission.
* Able to redirect with flash message of suceess to Index/home page.

## 7. Edit Insta-Blog page

I ensured that:
- form fill with correct data of selected Insta-Blog.
- form valid for submission all of field data from user.
* access to the edit selected Insta-Blog form only from Insta-Blog owner login user.
* Able to redirect with flash message of suceess to View page.

## 8. Delete page

I ensured that:
* The Selected Insta-Blog was deleted by Insta-Blog owner login user.
* Able to redirect with flash message of suceess to View page.

## 9. Search Result page

I ensured that:
* Only Insta-Blog with the keyword title will be displayed.
* Able to redirect to search page with Back button.

## 10. Details Insta-Blog page

I ensured that:
* Only selected Insta-Blog details will be presented.
* Able to redirect to view page with Back Button.