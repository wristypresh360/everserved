from flask import Flask
from config import Config
import os 
from flask_mail import Mail, Message

app = Flask(__name__,
			template_folder = '../template',
      		static_folder = '../static')

mail = Mail(app)
app.config.from_object(Config)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'thecheftee00@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('chef_pass')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

#calling the secret_key
app.config.from_object(Config)

#instantiate the mail
mail = Mail(app)

from app import main