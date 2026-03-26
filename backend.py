from flask import Flask, jsonify
from flask_cors import CORS  # Umožňuje prepojenie s tvojím JavaScriptom

app = Flask(__name__)
CORS(app)  # Povolíme prístup z iných adries (kvôli bonusu)

# 1. Databáza študentov (10 záznamov s obrázkami z internetu)
databaza = {
    "students": [
    {"id": 1, "name": "Adrian", "surname": "Červenka", "nickname": "chilli pepper", "image": "https://picsum.photos/id/1011/300/200"},
    {"id": 2, "name": "Milan", "surname": "Kokina", "nickname": "tanečník", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5efee63f1b04f230d150c5ce/formal-photo/e18f5e4d-9a8d-4196-9e18-30ebf1b60dc4"},
    {"id": 3, "name": "Martin", "surname": "Jelínek", "nickname": "král jelimán", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/68c9112594d10f7e9dd591c4/formal-photo/94387b0f-c431-49e2-b562-6a357f415c2d"},
    {"id": 4, "name": "Daniel", "surname": "Barta", "nickname": "skeleton", "image": "https://picsum.photos/id/1014/300/200"},
    {"id": 5, "name": "Matej", "surname": "Randziak", "nickname": "tankista", "image": "https://picsum.photos/id/1015/300/200"},
    {"id": 6, "name": "Matúš", "surname": "Bucko", "nickname": "xxxxxxxxxx", "image": "https://picsum.photos/id/1016/300/200"},
    {"id": 7, "name": "Jana", "surname": "Vargová", "nickname": "xxxxxxxxxx", "image": "https://picsum.photos/id/1018/300/200"},
    {"id": 8, "name": "Matúš", "surname": "Holečka", "nickname": "xxxxxxxxxx", "image": "https://picsum.photos/id/1019/300/200"},
    {"id": 9, "name": "Marko", "surname": "Mihalička", "nickname": "xxxxxxxxxx", "image": "https://picsum.photos/id/1020/300/200"},
    {"id": 10, "name": "Lukáš", "surname": "Vindiš", "nickname": "žirafa", "image": "https://picsum.photos/id/1021/300/200"}
    ]
}

# 2. Route pre domovskú stránku (/)
@app.route('/')
def home():
    return jsonify({"message": "Vitaj v mojom prvom Flask backende!"})

# 3. Route pre všetkých študentov (/api)
@app.route('/api')
def get_all_students():
    # Vracia celé pole študentov
    return jsonify(databaza["students"])

# 4. Route pre jedného študenta podľa ID (/api/student/X)
@app.route('/api/student/<int:student_id>')
def get_student_by_id(student_id):
    # Prechádzame zoznam a hľadáme zhodné ID
    for student in databaza["students"]:
        if student["id"] == student_id:
            return jsonify(student)
    
    # Ak sa ID nenájde, vráti chybu a kód 404
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
