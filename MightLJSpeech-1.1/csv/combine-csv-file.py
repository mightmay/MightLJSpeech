import glob
import csv

read_files = glob.glob("*.csv")
print(f"Found {len(read_files)} CSV files.")

with open("combined.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    for f in read_files:
        print(f"Reading file: {f}")
        with open(f, "r", newline='') as infile:
            reader = csv.reader(infile)
            for row in reader:
                print(f"Writing row: {row}")
                writer.writerow(row)