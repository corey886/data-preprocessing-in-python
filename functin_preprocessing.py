import pandas as pd
from tqdm import tqdm

import numpy as np
from sklearn.impute import SimpleImputer

from sklearn.preprocessing import LabelBinarizer


def dataPreprocess(inputDataFrame=pd.DataFrame(), doSimpleImputer=0):
    inputDataFrame['xInd'] = range(len(inputDataFrame))
    nColumName = inputDataFrame.columns

    print('replace all empty null nan')
    for ii in tqdm(range(len(inputDataFrame))):
        for jj in range(len(nColumName)):
            if inputDataFrame.iloc[ii][jj] == None or len(str(inputDataFrame.iloc[ii][jj]).strip()) < 1:
                inputDataFrame.loc[ii, nColumName[jj]] = np.nan
            else:
                try:
                    cds = str(inputDataFrame.iloc[ii][jj]).strip()
                    inputDataFrame.loc[ii, nColumName[jj]] = float(cds)
                except:
                    1+1

    transCol = []
    for ii in range(len(inputDataFrame.columns)):
        try:
            inputDataFrame[nColumName[ii]] = pd.to_numeric(
                inputDataFrame[nColumName[ii]])
            transCol.append(nColumName[ii])
        except:
            inputDataFrame[nColumName[ii]
                           ] = inputDataFrame[nColumName[ii]].astype(str)
            inputDataFrame[nColumName[ii]] = inputDataFrame[nColumName[ii]].str.replace(
                "nan", "")
            # print(nColumName[ii])

    if doSimpleImputer == 1:
        imr = SimpleImputer(missing_values=np.nan, strategy='mean')
        imr = imr.fit(inputDataFrame[transCol])
        inputDataFrame[transCol] = imr.transform(inputDataFrame[transCol])

    inputDataFrame = inputDataFrame.drop(columns=['xInd'])
    return inputDataFrame
