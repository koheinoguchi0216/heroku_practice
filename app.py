import random

from flask import Flask, render_template
from flask_migrate import Migrate

from database import db
from google_api import getImageUrl
from models import Character
from voice_input import speech

app = Flask(__name__)
app.config["DEBUG"] = True
app.config.from_object("config.Config")

db.init_app(app)
Migrate(app, db)


@app.route("/")
def top():

    return render_template("home.html")


@app.route("/images")
def hello():
    names = db.session.query(Character.name, Character.image_path).all()
    random.shuffle(names)
    filename = names[0][1]
    character_name = names[0][0]

    return render_template("index.html", title=character_name, file=filename)


@app.route("/anpanman")
def anpanman():

    speech_text = speech()

    API_KEY = "AIzaSyBRgWX8460TpSK0OszHvVLtmM34S2fDRwo"
    CUSTOM_SEARCH_ENGINE = "b382b10e1bccd60e1"

    page_limit = 1
    search_word = speech_text

    img_list = getImageUrl(API_KEY, CUSTOM_SEARCH_ENGINE, search_word, page_limit)
    image_path = img_list[1]

    return render_template("anpanman.html", file=image_path)


@app.route("/voice")
def mik():

    return render_template("voice.html")


if __name__ == "__main__":
    app.run()
