import sys
import site

site.addsitedir('/var/www/flaskapp/lib/python3.6/site-packages')
site.addsitedir('/home/ec2-user/jsh/env/lib/python3.6/site-packages')

sys.path.insert(0, '/var/www/flaskapp')

from app import app as application