from flask import Flask, render_template, request, redirect, url_for
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get('MONGO_URL')
DB_NAME = "insta_blogger"

client = pymongo.MongoClient(MONGO_URI)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
