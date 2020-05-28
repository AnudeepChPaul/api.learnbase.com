def getAppProperties():
    return {
        'title': "Learn",
        'allModules': {
            'text': "All Modules",
            'url': "/modules",
            'scheme': "/modules",
        }
    }


def getAllModules():
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


def getTop5Modules():
    return {
        'title': "Modules",
        'modules': {
            'baseUrl': "/modules",
            'list': [
                { 'text': "Python", 'url': "/python", 'scheme': "/[moduleId]" },
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
                },
            ],
        },
    }


def getModuleName(id):
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


def getModuleById(id):
    data = getModuleName(id)
    return {
        'title': data.get('title'),
        'modules': {
            'text': data.get('text'),
            'url': id,
            'scheme': "/[moduleId]",
        }
    }
