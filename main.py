from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)

api = Api(app,
          version='0.1',
          title='Our sample API',
          description='This is our sample API')

app_ns = api.namespace('app', description='TODO operations')
modules_ns = api.namespace('modules', description='TODO operations')


@app_ns.route('/getAppProperties')
class GetAppProperties(Resource):
    def get(self):
        return {
            'title': "Learn",
            'allModules': {
                'text': "All Modules",
                'url': "/modules",
                'scheme': "/modules",
            }
        }


@modules_ns.route('/<path:module_id>')
class GetModuleById(Resource):
    def get(self, module_id):
        data = self.getModuleName(module_id)
        return {
            'title': data.get('title'),
            'modules': {
                'text': data.get('text'),
                'url': module_id,
                'scheme': "/[moduleId]",
            }
        }

    def getModuleName(self, id):
        lower_id = str(id).lower()
        return {
            'python': { 'text': "Python", 'title': "Python Learning Modules" },
            'sql': { 'text': "SQL", 'title': "SQL Learning Modules" },
            'math': { 'text': "Mathematics", 'title': "Mathematics Learning Modules" },
            'statistics': { 'text': "Statistics", 'title': "Statistics Learning Modules" },
            'ai-ml-1': { 'text': "Artificial & Maching Learning (I)",
                         'title': "Artificial & Maching Learning (I) Learning Modules" },
            'ai-ml-2': { 'text': "Artificial & Maching Learning (II)",
                         'title': "Artificial & Maching Learning (II) Learning Modules" },
            'linear-regression': {
                'text': "Linear Regression",
                'title': "Linear Regression Learning Modules",
            },
            'simple-linear-regression"': {
                'text': "Simple Linear Regression",
                'title': "Simple Linear Regression Learning Modules",
            }
        }.get(lower_id, { 'text': id, 'title': "Unknown Module" })


@modules_ns.route('/list')
class GetModules(Resource):
    def get(self):
        return {
            'title': "Modules",
            'modules': {
                'baseUrl': "/modules",
                'list': [
                    { 'text': "Python", 'url': "/python", 'scheme': "/[moduleId]" },
                    { 'text': "SQL", 'url': "/sql", 'scheme': "/[moduleId]" },
                    { 'text': "Math", 'url': "/math", 'scheme': "/[moduleId]" },
                    { 'text': "Statistics", 'url': "/statistics", 'scheme': "/[moduleId]" },
                    { 'text': "AI & ML 1", 'url': "/ai-ml-1", 'scheme': "/[moduleId]" },
                    { 'text': "AI & ML 2", 'url': "/ai-ml-2", 'scheme': "/[moduleId]" },
                    {
                        'text': "Linear Regression",
                        'url': "/linear-regression",
                        'scheme': "/[moduleId]",
                    },
                    {
                        'text': "Simple Linear Regression",
                        'url': "/simple-linear-regression",
                        'scheme': "/[moduleId]",
                    }
                ]
            }
        }


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
