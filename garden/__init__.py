from flask import Flask
app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MONGO_CONNECT'] = False
app.config['MONGO_HOST'] = '0.0.0.0'

import garden.views.plant
