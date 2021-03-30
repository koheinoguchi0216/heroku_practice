from flask import Flask, render_template
import random
from database import db
from models import Character
from flask_migrate import Migrate

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config.Config')

db.init_app(app)
Migrate(app, db)

@app.route("/")
def hello():
    names = db.session.query(Character.name, Character.image_path).all()
    random.shuffle(names)
    filename = names[0][1]
    character_name = names[0][0]

    return render_template("index.html", title=character_name, file=filename)


if __name__ == "__main__":
    app.run()
