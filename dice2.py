#!/usr/bin/env python3
# another stab at the d20 tool, this time perhaps a bit more
# of a generalized RPG tool. it's going to be more complex,
# that's for sure.
#
import sys
import random
import json
from datetime import date, datetime

today = str(date.today())

# this section is going to require some sort of check to make
# sure the user is inputting valid input. won't matter if i get
# a GUI going.
#
if len(sys.argv) == 1:
    print ("input like this XdX <modifier>")
    sys.exit()
elif len(sys.argv) == 2:
    die = sys.argv[1]
    mod = 0
elif len(sys.argv) == 3:
    die = sys.argv[1]
    mod = sys.argv[2]
else:
    print ("\nHuh?")
    print("REPLACE WITH FUNNY TEXT")
    sys.exit()

# here is where we evaluate what the user has input as dice
#
dieCount = int(die.split("d", 1)[0])
dieValue = int(die.split("d", 2)[1])

# this is where we start the json
#
rollLog = {'dice_log': []}
rollLog['dice_log'].append({
    'game date': today
})

# a loop to roll the number and type of dice per the user input
#
dieTotal = 0
count = 1

while dieCount > 0:
    # so here is our simple dice rolling logic
    #
    letsRoll = random.randint(1, dieValue) + int(mod)
    print("d", dieValue, count, ":", sep="", end="")
    print("", letsRoll)
    dieTotal = int(letsRoll) + dieTotal
    rollLog['dice_log'].append({
        'roll ID': str(datetime.now()),
        'd': dieValue,
        'value': letsRoll,
        'total': dieTotal
    })
    dieCount = dieCount - 1
    count = count + 1

# write to file, exit to shell
#
print ("\n\nRoll Total:", dieTotal)
print ("Modifier:", mod)
rollLog['dice_log'].append({
    'Roll Total': dieTotal,
    'Modifier': int(mod)
})

# with open('history.json', 'r+') as outfile:
#     json_data = json.load(outfile)
#     json_data.update(rollLog)
#     outfile.seek(0)
#     json.dump(json_data, outfile, indent=2)
sys.exit()
