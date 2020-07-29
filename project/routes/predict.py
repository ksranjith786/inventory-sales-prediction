from flask import Blueprint, request, jsonify
import pandas as pd

predict_bp = Blueprint('predict', __name__, url_prefix="/predict")

PREDICT_DATASET='https://github.com/ksranjith786/inventory-sales-prediction/raw/master/data/predictions.csv'
df = pd.read_csv(PREDICT_DATASET)

@predict_bp.route('', methods=['GET'])
def predictFilter():
    skuInput = request.args.get('SKU', type=str)
    noOfPredictionsInput = request.args.get('noOfPredictions', default=2, type=int)
    print(skuInput)
    TYPE = "WEEK"
    if skuInput is None:
        return "Incorrect with URL; Use SKU as a Query Parameter; E.g. http://127.0.0.1:5000/predict?SKU=OFF-ST-10001809"
    else:
        df_out = pd.DataFrame(columns=['Type', 'Period', 'Quantity'])
        p = 1
        print(df.loc[df.loc[:, 'SKU'] == skuInput, 'yhat_upper'].values)
        for y in df.loc[df.loc[:, 'SKU'] == skuInput, 'yhat_upper'].values[-1 * noOfPredictionsInput:]:
            df_out = df_out.append({'Type': TYPE, 'Period': p, 'Quantity': round(y)}, ignore_index=True)
            p += 1
        df_out['SKU'] = skuInput
        df_out['ProductName'] = df.loc[df.loc[:, 'SKU'] == skuInput, 'ProductName'].values[0]
    return jsonify(df_out.to_dict('records'))

    return ""
# end predictFilter