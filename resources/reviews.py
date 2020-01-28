from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse

import models


class ReviewList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title',required=True,help='you do not enter title',location=['form','json'])
        self.reqparse.add_argument('url',required=True,help='No URL provided',location=['form','json'])
        super().__init__()
    def get(self):
        return jsonify({'reviews':[{'course':1,'rating':5}]})

class Review(Resource):
    def get(self,id):
        return jsonify({'course':1,'rating':5})
    def put(self,id):
        return jsonify({'course':1,'rating':5})
    def delete(self,id):
        return jsonify({'course':1,'rating':5})

review_api=Blueprint('resources.reviews',__name__)
api=Api(review_api)
api.add_resource(ReviewList,'/api/v1/reviews',endpoint='reviews')
api.add_resource(Review,'/api/v1/reviews/<int:id>')
