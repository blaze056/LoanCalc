from array import *
import math

def calc(loan_amount,rate,loan_period):

    Res = []
    #loan_amount = 100000
    #rate = 5
    #loan_period = 36

    RN = ((rate/12)/100)    #print(RN)

    i=0
    temp = 0
    P = []
    PP = []
    INT = []
    OB = []
    table = []

    while i<=loan_period:
        P_temp = ((RN*loan_amount)*(math.pow((1+RN), loan_period)))/((math.pow((1+RN), loan_period))-1)
        P.append(round(P_temp,2))

        PP_temp = P[i]/( math.pow((1+RN),(1+loan_period-i)))
        PP.append(round(PP_temp,2))
        INT_temp = P[i] - PP[i]
        INT.append(round(INT_temp,2))

        OB_temp = (INT[i]/RN) - PP[i]
        OB.append(round(OB_temp, 2))


        table.append([])
        if i != 0:
            table[i].append(i)
            table[i].append(P[i])
            table[i].append(PP[i])
            table[i].append(INT[i])
            table[i].append(OB[i])

        i += 1

    #print(table)
    return(table)