number = 1
name = input("What is the name of the file you wish to format? (Include Extension)\n")
WaypointName = input("What do you wish to name the Waypoints?\n")

with open(str(name), 'r') as istr:
    with open('output.txt', 'w') as ostr:
        for i, line in enumerate(istr):
            # Get rid of the trailing newline (if any).
            line = line.rstrip('\n')
            
            if i + 1 < 9999999999999999:
                #line += ' overworld'
                line = '.waypoint add ' + WaypointName + str(number) + ' ' + line + ' overworld'
                number += 1 
                
            print(line, file=ostr)
            print("Line " + str(number) + ": Formatting completed without errors")
print("Formatting Completed without issue")