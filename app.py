from flask import Flask, render_template, request, redirect, url_for, flash
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


# home page

@app.route('/')
def index():
    return render_template('index.template.html', title="Home")


# Search a insta blog
@app.route('/search')
def search():
    blog_title = client[DB_NAME].pictures.find()
    return render_template('search.template.html', title="search",
                           blog_title=blog_title)


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
        result_count=client[DB_NAME].pictures.find(search_criteria).count()
        return render_template('result_title.template.html',
                            title="Result Title",
                            result_title=result_title,
                            result_count=result_count)
    else:
        flash("Please select a title for search")
        return redirect(url_for('search'))


# Create a insta blogger


@app.route('/create')
def create():
    return render_template('create.template.html', title="Create",
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

    if (title and categories and date and thought and uploaded_file_url) != "":
        client[DB_NAME].pictures.insert_one({
            'title': title,
            'categories': categories,
            'create_date': date,
            'thoughts': thought,
            'uploaded_file_url': uploaded_file_url
        })

        flash(f"New insta - blog '{title}' has been created")
        return redirect(url_for('index'))
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
    if page_number == None:
        page_number = 0
    else:
        page_number = int(page_number)

    print("page number=", page_number)
    all_blog = client[DB_NAME].pictures.find().skip(
        page_number*6).limit(6)
    return render_template('view.template.html', title="View",
                           all_blog=all_blog,
                           page_number=page_number)

# details of the blog


@app.route('/details/<id>')
def details_blog(id):
    blog = client[DB_NAME].pictures.find_one({
        '_id': ObjectId(id)
    })
    return render_template('details_blog.template.html', title="Details",
                           blog=blog,
                           cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET)


# update of the blog


@app.route('/update/<id>')
def update_blog(id):
    blog = client[DB_NAME].pictures.find_one({
        '_id': ObjectId(id)
    })
    return render_template('update.template.html', title="Update", blog=blog,
                           cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET)


@app.route('/update/<id>', methods=["POST"])
def process_update_blog(id):
    title = request.form.get('title')
    blog_date = request.form.get('create-date')
    client[DB_NAME].pictures.update_one({
        "_id": ObjectId(id)
    }, {
        '$set': {
            'title': title,
            'categories': request.form.get('categories'),
            'create_date': blog_date,
            'thoughts': request.form.get('thought'),
            'uploaded_file_url': request.form.get('uploaded_file_url')
        }
    })
    flash(f"Update New insta - blog '{title}' has been updated")
    return redirect(url_for('view'))
# delete of the blog


@app.route('/delete/<id>')
def delete_blog(id):
    blog = client[DB_NAME].pictures.find_one({
        '_id': ObjectId(id)
    })
    return render_template('delete.template.html', title="Delete", blog=blog)


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
