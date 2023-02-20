"""
CURRENT STATUS:
- rules 1-3 are implemented and working (i think).
- it seems that the algorithm itself is working, except for one problem (see TODO #1).
- output format is correct.
"""

"""
TODO:
1. need to expand to have more than 5 top solutions throughout the process because it's
   seemingly eliminating the best solution early on.
2. possible placement array:
   - skip any placements that have 0 when doing calculations.
   - it won't make a difference in results because they end up with high scores anyway,
     but it will make calculations more efficient.
   - 0: NOT a possible finger placement for the current pitch
   - 1: possible finger placement for the current pitch
3. check if everything works for pitch1 > pitch2 -> could this be the reason for weird results rn?
4. implement black/white note flag & rules 5-7
5. rule #4
"""

if __name__ == "__main__":
    
    # initialize array assuming 0 = C4
    # [C, C#, D, D#, E, F, ...]
    # [0, 1,  2, 3,  4, 5, ...]

    #             [E,D,C,D,E,E,E,D,D,D,E,G,G,E,D,C,D,E,E,E,D,D,E,D,C]
    little_lamb = [4,2,0,2,4,4,4,2,2,2,4,7,7,4,2,0,2,4,4,4,2,2,4,2,0]
    # ideal soln: [3,2,1,2,3,3,3,2,2,2,3,5,5,3,2,1,2,3,3,3,2,2,3,2,1]
    
    # format of all reference arrays:
    # [1-1, 1-2, 1-3, 1-4, 1-5, 2-1, 2-2, 2-3, 2-4, 2-5, 3-1, 3-2, 3-3, 3-4, 3-5, ...]
    minComf = [0,-3,-3,-1,3,   -8,0,1,1,2,   -10,-3,0,1,1,   -12,-5,-2,0,1,   -13,-8,-5,-3,0]
    maxComf = [0,8,10,12,13,2,0,3,5,8,3,1,0,2,5,1,1,1,0,3,-3,-2,-1,-1,0]
    minRel = [0,1,3,5,7,-5,0,1,3,5,-7,-1,0,1,3,-5,-4,-3,0,1,-10,-6,-4,-2,0]
    maxRel = [0,5,7,9,10,-1,0,2,4,6,-3,-2,0,2,4,-9,-3,-1,0,2,-7,-5,-3,-1,0]

    # TODO #2
    possible_placement = []

    # limit to only the top 5 best solutions (based on total points after each pitch)
    sol1 = [1]
    sol2 = [2]
    sol3 = [3]
    sol4 = [4]
    sol5 = [5]
    
    sol1_temp = []
    sol2_temp = []
    sol3_temp = []
    sol4_temp = []
    sol5_temp = []

    # create arrays to hold current information about top 5 possible solutions
    scores = [0,0,0,0,0]
    temp_scores = [0,0,0,0,0]
    temp_sol_num = [1,2,3,4,5]
    temp_poss_sol_index = [0,0,0,0,0]

    # these hold the scores for each possible next finger placement for each current solution
    poss_sol1_scores = [0,0,0,0,0]
    poss_sol2_scores = [0,0,0,0,0]
    poss_sol3_scores = [0,0,0,0,0]
    poss_sol4_scores = [0,0,0,0,0]
    poss_sol5_scores = [0,0,0,0,0]
    
    # for every pitch in the song
    for p in range(1, len(little_lamb)):
    #for i in range(1,2):

        # TODO #3
        # TODO #4

        # if pitch1 < pitch2 (e.g. [C,D]), semitones > 0
        semitones = little_lamb[p] - little_lamb[p-1]

        if (p > 1):
            semitones_1_3 = little_lamb[p] - little_lamb[p-2]
        elif (p == 1):
            semitones_1_3 = little_lamb[p+1] - little_lamb[p-1]

        # if the current pitch is the same as the one which was just played
        # just assign the same number as the previous pitch
        """
        if (semitones == 0):
            # assign the same number, set a flag, don't go through the rules
        elif (semitones < 0):
            # rule out some placements
        else:
            # rule out some placements
        """

        # CALCULATE POINTS FOR ALL POSSIBLE SOLUTIONS, WITH F2=(1 THROUGH 5)
        for f2 in range(1,6): # iterates through values 1 to 5

            # calculate reference index for arrays minComf, minRel, maxComf, etc.
            reference_index_1 = ((sol1[p-1]-1)*5)+(f2-1)
            reference_index_2 = ((sol2[p-1]-1)*5)+(f2-1)
            reference_index_3 = ((sol3[p-1]-1)*5)+(f2-1)
            reference_index_4 = ((sol4[p-1]-1)*5)+(f2-1)
            reference_index_5 = ((sol5[p-1]-1)*5)+(f2-1)

            # calculate ref index for 1st & 3rd interval
            reference_index_1st_3rd_1 = ((sol1[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_2 = ((sol2[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_3 = ((sol3[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_4 = ((sol4[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_5 = ((sol5[p-2]-1)*5)+(f2-1)

            # TODO #2

            #
            #
            # RULE 1: DONE
            # solution 1
            if (semitones < minComf[reference_index_1]): poss_sol1_scores[f2-1] += 2*(minComf[reference_index_1] - semitones)
            elif (semitones > maxComf[reference_index_1]): poss_sol1_scores[f2-1] += 2*(semitones - maxComf[reference_index_1])
            # solution 2
            if (semitones < minComf[reference_index_2]): poss_sol2_scores[f2-1] += 2*(minComf[reference_index_2] - semitones)
            elif (semitones > maxComf[reference_index_2]): poss_sol2_scores[f2-1] += 2*(semitones - maxComf[reference_index_2])
            # solution 3
            if (semitones < minComf[reference_index_3]): poss_sol3_scores[f2-1] += 2*(minComf[reference_index_3] - semitones)
            elif (semitones > maxComf[reference_index_3]): poss_sol3_scores[f2-1] += 2*(semitones - maxComf[reference_index_3])
            # solution 4
            if (semitones < minComf[reference_index_4]): poss_sol4_scores[f2-1] += 2*(minComf[reference_index_4] - semitones)
            elif (semitones > maxComf[reference_index_4]): poss_sol4_scores[f2-1] += 2*(semitones - maxComf[reference_index_4])
            # solution 5
            if (semitones < minComf[reference_index_5]): poss_sol5_scores[f2-1] += 2*(minComf[reference_index_5] - semitones)
            elif (semitones > maxComf[reference_index_5]): poss_sol5_scores[f2-1] += 2*(semitones - maxComf[reference_index_5])

            #
            #
            # RULE 2: DONE
            # solution 1
            if (semitones < minRel[reference_index_1]): poss_sol1_scores[f2-1] += minRel[reference_index_1] - semitones
            elif (semitones > maxRel[reference_index_1]): poss_sol1_scores[f2-1] += semitones - maxRel[reference_index_1]
            # solution 2
            if (semitones < minRel[reference_index_2]): poss_sol2_scores[f2-1] += minRel[reference_index_2] - semitones
            elif (semitones > maxRel[reference_index_2]): poss_sol2_scores[f2-1] += semitones - maxRel[reference_index_2]
            # solution 3
            if (semitones < minRel[reference_index_3]): poss_sol3_scores[f2-1] += minRel[reference_index_3] - semitones
            elif (semitones > maxRel[reference_index_3]): poss_sol3_scores[f2-1] += semitones - maxRel[reference_index_3]
            # solution 4
            if (semitones < minRel[reference_index_4]): poss_sol4_scores[f2-1] += minRel[reference_index_4] - semitones
            elif (semitones > maxRel[reference_index_4]): poss_sol4_scores[f2-1] += semitones - maxRel[reference_index_4]
            # solution 5
            if (semitones < minRel[reference_index_5]): poss_sol5_scores[f2-1] += minRel[reference_index_5] - semitones
            elif (semitones > maxRel[reference_index_5]): poss_sol5_scores[f2-1] += semitones - maxRel[reference_index_5]

            #
            #
            # RULE 3
            # compare minComf & maxComf for 1st & 3rd interval
            
            # changes this so it will calculate the score for 1st/3rd interval in the first round to narrow down more. (p=1)
            # then, it will skip this calculation for the next round, instead of doing it again with the same interval. (p=2)
            # after this, it will operate normally. (p>2)
            if ((p == 1) | (p > 2)):
                # solution 1
                if (semitones_1_3 < minComf[reference_index_1st_3rd_1]): poss_sol1_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_1] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_1]): poss_sol1_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_1])
                # solution 2
                if (semitones_1_3 < minComf[reference_index_1st_3rd_2]): poss_sol2_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_2] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_2]): poss_sol2_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_2])
                # solution 3
                if (semitones_1_3 < minComf[reference_index_1st_3rd_3]): poss_sol3_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_3] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_3]): poss_sol3_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_3])
                # solution 4
                if (semitones_1_3 < minComf[reference_index_1st_3rd_4]): poss_sol4_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_4] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_4]): poss_sol4_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_4])
                # solution 5
                if (semitones_1_3 < minComf[reference_index_1st_3rd_5]): poss_sol5_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_5] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_5]): poss_sol5_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_5])

            #
            #
            # TODO #5
            # add point if sequence [3,4,5] occurs -> add 1pt

            # TODO #4
            # [3,4] or [4,3] AND 3=white & 4=black -> add 1pt

            # TODO #4
            # thumb plays black key -> add 1pt
            # note before = white -> add 2pts
            # note after = white -> add 2pts

            # TODO #4
            # thumb pass on same level -> add 1pt
            # thumb pass with lower pitch = white&not thumb, upper = black&thumb -> add 3pts
    
        #
        #
        # COMPARE SCORES

        # DONE: initialize the temporary solution variables
        for i in range (0,5):
            temp_scores[i] = poss_sol1_scores[i]
        temp_sol_num = [1,1,1,1,1]
        temp_poss_sol_index = [0,1,2,3,4]
        
        # DONE: compare scores of all possible solutions & update temporary solution arrays
        for i in range (0,5):
            #
            # SOLUTION 2
            # if sol2[i] is the new best score
            if (poss_sol2_scores[i] < temp_scores[0]):
                for j in range (4,0,-1):
                    # shift the other values
                    print("temp_scores[j] =", temp_scores[j])
                    print("temp_scores[j-1] =", temp_scores[j-1])
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new best solution
                temp_scores[0] = poss_sol2_scores.copy()[i]
                temp_sol_num[0] = 2
                temp_poss_sol_index[0] = i
            # if sol2[i] is the new 2nd-best score
            elif (poss_sol2_scores[i] < temp_scores[1]):
                for j in range (4,1,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 2nd-best solution
                temp_scores[1] = poss_sol2_scores.copy()[i]
                temp_sol_num[1] = 2
                temp_poss_sol_index[1] = i
            # if sol2[i] is the new 3rd-best score
            elif (poss_sol2_scores[i] < temp_scores[2]):
                for j in range (4,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 3rd-best solution
                temp_scores[2] = poss_sol2_scores.copy()[i]
                temp_sol_num[2] = 2
                temp_poss_sol_index[2] = i
            # if sol2[i] is the new 4th-best score
            elif (poss_sol2_scores[i] < temp_scores[3]):
                # shift the solution currently in 4th to be in 5th place
                temp_scores[4] = temp_scores.copy()[3]
                temp_sol_num[4] = temp_sol_num.copy()[3]
                temp_poss_sol_index[4] = temp_poss_sol_index.copy()[3]
                # set the new 4-th best solution
                temp_scores[3] = poss_sol2_scores.copy()[i]
                temp_sol_num[3] = 2
                temp_poss_sol_index[3] = i
            # if sol2[i] is the new 5th-best score
            elif (poss_sol2_scores[i] < temp_scores[4]):
                # set the new 5th-best solution
                temp_scores[4] = poss_sol2_scores.copy()[i]
                temp_sol_num[4] = 2
                temp_poss_sol_index[4] = i
            
            #
            # SOLUTION 3
            # if sol3[i] is the new best score
            if (poss_sol3_scores[i] < temp_scores[0]):
                for j in range (4,0,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new best solution
                temp_scores[0] = poss_sol3_scores.copy()[i]
                temp_sol_num[0] = 3
                temp_poss_sol_index[0] = i
            # if sol3[i] is the new 2nd-best score
            elif (poss_sol3_scores[i] < temp_scores[1]):
                for j in range (4,1,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 2nd-best solution
                temp_scores[1] = poss_sol3_scores.copy()[i]
                temp_sol_num[1] = 3
                temp_poss_sol_index[1] = i
            # if sol3[i] is the new 3rd-best score
            elif (poss_sol3_scores[i] < temp_scores[2]):
                for j in range (4,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 3rd-best solution
                temp_scores[2] = poss_sol3_scores.copy()[i]
                temp_sol_num[2] = 3
                temp_poss_sol_index[2] = i
            # if sol3[i] is the new 4th-best score
            elif (poss_sol3_scores[i] < temp_scores[3]):
                # shift the solution currently in 4th to be in 5th place
                temp_scores[4] = temp_scores.copy()[3]
                temp_sol_num[4] = temp_sol_num.copy()[3]
                temp_poss_sol_index[4] = temp_poss_sol_index.copy()[3]
                # set the new 4th-best solution
                temp_scores[3] = poss_sol3_scores.copy()[i]
                temp_sol_num[3] = 3
                temp_poss_sol_index[3] = i
            # if sol3[i] is the new 5th-best score
            elif (poss_sol3_scores[i] < temp_scores[4]):
                # set the new 5th-best solution
                temp_scores[4] = poss_sol2_scores.copy()[i]
                temp_sol_num[4] = 2
                temp_poss_sol_index[4] = i

            #
            # SOLUTION 4
            # if sol4[i] is the new best score
            if (poss_sol4_scores[i] < temp_scores[0]):
                for j in range (4,0,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new best solution
                temp_scores[0] = poss_sol4_scores.copy()[i]
                temp_sol_num[0] = 4
                temp_poss_sol_index[0] = i
            # if sol4[i] is the new 2nd-best score
            elif (poss_sol4_scores[i] < temp_scores[1]):
                for j in range (4,1,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 2nd-best solution
                temp_scores[1] = poss_sol4_scores.copy()[i]
                temp_sol_num[1] = 4
                temp_poss_sol_index[1] = i
            # if sol4[i] is the new 3rd-best score
            elif (poss_sol4_scores[i] < temp_scores[2]):
                for j in range (4,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 3rd-best solution
                temp_scores[2] = poss_sol4_scores.copy()[i]
                temp_sol_num[2] = 4
                temp_poss_sol_index[2] = i
            # if sol4[i] is the new 4th-best score
            elif (poss_sol4_scores[i] < temp_scores[3]):
                # shift the solution currently in 4th to be in 5th place
                temp_scores[4] = temp_scores.copy()[3]
                temp_sol_num[4] = temp_sol_num.copy()[3]
                temp_poss_sol_index[4] = temp_poss_sol_index.copy()[3]
                # set the new 4th-best solution
                temp_scores[3] = poss_sol4_scores.copy()[i]
                temp_sol_num[3] = 4
                temp_poss_sol_index[3] = i
            # if sol4[i] is the new 5th-best score
            elif (poss_sol4_scores[i] < temp_scores[4]):
                # set the new 5th-best solution
                temp_scores[4] = poss_sol4_scores.copy()[i]
                temp_sol_num[4] = 4
                temp_poss_sol_index[4] = i

            #
            # SOLUTION 5
            # if sol5[i] is the new best score
            if (poss_sol5_scores[i] < temp_scores[0]):
                for j in range (4,0,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new best solution
                temp_scores[0] = poss_sol5_scores.copy()[i]
                temp_sol_num[0] = 5
                temp_poss_sol_index[0] = i
            # if sol5[i] is the new 2nd-best score
            elif (poss_sol5_scores[i] < temp_scores[1]):
                for j in range (4,1,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 2nd-best solution
                temp_scores[1] = poss_sol5_scores.copy()[i]
                temp_sol_num[1] = 5
                temp_poss_sol_index[1] = i
            # if sol5[i] is the new 3rd-best score
            elif (poss_sol5_scores[i] < temp_scores[2]):
                for j in range (4,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 3rd-best solution
                temp_scores[2] = poss_sol5_scores.copy()[i]
                temp_sol_num[2] = 5
                temp_poss_sol_index[2] = i
            # if sol5[i] is the new 4th-best score
            elif (poss_sol5_scores[i] < temp_scores[3]):
                # shift the solution currently in 4th to be in 5th place
                temp_scores[4] = temp_scores.copy()[3]
                temp_sol_num[4] = temp_sol_num.copy()[3]
                temp_poss_sol_index[4] = temp_poss_sol_index.copy()[3]
                # set the new 4th-best solution
                temp_scores[3] = poss_sol5_scores.copy()[i]
                temp_sol_num[3] = 5
                temp_poss_sol_index[3] = i
            # if sol5[i] is the new 5th-best score
            elif (poss_sol5_scores[i] < temp_scores[4]):
                # set the new 5th-best solution
                temp_scores[4] = poss_sol5_scores.copy()[i]
                temp_sol_num[4] = 5
                temp_poss_sol_index[4] = i

        # for best solution
        if temp_sol_num[0] == 1: sol1_temp = sol1.copy()
        elif temp_sol_num[0] == 2: sol1_temp = sol2.copy() # copy sol2 to temp sol1
        elif temp_sol_num[0] == 3: sol1_temp = sol3.copy() # copy sol3 to temp sol1
        elif temp_sol_num[0] == 4: sol1_temp = sol4.copy() # copy sol4 to temp sol1
        elif temp_sol_num[0] == 5: sol1_temp = sol5.copy() # copy sol5 to temp sol1

        # for 2nd-best solution
        if temp_sol_num[1] == 1: sol2_temp = sol1.copy()
        elif temp_sol_num[1] == 2: sol2_temp = sol2.copy()
        elif temp_sol_num[1] == 3: sol2_temp = sol3.copy()
        elif temp_sol_num[1] == 4: sol2_temp = sol4.copy()
        elif temp_sol_num[1] == 5: sol2_temp = sol5.copy()

        # for 3rd-best solution
        if temp_sol_num[2] == 1: sol3_temp = sol1.copy()
        elif temp_sol_num[2] == 2: sol3_temp = sol2.copy()
        elif temp_sol_num[2] == 3: sol3_temp = sol3.copy()
        elif temp_sol_num[2] == 4: sol3_temp = sol4.copy()
        elif temp_sol_num[2] == 5: sol3_temp = sol5.copy()

        # for 4th-best solution
        if temp_sol_num[3] == 1: sol4_temp = sol1.copy()
        elif temp_sol_num[3] == 2: sol4_temp = sol2.copy()
        elif temp_sol_num[3] == 3: sol4_temp = sol3.copy()
        elif temp_sol_num[3] == 4: sol4_temp = sol4.copy()
        elif temp_sol_num[3] == 5: sol4_temp = sol5.copy()

        # for 5th-best solution
        if temp_sol_num[4] == 1: sol5_temp = sol1.copy()
        elif temp_sol_num[4] == 2: sol5_temp = sol2.copy()
        elif temp_sol_num[4] == 3: sol5_temp = sol3.copy()
        elif temp_sol_num[4] == 4: sol5_temp = sol4.copy()
        elif temp_sol_num[4] == 5: sol5_temp = sol5.copy()

        # append new finger placements
        sol1_temp.append(temp_poss_sol_index[0]+1) # append new finger placement for sol1
        sol2_temp.append(temp_poss_sol_index[1]+1) # append new finger placement for sol2
        sol3_temp.append(temp_poss_sol_index[2]+1) # append new finger placement for sol3
        sol4_temp.append(temp_poss_sol_index[3]+1) # append new finger placement for sol4
        sol5_temp.append(temp_poss_sol_index[4]+1) # append new finger placement for sol5

        # copy over current solutions
        sol1 = sol1_temp
        sol2 = sol2_temp
        sol3 = sol3_temp
        sol4 = sol4_temp
        sol5 = sol5_temp

        # copy over scores and reset array
        scores = temp_scores
        temp_scores = [0,0,0,0,0]

        # set possible scores to be the current score for each solution
        poss_sol1_scores = [scores[0],scores[0],scores[0],scores[0],scores[0]]
        poss_sol1_scores = [scores[1],scores[1],scores[1],scores[1],scores[1]]
        poss_sol1_scores = [scores[2],scores[2],scores[2],scores[2],scores[2]]
        poss_sol1_scores = [scores[3],scores[3],scores[3],scores[3],scores[3]]
        poss_sol1_scores = [scores[4],scores[4],scores[4],scores[4],scores[4]]
        
        #
        #
        # print results for debugging
        print("#1 solution:")
        print("score =", scores[0])
        print("sol_num =", temp_sol_num[0])
        print("solution =", sol1)

        print("\n#2 solution:")
        print("score =", scores[1])
        print("sol_num =", temp_sol_num[1])
        print("solution =", sol2)
        
        print("\n#3 solution:")
        print("score =", scores[2])
        print("sol_num =", temp_sol_num[2])
        print("solution =", sol3)

        print("\n#4 solution:")
        print("score =", scores[3])
        print("sol_num =", temp_sol_num[3])
        print("solution =", sol4)

        print("\n#5 solution:")
        print("score =", scores[4])
        print("sol_num =", temp_sol_num[4])
        print("solution =", sol5)