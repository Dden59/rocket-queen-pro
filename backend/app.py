from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

users = {}

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    user_id = data['user_id']
    
    if user_id not in users:
        users[user_id] = {
            'balance': 5000,
            'target': 50,
            'history': [],
            'level': '🪐 Новичок'
        }
    
    last_result = data.get('result')
    last_bet = data.get('bet', 100)
    
    if last_result == 'lose':
        new_bet = (sum([x['bet'] for x in users[user_id]['history'] if x['result'] == 'lose']) + 50) / 0.5
    else:
        new_bet = 100
    
    # Обновляем уровень
    wins = len([x for x in users[user_id]['history'] if x['result'] == 'win'])
    if wins > 10: users[user_id]['level'] = '🚀 Профи'
    
    return jsonify({
        'new_bet': round(new_bet),
        'balance': users[user_id]['balance'],
        'level': users[user_id]['level']
    })

if __name__ == '__main__':
    app.run(port=5000)
