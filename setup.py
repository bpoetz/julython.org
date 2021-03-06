
from setuptools import setup, find_packages

setup(
    name='july',
    version='0.1.0',
    install_requires=[
        'django >= 1.5b1',
        'virtualenv >= 1.5.1',
        'south',
        'fabric >= 1.5.1',
        'django-social-auth >= 0.7.12',
        'django-debug-toolbar >= 0.9.0',
        'django-tastypie >= 0.9.0',
        'requests',
        'iso8601 >= 0.1.4',
        'mock',
        'jsonfield',
    ],
    url='http://github.com/julython/julython.org',
    description=("31 days and nights Python"),
    packages=find_packages(),
)
