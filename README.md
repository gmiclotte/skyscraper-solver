# skyscraper-solver
Brute force solver for skyscraper puzzles in python3.  
Tested in python3.6.  
The solver builds a list of possible rows for each row. It then tries every combination of these rows to check if it is a valid solution to the puzzle.

# how to
there are two ways to run the solver:  
* circular input of the views, clockwise starting from the left number on the top row  
```
skyscraper.py -s<dimension> -c<circular views>  
```
* left, right, top, bottom input, where left and right are written from top to bottom, and top and bottom from left to right, the order of the l, r, t, b in the input does not matter  
```
  skyscraper.py -s<dimension> -l<left views> -r<right views> -t<top views> -b<bottom views>  
```
* a zero view indicates that the view was not given  
* the -v[v] option can be used to add additional output, the parameter v is the amount of seconds between progress updates. -v default to -v1.  

# examples
```
python3 skyscraper.py -s5 -c12432441322122532321
[5, 4, 1, 3, 2]
[4, 5, 3, 2, 1]
[3, 2, 4, 1, 5]
[2, 1, 5, 4, 3]
[1, 3, 2, 5, 4]
python3 skyscraper.py -s5 -l12323 -r44132 -t12432 -b52212
[5, 4, 1, 3, 2]
[4, 5, 3, 2, 1]
[3, 2, 4, 1, 5]
[2, 1, 5, 4, 3]
[1, 3, 2, 5, 4]
python3 skyscraper.py -s5 -c0000300320000235020
[2, 4, 5, 3, 1]
[5, 3, 1, 2, 4]
[3, 5, 4, 1, 2]
[4, 1, 2, 5, 3]
[1, 2, 3, 4, 5]
python3 skyscraper.py -s5 -l30205 -r00320 -t00003 -b32000
[2, 4, 5, 3, 1]
[5, 3, 1, 2, 4]
[3, 5, 4, 1, 2]
[4, 1, 2, 5, 3]
[1, 2, 3, 4, 5]
./skyscraper.py -s5 -c00000000000000000000 -v10
5 [0, 0, 0, 0, 0] [0, 0, 0, 0, 0] [0, 0, 0, 0, 0] [0, 0, 0, 0, 0] 10.0
24883200000 possible solutions
progress: 7270000 / 24883200000 = 0.03%, est. max. time left: 0:09:30:56
progress: 14540000 / 24883200000 = 0.06%, est. max. time left: 0:09:42:38
progress: 21810000 / 24883200000 = 0.09%, est. max. time left: 0:09:43:43
progress: 29080000 / 24883200000 = 0.12%, est. max. time left: 0:09:47:21
progress: 36350000 / 24883200000 = 0.15%, est. max. time left: 0:09:47:16
progress: 43620000 / 24883200000 = 0.18%, est. max. time left: 0:09:50:39
Solution found after searching 47588869 / 24883200000 = 0.19% in 0:00:01:08
[1, 2, 3, 4, 5]
[2, 1, 4, 5, 3]
[3, 4, 5, 1, 2]
[4, 5, 2, 3, 1]
[5, 3, 1, 2, 4]
```
