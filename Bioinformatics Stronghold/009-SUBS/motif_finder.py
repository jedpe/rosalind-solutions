"""
Finding a Motif in DNA
ID: SUBS
Number: 009
URL: https://rosalind.info/problems/subs/
"""

def find_motif(s, t):
    """
       Finds all locations of the string t in s.
    """
    # Sanity check
    if len(t) > len(s):
        print("Substring 't' is larger than string 's'")
        return

    # Check for substring match in windows
    locations = []  # In 1-based indexing
    for j in range(0, len(s) - len(t) + 1):
        # Check current window
        if t == s[j:j + len(t)]:
            locations.append(j + 1)  # +1 for 1-based indexing

    return locations


if __name__ == "__main__":

    with open("rosalind_subs.txt", "r") as filename:
        
        # Read the file
        lines = filename.readlines()

        # Get both strings
        s = lines[0].strip()
        t = lines[1].strip()

    answer = ' '.join([str(i) for i in find_motif(s, t)])
    print(answer)
    
    
