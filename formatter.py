# Created by KohimaNayagato on 14/10/2020

number = int(input("How many coordinates are you formatting?\n"))
name = input("What is the name of the file you wish to format? (Include Extension)\n")
waypointname = input("What do you wish to name the Waypoints? e.g egap = egap1, egap2, egap3 etc\n")

with open(str(name), 'r') as inputstring:
    with open('output.txt', 'w') as outputstring:
            while 0 < number:
                for i, line in enumerate(inputstring):
                    number = number - 1
                    line = line.strip("Dungeon Chest with ench gapple at: Minecart with ench gapple at: \n")
                    line = '.waypoint add ' + waypointname + str(number) + ' ' + line + ' overworld'
                    print(line, file=outputstring)
                    print("Line " + str(number) + ": Formatting completed without errors")
                    if number == 0:
                        quit()
