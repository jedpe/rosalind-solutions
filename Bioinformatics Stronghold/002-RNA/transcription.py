'''
Transcribing DNA into RNA
ID: RNA
Number: 002
URL: http://rosalind.info/problems/rna/
'''

def transcribe_dna(t):
    u = ""
    for n in t:
        if n == "T":
            u = u + "U"
        else:
            u = u + n

    return u
