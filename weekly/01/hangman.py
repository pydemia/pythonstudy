class Hangman:

    def __init__(self, word, chance=5):

        assert isinstance(word, str)
        assert isinstance(chance, int)

        self.answer = word.lower()
        self.remains = chance
        self.history = []
        self._marker = ['_ '] * len(self.answer)

        self._mrkstr = ''.join(self._marker)
        self.messege = self._mrkstr + '(Chance: {})'.format(self.remains)

        print(self.messege)

    def guess(self, character):

        assert isinstance(character, str)
        assert len(character) == 1
        
        character = character.lower()

        if character in self.history:

            print('Already spoken!')

        else:

            self.remains -= 1
            self.history.append(character)

            if character in self.answer:

                print('Correct!')
                idx = [i for i, x in enumerate(self.answer) if x == character]
                for i in idx:
                    self._marker[i] = self.answer[i] + ' '
                    self._mrkstr = ''.join(self._marker)
                    self.messege = (self._mrkstr +
                                    '(Chance: {})'.format(self.remains))
                print(self.messege)

            else:
                print('Wrong!')
                self.messege = (self._mrkstr +
                                '(Chance: {})'.format(self.remains))
                print(self.messege)

            if '_ ' not in list(self._marker):

                print('\nYou win!')
                print('Answer: ' + self.answer)

            elif self.remains == 0:

                print('\nYou lose!')
                print('Answer: ' + self.answer)


quiz1 = Hangman('abstract', chance=7)
quiz1
quiz1.guess('a')
quiz1._marker
quiz1.guess('x')
quiz1.guess('c')
quiz1.guess('s')
quiz1.guess('r')

quiz1.guess('q')
quiz1.guess('w')
quiz1.guess('p')

quiz1.guess('t')
quiz1.guess('b')
quiz1.history
quiz1.answer



quiz1 = Hangman('Hello')
quiz1.guess('t')
quiz1.guess('H')
quiz1.guess('e')
quiz1.guess('l')
quiz1.guess('o')
