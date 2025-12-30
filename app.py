import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
DATA_FILE ='felhasznalok.json'

# Segédfüggvény az adatok betöltéséhez
def load_data():
    if not os.path.exists(DATA_FILE):
        #Ha nincs fájl, alapértelmezett adatokkal indulunk
        default_data = [
            {"id": 1, "nev": "Kovács János"},
            {"id": 2, "nev": "Nagy Anna"}
        ]
        # Automatikus mentés, hogy létrejöjjön a fájl
        save_data(default_data)
        return default_data

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Segédfüggvény az adatok mentéséhez
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Üdvözlés a főoldalon
@app.route('/')
def home():
    return jsonify({"Üdv a REST API-ban! főoldala. Használd a /users végpontot."})

# --- CRUD MŰVELETEK ---

# 1. GET: Összes felhasználó
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(load_data())

# 2. POST kérés: Új felhasználók hibakezeléssel 
@app.route('/users', methods=['POST'])
def add_user():
    uj_adat = request.get_json()

    # Hibakezelés: hiányzó mezők ellenőrzése
    if not uj_adat or 'id' not in uj_adat or 'nev' not in uj_adat:
        return jsonify({"hiba": "Hiányzó adatok! Szükséges: id, nev"}), 400

    adatok = load_data()

    # Hibakezelés: létezik-e már az ID?
    if any(u['id'] == uj_adat['id'] for u in adatok):
        return jsonify({"hiba": "Ez az ID már foglalt!"}),400

    adatok.append(uj_adat)
    save_data(adatok)
    return jsonify({"uzenet": "Sikeres mentés!", "adat": uj_adat}), 201

# 3. PUT kérés: Felhasználó módosítása
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    uj_adatok = request.get_json()
    if not uj_adatok or 'nev' not in uj_adatok:
        return jsonify({"hiba": "Hiányzó adatok! A 'nev' mező megadása kötelező a frissítéshez."}), 400

    adatok = load_data()
    felhasznalo_talalt = False

    for u in adatok:
        if u['id'] == user_id:
            u['nev'] = uj_adatok['nev']
            felhasznalo_talalt = True
            break

    if not felhasznalo_talalt:
        return jsonify({"hiba": "Nincs ilyen ID-jú felhasználó!"}), 404    

    save_data(adatok)
    return jsonify({"uzenet": "Sikeres frissítés!", "adat": next(u for u in adatok if u['id'] == user_id)})

# 4. DELETE kérés: Felhasználó törlése ID alapján
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    adatok = load_data()
    uj_lista = [u for u in adatok if u['id'] != user_id]

    if len(uj_lista) == len(adatok):
        return jsonify({"hiba": "Nincs ilyen felhasználó!"}),404
    
    save_data(uj_lista)
    return jsonify({"uzenet": f"A(z) {user_id} ID-jú felhasználó törölve!"})

if __name__ == '__main__':
    load_data()
    app.run(debug=True)