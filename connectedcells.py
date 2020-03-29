#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):

#---variables---

    rowLoc=[]
    columnLoc=[]
    rowReg={}
    regionCount=[]
    markDel=[]
    rowRegIndex=[]
    finalSize=[]
    columnReg={}
    columnRegIndex=[]
    fullRowIndex={} 
    fullColumnIndex={}

#---FUNCTION refines index list---

    def regionIndex(index,dictionary):
        g=0
        while g<len(index):
            if index[g] in dictionary:
                g+=1
            else:
                del index[g]

#---FUNCTION builds dictionary of column regions---
#---also builds a corresponding index list---

    def columnRegionBuilder(x,y):
        #print("running columnCombine...")
        #print(f"x={x}")
        #print(f"y={y}")
        xStr=str(x[0])+","+str(x[1])
        yStr=str(y[0])+","+str(y[1])
        columnRegIndex.append(xStr)
        columnRegIndex.append(yStr)
        #print(f"xStr={xStr}")
        #print(f"yStr={yStr}")
        #print(f"a={a}")
        #print(f"b={b}")

        
        if xStr in columnReg:
            z=columnReg[xStr]+1
            del columnReg[xStr]
            columnReg[yStr]=z
        else:
            columnReg[yStr]=2

#---FUNCTION builds a dictionary that includes each element in a row or column index
#---and corresponds that to a global index---

    def fullIndexer(index,dictionary,fullIndexName,marker):
        x=marker
        v=0
        if x=="r":
            while v<len(index):
                x=index[v]
                w=int (x[0])
                y=int (x[2])
                i=dictionary[(index[v])]
                tempList=[]
                for j in range (i):
                    tempList.append([w,y-j])
                fullIndexName[(index[v])]=tempList
                v+=1
        elif x=="c":
            while v<len(index):
                x=index[v]
                w=int (x[0])
                y=int (x[2])
                i=dictionary[(index[v])]
                tempList=[]
                for j in range (i):
                    tempList.append([w-j,y])
                fullIndexName[(index[v])]=tempList
                v+=1

#---defines list for x values of elements with 1s in them 
#---defines list for y values of elements with 1s in them

    for i in range(n):
        for j in range(m):
            if matrix [i][j] == 1:
                rowLoc.append(i)
                columnLoc.append(j)

#---identifies row regions and logs them in a dictionary

    for i in range(len(rowLoc)-1):
        if rowLoc[i]==rowLoc[i+1] and columnLoc[i]==(columnLoc[i+1]-1): #represents row connections
            #print(f"row connection at matrix[{rowLoc[i]}][{columnLoc[i]}] and matrix[{rowLoc[i+1]}][{columnLoc[i+1]}]")
            rIndex=[rowLoc[i],columnLoc[i]]
            regionCount.append(rIndex)
            rIndex=[rowLoc[i+1],columnLoc[i+1]]
            regionCount.append(rIndex)
            riStr=str(rowLoc[i])
            ciStr=str(columnLoc[i])
            rjStr=str(rowLoc[i+1])
            cjStr=str(columnLoc[i+1])
            riciStr=riStr+","+ciStr
            rjcjStr=rjStr+","+cjStr
            rowRegIndex.append(riciStr)
            rowRegIndex.append(rjcjStr)
            if riciStr in rowReg:
                #print(f"rowReg[riciStr]={rowReg[riciStr]}")
                x=rowReg[riciStr]+1
                #print(f"riciStr={riciStr}")
                #print(f"rjcjStr={rjcjStr}")
                #print(f"x={x}")
                del rowReg[riciStr]
                rowReg[rjcjStr]=x
                #print(f"rowReg[rjcjStr]={rowReg[rjcjStr]}")          
            else:
                rowReg[rjcjStr]=2

#---Index row regions---
    regionIndex(rowRegIndex,rowReg) 
    fullIndexer(rowRegIndex,rowReg,fullRowIndex,"r")

#---locates column regions---

    for j in range(len(columnLoc)-1): 
        for k in range(j+1,len(columnLoc)):
            if columnLoc[j]==columnLoc[k] and rowLoc[j]==(rowLoc[k]-1):
                #print(f"column connection at matrix[{rowLoc[j]}][{columnLoc[j]}] and matrix[{rowLoc[k]}][{columnLoc[k]}]")
                rIndex=[rowLoc[j],columnLoc[j]]
                regionCount.append(rIndex)
                rIndex=[rowLoc[k],columnLoc[k]]
                regionCount.append(rIndex)
                c=[rowLoc[j],columnLoc[j]]
                d=[rowLoc[k],columnLoc[k]]
                columnRegionBuilder(c,d)

#---index column regions---

    regionIndex(columnRegIndex,columnReg)
    fullIndexer(columnRegIndex,columnReg,fullColumnIndex,"c")

#---older list regionCount, may still be usefull---
    
    for i in range(len(regionCount)-1):
        for j in range(i+1,len(regionCount)):
            if regionCount[i]==regionCount[j]:
                markDel.append(j)
            for k in range(len(markDel)-1):
                for l in range(k+1,len(markDel)):
                    if markDel[k]==markDel[l]:
                        del markDel[l]
    
    for i in range(len(markDel)-1):
        for j in range(i+1,len(markDel)):
            if markDel [i] < markDel[j]:
                x=markDel[i]
                y=markDel[j]
                markDel[i]=y
                markDel[j]=x

    for i in range(len(markDel)):
        del regionCount[markDel[i]]

#---may be able to use this as a start for combining rows into regions---

    #for column Combination: (column combination should be a function that can combine rows
    #  which have a common column combination)
    #    a=""
    #    b=""
    #    for key,value in fullRowIndex.items():
    #        if x in value:
    #            a=key
    #        if y in value:
    #            b=key

#---print commands---
    
    #print("\n")
    #print(f"{rowLoc}\n{columnLoc}")
    #print(f"regionCount={regionCount}")
    print("\n")
    print(f"rowReg={rowReg}")
    print(f"rowRegIndex={rowRegIndex}")
    print(f"fullRowIndex={fullRowIndex}")
    print("\n")
    print(f"columnReg={columnReg}")
    print(f"columnRegIndex={columnRegIndex}")
    print(f"fullColumnIndex={fullColumnIndex}")
    print("\n")
    

    return 0

n = int(input())

m = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

result = connectedCell(matrix)

print(result)
