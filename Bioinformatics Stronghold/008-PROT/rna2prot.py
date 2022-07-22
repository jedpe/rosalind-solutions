"""
Translating RNA into Protein
ID: PROT
Number: 008
URL: https://rosalind.info/problems/prot/
"""


def rna_to_prot(s):
    """
       Translate an mRNA string into a sequence of
       aminoacids.
    """
    # Dictionary of RNA codons
    codon_dict = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 
            'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y',
            'UAA': 'Stop', 'UAG': 'Stop', 'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop',
            'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P',
            'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAU': 'H', 'CAC': 'H',
            'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R',
            'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N',
            'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S',
            'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
            'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G',
            'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
            }

    # Change the RNA string
    prot = ''
    for idx in range(0, len(s), 3): 
        codon = s[idx:idx + 3] 
        amino_acid = codon_dict[codon]

        # Check for stop codons
        if amino_acid == 'Stop':
            break

        # Otherwise add the amino acid to the chain
        else:
            prot += amino_acid

    return prot



if __name__ == "__main__":

    with open('rosalind_prot.txt', 'r') as filename:

        # Read file
        s = filename.read().strip()

    print(rna_to_prot(s))
