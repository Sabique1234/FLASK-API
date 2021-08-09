from flask import Flask, json, jsonify, request

import csv
all_articles = []

with open('articles.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
disliked_articles = []

app = Flask(__name__)
@app.route('/all-articles')
def get_all_articles():
    return jsonify({
        'data': all_articles,
        'status': 'success'
    }), 200

@app.route('/liked-articles', methods = ['POST'])
def liked_articles():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status': 'success'
    }), 200

@app.route('/disliked-articles', methods = ['POST'])
def disliked_articles():
    article = all_articles[0]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        'status': 'success'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)