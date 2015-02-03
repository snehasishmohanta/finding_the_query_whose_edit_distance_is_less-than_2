"""a program to find all the query whose edit distance is less than 2"""


def min_edit_dist(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]
d = {}
with open("all_search.txt") as text:
    for line in text:
        line = line.strip("\n")

        for lines in line.split("\n"):
            try:
                key, val = lines.split(",")
                d.setdefault(key,[]).append(val.lower())
            except:
                pass
values = d.values()
keys = d.keys()
for v in values:
    for i in range(0,len(v)-1):
        if v[i] != v[i+1]:
            if min_edit_dist(v[i], v[i+1]) <= 2:
                print v[i]+" > "+v[i+1]
