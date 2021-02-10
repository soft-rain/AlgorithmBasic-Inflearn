def seqSearch(n, S, x):
    location = 1
    while(location <= n and S[location] != x):
        location += 1
    if(location > n):
        location = 0
    return location

#example
S=[0,10,7,11,5,13,8]
x=5

location = seqSearch(len(S)-1,S,x)
print(location)
