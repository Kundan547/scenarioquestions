"""In cricket match, the batting team is scoring runs with some run rate. 
The match is of 20 overs. Write a program to find the total runs scored by the batting.

example:
input: 13
Output: Total runs scored in 20 overs : 260.00

example:
input: 15
Output: Total runs scored in 20 overs : 300.00
"""

run_rate = float(input("Enter the run rate :"))

total_over = 20

total_run = run_rate * total_over

print(f"Total runs scored in 20 overs: {total_run:.2f}")