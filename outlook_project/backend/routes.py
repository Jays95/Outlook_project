from flask import request, jsonify, render_template
from app import app, db
from models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.email)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "Bad username or password"}), 401
    return render_template('login.html')

@app.route('/enrichment', methods=['GET'])
@jwt_required()
def enrichment():
    current_user = get_jwt_identity()
    contact_details = {
        "full_name": "Jayson Ranck",
        "department": "Engineering",
        "phone_number": "0671799160",
        "job_title": "Senior Developer"
    }
    return jsonify(contact_details), 200
