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
    print(skuInput)
    TYPE = "WEEK"
    if skuInput is None:
        return "Error with URL; E.g. http://127.0.0.1:5000/predict?SKU=OFF-PA-10001970"
    else:
        df_out = pd.DataFrame(columns=['Type', 'Period', 'Quantity'])
        p = 1
        print(df.loc[df.loc[:, 'SKU'] == skuInput, 'yhat_upper'].values)
        for y in df.loc[df.loc[:, 'SKU'] == skuInput, 'yhat_upper'].values:
            df_out = df_out.append({'Type': TYPE, 'Period': p, 'Quantity': round(y,0)}, ignore_index=True)
            p += 1

    return jsonify(df_out.to_dict('records'))

    return ""
# end predictFilter

get_config(app)

register_blueprint(app, blueprints)

#db.init_app(app)

if __name__ == '__main__':
    app.run()
