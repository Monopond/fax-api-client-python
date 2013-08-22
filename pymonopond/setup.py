try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'name': 'pymonopond',
	'description': 'Python Client for Monopond',
	'author': 'Froilan Co',
	'url': 'URL to get it at.',
	'download_url': 'https://github.com/Monopond/fax-api-client-python',
	'author_email': 'froilan.co@orangeandbronze.com',
	'version': '2.0',
	'install_requires': ['suds'],
    'tests_require': ['mockito'],
	'packages': ['pymonopond'],
}

setup(**config)
