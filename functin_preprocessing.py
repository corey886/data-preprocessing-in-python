import pandas as pd
from tqdm import tqdm

import numpy as np
from sklearn.impute import SimpleImputer

from sklearn.preprocessing import LabelEncoder


def dataPreprocess(inputDataFrame=pd.DataFrame(), doSimpleImputer=False, dropNa=False):
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
    print('update datatype')
    for ii in tqdm(range(len(inputDataFrame.columns))):
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

    if doSimpleImputer == True:
        print('update SimpleImputer')
        imr = SimpleImputer(missing_values=np.nan, strategy='mean')
        imr = imr.fit(inputDataFrame[transCol])
        inputDataFrame[transCol] = imr.transform(inputDataFrame[transCol])

    if dropNa == True:
        inputDataFrame = inputDataFrame.dropna()

    return inputDataFrame


def NonNumerical2Label(inputDf):
    transEncoder = pd.DataFrame()

    inColumn = inputDf.columns
    hsList = inputDf.dtypes
    for ii in range(len(inColumn)):
        if str(hsList[ii]) == 'float64':
            1+1
        else:
            '''print(hsList[ii])
            print(inColumn[ii])
            print()'''

            gLabBinEnco = LabelEncoder()
            trn = gLabBinEnco.fit(inputDf[inColumn[ii]])
            aaa = trn.transform(inputDf[inColumn[ii]])

            # print(aaa)
            # print(inputDf[inColumn[ii]])
            ppp = list(trn.classes_)
            print('Column : '+inColumn[ii])
            print(ppp)
            print(trn.transform(ppp))

            print('- '*20)
            print()

            transEncoder.loc[0, inColumn[ii]] = trn

    return transEncoder


def labelTransform(dfData, skEncoder):
    '''print('sample column: class label')
    print(dfData['class label'])

    ypEnc = skEncoder.iloc[0]['class label']

    print('label to number')
    sample01 = ypEnc.transform(dfData['class label'])
    print(sample01)

    print('number to label (inverse)')
    sample02 = ypEnc.inverse_transform(sample01)
    print(sample02)'''

    for ii in tqdm(skEncoder.columns):
        dfData[ii] = skEncoder.iloc[0][ii].transform(dfData[ii])

    return dfData



