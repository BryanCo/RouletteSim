import random

class RouletteWheel:
    def __init__(self, bet, pick):
        self.bet = bet
        self.pick = pick

    def assessSpin(self, pick, spin):
        if pick == 'black':
            if(spin == 2 or spin == 35 or spin == 4 or spin == 33 or spin == 6 or spin == 31 or spin == 8 or spin == 29 or spin == 10 or spin == 13 or spin == 24 or spin == 15 or spin == 22 or spin == 17 or spin == 20 or spin == 11 or spin == 26 or spin == 28):
                return True
            else:
                return False
        else:
            #TODO add more casses
            return False
    
    def spin(self):
        spinResult = random.randint(1,38)
        if self.assessSpin(self.pick, spinResult):
            return self.bet*2
        else:
            return 0


