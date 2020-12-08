# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:17:06 2020

@author: Bartosz Durys
"""

from fuzzywuzzy import fuzz

class Searcher():
    def DictionarySort(self, dictionary):
        return sorted(dictionary.items(), key = 
             lambda kv:(kv[1], kv[0]), reverse=True)
    
    def Search(self, inputText, titleList, tagStringList):
        score = self.SearchManager(inputText, titleList, tagStringList)
        return score
        
    def SearchManager(self, inputText, titleList, tagStringList):
        score = {}
        for noteIndex in range(len(titleList)):
            score[noteIndex] = 0
            score[noteIndex] += fuzz.token_set_ratio(
                titleList[noteIndex], inputText)
            score[noteIndex] += fuzz.token_set_ratio(tagStringList[noteIndex],
                                              inputText)
        return self.DictionarySort(score)
