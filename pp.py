from flask import Flask 
import pandas as pd
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

pd.set_option('display.max_colwidth', None)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv',sep = '\t')

app=Flask(__name__)

@app.route('/')
def home():
    profile = ProfileReport(df, title='Heart Data', explorative=True)
    return profile.to_html()

if __name__=='__main__':
    app.run(debug=True)