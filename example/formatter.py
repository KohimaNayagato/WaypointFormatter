EgapNumber = 1



with open('input.txt', 'r') as istr:
    with open('output.txt', 'w') as ostr:
        for i, line in enumerate(istr):
            # Get rid of the trailing newline (if any).
            line = line.rstrip('\n')
            
            if i + 1 < 9999999999999999:
                #line += ' overworld'
                line = '.waypoint add waypoint' + str(EgapNumber) + ' ' + line + ' overworld'
                EgapNumber += 1 
                
            print(line, file=ostr)
