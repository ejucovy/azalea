import sys

from paste.deploy.loadwsgi import loadapp

loadapp('config:' + sys.argv[1])
