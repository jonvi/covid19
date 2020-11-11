import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def plot(df):
    df_long=pd.melt(df, id_vars=['veckonummer', 'KnNamn'], value_vars='antal_fall_per10000_inv') # 'antal_fall_per10000_inv'
    print(df)
    print(df_long)
    #df_lkpg = df[df["Kommun_stadsdel"] == 'Linköping']
    #df_sthlm = df[df["Kommun_stadsdel"] == 'Stockholm']
    fig = px.line(df_long, x="veckonummer", y="value", color='KnNamn', title='c19')

    #fig.add_scatter(x=df_sthlm["veckonummer"], y=df_sthlm["nya_fall_vecka"], name='Stockholm')

    fig.show()