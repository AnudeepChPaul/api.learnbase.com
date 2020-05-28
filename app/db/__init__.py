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
