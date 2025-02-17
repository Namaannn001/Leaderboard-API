from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Global storage for users and leaderboard
users = set()
players = []

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    
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
    
    # Ensure username is unique in leaderboard
    if any(player['name'] == data['name'] for player in players):
        return jsonify({'error': 'Username already exists in leaderboard'}), 400
    
    players.append({'name': data['name'], 'score': data['score']})
    return jsonify({'message': 'Player added successfully'}), 201

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    sorted_leaderboard = sorted(players, key=lambda x: x['score'], reverse=True)
    return jsonify(sorted_leaderboard)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
