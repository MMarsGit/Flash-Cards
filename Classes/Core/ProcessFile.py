# -*- coding: UTF-8 -*-

def processTxT():
    dict = {}
    with open("dataSet.txt", mode="r", encoding="UTF-8") as file:
        for line in file:
            for word in line.split():
                rawWord = word.replace(",","")
                rawWord = rawWord.replace(".","") 
                if rawWord in dict:
                    dict[rawWord] += 1
                else:
                    dict[rawWord] = 1

    return dict

def sortByFrequency(dict):
    #Check sorting algos
    #Bubble sort
    array = []
    dict = {k: v for k, v in sorted(dict.items(),key=lambda item: item[1])}
    for key, val in dict.items():
        array.append(key)
    
    array = list(reversed(array))
    return array

dict = processTxT()
sortByFrequency(dict)