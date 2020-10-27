from RouletteWheel import RouletteWheel

class Sprint:
    def __init__(self, budget):
        self.budget = budget
        self.bet = 1
        self.winnings = 0
        self.lowpoint = 0
        self.rounds = 0
        self.numlost = 0
        self.numwon = 0
    
    #subtract the bet from the winnings pot, record if this is the low point, and run the roulette spin
    def placeBet(self, pick):
        self.winnings = self.winnings - self.bet
        if self.winnings < self.lowpoint:
            self.lowpoint = self.winnings
        roulette = RouletteWheel(self.bet, pick)
        return roulette.spin()
    
    #act on the result of the spin
    def actOnResult(self, result):
        if result == 0:
            self.bet = self.bet *2
            self.numlost = self.numlost+1
        else:
            self.winnings = self.winnings + result
            self.bet = 1
            self.numwon = self.numwon+1
    
    #place bets until budget is gone or doubled
    #print results after each spin
    def run(self):
        while self.winnings - self.bet > (0 - self.budget) and self.winnings <= self.budget:
            result = self.placeBet('black')
            thisbet = self.bet
            self.actOnResult(result)
            if result == 0:
                lost = "lost"
            else:
                lost = "won"
            print( "You Bet: " + str(thisbet) + " and "+ lost + "; Winnings: " + str(self.winnings) + " Lowpoint: " + str(self.lowpoint))
            self.rounds = self.rounds + 1
        print("Number of rounds: " + str(self.rounds) + " Number of wins: " + str(self.numwon) + " Number of losses: " + str(self.numlost))

    #place bets until budget is gone or is doubled
    #run silently and just report true if budet is doubled or false if budget is lost
    def runSilent(self):
        while self.winnings - self.bet > (0 - self.budget) and self.winnings < self.budget:
            result = self.placeBet('black')
            thisbet = self.bet
            self.actOnResult(result)
            self.rounds = self.rounds + 1
        if self.winnings >= self.budget:
            return True
        else:
            return False


