import re
from Matrice import *

def destringifyTupleData(d):
    return [tuple(destringifyList(l)) for l in d]

def destringifyList(l):
    return map(int, l)

def get_data(data_file):
    data = []
    with open(data_file, "r+") as csvfile:
        for row in csvfile:
            data.append(re.sub('\n', '', row).split(','))
    del data[0]
    i = 0
    j = 0
    data_int = []
    for i in range(0, len(data)):
       for j in range(0, 2):      
           data[i][j] = int(data[i][j])
    matrices = Matrice(data)