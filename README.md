# nearest-neighbors-algo
This project uses python to create a nearest-neighbors algorithm. Check the README for details.
This program was created by Brett Cornick to satisfy the challenge statement at the end of this document.
______________________________________________________________________________________________

BUILD AND RUN INSTRUCTIONS:

Mac/Linux/Windows:
The application can be run from the terminal/command line from the "Nearest_Neighbors" 
directory using Python 3 (Python 3 is required since program utilizes f-strings). Simply 
run the following command:

$ python3 Nearest_Neighbors.py

The program will ask for the name of the input file. Ensure that input file is in same
directory as Nearest_Neighbors.py. A sample input file called "NN_test_input.txt" has 
already been included. Required format of input file is shown in "NN_input_format.txt".
______________________________________________________________________________________________

REASONING FOR USING SELECTED LANGUAGE:

I hope that I didn't over-simplify this challenge with my choice to use Python and the NumPy
and SciPy libraries. I have significant experience using Python to analyze large data sets, 
including projects in machine learning that utilize the nearest-neighbor algorithm and I 
knew that SciPy already contained a tool (cKDTree) that could perform this function and 
operate more efficiently than any tool I could likely create in an afternoon. This makes the
program exceptionally scalable and cKDTree includes support for parallel queries and 
pickling. Python is my language of choice for performing complex mathematical operations.

When creating the nearest neighbors algorithm, there are a few considerations to be made to
ensure that time complexity and space complexity stay low as the input dataset gets large.
First, calculating the distance between one point and ALL other points is inefficient.
Instead, quick checks can be performed on points to see if they would fall within the 
distance r (ie. if the distance along one axis is greater than r, that value can be excluded
from calculations, saving time and space). The cKDTree tool utilizes a binary tree structure
to perform this check (detailed in Maneewongvatana and Mount 1999). Additionally, ensuring
distance calculations are not performed twice for a given point pair is important, as simply
creating a program that utilizes embedded for loops to check point pair distances would surely
create unnecessary duplicate calculations. Also, while working with lists and arrays, I made
sure to delete datasets when they were no longer needed. 
______________________________________________________________________________________________
CHALLENGE
For this challenge, please write a program that takes as input:
1) a list of spatial locations (double precision 𝑥, 𝑦, and 𝑧 values) indexed by an integer 
2) node id which runs between 1 and the total number of nodes; and
3) a double precision search radius, 𝑟;
and returns a two-dimensional integer array, nndata[i, j], where the first index maps to the 
node id and the second index contains the following integer data, in turn: the number of 
neighbor nodes associated with the node id of the fast index which fall within the search 
radius, followed by the node ids of those neighbors. If you are using a column major 
programming language such as Julia or FORTRAN, you may swap the order the of the indices.
Please discuss the time and space complexity of your solution and any implementation decisions 
that you feel were important when writing your program.

Constraints:
• 1 ≤ 𝑛 ≤ 105, where 𝑛 is the number of nodes.
• {(𝑥,𝑦,𝑧) ∈ R3:−10^7 ≤ 𝑥,𝑦,𝑧 ≤ 10^7}
• The node IDs are enumerated from 1 to 𝑛.
• There are no other constraints on the input. You may format the input however you wish.

Example:
We can consider the case where one corner is at (0, 0, 0) and the far corner is at (1, 1, 1). 
The input points would then be:
#1 (0, 0, 0)
#2 (1, 0, 0)
#3 (0, 1, 0)
#4 (0, 0, 1)
#5 (1, 1, 0)
#6 (0, 1, 1)
#7 (1, 0, 1)
#8 (1, 1, 1)
#9 (0.5, 0.5, 0.5)

If we let the radius be 1.0, a completed search would give us the answer with the corresponding 
nndata array:
[num_nodes, id_1, id_2, ..., id_n]
#1 [[4,2,3,4,9],
#2 [4,1,5,7,9],
#3 [4,1,5,6,9],
#4 [4,1,6,7,9],
#5 [4,2,3,8,9],
#6 [4,3,4,8,9],
#7 [4,2,4,8,9],
#8 [4,5,6,7,9],
#9 [8,1,2,3,4,5,6,7,8]]
