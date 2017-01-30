
from unipy.tools.misc import splitor
import random
import numpy as np
import pandas as pd

numGen = random.sample(range(1, 26), 25)
numGen
aa = splitor(numGen, 5)
aaa = list(aa)
data = pd.DataFrame(np.array(aaa))

#%%


class Bingo:

    def __init__(self, startNum, endNum, size=(5, 5)):

        numGen = np.random.randint(startNum, high=endNum,
                                   size=size, dtype='int')
        self.bingoTbl = pd.DataFrame(numGen)
        self.printTbl = pd.DataFrame(np.full(size, np.nan)).fillna('-')
        self.history = []

    def guess(self, number):

        if number in self.history:

            print('Already spoken!')

        else:

            self.history.append(number)
            x, y = np.where(self.bingoTbl == number)

            if len(x) == 0:
                print('{num} doesn\'t exist'.format(num=number))

            else:
                print('{num} was Found!'.format(num=number))
                self.printTbl.iloc[x, y] = '#'

        bingoRow = sum([all(self.printTbl.iloc[:, i].unique() == '#')
                        for i in self.printTbl.index])
        bingoCol = sum([all(self.printTbl.iloc[j, :].unique() == '#')
                        for j in self.printTbl.columns])
        bingoDia = all(np.diagonal(np.fliplr(self.printTbl)) == '#')
        bingoRdi = all(np.diagonal(self.printTbl) == '#')

        if sum([bingoRow, bingoCol, bingoDia, bingoRdi]) == 5:

            print('\nBingo!')

#%%

aa = Bingo(1, 50, (5, 5))

aa.guess(1)
aa.guess(2)
aa.guess(3)
aa.guess(4)
aa.guess(5)
aa.guess(6)
aa.guess(7)
aa.guess(8)
aa.guess(9)
aa.guess(25)
aa.guess(20)
aa.guess(14)
aa.guess(29)
aa.guess(28)
aa.guess(31)
aa.guess(15)
aa.guess(10)
aa.guess(17)
aa.guess(18)
aa.guess(42)
aa.bingoTbl
aa.printTbl

#%% Modify it: Generate another bingo table and for competition.

# 1. create another table for competition; with the same condition & size, containing the different numbers.
# 2. Count 'bingo' lines in both of tables, at the end of the 'guess' method.(print it)
# 3. make 'Bingo' competitive.
# 4. Change the 'bingo' number; from a constant to the relative to its size.
