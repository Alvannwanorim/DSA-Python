from typing import Counter, List


def scores(teamA: List[int], teamB: List[int]):
    teamADic = Counter(teamA)
    teamBDic = Counter(teamB)

    res = []
    count = 0
    combinedTeams = []
    for i in teamA:
        combinedTeams.append(i)
    for j in teamB:
        if j not in teamADic:
            combinedTeams.append(j)
    combinedTeams.sort()
    print(teamADic)
    print(teamBDic)
    for n in combinedTeams:
        if n in teamADic:
            count +=1
        if n in teamBDic:
            res.append(count)
    return res

print(scores([1, 2, 3], [2, 4]))