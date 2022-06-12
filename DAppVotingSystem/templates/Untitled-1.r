
validCandidates = ["A" ,"B","C"]
votes=["A","F","A","B","A","B","A","C","E"]
def countVotes(validCandidates, votes):
    # Write your code here
    count = {}
    othervotes=0
    for i in validCandidates:
        
        count.update({i:votes.count(i)})
    invalid =len(votes)-(count.get("A")+count.get("B")+count.get("C"))
    maxKey=max(list(count.values()))
    print(maxKey)
    # winner=count[]
    return count,invalid



print(countVotes(validCandidates, votes))
