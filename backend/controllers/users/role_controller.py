from flask import Blueprint, request, jsonify
from backend.services.user_management.role_service.py import RoleService
from backend.repositories.roles.role_repository import RoleRepository
from backend.repositories.user_roles.user_role_repository import UserRoleRepository

role_controller = Blueprint('role_controller', __name__)
role_repository = RoleRepository()
user_role_repository = UserRoleRepository()
role_service = RoleService(role_repository, user_role_repository)

@role_controller.route('/roles', methods=['POST'])
def create_role():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    
    if not name or not description:
        return jsonify({'message': 'Name and description are required'}), 400
    
    role = role_service.create_role(name, description)
    return jsonify(role.dict()), 201

@role_controller.route('/roles', methods=['GET'])
def get_roles():
    roles = role_service.get_all_roles()
    return jsonify([role.dict() for role in roles]), 200

@role_controller.route('/roles/<int:role_id>', methods=['GET'])
def get_role(role_id):
    role = role_service.get_role(role_id)
    return jsonify(role.dict()), 200

@role_controller.route('/roles/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    
    if not name or not description:
        return jsonify({'message': 'Name and description are required'}), 400

    role = role_service.get_role(role_id)
    role.name = name
    role.description = description
    updated_role = role_service.update_role(role)
    return jsonify(updated_role.dict()), 200

@role_controller.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    role_service.delete_role(role_id)
    return jsonify({'message': 'Role deleted successfully'}), 204

@role_controller.route('/users/<int:user_id>/roles', methods=['POST'])
def assign_role_to_user(user_id):
    data = request.json
    role_id = data.get('role_id')
    
    if not role_id:
        return jsonify({'message': 'Role ID is required'}), 400

    user_role = role_service.assign_role_to_user(user_id, role_id)
    return jsonify(user_role.dict()), 201

@role_controller.route('/users/<int:user_id>/roles', methods=['GET'])
def get_user_roles(user_id):
    user_roles = role_service.get_user_roles(user_id)
    return jsonify([user_role.dict() for user_role in user_roles]), 200

@role_controller.route('/users/<int:user_id>/roles', methods=['DELETE'])
def revoke_roles_from_user(user_id):
    role_service.revoke_roles_from_user(user_id)
    return jsonify({'message': 'Roles revoked successfully'}), 204