
from functools import wraps
import json
from flask import Flask, jsonify, make_response, url_for, json
import jwt
import secrets
from Investor import Investor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zHBPmzZvQmaptH_x'


# def check_for_token(func):
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         token = request.header['SECRET_KEY']
#         if not token:
#             return jsonify({'message': 'Missing Token'}), 403
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'])
#         except:
#             return jsonify({ 'message': 'Invalid Token'}), 403
#         return func(*args, **kwargs)
#     return wrapped

# @check_for_token
@app.route('/')
def Index(): 
    return jsonify( {'Message': 'Wrong Route'})

# @check_for_token
@app.route('/create/<name>/<email>/<phonenumber>', methods = ['POST'])
def create(name, email, phonenumber):
    newInvestor = Investor(name,email,phonenumber)
    with open ("database.json", "r") as f:
        database = json.load(f)
    database.append(newInvestor.__dict__)
    with open ("database.json", "w") as f:
        json.dump(database, f, indent=4)
    return jsonify({'message': 'Entry has been Added'}), 200

# @check_for_token
@app.route('/delete/<email>' , methods=['DELETE'])
def delete(email):
    response = ""
    statuscode = 200
    with open ('database.json', "r") as f:
        database = json.load(f)
    if(database):
        for idx, obj in enumerate(database):
            if obj['email'] == email:
                database.pop(idx)
                response = jsonify({'Deleted': email}, statuscode)
            else:
                statuscode = 400
                response = jsonify({'Couldnt delete': email}, statuscode)

    databaseName = 'database.json'
    with open(databaseName, 'w') as f:
        f.write(json.dumps(database, indent=4))
    return make_response(response, 400)

@app.route('/show/' , methods=['GET'])
# @check_for_token
def showInvestors():
    
    with open ('database.json', "r") as f:
        database = json.load(f)
    
    return database


@app.route('/filter/<field>=<name>' , methods=['GET'])
# @check_for_token
def filter(field,name):
    
    with open ('database.json', "r") as f:
        database = json.load(f)
    newList = filterInvestor(name, database, field)
    return newList

# @check_for_token
@app.route('/modify/email=<email>,<field>=<info>' , methods=['POST'])
def modify(email, field,info):
    
    with open ('database.json', "r") as f:
        database = json.load(f)
    for records in database:
        if records['email'] == email:
            records[field] = info
            break
    databaseName = 'database.json'
    with open(databaseName, 'w') as f:
        f.write(json.dumps(database, indent=4))
    return f"Modified ${email}"



def filterInvestor(name, database, type):
    newList = [x for x in database if x[type] == name]
    return newList




