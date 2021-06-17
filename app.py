import random

import speech_recognition as sr
from flask import Flask, render_template
from flask_migrate import Migrate

from database import db
from google_api import getImageUrl
from models import Character
import pyaudio

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
    # 音声入力
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("何かお話しして下さい。")
            audio = r.listen(source)

        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            print("Google Web Speech APIは音声を認識できませんでした。")
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;" " {0}".format(e))
        else:
            break

    API_KEY = "AIzaSyBRgWX8460TpSK0OszHvVLtmM34S2fDRwo"
    CUSTOM_SEARCH_ENGINE = "b382b10e1bccd60e1"

    page_limit = 1
    search_word = text

    img_list = getImageUrl(API_KEY, CUSTOM_SEARCH_ENGINE, search_word, page_limit)
    image_path = img_list[0]

    return render_template("anpanman.html", file=image_path)


if __name__ == "__main__":
    app.run()
