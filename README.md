# inventory-sales-prediction


## LIVE on

https://inventory-sales-prediction.herokuapp.com

Please click [here](https://inventory-sales-prediction.herokuapp.com) to view the LIVE app.

## Team
Sai Borusu (Product Owner)
Dharma J (Engineer)
Ranjith KS (Engineer)

## Source checkout
```
git clone https://github.com/ksranjith786/inventory-sales-prediction.git
cd inventory-sales-prediction
```
### Creates a virtual env
```
python -m venv venv
```
Note: _If virutal environment **venv** not available then install it using **python -m pip venv**_

### Switch/Activate to venv
```
source venv/Scripts/activate
```

### Install the Python modules
```
pip install -r requirements.txt
```

## Execution Steps
```
export FLASK_ENV=development
python project/app.py
```
You can now view on http://127.0.0.1:5000/

## Initial Steps
The below are the steps I have done when I initially started creating this project.
```
python -m venv venv
source venv/Scripts/activate

python -m pip install --upgrade pip
python -m pip install flask
python -m pip install gunicorn
python -m pip install pandas
python -m pip install cython
python -m pip install pystan
python -m pip install fbprophet

python -m pip freeze > requirements.txt
