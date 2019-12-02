from flask import Flask, request
from flask import render_template

from Toxicity.Model import Model


from webfunctions.TwitterDataHandler import TwitterDataHandler

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/usertweets', methods=['POST'])
def usertweets():
    td = TwitterDataHandler(model)
    username = request.form.get("username")
    tweets_dict = td.scoreUser(username)
    return render_template("tweets.html", tweets=tweets_dict)


@app.route('/texteval', methods=['POST'])
def texteval():
    text = request.form.get("text_content")
    score = model.score(text)
    return render_template("index.html", score_value=score, text_content=text)

model = Model()
# model = Model_Word2Vec()
if __name__ == "__main__":
    app.run(debug=True)
