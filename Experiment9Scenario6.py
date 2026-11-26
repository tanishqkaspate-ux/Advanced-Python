
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--s1", nargs=5, type=int)
parser.add_argument("--s2", nargs=5, type=int)
parser.add_argument("--s3", nargs=5, type=int)
parser.add_argument("--s4", nargs=5, type=int)

args = parser.parse_args()

students = []

for i in range(5):
    students.append([
        args.s1[i],
        args.s2[i],
        args.s3[i],
        args.s4[i]
    ])

print("Student Marks (2D Array):")

for row in students:
    print(row)
