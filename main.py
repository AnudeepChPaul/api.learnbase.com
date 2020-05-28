from flask import Flask, request
from flask_restplus import Api, Resource
from flask_cors import CORS
from app.db import getAppProperties, getAllModules, getModuleById, getTop5Modules, getModuleName

app = Flask(__name__)
CORS(app)

api = Api(app,
          version='0.1',
          title='Our sample API',
          description='This is our sample API')

app_ns = api.namespace('app', description='TODO operations')
modules_ns = api.namespace('modules', description='TODO operations')


@app_ns.route('/getAppProperties')
class GetAppProperties(Resource):
    def get(self):
        return getAppProperties()


@modules_ns.route('/list/<path:module_id>')
class GetModuleById(Resource):
    def get(self, module_id):
        return getModuleById(module_id)


@modules_ns.route('/list')
class GetModules(Resource):
    def get(self):
        top = request.args.get('top')
        if top is not None:
            return getTop5Modules()
        return getAllModules()


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
