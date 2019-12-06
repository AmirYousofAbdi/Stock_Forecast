def vertical(khane,mohreha):
    while khane >  8:               #
        khane -= 8                  #
    t = 0                           #

    
    while khane > 56:               #
        if khane in mohreha:        #
            t += 1                  #
    if t <= 1:                      #
        return True                 #
    return False                    #




mohreha = [1]*8
for i in range(1,9):
    
    for k in range((8 * (i - 1)) + 1,(i * 8) + 1):
        
        if vertical(k,mohreha):

            
            mohreha[i-1] = [k]
print(mohreha)
