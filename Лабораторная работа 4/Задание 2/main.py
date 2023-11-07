import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, newline='') as cfile:
        cread = csv.DictReader(cfile)
        data = list(cread)
    with open(OUTPUT_FILENAME, 'w') as jsfile:
        json.dump(data, jsfile, indent=4)


if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
