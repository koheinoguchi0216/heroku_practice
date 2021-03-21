from flask import Flask, render_template
import random
from database import db
from models import Character

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config.Config')

db.init_app(app)


@app.route("/")
def hello():
    # names = [['image_1.jpg','ロールパンナ'],['image_2.jpg','アンパンマン'],['image_3.jpg','ばいきんまん'],['image_4.jpg','ダダンダン'],['image_5.jpg','カレーパンマン']]
    names = db.session.query(Character.name, Character.image_path).all()
    app.logger.debug(names)
    # app.logger.debug(names)
    random.shuffle(names)
    # app.logger.debug(filenames)
    filename = names[0][1]
    app.logger.debug("filename: " + filename)
    character_name = names[0][0]
    app.logger.debug("character_name: " + character_name)

    return render_template("index.html", title=character_name, file=filename)


if __name__ == "__main__":
    app.run()
