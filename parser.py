import pandas as pd

def loadData():
    df = pd.read_excel(io="Folkhalsomyndigheten_Covid19.xlsx", sheet_name="Veckodata Kommun_stadsdel")
    df = df[["veckonummer", "KnNamn", "Kommun_stadsdel", "antal_fall_per10000_inv"]]
    return df

def divideData(df, cities=None):
    if cities is None:
        cities = ['Stockholm', 'Göteborg', 'Malmö', 'Umeå', 'Linköping', 'Norrköping', 'Jönköping']
    df = df[df['KnNamn'].isin(cities)]
    df = df.groupby(['veckonummer', 'KnNamn'], as_index=False).sum()
    print("vvvvvvvvvvvvvv")
    print(df)
    print("^^^^^^^^^^^^^^")
    return df

def sanitizeData(df):
    return df.dropna()


if __name__ == "__main__":
    df = loadData()
    df = divideData(df)
    df = sanitizeData(df)