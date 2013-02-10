Thanks to the e-mail collaboration between chris/eric/tyler/austin I was able to get my VM running. Running the db initialize step from my VM seemed to be one solution to my configuration woes. :: https://github.com/cewing/training.python_web/blob/master/source/presentations/week05.rst#initialize-the-db-irl

In a moment of desperation I installed Flask at root. I know it is taboo, but after 5 hours of 
debugging I was willing to try anything. 

You can give flaskr a try here: http://block647060-3is.blueboxgrid.com/

I made no modifications to the code offered on git. 


My flaskr.wsgi (thanks eric!):

**/var/www/flaskr.wsgi**

#!/usr/bin/python

import sys
sys.path.insert(0, '/home/uw/flaskrenv/venv/lib/python2.6/site-packages/flask')
sys.path.insert(0, '/home/uw/flaskrenv/flaskr')
sys.path.insert(0, '/usr/lib/python2.6')
sys.path.insert(0, '/usr/lib/python2.6/plat-linux2')
sys.path.insert(0, '/usr/lib/python2.6/lib-tk')
sys.path.insert(0, '/usr/lib/python2.6/lib-old')
sys.path.insert(0, '/usr/lib/python2.6/lib-dynload')
sys.path.insert(0, '/usr/lib/python2.6/dist-packages')
sys.path.insert(0, '/usr/lib/pymodules/python2.6')
sys.path.insert(0, '/usr/lib/python2.6/dist-packages/wx-2.8-gtk2-unicode')
sys.path.insert(0, '/usr/local/lib/python2.6/dist-packages')

from flaskr import app as application
