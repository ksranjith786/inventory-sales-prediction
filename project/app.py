from flask import Flask, Blueprint, jsonify, request
from os import environ
import pandas as pd 

from routes.home import home_bp

blueprints = (home_bp,)

app = Flask(__name__)

PREDICT_DATASET='https://github.com/ksranjith786/inventory-sales-prediction/raw/master/data/predict.csv'
df = pd.read_csv(PREDICT_DATASET)

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

@app.route('/predict', methods=['GET'])
def predictFilter():
    skuInput = request.args.get('SKU', type=str)
    print(df.columns)
    print(skuInput)
    if skuInput is None:
        return jsonify(df.to_dict('records'))
    
    return jsonify(df.loc[df.loc[:, 'SKU'] == skuInput].to_dict('records'))
# end predictFilter

get_config(app)

register_blueprint(app, blueprints)

#db.init_app(app)

if __name__ == '__main__':
    app.run()
