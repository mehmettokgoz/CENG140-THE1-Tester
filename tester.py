import os
import sys
import time

CASE_NUMBER = 2
total_wrong = 0

compile_part1 = "gcc the1_part1.c main_part1.c -ansi -pedantic-errors -Wall -lm -o the1_part1"
compile_now = os.popen(compile_part1)

time.sleep(1)


def controlOutput(out, real_out):

    if out == real_out:
        return 1
    else:
        return 0


for case in range(1,CASE_NUMBER+1):

    input_direction = "in/" + str(case) + ".txt"

    run = "./the1_part1 < in/" + str(case) + ".txt"

    stream = os.popen(run)


    out = stream.read()

    output_direction = "out/" + str(case) + ".txt"
    get_out = open(output_direction, "r")
    correct_out = get_out.read()

    newFile = open("newOut.txt","w")
    newFile.write(get_out)

    if controlOutput(out, correct_out) == 0:

        print("[FAILED] at case :"+str(case) + "/"+str(CASE_NUMBER))
        print("Correct:\n" + correct_out)
        print("\nYour Output:\n"+out)

        total_wrong += 1
    else:
        print("[PASSED] at case : " + str(case) + "/"+str(CASE_NUMBER))