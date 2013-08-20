try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Python Client for Monpond',
	'author': ['JC Francisco', 'Froilan Co'],
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '2.0',
	'install_requires': ['suds'],
	'packages': ['pymonopond'],
}

setup(**config)
