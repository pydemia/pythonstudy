
class Bingo2:

    # 1. Create a New Bingo Game with given arguments
    def __init__(self, startNum, endNum, size=(None, None), bingoNum=5):

        # 1-0. Define a Function: Bingo Table Creator
        def tblGen(startNum, endNum, size=(5, 5)):

            # 1-0-1. Generate an array with random integers
            numGen = np.random.randint(startNum, high=endNum,
                                       size=size, dtype='int')

            # 1-0-2. Create DataFrames(Integers & Markers) with the above array
            resTbl = pd.DataFrame(numGen)
            prtTbl = pd.DataFrame(np.full(size, np.nan)).fillna('-')

            # 1-0-3. Define returning variables of this function
            return {'numTbl': resTbl, 'mrkTbl': prtTbl}

        # 1-1. Create Tables & Markers and a history table
        self.history = []
        self.bingoNum = bingoNum
        self.myBingo = tblGen(startNum, endNum, size=(5, 5))
        self.cmBingo = tblGen(startNum, endNum, size=(5, 5))

        self.myBingo['name'] = 'Player'
        self.cmBingo['name'] = 'Computer'

    # 2. Create a Method for Bingo
    def guess(self, number):

        # 2-1. Check if a number already used
        if number in self.history:

            # 2-1-1. IF 'True', THEN print a messege
            print('Already spoken!')

        else:

            # 2-1-2. IF 'False', Append it to history table & Get its indices
            self.history.append(number)
            x1, y1 = np.where(self.myBingo['numTbl'] == number)
            x2, y2 = np.where(self.cmBingo['numTbl'] == number)

            # 2-1-3. Define a Function for marking
            def marker(name, x, y, tbl):

                # 'len(x) == 0' means that array 'x' contains Nothing
                if len(x) == 0:
                    print('{nm}: {num} doesn\'t exist'.format(nm=name,
                                                              num=number))
                else:
                    # IF 'False', THEN mark it with '#', using its indices
                    print('{nm}: {num} was Found!'.format(nm=name,
                                                          num=number))
                    tbl.iloc[x, y] = '#'

            # 2-2. Apply 'marker' Function to both of tables
            marker(self.myBingo['name'], x1, y1, self.myBingo['mrkTbl'])
            marker(self.cmBingo['name'], x2, y2, self.cmBingo['mrkTbl'])

        # 2-3. Define a Function to check if 'Bingo' is done
        def checker(adict, num):

            name = adict['name']
            nTbl = adict['numTbl']
            mTbl = adict['mrkTbl']

            bRow = [all(mTbl.iloc[:, i].unique() == '#') for i in mTbl.index]
            bCol = [all(mTbl.iloc[j, :].unique() == '#') for j in mTbl.columns]
            bDia = all(np.diagonal(np.fliplr(mTbl)) == '#')
            bRdi = all(np.diagonal(mTbl) == '#')

            bingoCnt = sum(bRow + bCol + [bDia, bRdi])

            if bingoCnt >= num:
                print('\nBingo!\n{nm} Wins!'.format(nm=name))
                print(nTbl, '\t', mTbl)
                print('The game has closed.')
            else:
                print(name, 'Bingo Count: ', bingoCnt)

        # 2-4. Apply 'checker' Function to both of tables
        checker(self.myBingo, self.bingoNum)
        checker(self.cmBingo, self.bingoNum)

        def __del__(self):
            pass

#%%
tmp = Bingo2(1, 50, size=(5, 5), bingoNum=5)

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
tmp.guess(16)
tmp.guess(19)
tmp.guess(24)
tmp.guess(38)
tmp.guess(43)
tmp.guess(26)
tmp.guess(48)
tmp.guess(36)
tmp.guess(23)
tmp.guess(49)
tmp.guess(27)
tmp.guess(33)
tmp.guess(22)
tmp.guess(11)
tmp.guess(44)
tmp.guess(40)
tmp.guess(30)
tmp.guess(34)
tmp.guess(37)
tmp.guess(45)
tmp.guess(50)
tmp.guess(32)
tmp.guess(13)


tmp.myBingo['mrkTbl']
tmp.cmBingo['mrkTbl']
