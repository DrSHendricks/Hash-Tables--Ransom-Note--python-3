from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m,r=Counter(magazine),Counter(note)
    match="Yes"
    diff = {x: m[x] - r[x] for x in r}
    k=list(diff.values())
    if any(value < 0 for value in k):
        match ="No"
    print (match)
