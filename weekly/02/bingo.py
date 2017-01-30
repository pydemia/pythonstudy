
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

tmp = Bingo(1, 50, (5, 5))

tmp.guess(1)
tmp.guess(2)
tmp.guess(3)
tmp.guess(4)
tmp.guess(5)
tmp.guess(6)
tmp.guess(7)
tmp.guess(8)
tmp.guess(9)
tmp.guess(25)
tmp.guess(20)
tmp.guess(14)
tmp.guess(29)
tmp.guess(28)
tmp.guess(31)
tmp.guess(15)
tmp.guess(10)
tmp.guess(17)
tmp.guess(18)
tmp.guess(42)
tmp.bingoTbl
tmp.printTbl

#%% Modify it: Generate another bingo table and for competition.

# 1. create another table for competition; with the same condition & size, containing the different numbers.
# 2. Count 'bingo' lines in both of tables, at the end of the 'guess' method.(print it)
# 3. make 'Bingo' competitive.
# 4. make a 'input checker step' in 'guess' method; only 'integer' can be used for the 'guess' method.
# 5. Change the 'bingo' number; from a constant to the relative to its size.

class Bingo2:

    pass

