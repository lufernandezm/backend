import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/flask-app-template/')
from template import create_app
application = create_app()
