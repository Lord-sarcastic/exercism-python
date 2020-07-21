def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length")
    count = 0
    for each in zip(strand_a, strand_b):
        if each[0] != each[1]:
            count += 1
    return count
