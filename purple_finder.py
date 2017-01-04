#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:35:06 2017

@author: Zoe
"""
import csv
import numpy as np
colorScores = []
with open('purple_responses.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        colorScores.append(row)
f.close()
processedScores=[]
for j in range(len(colorScores)):
    processedScores.append([])
    for i in range(len(colorScores[j])):
        processedScores[j].append(int(colorScores[j][i]))
finalScores = []
for row in processedScores:
    finalScores.append(np.asarray(row))
    
red = int(input('enter the red value: '))
green = int(input('enter the green value: '))
blue = int(input('enter the blue value: '))

    
inputColor = np.asarray([red,green,blue])

k=4

distList = []
for i in range(len(finalScores)):
    dist = np.linalg.norm(inputColor-finalScores[i][0:3])
    distList.append(dist)

nearestNeighborsList = []
for j in range(k):
    nearestNeighborsList.append(distList.index(min(distList)))
    distList.remove(min(distList))
    
total = 0
for l in range(k):
    total = total + finalScores[nearestNeighborsList[l]][3]

average = total/k

if average < 0.5:
    print("probably not purple")
else:
    print("probably purple")
