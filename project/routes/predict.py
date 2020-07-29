from flask import Blueprint, render_template
from fbprophet import Prophet
predict_bp = Blueprint('predict', __name__, url_prefix='/predict')

@predict_bp.route('/', methods=['GET', 'POST'])
def predict():
    print(dir(Prophet))
    return "Prediction in Progress"
# end predict
