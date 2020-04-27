import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import colorsys
import numpy as np

def load_data(filename):
    df = pd.read_csv(filename,
                     names=['name', 'date',
                             'r1', 'g1', 'b1',
                             'r2', 'g2', 'b2',
                             'rating'])
    return df


def symmetrize(df):
    df_copy = df.copy()
    df.columns = ['name', 'date',
                  'r2', 'g2', 'b2',
                  'r1', 'g1', 'b1',
                  'rating']
    return pd.concat([df, df_copy], axis=0)

def make_model(df):
    X = df[['r1', 'g1', 'b1', 'r2', 'g2', 'b2']]
    y = df['rating'] 
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def hue_hue_chart(ax, model):
    pass


