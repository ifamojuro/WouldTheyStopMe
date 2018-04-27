from flask import Flask
import pandas as pd

app = Flask(__name__)
data = pd.read_csv("application/static/data/raw_data.csv")
boston_data = pd.read_csv("application/static/data/boston_data_1.csv")
phili_data = pd.read_csv("application/static/data/phili_2016.csv")
noladata = pd.read_csv("application/static/data/nola_2016.csv")
la_data = pd.read_csv("application/static/data/la_2016.csv")

rows = len(data)
bos_rows = len(boston_data)
phili_rows = len(phili_data)
nola_rows = len(noladata)
la_rows = len(la_data)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

