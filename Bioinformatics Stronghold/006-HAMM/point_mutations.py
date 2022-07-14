"""
Counting Point Mutations
ID: HMM
Number: 006
URL: http://rosalind.info/problems/gc/ 
"""


def hamming_distance(s, t):
    counts = 0

    # Compare entry by entry
    for idx in range(len(s)):
        if s[idx] != t[idx]:
            counts += 1

    return counts


if __name__ == "__main__":

    with open('rosalind_hamm.txt', 'r') as filename:

        # Read the file
        lines = filename.readlines()

        # Retrieve strings
        s = lines[0].strip()
        t = lines[1].strip()

        print(hamming_distance(s, t))
