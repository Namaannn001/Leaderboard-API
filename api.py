from flask import Flask, request, jsonify
import sqlite3

app = Flask(_name_)

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    
    # Simulated in-memory user check
    if data['name'] in users:
        return jsonify({'message': 'Username already exists'}), 200
    else:
        users.add(data['name'])
        return jsonify({'message': 'Username registered successfully'}), 201

@app.route('/player', methods=['POST'])
def add_player():
    data = request.get_json()
    if 'name' not in data or 'score' not in data:
        return jsonify({'error': 'Missing name or score'}), 400
    
    if data['name'] not in users:
        return jsonify({'error': 'Username not registered'}), 400
    
    try:
        players.append({'name': data['name'], 'score': data['score']})
        return jsonify({'message': 'Player added successfully'}), 201
    except Exception:
        return jsonify({'error': 'Username already exists in leaderboard'}), 400

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    sorted_leaderboard = sorted(players, key=lambda x: x['score'], reverse=True)
    return jsonify(sorted_leaderboard)

if _name_ == '_main_':
    users = set()
    players = []
    app.run(debug=True)
