from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def generate_form():
    """Generate and Display Form"""

    return render_template("questions.html", words = excited_story.prompts)

@app.get('/results')
def generate_sentence():
    """Generate and Display Story Based On What Was Passed In Query Param"""

    input_words = request.args
    return render_template("results.html",story=excited_story.generate(input_words))
    # add new line to generate story 