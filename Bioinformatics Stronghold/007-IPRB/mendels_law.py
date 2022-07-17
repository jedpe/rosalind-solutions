"""
Mendel's First Law
ID: IPRB
Number: 007
URL: https://rosalind.info/problems/iprb/
"""


def prob_dominant(k, m, n):
    """
        Compute the probability of having a dominant phenotype 
        offspring from two randomly selected individuals from
        the following populations:

        k = homozygous dominant (AA)
        m = heterozygous (Aa)
        n = homozygous recessive (aa)
    """
    # Total of individuals
    tot = k + m + n

    # Compute selection probabilities
    p1 = (k / tot) * ((k - 1) / (tot - 1))  # AA + AA
    p2 = 2 * (k / tot) * (n / (tot - 1))    # AA + aa & aa + AA
    p3 = 2 * (k / tot) * (m / (tot - 1))    # AA + Aa & Aa + AA
    p4 = (m / tot) * ((m - 1) / (tot - 1))  # Aa + Aa
    p5 = 2 * (m / tot) * (n / (tot - 1))    # Aa + aa & aa + Aa

    # Compute probability of the desired outcome for each selection
    prob = p1*1 + p2*1 + p3*1 + p4*0.75 + p5*0.5

    return prob


if __name__ == "__main__":

    with open("rosalind_iprb.txt", 'r') as filename:

        # Read the file
        k, m, n = filename.read().strip().split(' ')

    print(prob_dominant(int(k), int(m), int(n)))
