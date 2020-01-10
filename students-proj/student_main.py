from flask import Flask
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
api = Api(app)

# ###
# This is student file created for the building projects
#
#######
#
###
class ClsStudents( Resource):
    def get(self, name):
        return {'GET students name': name}

    def put(self, name):
        return {'PUT students name is set to ': name}

    def post(self, name):
        return {'POST students name is set to ': name}

    def delete(self, name):
        return {'DELETE students name is set to ': name}


class ClsTeachers(Resource):
    def get(self, name):
        return  { 'Name of the Teatcher': name}


api.add_resource(ClsStudents, '/student/<string:name>')
api.add_resource(ClsTeachers, '/teacher/<string:name>')
app.run(port=5001)
