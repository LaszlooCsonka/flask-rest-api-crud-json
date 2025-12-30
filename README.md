# flask-rest-api-crud-json
A simple Python Flask REST API implementing full CRUD operations with JSON file storage. Includes a Postman collection for easy API testing.

# Simple Flask REST API

Ez egy gyakorló projekt, amely egy alapvető REST API-t valósít meg Python és Flask használatával. 
A projekt célja a CRUD műveletek és az API tesztelés folyamatának bemutatása.

## Funkciók
- **GET /users**: Felhasználók listázása
- **POST /users**: Új felhasználó létrehozása (id, nev)
- **PUT /users/<id>**: Meglévő felhasználó nevének módosítása
- **DELETE /users/<id>**: Felhasználó törlése

## Technológiai stack
- **Backend:** Python 3, Flask
- **Adattárolás:** JSON fájl
- **Tesztelés:** Postman

## Használat
1. Telepítsd a függőségeket: `pip install -r requirements.txt`
2. Indítsd el a szervert: `python app.py`
3. Az API a `http://127.0.0.1:5000` címen lesz elérhető.

## Tesztelés
A `tests/` mappában található egy exportált Postman Collection, amelyet importálhatsz a Postmanbe a végpontok teszteléséhez.
