import pandas as pd

def conteo_diego(tmx,valor=5):
    return len(tmx[tmx.a==valor].a)

def conteo_memo(tmx,valor=5):
    return tmx[tmx.a==valor].a.count()

def conteo_elisa(tmx):
   print( tmx.groupby("a").count())

def conteo_areli(tmx,valor=5):
    lista = []
    for i in range(len(tmx.a)):
        if (tmx.a.iloc[i] == valor):
            lista.append(tmx.a.iloc[i])
    return len(lista)

def importa_tmx(ar = "../data/temixco_2018.csv",):

    tmx = pd.read_csv(ar,header=None,
                     names=["year","month","day","hour","minute",
                           "a","b","c","d","e","f","g"],
                     parse_dates={"fecha":["year","month","day","hour","minute"]} )
    tmx.fecha = pd.to_datetime(tmx.fecha,format="%Y %m %d %H %M")
    tmx.set_index("fecha",inplace=True)
    return tmx