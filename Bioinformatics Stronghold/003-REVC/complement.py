"""
Complementing a Strand of DNA
ID: REVC
Number: 003
URL: http://rosalind.info/problems/revc/
"""


def reverse_complement(s):
    # Dictionary of of the base complements
    base_complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

    # We want the reverse of s. We need a way to access it from back to front
    idx_range = range(1, len(s) + 1)

    # Get the complement of s
    s_c = ""
    for i in idx_range:
        s_c = s_c + base_complement[s[-i]]

    return s_c


if __name__ == "__main__":
    with open("rosalind_revc.txt", "r") as input_data:
        # Read the first line of the file
        s = input_data.readline().strip()

        # Get reverse complement
        s_c = reverse_complement(s)

        # Print answer
        print("Answer is: {}".format(s_c))
