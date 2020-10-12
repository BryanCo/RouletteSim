
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

class Sprint:
    def __init__(self, budget):
        self.budget = budget
        self.bet = 1
        self.winnings = 0
        self.lowpoint = 0
        self.rounds = 0
        self.numlost = 0
        self.numwon = 0

    def run(self):
        while self.winnings - self.bet > (0 - self.budget) and self.winnings < self.budget:
            self.winnings = self.winnings - self.bet
            if self.winnings < self.lowpoint:
                self.lowpoint = self.winnings
            r = RouletteWheel(self.bet, 'black')
            result = r.spin()
            thisbet = self.bet
            if result == 0:
                self.bet = self.bet *2
                lost = 'Lost'
                self.numlost = self.numlost+1
            else:
                self.winnings = self.winnings + result
                self.bet = 1
                lost = 'Won'
                self.numwon = self.numwon+1
            print( "You Bet: " + str(thisbet) + " and "+ lost + "; Winnings: " + str(self.winnings) + " Lowpoint: " + str(self.lowpoint))
            self.rounds = self.rounds + 1
        print("Number of rounds: " + str(self.rounds) + " Number of wins: " + str(self.numwon) + " Number of losses: " + str(self.numlost))

    def runSilent(self):
        while self.winnings - self.bet > (0 - self.budget) and self.winnings < self.budget:
            self.winnings = self.winnings - self.bet
            if self.winnings < self.lowpoint:
                self.lowpoint = self.winnings
            r = RouletteWheel(self.bet, 'black')
            result = r.spin()
            thisbet = self.bet
            if result == 0:
                self.bet = self.bet *2
                lost = 'Lost'
                self.numlost = self.numlost+1
            else:
                self.winnings = self.winnings + result
                self.bet = 1
                lost = 'Won'
                self.numwon = self.numwon+1
            self.rounds = self.rounds + 1
        if self.winnings >= self.budget:
            return True
        else:
            return False

for budget in range(100):
    won = 0
    total = 0
    for x in range(1000):
        s = Sprint(budget)
        if s.runSilent():
            won = won +1
        total = total +1

    print("At "+ str(budget) +" You double your money " + str(won/total) + " percent of the time." + str(won) + " ; " + str(total))