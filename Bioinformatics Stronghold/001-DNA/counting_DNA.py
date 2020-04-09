'''
Problem: Counting DNA Nucleotides
ID: DNA
Number: 001
URL: http://rosalind.info/problems/dna/
'''

def count_bases(s):
    base_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in s:
        base_dict[base] = base_dict[base] + 1

    return base_dict
