from flask import Flask, Blueprint, jsonify
from os import environ
from flask_sqlalchemy import SQLAlchemy
import pandas as pd 

from routes.home import home_bp

blueprints = (home_bp,)
db = SQLAlchemy()
app = Flask(__name__)

def get_config(app):
    app.config.from_pyfile('config.py', silent=True)

    envFLASK = environ.get('FLASK_ENV')
    if envFLASK == 'development':
        app.debug = True
    else:
        app.debug = False
# end get_config

def register_blueprint(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # Configure explicit url routes to home blueprint
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/home', endpoint='home')
    
# end register_blueprint

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    from routes.predict import Transaction
    PREDICT_DATASET='data/predict.csv'
    df = pd.read_csv(PREDICT_DATASET)
    #db.session()
    #trans = Transaction.query.filter_by(TransactionID="CA-2016-152156").first_or_404()
    return jsonify(df.to_dict('records'))
# end predict

get_config(app)

register_blueprint(app, blueprints)

db.init_app(app)
with app.app_context():
    from routes import predict  # Import routes

if __name__ == '__main__':
    app.run()
