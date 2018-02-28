# skyscraper-solver
Brute force solver for skyscraper puzzles in python3.  
Tested in python3.6.  
The solver builds a list of possible rows for each row. It then tries every combination of these rows to check if it is a valid solution to the puzzle. For each attempt the attempt number and total number of possible solutions is printed.

# how to
there are two ways to run the solver:  
* circular input of the views, clockwise starting from the left number on the top row  
```
skyscraper.py <dimension> c<circular views>  
```
* left, right, top, bottom input, where left and right are written from top to bottom, and top and bottom from left to right, the order of the l, r, t, b in the input does not matter  
```
  skyscraper.py <dimension> l<left views> r<right views> t<top views> b<bottom views>  
```
* a zero view indicates that the view was not given  

# examples
```
python3 skyscraper.py 5 c12432441322122532321
(5, 4, 1, 3, 2)
(4, 5, 3, 2, 1)
(3, 2, 4, 1, 5)
(2, 1, 5, 4, 3)
(1, 3, 2, 5, 4)
python3 skyscraper.py 5 l12323 r44132 t12432 b52212
(5, 4, 1, 3, 2)
(4, 5, 3, 2, 1)
(3, 2, 4, 1, 5)
(2, 1, 5, 4, 3)
(1, 3, 2, 5, 4)
python3 skyscraper.py 5 c0000300320000235020
(2, 4, 5, 3, 1)
(5, 3, 1, 2, 4)
(3, 5, 4, 1, 2)
(4, 1, 2, 5, 3)
(1, 2, 3, 4, 5)
python3 skyscraper.py 5 l30205 r00320 t00003 b32000
(2, 4, 5, 3, 1)
(5, 3, 1, 2, 4)
(3, 5, 4, 1, 2)
(4, 1, 2, 5, 3)
(1, 2, 3, 4, 5)
```
