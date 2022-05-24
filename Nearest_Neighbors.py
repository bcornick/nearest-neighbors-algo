#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:44:35 2020

@author: brettcornick

Submitted for evaluation by Karagozian & Case as part of interview Challenge #2.
"""

import numpy as np
import scipy.spatial as spatial


#use nearest-neighbors solver from scipy
def findIndex(pointsArray, currentPoint, r):
    point_tree = spatial.cKDTree(pointsArray)
    indices = point_tree.query_ball_point(currentPoint, r)
    return indices


#format input file into usable data
def formatInput(inputFile):
    with open(inputFile,'r') as i_f:
        read_data = i_f.readlines()
        pointsList = []
        r = float(read_data.pop(0))
        n = int(read_data.pop(0))
        index = 1
        for i in read_data:
            i = i.replace(f'#{index}(','')
            i = i.replace(')','')
            i = i.replace('\n','')
            x = float(i.split(',')[0])
            y = float(i.split(',')[1])
            z = float(i.split(',')[2])
            pointsList.append([x,y,z])
            index += 1
        return (r,n,pointsList)
    

def main():  
    filename = input('Please enter the name of the input file: ')
    (r, n, pointsList) = formatInput(filename)
    pointIndex = 0
    allIndices = []
    for currentPoint in pointsList:
        pointsArray = np.array(pointsList)
        indices = findIndex(pointsArray,currentPoint, r)
        indices.remove(pointIndex)
        fixedIndices = list(map(lambda x : x + 1, indices))
        numNodes = len(fixedIndices)
        fixedIndices.insert(0, numNodes)
        indicesArray = np.array(fixedIndices)
        allIndices.append(indicesArray)
        pointIndex += 1
        del pointsArray
        del indicesArray
        del fixedIndices
        del indices
        
    outArray = np.array(allIndices)
    del allIndices
    del pointsList
    
    print('Output:\n\n')
    print(outArray)
    print('\n\nAll done!')

if __name__ == '__main__': 
    main() 

