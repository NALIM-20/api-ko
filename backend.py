import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Databáza študentov
databaza = {
    "students": [
        {"id": 1, "name": "Adrian", "surname": "Červenka", "nickname": "chilli pepper", "image": "https://picsum.photos/id/1011/300/200", "bio": "Má fakt divné hlášky."},
        {"id": 2, "name": "Milan", "surname": "Kokina", "nickname": "tanečník", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5efee63f1b04f230d150c5ce/formal-photo/e18f5e4d-9a8d-4196-9e18-30ebf1b60dc4", "bio": "Nechcelo sa mi toto vobec robiť."},
        {"id": 3, "name": "Martin", "surname": "Jelínek", "nickname": "král jelimán", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/68c9112594d10f7e9dd591c4/formal-photo/94387b0f-c431-49e2-b562-6a357f415c2d", "bio": "............"},
        {"id": 4, "name": "Daniel", "surname": "Barta", "nickname": "skeleton", "image": "https://picsum.photos/id/1014/300/200", "bio": "..........."},
        {"id": 5, "name": "Matej", "surname": "Randziak", "nickname": "tankista", "image": "https://picsum.photos/id/1015/300/200", "bio": "..........."},
        {"id": 6, "name": "Matúš", "surname": "Bucko", "nickname": "xxxxxxxxxx", "image": "https://picsum.photos/id/1016/300/200", "bio": "Nechcelo sa mi toto vobec robiť."},
        {"id": 7, "name": "Jana", "surname": "Vargová", "nickname": "xxxxxxxxxx", "image": "https://picsum.photos/id/1018/300/200", "bio": "Má fakt divné hlášky."},
        {"id": 8, "name": "Matúš", "surname": "Holečka", "nickname": "xxxxxxxxxx", "image": "https://picsum.photos/id/1019/300/200", "bio": "............"},
        {"id": 9, "name": "Marko", "surname": "Mihalička", "nickname": "xxxxxxxxxx", "image": "https://picsum.photos/id/1020/300/200", "bio": "............"},
        {"id": 10, "name": "Lukáš", "surname": "Vindiš", "nickname": "žirafa", "image": "https://picsum.photos/id/1021/300/200", "bio": "............"}
    ]
}

@app.route('/')
def home():
    return jsonify({"message": "Backend beží!"})

@app.route('/api')
def get_all_students():
    return jsonify(databaza["students"])

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get("message")
    char_name = data.get("name")
    char_bio = data.get("bio")

    # API kľúč si Render vytiahne z tajných nastavení (ukážem ti neskôr)
    api_key = os.getenv("GEMINI_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    prompt = f"Hráš rolu študenta na zoznamke. Tvoje meno: {char_name}. Bio: {char_bio}. Odpovedaj krátko a slovensky na: {user_msg}"
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        ai_text = result['candidates'][0]['content']['parts'][0]['text']
        return jsonify({"reply": ai_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
