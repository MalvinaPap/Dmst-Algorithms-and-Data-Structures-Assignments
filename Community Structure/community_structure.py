import argparse
import itertools
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--Groups", type=int, help="num of teams",default=2)
parser.add_argument("filename", help="name of input file")

args = parser.parse_args()
graph_file=args.filename
teams=args.Groups

contents =open(graph_file)

#find the number of lines in the graph which is the
#number of connections between the nodes
num_lines=0
for line in open(graph_file):
    num_lines=num_lines+1


#each node initialy becomes a team
list_teams=[]
for line in contents:
    nodes = [x for x in line.split()]
    if nodes[0] not in list_teams:
        list_teams.append(nodes[0])
    if nodes[1] not in list_teams:
        list_teams.append(nodes[1])

#contains the teams and the 'ai' value of each one
ais={}

#find the initial modularity Q0
q0=0
for i in list_teams:
    a=0
    for line in open(graph_file):
        if (i+" " in line) or (i+"\n" in line) :
            a=a+1
    ais.update({i:a})
    q0=q0-(a/(num_lines*2))**2


#start calculating final modularity and teams
while len(list_teams)>teams:

    combinations=list(itertools.combinations(list_teams,2))

    maxdq=-sys.maxsize

    for comb in combinations:

        dq=-sys.maxsize

        #when both teams are single nodes
        if isinstance(comb[0],str) and isinstance(comb[1],str):
             couple=str(comb[0]+" "+comb[1])

             a1=ais.get(comb[0])
             a2=ais.get(comb[1])
             for line in open(graph_file):
                 if couple in line:
                     dq=2*((1/(num_lines*2))-(a1/(num_lines*2))*(a2/(num_lines*2)))

        #when one team is a node and the other is a group of nodes
        elif isinstance(comb[0],str) and isinstance(comb[1],list):
             a1=ais.get(comb[0])
             a2=0

             for c in comb[1]:
                a2=a2+ais.get(c)

             e12=0
             for i in comb[1]:
                 for line in open(graph_file):
                     if (comb[0]+" "+i in line) or (i+" "+comb[0] in line):
                         e12=e12+1

             #check if teams are connected
             if e12==0:
                 continue
             dq=2*((e12/(num_lines*2))-(a1/(num_lines*2))*(a2/(num_lines*2)))

        #when both teams are lists of nodes
        elif isinstance(comb[0],list) and isinstance(comb[1],list):
             a1=0
             for c in comb[0]:
                 a1=a1+ais.get(c)
             a2=0
             for c in comb[1]:
                 a2=a2+ais.get(c)

             e12=0
             for i in comb[0]:
                 for j in comb[1]:
                     for line in open(graph_file):
                        if (i+" "+j in line) or (j+" "+i in line):
                            e12=e12+1
             #check if teams are connected
             if e12==0:
                continue
             dq=2*((e12/(num_lines*2))-(a1/(num_lines*2))*(a2/(num_lines*2)))

        #update max and the couple of teams that have it

        if dq>maxdq:
            maxdq=dq
            couple_to_put_together=comb
#end of for loop

    #update table teams accordingly
    q0=q0+maxdq


    list_teams.remove(couple_to_put_together[0])
    list_teams.remove(couple_to_put_together[1])

    new_team=[]

    if isinstance(couple_to_put_together[0],str):
        new_team.append(couple_to_put_together[0])
    else:
        for comb in couple_to_put_together[0]:
            new_team.append(comb)


    if isinstance(couple_to_put_together[1],str):
        new_team.append(couple_to_put_together[1])
    else:
        for comb in couple_to_put_together[1]:
            new_team.append(comb)

    list_teams.append(new_team)

#end of while loop

#print results

help_teams=sorted(list_teams)
final_teams=[]
for team in help_teams:
    steam=[int(y) for y in team]
    final_teams.append(steam)

for team in final_teams:
    print(sorted(team))
print("Q= %.4f"%q0)

contents.close()
