from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(name)

es = Elasticsearch(["http://localhost:9200"])  # Explicitly specify the scheme

@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    index = request.json['index']
    
    result = es.search(index=index, body={
        "query": {
            "match": {
                "content": query
            }
        }
    })
    
    return jsonify(result['hits']['hits'])

if name == 'main':
    app.run(port=5001)