from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.api import api

api_bp = Blueprint("api", __name__)
api_api = Api(api_bp)

class apiAPI(Resource):
    def get(self):
        id = request.args.get("id")
        Api = db.session.query(api).get(id)
        if Api:
            return Api.to_dict()
        return {"message": "not found"}, 404

api_api.add_resource(apiAPI, "/api")