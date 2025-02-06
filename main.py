from flask import Flask
from uuid import uuid4
from flask import render_template
from data.item_getter import get_single_item_set

app = Flask(__name__)


@app.route("/")
def index():
    """renders a template which loads data and populates.

    Returns:
        _type_: html, string
    """
    return render_template("index.html")


@app.route("/get_items")
def get_data():
    """api returns a list of items.
    randamization has been done to simulate request specific modifications.

    Returns:
        _type_: list of dict
    """
    data = get_single_item_set()
    for d in data:
        d["id"] = uuid4().hex
    return data
