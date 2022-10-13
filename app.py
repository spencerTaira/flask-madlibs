from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories, silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
selected_story = []

debug = DebugToolbarExtension(app)

@app.get('/')
def pick_story():
    """Generate a form that allows user to pick a story"""

    story_names = [story_name for story_name in stories]
    return render_template("story_form.html", stories = story_names)

@app.get('/input_form')
def generate_form():
    """Generate and Display Form"""
    story_name = request.args["story"]
    selected_story = stories[story_name]
    return render_template("questions.html", words = selected_story.prompts)

@app.get('/results')
def generate_sentence():
    """Generate and Display Story Based On What Was Passed In Query Param"""

    input_words = request.args
    print(selected_story)
    return render_template("results.html",story=selected_story[0].generate(input_words))
    # add new line to generate story