# DMST-Algorithms-and-Data-Structures-Assignments (Python)
The Algorithms in this repository are implemented in Python programming language and where written in the context of the course ‘Algorithms-and-Data-Structures’ in Athens University of Economics and Business, department of Management Science and Technology.
## Assignment No.1: Tournament planning
You can find the assignment [here](https://github.com/dmst-algorithms-course/assignment-2017-1).
In this program we must schedule the tournament so that each competitor has only one match each day. The problem is also described as the edge 'colouring problem'.
The program reads a file from cmd like this:
`python plan_matches.py graph_file`
* `graph_file` is in the form:
```
a b
a c
b c
c d
d e
e c
...
```
## Assignment: Findings groups 
You can find the assignment [here](http://nbviewer.jupyter.org/github/dmst-algorithms-course/assignment-2017-2/blob/master/assignment_2017_2.ipynb).
The program reads a file from cmd like this:
`python community_structure.py [-n GROUPS ] graph_file` and detects community structure in networks.

* `graph_file` is in the form:

```
1 3
1 10
2 3
4 10
...
```
* The `GROUPS` is the number of the teams we want to create. If we don't write any number then it's 2 teams, by default.

**More information:**
* The algorithm that we use at the exercise was added by M. E. J. Newman at the article "Fast algorithm for detecting community structure in networks", Phys. Rev. E 69, 066133, 2004. You can find it [here](https://arxiv.org/abs/cond-mat/0309508).

## Assignment: Steiner system (Steiner Triple Systems)
You can find the assignment [here](http://nbviewer.jupyter.org/github/dmst-algorithms-course/assignment-2017-3/blob/master/assignment_2017_3.ipynb).
The program reads a file from cmd like this:
`python sts.py n`
and creates a list with all blocks sorted, and their number.

**More information:**
* More information about Steiner systems you can find at this [article of Wikipedia](https://en.wikipedia.org/wiki/Steiner_system).
* you can also see this link about steiner. (http://mathworld.wolfram.com/SteinerTripleSystem.html)

