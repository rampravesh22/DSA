def solve(N, A, B, C):
    #
    if ((A | B | C) == A ) and ((A & B & C) == B ) and ((A ^ B ^ C) == C ):
        return [A,B,C]
    else:
        return [-1]

print(solve(3,5,5,5))