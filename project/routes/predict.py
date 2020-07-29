from flask import Blueprint, render_template

predict_bp = Blueprint('predict', __name__, url_prefix='/predict')

@predict_bp.route('/', methods=['GET', 'POST'])
def predict():
    return "Prediction in Progress"
# end predict
