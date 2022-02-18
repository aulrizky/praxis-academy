from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2 
from flask_cors import CORS

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres@localhost:5000/pets'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# CORS(app, support_credentials=True)

conn = psycopg2.connect(
    database='postgres', 
    user='john', 
    host='localhost',
    password='1234',
)

conn.autocommit = True
cur = conn.cursor()



@app.route('/')
def index():
    return jsonify({"message":"welcome"})


# @cross-origin()
@app.route('/pet', methods=['POST'])
def create_pets():
    #postman
    '''postman side'''
    '''sql query'''
    try:
        pet_data = request.json
        pet_name = pet_data['pet_name']
        pet_type = pet_data['pet_type']
        pet_decription = pet_data['pet_decription']

        query = f"INSERT INTO pet(pet_name, pet_type, pet_decription) VALUES('{pet_name}', '{pet_type}', '{pet_decription}')"
        cur.execute(query)
        conn.commit()
        conn.close()
        return jsonify({"success": True,"response":"Pet added"})
    except Exception as e:
        return jsonify({"error": f"{e}"})


@app.route('/getpet',methods=['GET'])
def getpet():
    
    try:
        sql= f'SELECT * From pet'
        cur.execute(sql)
        data = cur.fetchall()
        view = []
        for row in data:
            view.append(row)
        conn.commit()
        conn.close()
        return jsonify(
            {   
                "data":view,
                "message":"ber hasil" 
                
            }
        )
    except Exception as e:
        return jsonify({"error": f"{e}"})

@app.route('/update', methods=['PUT'])
def update_pet():
    try:
        pet_id = request.json['id']
        pet_decription = request.json['pet_decription']
        query = f"UPDATE pet SET pet_decription ='{pet_decription}' WHERE id ='{pet_id}'"
        cur.execute(query)
        conn.commit()
        conn.close()
        return jsonify({"success": True,"response":"Pet update"})
    except Exception as e:
        return jsonify({"error": f"{e}"})

@app.route('/del',methods=['DELETE'])
def del_pet():
    try:
        pet_id = request.json['id']
        query = f"DELETE from pet WHERE id ='{pet_id}'"
        cur.execute(query)
        conn.commit()
        conn.close()
        return jsonify({"success": True,"response":"Pet delete"})
    except Exception as e:
        return jsonify({"error": f"{e}"})

        
if __name__ == '__main__':
  app.run(debug=True)
