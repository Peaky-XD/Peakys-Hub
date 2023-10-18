import argparse

def remove_duplicates(x1, x2):
    with open(x1, 'r') as x3, open(x2, 'w') as x4:
        x5 = set()
        for x6 in x3:
            if x6 not in x5:
                x5.add(x6)
                x4.write(x6)

if __name__ == "__main__":
    x7 = argparse.ArgumentParser(description="Remove duplicate lines from a file")
    x7.add_argument("-f", "--file", help="Input file", required=True)
    x7.add_argument("-u", "--output", help="Output file", required=True)
    x8 = x7.parse_args()

    x1 = x8.file
    x2 = x8.output

    remove_duplicates(x1, x2)
    print(f"Duplicate lines removed. Result saved to {x2}")
