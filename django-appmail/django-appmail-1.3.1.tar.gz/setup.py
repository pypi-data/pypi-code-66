# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['appmail', 'appmail.migrations']

package_data = \
{'': ['*'],
 'appmail': ['templates/*',
             'templates/admin/appmail/emailtemplate/*',
             'templates/appmail/*']}

install_requires = \
['django>=2.2,<4.0']

setup_kwargs = {
    'name': 'django-appmail',
    'version': '1.3.1',
    'description': 'Django app for managing localised email templates.',
    'long_description': '.. image:: https://travis-ci.org/yunojuno/django-appmail.svg?branch=master\n    :target: https://travis-ci.org/yunojuno/django-appmail\n\n.. image:: https://badge.fury.io/py/django-appmail.svg\n    :target: https://badge.fury.io/py/django-appmail\n\nDjango-AppMail\n--------------\n\nDjango app for managing transactional email templates.\n\nCompatibility\n=============\n\nThis project now requires Django2.2+ and Python3.7+. If you require a previous\nversion you will have to refer to the relevant branch or tag.\n\nBackground\n==========\n\nThis project arose out of a project to integrate a large transactional Django\napplication with Mandrill, and the lessons learned. It also owes a minor h/t\nto this project from 2011 (https://github.com/hugorodgerbrown/AppMail).\n\nThe core requirement is to provide an easy way to add / edit email templates\nto a Django project, in such a way that it doesn\'t require a developer to make\nchanges. The easiest way to use templated emails in Django is to rely on the\nin-built template structure, but that means that the templates are held in\nfiles, under version control, which makes it very hard for non-developers to\nedit.\n\nThis is **not** a WYSIWYG HTML editor, and it doesn\'t do anything clever. It\ndoesn\'t handle the sending of the emails - it simply provides a convenient\nmechanism for storing and rendering email content.\n\n.. code:: python\n\n    from appmail.models import EmailTemplate\n\n    def send_order_confirmation(order_id):\n        order = Orders.objects.get(id=order_id)\n        template = EmailTemplate.objects.current(\'order_confirmation\')\n        context = { "order": order }\n        # create_message accepts EmailMultiAlternatives constructor kwargs\n        # and returns a standard Django email object which can be updated / sent.\n        message = template.create_message(context, to=[order.recipient.email])\n        message.send()\n\nThe core requirements are:\n\n1. List / preview existing templates\n2. Edit subject line, plain text and HTML content\n3. Use standard Django template syntax\n4. Support base templates\n5. Template versioning\n6. Language support\n7. Send test emails\n\n**Template properties**\n\nIndividual templates are stored as model objects in the database. The\nstandard Django admin site is used to view / filter templates. The templates\nare ordered by name, language and version. This combination is unique. The\nlanguage and version properties have sensible defaults (\n`version=settings.LANGUAGE_CODE` and `version=0`) so don\'t need to set if you\ndon\'t require it. There is no inheritance or relationship between different\nlanguages and versions - they are stored as independent objects.\n\n.. code:: python\n\n    # get the default order_summary email (language = settings.LANGUAGE_CODE)\n    template = EmailTemplate.objects.current(\'order_summary\')\n    # get the french version\n    template = EmailTemplate.objects.current(\'order_summary\', language=\'fr\')\n    # get a specific version\n    template = EmailTemplate.objects.version(\'order_summary\', 1)\n\n**Template syntax**\n\nThe templates themselves use standard Django template syntax, including\nthe use of tags, filters. There is nothing special about them, however there\nis one caveat - template inheritance.\n\n**Template inheritance**\n\nAlthough the template content is not stored on disk, without re-engineering\nthe template rendering methods any parent templates must be. This is annoying,\nbut there is a valid assumption behind it - if you are changing your base\ntemplates you are probably involving designers and developers already, so\nhaving to rely on a developer to make the changes is acceptable.\n\n**Sending test emails**\n\nYou can send test emails to an email address through the admin list view.\n\n.. image:: screenshots/appmail-test-email-action.png\n    :alt: EmailTemplate admin change form\n\nThe custom admin action \'Send test emails\' will redirect to an intermediate\npage where you can enter the recipient email address and send the email:\n\n.. image:: screenshots/appmail-test-email-send.png\n\nThere is also a linkon individual template admin pages (top-right, next to the history link):\n\n.. image:: screenshots/appmail-template-change-form.png\n    :alt: EmailTemplate admin change form\n\nTests\n-----\n\nThere is a test suite for the app, which is best run through ``tox``.\n\nLicence\n-------\n\nMIT\n\nContributing\n------------\n\nUsual rules apply:\n\n1. Fork to your own account\n2. Create a branch, fix the issue / add the feature\n3. Submit PR\n\nPlease take care to follow the coding style - and PEP8.\n\n\nRelease\n-------\n\nIf you have found yourself in the situation of having to release a new version, and assuming you already have the necessary PyPi permissions, here are the next steps you need to take:\n\n**1. Update `setup.py` with the bumped version. Push it to master**\n - PATCH version for backwards-compatible hotfixes\n - MINOR version for backwards-compatible features\n - MAJOR version for incompatible features\n\n**2. Tag this new version by running the following commands**\n - `git tag -a v1.0.x -m v.1.0.x`\n - `git push --tags`\n\nNow, if you go to github and take a look at the tags, you should be able to see your version among them.\n\n**3. Build the wheel**\n - `python3 setup.py sdist bdist_wheel`\n\n**4. Upload it on PyPi using twine**\n - `twine upload dist/*`\n - you will be asked to provide your PyPi username and password\n',
    'author': 'YunoJuno',
    'author_email': 'code@yunojuno.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
