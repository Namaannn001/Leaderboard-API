from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS for cross-origin requests
import os

app = Flask(__name__)
CORS(app, supports_credentials=True, allow_headers=["Content-Type", "Authorization"])  # Enable CORS

# Global storage for users and leaderboard
users = set()
players = []

@app.route('/start_game', methods=['POST'])
def start_game():
    """Registers a new player if the username does not already exist."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    
    if data['name'] in users:
        return jsonify({'message': 'Username already exists'}), 200
    
    users.add(data['name'])
    return jsonify({'message': 'Username registered successfully'}), 201

@app.route('/player', methods=['POST'])
def add_player():
    """Adds a player to the leaderboard with their score."""
    data = request.get_json()
    if not data or 'name' not in data or 'score' not in data:
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
    """Retrieves the leaderboard, sorted by highest score."""
    sorted_leaderboard = sorted(players, key=lambda x: x['score'], reverse=True)
    return jsonify(sorted_leaderboard), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
