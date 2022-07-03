
#each month person will get incomeand will have to pay taxes(25%)
#good/bad events will happen
#list of bad events: tree falls on home($1500) , car accident repair (2000) , broke windows and door during robbery(750),broke leg health incident(2500), unhealthly splurge(2000), lending someone money(500), sibling lost job and moves in with you for the month (2300)
#list of good events: raise in income(+.03% of income), find 1,000 dollars in the floorboards,bonus(500), lottery(500,000),money left in will(10,000), friend finally pays you back(500), win a lawsuit (100,000)

print ("Welcome to a yearly finance simulation. Press enter to input your monthly salary and savings.")

#Taking user input for salary and savings

monthlyIncome = input("Enter your monthly income: ")
#adds an empty line after the input to make the simulation easier to read
print()
#making the input an integer so values can be added and subtracted
monthlyIncome = int(monthlyIncome) 

savingsAmount = input("Enter your amount of savings: ")
print()
savingsAmount = int(savingsAmount)




import random

months = ["January:", "February:", "March:", "April:", "May:", "June:", "July:", "August:", "September:", "October:", "November:", "December:"]
k=0

for k in range(0,12):
  print("---------", months[k], "---------")
  print()

  #income
  savingsAmount = savingsAmount + monthlyIncome
  print("Initial income: $", savingsAmount)
  print()
  #taxes
  savingsAmount = savingsAmount - (monthlyIncome*0.25)
  print("Income after taxes: $", savingsAmount)
  print()
  #Subtract money event probabilities

  #generates a random number between x and y inclusive and if that number is > than z, the event will occur
  homeDamage = random.randint(0,100)
  if homeDamage > 80:
    print("Oh no! Looks like a tree crashed into your house! -$1500 for repairs.")
    print()
    #subtracts cost from savings
    savingsAmount = savingsAmount - 1500

  carRepair = random.randint(0,100)
  if carRepair > 90:
    print("You were involved in a small car accident and have to pay for repairs. -$2000")
    print()
    savingsAmount = savingsAmount - 2000

  robberyRepairs = random.randint(0,200)
  if robberyRepairs > 120:
    print("Your house was broken into. The burglar broke two windows and your front door. -$750 for repairs.")
    print()
    savingsAmount = savingsAmount - 750  
  
  brokenLeg = random.randint(0,70)
  if brokenLeg > 50:
    print("You fell down the stairs at work and break your leg. -$2500 for the hospital bill and cast.")
    print()
    savingsAmount = savingsAmount - 2500

  unhealthySplurge = random.randint(0,500)
  if unhealthySplurge > 130:
    print("You saw that your friend from high school is now happily married with seven kids. You realize that you're in your thirties and still alone. You splurge on takeout to eat away your feelings. -$2000")
    print()
    savingsAmount = savingsAmount - 2000

  lentMoney = random.randint(0,300)
  if lentMoney > 75:
    print("Your co-worker says they're in a rut and needs some money. Since they're extremely muscular, you give them some out of fear. -$500")
    print()
    savingsAmount = savingsAmount - 500

  freeloader = random.randint(0,50)
  if freeloader > 25:
    print("Your brother lost his job again and guilts you into letting him leech off of you for the month. -$2300")
    print()
    savingsAmount = savingsAmount - 500



  #Add money events probabilities

  floorboardMoney = random.randint(0,200)
  if floorboardMoney > 115:
    print("You couldn't sleep and decided to rip up your floorboards at 3:00 a.m. and found $1000. +$1000")
    print()
    #adds money to savings
    savingsAmount = savingsAmount + 1000

  lottery = random.randint(0,10000)
  if lottery > 9473:
    print("You won the lottery! +$500,000")
    print()
    savingsAmount = savingsAmount + 500000

  grandpasDead = random.randint(0,50)
  if grandpasDead > 20:
    print("Great news! Kind of. A very distant relative of your's passed away and left you $10,000 in their will! +$10,000")
    print()
    savingsAmount = savingsAmount + 10000

  moneyBack = random.randint(0,200000000)
  if moneyBack > 99999999:
    print("Your friend finally paid you back for when you lended them money to buy a PS2 that you two would 'share' in middle school. +$299")
    print()
    savingsAmount = savingsAmount + 299

  winLawsuit = random.randint(0,700)
  if winLawsuit > 578:
    print("You win a lawsuit. About what? I'm not sure. +$100,000")
    print()
    savingsAmount = savingsAmount + 100000
  
  
    

  print("Remaining money in savings: $" + str(savingsAmount))
  print()

  input("Hit enter to see next month.")
  print()

print("*********END OF SIMULATION*********")