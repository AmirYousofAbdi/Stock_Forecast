def vertical(x,mohre):
    for i in range(x//8):
        for k in range(8):
            if x - 8 == mohre[k]:
                return False
    return True
mohre = [0,1,2,3,4,5,6,7] 
for i in range(len(mohre)):
    for k in range(65):
        if vertical(k,mohre):
            mohre[i] = k
    mohre = mohre.pop(0)
print(mohre)

