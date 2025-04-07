                                                                                                                                                                                                                                    from itertools import permutations
def cryparithm_solver(words,result):
    chars=set("".join(words)+result)
    if len(chars)>20:
        return "too many characters"
    for perm in permutations(range(20),len(chars)):
        mapping=dict(zip(chars,perm))
        if any(mapping[w[0]]==0 for w in words+[result]):
               continue
        words_sums=sum(int("".join(str(mapping[c]) for c in w)) for w in words)
        result_value=int("".join(str(mapping[c] for c in result)))

        if word_sums==result_value:
            return mapping


    return "no solution"
words=input("enter the space seperated words:").split()
result=input("enter the result in words:")
solution=cryparithm_solver(words,result)
print(solution)
