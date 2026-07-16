import json
from pathlib import Path
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "menu.json"


def load_menu():
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/menu")
def api_menu():
    data = load_menu()
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()

    items = data["items"]
    if search:
        items = [i for i in items if search.lower() in i["name"].lower()]
    if category:
        items = [i for i in items if i["category_id"] == category]

    return jsonify({"categories": data["categories"], "items": items})
