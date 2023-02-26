def getFolderNames(self, names: List[str]) -> List[str]:
    memo = defaultdict(int)
    res = []
    for n in names:
        if memo[n] > 0:
            while n+'('+ str(memo[n]) +')' in memo.keys():
                memo[n]+=1
            res.append(n+'('+ str(memo[n]) +')')
            memo[n+'('+ str(memo[n])+')']+=1
        else:
            res.append(n)
        memo[n]+=1
    return res