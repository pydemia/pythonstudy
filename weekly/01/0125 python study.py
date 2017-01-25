#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ggg="""
Created on Wed Jan 25 19:49:47 2017

@author: dawkins
"""

word = "starbucks"
print(word)
len(word)
word[0]
y=[1.,.2,3.5,4]
y
c=(1,2,3,4)
c
y[0]=2
y.append(5)
y.pop(3)
y
a=list(word)
a
word
youngju = "_"*len(word)
wordlist = list(word)
wordlist
hiddenlist = list(hidden)
hiddenlist

#%%

list(range(len(wordlist)))

wordlist[3]


#%%
def guess(cht):
    if isinstance(cht, str):
        global count 
        count -= 1
        for i in range(len(wordlist)):
            if wordlist[i] == cht:
                hiddenlist[i] = wordlist[i]
                print("conglatulation!")
            else:
                print("What the hell")
    else:
        print("Fool!")

#%%
count = 3

def guess(cht):
    try:
        assert isinstance(cht, str)
        cht = cht.lower()
        global count 
        count -= 1
        for i in range(len(wordlist)):
            if wordlist[i] == cht:
                hiddenlist[i] = wordlist[i]
                print("conglatulation!")
            else:
                print("What the hell")
    except AssertionError:
        print("Fool!")

hiddenlist    
import numpy as np
aaa = np.empty((2,3))
np.mean(aaa)
aaa.mean()
#%%
def guess(cht):
    try:
        assert isinstance(cht, str)
        cht = cht.lower()
        global count 
        count -= 1
        for i in range(len(wordlist)):
            if wordlist[i] == cht:
                hiddenlist[i] = wordlist[i]
                print("conglatulation!")
            else:
                print("What the hell")
    except AssertionError:
        print("Fool!")


#%%

guess()
guess(7)

count

guess("t")

count    
aaa.unique()
#%%

a = 'H'
a = a.lower()
a    

    
