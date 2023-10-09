from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.souls import Souls

souls_bp = Blueprint("souls", __name__)
souls_api = Api(souls_bp)

class SoulsAPI(Resource):
    def get(self):
        id = request.args.get("id")
        souls = db.session.query(Souls).get(id)
        if souls:
            return souls.to_dict()
        return {"message": "not found"}, 404

class SoulsListAPI(Resource):
    def get(self):
        souls = db.session.query(Souls).all()
        return [soul.to_dict() for soul in souls]

souls_api.add_resource(SoulsAPI, "/souls")
souls_api.add_resource(SoulsListAPI, "/soulsList")