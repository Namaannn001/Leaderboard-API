from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('leaderboard.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            score INTEGER NOT NULL)''')
        conn.commit()

@app.route('/player', methods=['POST'])
def add_player():
    data = request.get_json()
    if 'name' not in data or 'score' not in data:
        return jsonify({'error': 'Missing name or score'}), 400
    
    with sqlite3.connect('leaderboard.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO players (name, score) VALUES (?, ?)', (data['name'], data['score']))
        conn.commit()
    
    return jsonify({'message': 'Player added successfully'}), 201

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    with sqlite3.connect('leaderboard.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT name, score FROM players ORDER BY score DESC')
        sorted_leaderboard = [{'name': row[0], 'score': row[1]} for row in cursor.fetchall()]
    
    return jsonify(sorted_leaderboard)

if __name__ == "__main__":
    init_db()
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
