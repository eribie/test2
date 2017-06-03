import pandas as pd
import csv

def CreationDataframe(fichier):

    df = pd.read_csv(fichier + '.txt', delimiter=',')
    return(df)



def concatener_dataframes(fichier1,fichier2):
    DF1 = CreationDataframe("C:\\Users\\Emmanuel\\Desktop\\conculcouille\\Retraités\\" + fichier1)
    DF2 = CreationDataframe("C:\\Users\\Emmanuel\\Desktop\\conculcouille\\Retraités\\" + fichier2)

    dataframe = DF1.merge(DF2,left_on='timestamp',right_on='timestamp')

    return dataframe
