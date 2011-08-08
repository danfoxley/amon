from jinja2 import Environment, FileSystemLoader
from settings import TEMPLATES_DIR
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
from datetime import datetime
import re

# Custom filters
def dateformat(value, format='%d-%m-%Y-%H:%M'):
	# Converts unix time to a readable date format
	_ = datetime.fromtimestamp(value)
	return _.strftime(format)

def timeformat(value, format='%H:%M'):
	# Converts unix time to a readable 24 hour-minute format
	_ = datetime.fromtimestamp(value)
	return _.strftime(format)

def to_int(value):
	number = re.compile('(\d+)')
	
	try:
		_int = number.search(value).group(1)
	except:
		_int = 0

	return _int

def render(*args, **kwargs):
		
	env.filters['time'] = timeformat
	env.filters['date'] = dateformat
	env.filters['to_int'] =  to_int

	if 'name' in kwargs:
		template = env.get_template(kwargs['name'])
	else:
		template = env.get_template('blank.html')

	return template.render(*args, **kwargs)
