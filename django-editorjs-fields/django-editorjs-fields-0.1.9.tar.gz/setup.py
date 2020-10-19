# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_editorjs_fields']

package_data = \
{'': ['*'],
 'django_editorjs_fields': ['static/django-editorjs-fields/css/*',
                            'static/django-editorjs-fields/js/*']}

setup_kwargs = {
    'name': 'django-editorjs-fields',
    'version': '0.1.9',
    'description': 'Django plugin for using Editor.js',
    'long_description': '# Editor.js for Django\n\nDjango plugin for using [Editor.js](https://editorjs.io/)\n\n> This plugin works fine with JSONField in Django >= 3.1\n\n[![Python versions](https://img.shields.io/pypi/pyversions/django-editorjs-fields)](https://pypi.org/project/django-editorjs-fields/)\n[![Python versions](https://img.shields.io/pypi/djversions/django-editorjs-fields)](https://pypi.org/project/django-editorjs-fields/)\n[![Downloads](https://pepy.tech/badge/django-editorjs-fields/month)](https://pepy.tech/project/django-editorjs-fields/month)\n\n## Installation\n\n```bash\npip install django-editorjs-fields\n```\n\nAdd `django_editorjs_fields` to `INSTALLED_APPS` in `settings.py` for your project:\n\n```python\n# settings.py\nINSTALLED_APPS = [\n    ...\n    \'django_editorjs_fields\',\n]\n```\n\n## Usage\n\nAdd code in your model\n\n```python\n# models.py\nfrom django.db import models\nfrom django_editorjs_fields import EditorJsJSONField, EditorJsTextField  # import\n\n\nclass Post(models.Model):\n    body_default = models.TextField()\n    body_editorjs = EditorJsJSONField()  # Django >= 3.1\n    body_editorjs_text = EditorJsTextField()  # Django <= 3.0\n\n```\n\nOr add custom Editor.js plugins and configs ([List plugins](https://github.com/editor-js/awesome-editorjs))\n\n**django-editorjs-fields** includes this list of Editor.js plugins by default:\n\n```python\n[\n    \'@editorjs/paragraph\',\n    \'@editorjs/image\',\n    \'@editorjs/header\',\n    \'@editorjs/list\',\n    \'@editorjs/checklist\',\n    \'@editorjs/quote\',\n    \'@editorjs/raw\',\n    \'@editorjs/code\',\n    \'@editorjs/inline-code\',\n    \'@editorjs/embed\',\n    \'@editorjs/delimiter\',\n    \'@editorjs/warning\',\n    \'@editorjs/link\',\n    \'@editorjs/marker\',\n    \'@editorjs/table\',\n]\n```\n\n```python\n# models.py\nfrom django.db import models\nfrom django_editorjs_fields import EditorJsJSONField, EditorJsTextField\n\n\nclass Post(models.Model):\n    body_custom = EditorJsJSONField(\n        plugins=[\n            "@editorjs/image",\n            "@editorjs/header",\n            "editorjs-github-gist-plugin",\n            "@editorjs/code@2.6.0",  # version allowed :)\n            "@editorjs/list@latest",\n            "@editorjs/inline-code",\n            "@editorjs/table",\n        ],\n        tools={\n            "Image": {\n                "config": {\n                    "endpoints": {\n                        # Your custom backend file uploader endpoint\n                        "byFile": "/editorjs/image_upload/"\n                    }\n                }\n            }\n        },\n        null=True,\n        blank=True\n    )\n\n```\n\nIf you want to upload images to the editor then add `django_editorjs_fields.urls` to `urls.py` for your project with `DEBUG=True`:\n\n```python\n# urls.py\nfrom django.contrib import admin\nfrom django.urls import path, include\nfrom django.conf import settings\nfrom django.conf.urls.static import static\n\nurlpatterns = [\n    ...\n    path(\'editorjs/\', include(\'django_editorjs_fields.urls\')),\n    ...\n] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n```\n\nIn production `DEBUG=False` (use nginx to display images):\n\n```python\n# urls.py\nfrom django.contrib import admin\nfrom django.urls import path, include\n\nurlpatterns = [\n    ...\n    path(\'editorjs/\', include(\'django_editorjs_fields.urls\')),\n    ...\n]\n```\n\nSee an example of how you can work with the plugin [here](https://github.com/2ik/django-editorjs-fields/blob/main/example)\n\n## Configure\n\nThe application can be configured by editing the project\'s `settings.py`\nfile.\n\n| Key                            | Description                                                                     | Default                                                |\n| ------------------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------ |\n| `EDITORJS_IMAGE_UPLOAD_PATH`   | Path uploads images                                                             | `settings.MEDIA_URL + \'uploads/images/\'`               |\n| `EDITORJS_IMAGE_NAME_ORIGINAL` | To use the original name of the image file?                                     | `False`                                                |\n| `EDITORJS_IMAGE_NAME_POSTFIX`  | Image file name postfix. Ignored when `EDITORJS_IMAGE_NAME_ORIGINAL` is `True`  | `token_urlsafe(5) # from secrets import token_urlsafe` |\n| `EDITORJS_IMAGE_NAME`          | Image file name postfix. Ignored when `EDITORJS_IMAGE_NAME_ORIGINAL` is `False` | `token_urlsafe(8) # from secrets import token_urlsafe` |\n\n## Support and updates\n\nUse github issues https://github.com/2ik/django-editorjs-fields/issues\n',
    'author': 'Ilya Kotlyakov',
    'author_email': 'm@2ik.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/2ik/django-editorjs-fields',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
