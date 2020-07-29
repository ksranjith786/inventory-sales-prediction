import os 

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI="DRIVER={ODBC Driver 17 for SQL Server};SERVER=hackathon2020-paymentors.database.windows.net;DATABASE=RetailInventory;UID=paymentors;PWD=ncrhyd2020@"
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#@"Server=tcp:hackathon2020-paymentors.database.windows.net,1433;Initial Catalog=RetailInventory;Persist Security Info=False;User ID=paymentors;Password=ncrhyd2020@;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";
