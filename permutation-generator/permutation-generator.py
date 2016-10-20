 # given integer N < 10, create generator that will return a new permutation of
# the integers between 1 and N until permutations exhausted
# example:
# N = 4
# output: generator that returns permutations of 1234
def permutations(seq):
    string = False
    if type(seq) == str:
        string = True
    if type(seq) == int:
        seq = range(1, seq+1)
    else:
        seq = sorted([i for i in seq])
    perm, desc = list(seq), -1
    while desc != 0:
        if string:
            yield ''.join(perm)
        else:
            yield perm
        desc = len(perm) - 1
        while perm[desc - 1] >= perm[desc]:
            desc -= 1
        num = perm[desc - 1]
        new_seq = sorted([num] + perm[desc:])
        i = new_seq.index(num)
        while new_seq[i] <= num:
            i += 1
        perm = perm[:desc-1] + [new_seq.pop(i)] + new_seq

for i in permutations(120):
    i = list(map(str, i))
    print(' '.join(i))
    input("Next? ")
