from Sprint import Sprint

for budget in range(100):
    won = 0
    total = 0
    for x in range(1000):
        s = Sprint(budget)  
        if s.runSilent():
            won = won +1
        total = total +1

    print("At "+ str(budget) +" You double your money " + str(won/total) + " percent of the time." + str(won) + " ; " + str(total))