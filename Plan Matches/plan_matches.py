import sys

graph_file=sys.argv[1]
contents =open(graph_file)

#find the number of lines in the text file
num_lines=0
for line in open(graph_file):
    num_lines=num_lines+1

#map matches contains for every team a list of the days in which they already have a match
matches={}
final_table={}

#check every team couple
for line in contents:

    #split the couple of teams
    nodes = [x for x in line.split()]

    #check if the teams are already in the dictionary
    if nodes[0] not in matches.keys():
        #create an entry for team 0 if its not found before
        matches.update({nodes[0]: []})
    if nodes[1] not in matches.keys():
        #create an entry for team 1 if its not found before
        matches.update({nodes[1]: []})

    #the number of days cannot be biger than the total number of matches
    #start from day 0 and go up until you find a day where neither team plays a match
    for i in range(num_lines+1):
        #check if team 0 has a match in day i
        if i not in matches.get(nodes[0]):
            #if not,check if team 1 doesn't either
            if i not in matches.get(nodes[1]):
                #if not, update map matches for both teams
                matches.get(nodes[0]).append(i)
                matches.get(nodes[1]).append(i)
                #check the alphabetical order of the coyple and update final_table
                if nodes[0]<nodes[1]:
                    final_table.update({'('+nodes[0]+', '+nodes[1]+')':i})
                else:
                    final_table.update({'('+nodes[1]+', '+nodes[0]+')':i})
                #break the loop and go check the next couple
                break
            else:
                continue

#put the coyples in alphabetical order
sorted_keys=sorted(final_table.keys())
for j in sorted_keys:
    print(j,final_table[j])

contents.close()
