from ..models.User import User
from flask import Blueprint, request, jsonify
from ..repositories import userRepository

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try: 
        data = request.json

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"message": "Email ou senha ausentes"}), 400

        user = userRepository.find_user_by_id(data.get("user_id"))
        if not user:
            return jsonify({"message": "Usuário não encontrado"}), 404

        if user.password != password:
            return jsonify({"message": "Senha incorreta"}), 401

        return jsonify({"message": "Login bem-sucedido"}), 200
    except Exception as e:
        return jsonify({"message": f"Erro desconhecido ocorreu no servidor: {e}"}), 500

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        email = data.get("email")
        name = data.get("name")
        password = data.get("password")

        if not email or not password or not name:
            return jsonify({"message": "Email, senha ou nome ausentes"}), 400

        if (userRepository.find_user_by_email(email)):
            return jsonify({"message": "Usuário já existe"}), 409

        newUser = User(data)
        userRepository.save(newUser)
        return jsonify({"message": "Cadastro bem-sucedido"}), 201
    
    except Exception as e:
        return jsonify({"message": f"Erro desconhecido ocorreu no servidor: {e}"}), 500
