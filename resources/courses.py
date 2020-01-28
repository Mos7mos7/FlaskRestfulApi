from flask import jsonify, Blueprint
from flask_restful import Resource, Api ,reqparse

import models


class CourseList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title',required=True,help='you do not enter title',location=['form','json'])
        self.reqparse.add_argument('url',required=True,help='No URL provided',location=['form','json'])
        super().__init__()
    
    def get(self):
        return jsonify({'courses':[{'title':'python basics'}]})
    def post(self):
       args = self.reqparse.parse_args()
       models.Course.create(**args)

class Course(Resource):
    def get(self,id):
        return jsonify({'title':'python basics'})
    def put(self,id):
        return jsonify({'title':'python basics'})
    def delete(self,id):
        return jsonify({'title':'python basics'})

course_api=Blueprint('resources.courses',__name__)
api=Api(course_api)
api.add_resource(CourseList,'/api/v1/courses',endpoint='courses')
api.add_resource(Course,'/api/v1/courses/<int:id>',endpoint='course')