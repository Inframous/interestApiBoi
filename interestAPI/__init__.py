from flask import Flask
 
app = Flask(__name__)

from interestAPI import routes
routes.refresh_data()