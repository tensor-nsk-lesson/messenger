from flask import Blueprint, request, jsonify
from db_handle import db_getProfileInfo, db_updateProfileInfo, db_getProfilesInfo

api_module = Blueprint('api', __name__)

@api_module.route('/profile/<int:ID>', methods=['GET', 'PUT', 'DELETE'])
def profile(ID):
    if request.method == 'GET':
        return jsonify(db_getProfileInfo(ID))

    elif request.method == 'PUT':
        db_updateProfileInfo(ID, request.json.to_dict)
        return jsonify({'message': 'User data has been updated'})

    # elif request.method == 'DELETE':
    #     db_delUser(ID, request.json.to_dict)


@api_module.route('/profiles')
def profiles():
    return jsonify(db_getProfilesInfo())
