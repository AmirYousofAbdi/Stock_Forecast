def safe(ls):

    ##########################    khane ha

    place = []
    for i in range(4):

        for k in range(4):

            if ls[i,k] == 9:
                place.append([i,k])



    ########################    stoniiii


    for ston in range(4):

        t = 0
        for radif in range(4):

            if ls[radif,ston] == 9:
                t += 1


        if t != 1:
            return False
    #########################   ghotri    chap => rast


    for i in place:

        tedad = 4 - (abs(i[0] - i[1]))
        for i in range(tedad):


            if tedad == 2:


                if (ls[2,0] == 9 and ls[3,1] == 9) or (ls[0,2] == 9 and ls[1,3] == 9):


                    return False

            elif tedad == 3:


                if ((ls[1,0] == 9 and ls[2,1]) or (ls[2,1] == 9 and ls[3,2] == 9) or (ls[1,0] == 9 and ls[3,2] == 9)) or (((ls[0,1] == 9 and ls[1,2]) or (ls[1,2] == 9 and ls[2,3] == 9) or (ls[0,1] == 9 and ls[2,3] == 9))):

                    return False
            elif tedad == 4:


                if (ls[0,0] == 9 and ls[1,1] == 9) or (ls[0,0] == 9 and ls[2,2] == 9) or (ls[0,0] == 9 and ls[3,3] == 9) or (ls[1,1] == 9 and ls[2,2] == 9) or (ls[1,1] == 9 and ls[3,3] == 9) or (ls[2,2] == 9 and ls[3,3] == 9):


                    return False
    ######################################      ghotri     rast => chap
    for i in place:


        tedad = 4 - (abs(i[0] - i[1]))
        for i in range(tedad):


            if tedad == 2:

                if (ls[0,1] == 9 and ls[1,0] == 9) or (ls[2,3] == 9 and ls[3,2] == 9):



                    return False
            elif tedad == 3:


                if ((ls[0,2] == 9 and ls[1,1]) or (ls[0,2] == 9 and ls[2,0] == 9) or (ls[1,1] == 9 and ls[2,0] == 9)) or (((ls[1,3] == 9 and ls[2,2]) or (ls[1,3] == 9 and ls[3,1] == 9) or (ls[2,2] == 9 and ls[3,1] == 9))):

                    return False
            elif tedad == 4:


                if (ls[0,3] == 9 and ls[1,2] == 9) or (ls[0,3] == 9 and ls[2,1] == 9) or (ls[0,3] == 9 and ls[3,0] == 9) or (ls[1,2] == 9 and ls[2,1] == 9) or (ls[1,2] == 9 and ls[3,0] == 9) or (ls[2,1] == 9 and ls[3,0] == 9):

                    return False
    return True


#######################################

import numpy as np

ls = np.array([(0,)*4]*4)

for m0 in range(4):

    for m1 in range(4):

        for m2 in range(4):

            for m3 in range(4):


                ls = np.array([(0,)*4]*4)

                ls[0,m0] = 9
                ls[1,m1] = 9
                ls[2,m2] = 9
                ls[3,m3] = 9


                if safe(ls):
                    print(ls)
