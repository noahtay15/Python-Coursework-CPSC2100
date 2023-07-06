
import random

class Die:
    def __init__(self):
        self.value = self.roll()
    
    def roll(self):
        self.value = random.randint(1, 6)
        
    def getValue(self):
        return self.value
    

def getPerc(count, total):
    j = 2
    for i in count:
        perc = i / total * 100
        print(f"{perc:.2f}" + "% of the rolls were " + str(j))
        j += 1

die1 = Die()
die2 = Die()   
run = True
while (run):
    try:
        userinp = int(input("How many times do you want to roll? (0 to quit) \n"))
        if userinp == 0:
            run = False
        else:
            count = [0] * 11
            for i in range(1, userinp):
                die1.roll()
                die2.roll()
                roll = die1.getValue() + die2.getValue()
                if roll == 2:
                    count[0] += 1
                elif roll == 3:
                    count[1] += 1
                elif roll == 4:
                    count[2] += 1
                elif roll == 5:
                    count[3] += 1
                elif roll == 6:
                    count[4] += 1
                elif roll == 7:
                    count[5] += 1
                elif roll == 8:
                    count[6] += 1
                elif roll == 9:
                    count[7] += 1
                elif roll == 10:
                    count[8] += 1
                elif roll == 11:
                    count[9] += 1
                elif roll == 12:
                    count[10] += 1
                    
            getPerc(count, userinp)
    except:
        print("Invalid input")
        
        