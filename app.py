from flask import Flask, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def hello():
    filenames = ['image_1.jpg', 'image_2.jpg']
    app.logger.debug(filenames)
    random.shuffle(filenames)
    app.logger.debug(filenames)
    filename = filenames[0]
    return render_template("index.html", title="ロールパンダ", file=filename)

if __name__ == "__main__":
    app.run()
