[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ts0Me_yD)

This is the implementation given to Assignment 1 of the Formal Languages and Compilers course by students *Samuel Acosta Aristizabal* and *Katherin Nathalia Allin Murillo*.

Below we can see the content of the assignment and references

# Formal Languages and Compilers
#### Assignment 1

This repository contains the first assignment for the Formal Languages and Compilers course. The assignment focuses on deterministic finite automata (DFA)
<br>

## Preliminaries
For this assignment some definitions and notions are required. Let M = (Q,Σ,δ,s,F) be a deter-
ministic finite automaton (DFA).

1. **Inaccessible states.** A state q ∈ Q is said to be **inaccessible** if there is no string x ∈ Σ∗ such that ˆδ(s, x) = q
   
2. **Equivalent states.** A pair of states p,q ∈ Q is said to be equivalent if and only if (∀x ∈ Σ∗)(ˆδ(p, x) ∈ F ≡ ˆδ(q, x) ∈ F).
   That is, any string x that from p allows us to access a final state, must also allows us to reach a final state from q, and vice versa.
   
3. We say that two states can be **collapsed** if they are equivalent.

## Assignment

The assignment is to implement, in any programming language, the minimization algorithm pre-
sented in Kozen 1997, Lecture 14.

Given a DFA with no inaccessible states, the algorithm returns the states that are equivalent.
Therefore, such states can be collapsed and we shall obtain a minimized automaton.
The minimization algorithm in Lecture 14 is based on the construction given in Lecture 13. It is
not necessary to read Lecture 13 to implement the algorithm, but if you choose to read it, you can
gain a high level understanding of the minimization procedure.

## Input/output

Your program should fulfill the following specifications.

#### Input
A case is a DFA M with no inaccessible states.
You may assume states are denoted by natural numbers and the initial state (s) is always the
number 0 (zero). Alphabets are formed with letters of the latin alphabet (with 26 letters). In ASCII
code, characters from 97 to 122.
The input of the program is as follows.
1. A line with a number c > 0 indicating how many cases you will receive.
2. For each case, in a single line a number n > 0 denoting of states of M.
3. Then, a single line with the alphabet of M. Symbols are separated by blank spaces.
4. Then, the final states of M separated by blank spaces.
5. Finally, n lines, one for each state. Each line contains a row of the table that represents M.
Assume that the symbols of the alphabet appear in the table in the same order as they were
given in step 3. For instance, if the automaton is

<div align="center">
  
![image](https://github.com/user-attachments/assets/d64cab34-a4bb-4f7f-8323-d5da4c0d29ca)

</div>

#### Output

For each case, print the pairs of states that are equivalent in lexicographical order. All the pairs in a
single line separated by blank spaces.

## References
Kozen, Dexter C. (1997). Automata and Computability. 1st. Berlin, Heidelberg: Springer-Verlag.
ISBN: 0387949070. DOI: https://doi.org/10.1007/978-1-4612-1844-9.

In this README we are going to show the language used, operating system, explanation of what the code does and how it is executed:

The language used for this solution was Python and Windows Operating System version 11.
This is a Python script that minimizes a deterministic finite automaton (DFA) by finding equivalent states. In the following we will detail the functionality of the code:

### read_input() function:

1.	Reads the standard input (usually the console) line by line.

2.	Stores the input lines in a line list.

3. The input is expected to be in a specific format:

3.1. The first line contains an integer c, representing the number of test cases.

3.2. Each test case consists of:

- An integer *n*, representing the number of states in the DFA.

- A line containing the alphabet (a list of symbols separated by spaces).

- A line containing the final states (a list of integers separated by spaces).

- *n* lines, each containing a transition (a list of integers separated by spaces).

The function returns a list of duplicates, where each duplicate represents a test case and contains *n, alphabet, final_states and transitions*.


### minimize_dfa() function:

1. It takes four arguments: *n, alphabet, final_states and transitions*, which represent a DFA.

2.	The function minimizes the DFA by finding equivalent states using the following steps:

3. It marks pairs of states where one is final and the other is not.

4.	Iteratively marks pairs of states based on their transitions.

5.	Collect the pairs of equivalent states.

6.	The function returns a list of equivalent pairs of states.

### main() function:

1.	Call read_input() to read the input and store it in the cases.
2. Iterate over each test case in the cases and call minimize_dfa() to minimize the DFA.
3.	Store the results in a results list.
4.	Print each result, which is a string representing the equivalent pairs of states.

### if __name__ == "__main__"::
 This block ensures that main() is executed only when the script is executed directly, and not when it is imported as a module.

## EXECUTION:

1. Save the code in a file, for example, dfa_minimizer.py.
2.	Run the script from the command line: python dfa_minimizer.py
3.	When running this script the program waits for the user to enter data describing one or more DFA and after processing the input, prints the pairs of states that are equivalent according to the DFA minimization process, for example:
```
2
3
a b
1 2
0 1
1 2
0 0
1 1
4
a b
2 3
0 1 2 3
1 2 3 0
2 3 0 1
3 0 1 2

```
This entry represents two test cases. The first test case has 3 states, alphabet {a, b}, final states {1, 2} and their transitions.
The second test case has 4 states, alphabet {a, b}, end states {2, 3} and their transitions.
The script will display the equivalent pairs of states for each test case, which in this case would be:
```
(0,2) (0,1}
(0,1) (2,3)

```
This output indicates that states 0,2 and 0,1 are equivalent, in the first test case. Similarly, the output of the second test case would indicate that states 0,1 are equivalent, as are states 2 ,3, meaning that they could be combined in the minimized DFA.
