from flask import Blueprint, render_template
from fbprophet import prophet
predict_bp = Blueprint('predict', __name__, url_prefix='/predict')

@predict_bp.route('/', methods=['GET', 'POST'])
def predict():
    print(prophet.__version__)
    return "Prediction in Progress"
# end predict
