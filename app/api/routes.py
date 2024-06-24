from flask import jsonify, request
from . import api_bp
from app.models import db
from app.models.user import User

@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

@api_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    telegram_id = data.get('telegram_id')
    user = User(username=username, telegram_id=telegram_id)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201
