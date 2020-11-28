import os
import sys
import time

# Color code definitions for terminal
class bcolors:
    GREEN = '\033[0;32m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    RED = '\033[0;31m'

# Function to check if the outputs are equal
def controlOutput(out, real_out):
    if out == real_out:
        return 1
    else:
        return 0

# Part 1 variable declarations
CASE_NUMBER = 7
total_wrong = 0
compile_part1 = "gcc the1_part1.c main_part1.c -ansi -pedantic-errors -Wall -lm -o the1_part1"

# Program execution starts from here
print("\nCENG140 - THE #1 Tester\n")

print("Running part 1\n ")

compile_1 = os.popen(compile_part1)
time.sleep(0.5)

for case in range(1, CASE_NUMBER + 1):

    input_direction = "in/part1/" + str(case) + ".txt"

    run = "./the1_part1 < in/part1/" + str(case) + ".txt"

    stream = os.popen(run)
    out = stream.read()

    output_direction = "out/part1/" + str(case) + ".txt"
    get_out = open(output_direction, "r")

    correct_out = get_out.read()

    if controlOutput(out, correct_out) == 0:
        print(bcolors.RED + "[FAILED]" + bcolors.ENDC + " at case : " + str(case) + "/" + str(CASE_NUMBER) + " (in/part1/"+str(case)+".txt)")
        total_wrong += 1
    else:
        print(bcolors.GREEN + "[PASSED]" + bcolors.ENDC + " at case : " + str(case) + "/" + str(CASE_NUMBER))

print(bcolors.WARNING + "\n In part 2, your code failed at " + str(total_wrong) + " case and passed" + str(
    CASE_NUMBER-total_wrong) + " case. "+ bcolors.ENDC)

# Part 2 variable declarations
CASE_NUMBER = 10
total_wrong = 0
compile_part2 = "gcc the1_part2.c main_part2.c -ansi -pedantic-errors -Wall -lm -o the1_part2"

# Part 2 execution starts from here
print("\n Running part 2:\n")

compile_2 = os.popen(compile_part2)

time.sleep(0.5)

for case in range(1, CASE_NUMBER + 1):

    input_direction = "in/part2/" + str(case) + ".txt"

    run = "./the1_part2 < in/part2/" + str(case) + ".txt"

    stream = os.popen(run)

    out = stream.read()

    output_direction = "out/part2/" + str(case) + ".txt"
    get_out = open(output_direction, "r")
    correct_out = get_out.read()

    if controlOutput(out, correct_out) == 0:
        print(bcolors.RED + "[FAILED]" + bcolors.ENDC + " at case : " + str(case) + "/" + str(CASE_NUMBER) + " (in/part1/"+str(case) + ".txt)")

        total_wrong += 1
    else:
        print(bcolors.GREEN + "[PASSED]" + bcolors.ENDC + " at case : " + str(case) + "/" + str(CASE_NUMBER))

print(bcolors.WARNING + "\n In part 2, your code failed at " + str(total_wrong) + " case and passed" + str(
    CASE_NUMBER-total_wrong) + " case. "+ bcolors.ENDC)
