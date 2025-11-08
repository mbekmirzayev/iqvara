from django.contrib import admin


def get_app_list(self, request, app_label=None):
    app_dict = self._build_app_dict(request)

    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
    all_models = []
    for app in app_list:
        all_models.extend(app.pop('models', []))
        app['models'] = []

    new_apps = {
        'label1': {
            'name': "Users",
            "app_label": 'label1',
            'models': list()
        },

        'label2': {
            'name': "Blogs",
            "app_label": 'label2',
            'models': list()
        },

        'label3': {
            'name': "Categories & Courses",
            "app_label": 'label3',
            'models': list()
        },

        'label4': {
            'name': "Settings & FAQ & Tags",
            "app_label": 'label4',
            'models': list()
        },
        'label5': {
            'name': "Payments & Promo code",
            "app_label": 'label5',
            'models': list()
        },
    }


    model_order = {
        'User': 'label1',

        'Blog': 'label2',
        'Comment': 'label2',
        'Step': 'label2',
        'Leaderboard': 'label2',

        'Category': 'label3',
        'Course': 'label3',
        'Section': 'label3',
        'Lesson': 'label3',
        'Enrollment': 'label3',
        'Review': 'label3',

        'Setting': 'label4',
        'FAQ': 'label4',
        'Tag': 'label4',

        'Payment': 'label5',
        'Promo': 'label5',


    }
    for _model in all_models:
        if _model['object_name'] in model_order.keys():
            new_apps[model_order[_model['object_name']]]['models'].append(_model)
        else:
            app_list[0]['models'].append(_model)

    app_list.extend(new_apps.values())
    return app_list


admin.AdminSite.get_app_list = get_app_list