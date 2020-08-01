from flask import render_template
from flask import Flask, request
from flask import url_for, flash, session, redirect
import flask_login
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo


load_dotenv()

app = Flask(__name__)

# read in the SESSION_KEY variable from the operating system environment
SESSION_KEY = os.environ.get('SESSION_KEY')
# set the session key
app.secret_key = SESSION_KEY
UPLOAD_PRESET = os.environ.get("UPLOAD_PRESET")
CLOUD_NAME = os.environ.get("CLOUD_NAME")

# connect to mongo
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# define my db_name
DB_NAME = "insta_blogger"

# Create the login manager and assign to our Flask app
login_manager = flask_login.LoginManager()
# tell Flask to use the Flask-Login's login manager
login_manager.init_app(app)


# User object
# The user object basically represents one user
class User(flask_login.UserMixin):
    pass
# user loader for the Flask-Login login manager


@login_manager.user_loader
def user_loader(email):
    # find the user from the database by its email
    user_in_db = client[DB_NAME].users.find_one({
        "email": email
    })
    print(user_in_db)
    if user_in_db:
        # create a new user object
        user = User()
        # set the id of the user object to be the user's email
        user.id = user_in_db['email']
        return user
    else:
        return None
# home page


@app.route('/')
def index():
    auth_user = session.get('_user_id')
    return render_template('index.template.html',
                           title="Home",
                           auth_user=auth_user)
# register


@app.route('/register')
def register():
    return render_template('register.template.html', title="register")


@app.route('/register', methods=['POST'])
def process_register():
    email = request.form.get('user-email')
    email_in_db = client[DB_NAME].users.find_one({
        'email': email
    })
    if email != email_in_db:
        client[DB_NAME].users.insert_one({
            'username': request.form.get('user-name'),
            'email': email,
            'password': request.form.get('user-password')
        })
        flash(f"Email'{email}' was created successful.")
        return redirect(url_for('login'))
    else:
        flash("Please login with registered email!")
        return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login_form.template.html', title="Login")


@app.route('/login', methods=["POST"])
def process_login():

    # grab the user from the db by email
    user_in_db = client[DB_NAME].users.find_one({
        'email': request.form.get('user-email')
    })

    if user_in_db:
        user = User()
        user.id = user_in_db['email']
        print(user)
        print(user.id)
        if request.form.get('user-password') == user_in_db['password']:
            flask_login.login_user(user)
            auth_user = session.get('_user_id')
            flash(f"Email'{user.id}' has been success logged in.")
            return render_template('index.template.html', title="Home",
                                   auth_user=auth_user)
        else:
            flash("Wrong user or password!")
            return redirect(url_for('login'))

    else:
        flash("Please register a valid email!")
        return redirect(url_for('register'))


@app.route('/restricted_page')
@flask_login.login_required
def my_secret_page():
    return "Restricted Area Entered"


@app.route('/logout')
def logout():
    flask_login.logout_user()
    flash("Logout Successfully")
    return redirect(url_for('index'))


# Search a insta blog
@app.route('/search')
def search():
    auth_user = session.get('_user_id')
    blog_title = client[DB_NAME].pictures.find()
    return render_template('search.template.html', title="search",
                           blog_title=blog_title,
                           auth_user=auth_user)


@app.route('/search', methods=["POST"])
def result_title():

    search_title = request.form.get('search_title')
    search_criteria = {}

    if search_title != "":
        search_criteria['title'] = {
            "$regex": search_title,
            "$options": "i"
        }
        result_title = client[DB_NAME].pictures.find(search_criteria)
        result_count = client[DB_NAME].pictures.find(search_criteria).count()
        auth_user = session.get('_user_id')
        return render_template('result_title.template.html',
                               title="Result Title",
                               result_title=result_title,
                               result_count=result_count,
                               auth_user=auth_user)
    else:
        flash("Please select a title for search!")
        return redirect(url_for('search'))


# Create a insta blogger


@app.route('/create')
def create():
    auth_user = session.get('_user_id')
    if auth_user is None:
        flash("Please login to continue!")
        return redirect(url_for('login'))
    else:
        return render_template('create.template.html', title="Create",
                               auth_user=auth_user,
                               cloud_name=CLOUD_NAME,
                               upload_preset=UPLOAD_PRESET)


# process the create form
@app.route('/create', methods=['POST'])
def process_create():
    # extract information from the form
    title = request.form.get('title')
    categories = request.form.get('categories')
    date = request.form.get('create-date')
    thought = request.form.get('thought')
    uploaded_file_url = request.form.get('uploaded_file_url')
    user_email = session.get('_user_id')

    if (title and categories and date and thought and uploaded_file_url) != "":
        client[DB_NAME].pictures.insert_one({
            'title': title,
            'categories': categories,
            'create_date': date,
            'thoughts': thought,
            'uploaded_file_url': uploaded_file_url,
            'user_email': user_email
        })

        flash(f"New insta - blog '{title}' has been created.")
        return redirect(url_for('view'))
    else:
        flash("Please fill in the blank to continue")
        return render_template('create.template.html', title="Create",
                               cloud_name=CLOUD_NAME,
                               upload_preset=UPLOAD_PRESET)


# display the insta blog


@app.route('/view')
def view():
    # get the current page number
    page_number = request.args.get('page')
    # if there is no page number (aka, None) then assume we are at page 0
    if page_number is None:
        page_number = 0
    else:
        page_number = int(page_number)

    print("page number=", page_number)
    all_blog = client[DB_NAME].pictures.find().skip(
        page_number*6).limit(6)
    auth_user = session.get('_user_id')
    return render_template('view.template.html', title="View",
                           all_blog=all_blog,
                           page_number=page_number,
                           auth_user=auth_user)

# details of the blog


@app.route('/details/<id>')
def details_blog(id):
    blog = client[DB_NAME].pictures.find_one({
        '_id': ObjectId(id)
    })
    auth_user = session.get('_user_id')
    return render_template('details_blog.template.html', title="Details",
                           blog=blog,
                           auth_user=auth_user,
                           cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET)


# update of the blog


@app.route('/update/<id>')
def update_blog(id):
    auth_user = session.get('_user_id')
    blog = client[DB_NAME].pictures.find_one({
        '_id': ObjectId(id)
    })

    if auth_user == blog['user_email']:
        return render_template('update.template.html', title="Update",
                               blog=blog,
                               auth_user=auth_user,
                               cloud_name=CLOUD_NAME,
                               upload_preset=UPLOAD_PRESET)
    else:
        flash("Invalid email for editing")
        return redirect(url_for('view'))


@app.route('/update/<id>', methods=["POST"])
def process_update_blog(id):
    title = request.form.get('title')
    blog_date = request.form.get('create-date')
    user_email = session.get('_user_id')
    client[DB_NAME].pictures.update_one({
        "_id": ObjectId(id)
    }, {
        '$set': {
            'title': title,
            'categories': request.form.get('categories'),
            'create_date': blog_date,
            'thoughts': request.form.get('thought'),
            'uploaded_file_url': request.form.get('uploaded_file_url'),
            'user_email': user_email
        }
    })
    flash(f"Insta - blog '{title}' has been updated.")
    return redirect(url_for('view'))
# delete of the blog


@app.route('/delete/<id>')
def delete_blog(id):
    auth_user = session.get('_user_id')
    blog = client[DB_NAME].pictures.find_one({
        '_id': ObjectId(id)
    })

    if auth_user == blog['user_email']:
        auth_user = session.get('_user_id')
        return render_template('delete.template.html',
                               title="Delete",
                               blog=blog,
                               auth_user=auth_user)
    else:
        flash("Invalid email for edit")
        return redirect(url_for('view'))


@app.route('/delete/<id>', methods=["POST"])
def process_delete_blog(id):
    client[DB_NAME].pictures.remove({
        '_id': ObjectId(id)
    })
    flash("The Blog had been deleted")
    return redirect(url_for('view'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
