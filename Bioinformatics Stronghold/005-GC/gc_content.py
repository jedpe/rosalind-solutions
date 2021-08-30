"""
Computing GC Content
ID: GC
Number: 005
URL: http://rosalind.info/problems/gc/
"""

import csv


def get_gc_content(sequence):

    # Get the length of the sequence (total bases)
    total = len(sequence)

    # Count the Cs and Gs
    cgs = 0
    for base in sequence.upper():
        if base == 'C' or base == 'G':
            cgs += 1

    # Return the percentage of CGs with 6 decimal places
    return round(100*cgs/float(total), 6)


if __name__ == "__main__":

    with open('rosalind_gc.txt', 'r') as filename:

        # Read the file
        reader = csv.reader(filename)

        # Get all sequences with their identifiers
        sequences = {}
        for line in reader:
            if line[0].startswith('>'):
                identifier = line[0].replace('>', '')  # For the output
                sequences[identifier] = ''

            else:
                sequences[identifier] = sequences[identifier] + line[0]

        # Compute the GC content of a sequence and store it in the dictionary
        gc_dict = {}
        for identifier, sequence in sequences.items():
            gc_dict[identifier] = get_gc_content(sequence)

    # Get keys and values
    key_list = list(gc_dict.keys())
    val_list = list(gc_dict.values())

    # Get the identifier of the sequence with maximum GC content
    max_idx = val_list.index(max(val_list))
    print(key_list[max_idx])
    print(val_list[max_idx])
