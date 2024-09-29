from flask import Flask, request, jsonify
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(_name_)

@app.route('/cosine_similarity', methods=['POST'])
def calculate_cosine_similarity():
    vector1 = np.array(request.json['vector1']).reshape(1, -1)
    vector2 = np.array(request.json['vector2']).reshape(1, -1)
    
    similarity = cosine_similarity(vector1, vector2)[0][0]
    return jsonify({"similarity": float(similarity)})

if _name_ == '_main_':
    app.run(port=5003)