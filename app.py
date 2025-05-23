from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('links.json', 'r', encoding='utf-8') as file:
        links = json.load(file)
    return render_template('index.html', links=links)

@app.route('/api/links')
def api_links():
    with open('links.json', 'r', encoding='utf-8') as file:
        return jsonify(json.load(file))

if __name__ == '__main__':
    app.run(debug=True)
