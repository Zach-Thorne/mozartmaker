"""
TODO from before:
1. possible placement array: (don't know if this is actually necessary at all)
   - skip any placements that have 0 when doing calculations.
   - it won't make a difference in results because they end up with high scores anyway,
     but it will make calculations more efficient.
   - 0: NOT a possible finger placement for the current pitch
   - 1: possible finger placement for the current pitch
2. implement black/white note flag & rules 5-7
"""

if __name__ == "__main__":
    
    #
    #
    # initialize song arrays assuming 0 = C4

    # mary had a little lamb
    #             [E,D,C,D,E,E,E,D,D,D,E,G,G,E,D,C,D,E,E,E,D,D,E,D,C]
    little_lamb = [4,2,0,2,4,4,4,2,2,2,4,7,7,4,2,0,2,4,4,4,2,2,4,2,0]
    # ideal soln: [3,2,1,2,3,3,3,2,2,2,3,5,5,3,2,1,2,3,3,3,2,2,3,2,1]
    little_lamb_chars = ['E','D','C','D','E','E','E','D','D','D','E','G','G','E','D','C','D','E','E','E','D','D','E','D','C']

    # twinkle twinkle little star
    #                 [C,C,G,G,A,A,G,F,F,E,E,D,D,C,G,G,F,F,E,E,D,G,G,F,F,E,E,D,C,C,G,G,A,A,G,F,F,E,E,D,D,C]
    twinkle_twinkle = [0,0,7,7,9,9,7,5,5,4,4,2,2,0,7,7,5,5,4,4,2,7,7,5,5,4,4,2,0,0,7,7,9,9,7,5,5,4,4,2,2,0]
    # ideal soln:     [1,1,4,4,5,5,4,3,3,2,2,1,1,2,5,5,4,4,3,3,2,5,5,4,4,3,3,2,1,1,4,4,5,5,4,3,3,2,2,1,1,2]
    twinkle_twinkle_little_chars = ['C','C','G','G','A','A','G','F','F','E','E','D','D','C','G','G','F','F','E','E','D','G','G','F','F','E','E','D','C','C','G','G','A','A','G','F','F','E','E','D','D','C']
    
    # format of all reference arrays:
    # [1-1, 1-2, 1-3, 1-4, 1-5, 2-1, 2-2, 2-3, 2-4, 2-5, 3-1, 3-2, 3-3, 3-4, 3-5, ...]
    minComf = [0,-3,-3,-1,3,   -8,0,1,1,2,   -10,-3,0,1,1,   -12,-5,-2,0,1,   -13,-8,-5,-3,0]
    maxComf = [0,8,10,12,13,   2,0,3,5,8,    3,1,0,2,5,      1,1,1,0,3,       -3,-2,-1,-1,0]
    minRel =  [0,1,3,5,7,      -5,0,1,3,5,   -7,-2,0,1,3,    -5,-4,-3,0,1,    -10,-6,-4,-2,0]
    maxRel =  [0,5,7,9,10,     -1,0,2,4,6,   -3,-2,0,2,4,    -9,-3,-1,0,2,    -7,-5,-3,-1,0]

    # TODO #2
    possible_placement = []

    # limit to only the top 5 best solutions (based on total points after each pitch)
    sol1 = [1]
    sol2 = [2]
    sol3 = [3]
    sol4 = [4]
    sol5 = [5]
    sol6 = [1]
    sol7 = [2]
    sol8 = [3]
    sol9 = [4]
    sol10 = [5]
    sol11 = [1]
    sol12 = [2]
    sol13 = [3]
    sol14 = [4]
    sol15 = [5]
    
    sol1_temp = []
    sol2_temp = []
    sol3_temp = []
    sol4_temp = []
    sol5_temp = []
    sol6_temp = []
    sol7_temp = []
    sol8_temp = []
    sol9_temp = []
    sol10_temp = []
    sol11_temp = []
    sol12_temp = []
    sol13_temp = []
    sol14_temp = []
    sol15_temp = []

    # create arrays to hold current information about top 15 possible solutions
    scores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    temp_scores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    temp_sol_num = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
    temp_poss_sol_index = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # these hold the scores for each possible next finger placement for each current solution (expand)
    poss_sol1_scores = [0,0,0,0,0]
    poss_sol2_scores = [0,0,0,0,0]
    poss_sol3_scores = [0,0,0,0,0]
    poss_sol4_scores = [0,0,0,0,0]
    poss_sol5_scores = [0,0,0,0,0]
    poss_sol6_scores = [0,0,0,0,0]
    poss_sol7_scores = [0,0,0,0,0]
    poss_sol8_scores = [0,0,0,0,0]
    poss_sol9_scores = [0,0,0,0,0]
    poss_sol10_scores = [0,0,0,0,0]   
    poss_sol11_scores = [0,0,0,0,0]
    poss_sol12_scores = [0,0,0,0,0]
    poss_sol13_scores = [0,0,0,0,0]
    poss_sol14_scores = [0,0,0,0,0]
    poss_sol15_scores = [0,0,0,0,0] 
    
    # for every pitch in the song
    # for p in range(1, len(little_lamb)):
    for p in range(1, len(little_lamb)):

        # TODO #3
        # TODO #4

        # if pitch1 < pitch2 (e.g. [C,D]), semitones > 0
        # semitones = little_lamb[p] - little_lamb[p-1]
        semitones = little_lamb[p] - little_lamb[p-1]


        if (p > 1):
            # semitones_1_3 = little_lamb[p] - little_lamb[p-2]
            semitones_1_3 = little_lamb[p] - little_lamb[p-2]

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
            reference_index_6 = ((sol1[p-1]-1)*5)+(f2-1)
            reference_index_7 = ((sol2[p-1]-1)*5)+(f2-1)
            reference_index_8 = ((sol3[p-1]-1)*5)+(f2-1)
            reference_index_9 = ((sol4[p-1]-1)*5)+(f2-1)
            reference_index_10 = ((sol5[p-1]-1)*5)+(f2-1)
            reference_index_11 = ((sol5[p-1]-1)*5)+(f2-1)
            reference_index_12 = ((sol5[p-1]-1)*5)+(f2-1)
            reference_index_13 = ((sol5[p-1]-1)*5)+(f2-1)
            reference_index_14 = ((sol5[p-1]-1)*5)+(f2-1)
            reference_index_15 = ((sol5[p-1]-1)*5)+(f2-1)            

            # calculate ref index for 1st & 3rd interval
            reference_index_1st_3rd_1 = ((sol1[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_2 = ((sol2[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_3 = ((sol3[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_4 = ((sol4[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_5 = ((sol5[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_6 = ((sol1[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_7 = ((sol2[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_8 = ((sol3[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_9 = ((sol4[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_10 = ((sol5[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_11 = ((sol5[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_12 = ((sol5[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_13 = ((sol5[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_14 = ((sol5[p-2]-1)*5)+(f2-1)
            reference_index_1st_3rd_15 = ((sol5[p-2]-1)*5)+(f2-1)
            
            # ADDING A RULE: if going down 1 or 2 semitones, add points if difference in finger is >1
            if (semitones == -1 or semitones == -2):
                if (sol1[-1] - f2 > 1): poss_sol1_scores[f2-1] += 2
                if (sol2[-1] - f2 > 1): poss_sol2_scores[f2-1] += 2
                if (sol3[-1] - f2 > 1): poss_sol3_scores[f2-1] += 2
                if (sol4[-1] - f2 > 1): poss_sol4_scores[f2-1] += 2
                if (sol5[-1] - f2 > 1): poss_sol5_scores[f2-1] += 2
                if (sol6[-1] - f2 > 1): poss_sol6_scores[f2-1] += 2
                if (sol7[-1] - f2 > 1): poss_sol7_scores[f2-1] += 2
                if (sol8[-1] - f2 > 1): poss_sol8_scores[f2-1] += 2
                if (sol9[-1] - f2 > 1): poss_sol9_scores[f2-1] += 2
                if (sol10[-1] - f2 > 1): poss_sol10_scores[f2-1] += 2
                if (sol11[-1] - f2 > 1): poss_sol11_scores[f2-1] += 2
                if (sol12[-1] - f2 > 1): poss_sol12_scores[f2-1] += 2
                if (sol13[-1] - f2 > 1): poss_sol13_scores[f2-1] += 2
                if (sol14[-1] - f2 > 1): poss_sol14_scores[f2-1] += 2
                if (sol15[-1] - f2 > 1): poss_sol15_scores[f2-1] += 2

            # if going UP 1 or 2 STs, add points if difference in fingers is >1
            elif (semitones == 1 or semitones == 2):
                if (f2 - sol1[-1] > 1): poss_sol1_scores[f2-1] += 2
                if (f2 - sol2[-1] > 1): poss_sol2_scores[f2-1] += 2
                if (f2 - sol3[-1] > 1): poss_sol3_scores[f2-1] += 2
                if (f2 - sol4[-1] > 1): poss_sol4_scores[f2-1] += 2
                if (f2 - sol5[-1] > 1): poss_sol5_scores[f2-1] += 2
                if (f2 - sol6[-1] > 1): poss_sol6_scores[f2-1] += 2
                if (f2 - sol7[-1] > 1): poss_sol7_scores[f2-1] += 2
                if (f2 - sol8[-1] > 1): poss_sol8_scores[f2-1] += 2
                if (f2 - sol9[-1] > 1): poss_sol9_scores[f2-1] += 2
                if (f2 - sol10[-1] > 1): poss_sol10_scores[f2-1] += 2
                if (f2 - sol11[-1] > 1): poss_sol11_scores[f2-1] += 2
                if (f2 - sol11[-1] > 1): poss_sol12_scores[f2-1] += 2
                if (f2 - sol11[-1] > 1): poss_sol13_scores[f2-1] += 2
                if (f2 - sol11[-1] > 1): poss_sol14_scores[f2-1] += 2
            
            # if going DOWN 7 or more semitones, add points if difference in fingers is less than 4
            if (semitones < -6):
                if (sol1[-1] - f2 < 3): poss_sol1_scores[f2-1] += 5
                if (sol2[-1] - f2 < 3): poss_sol2_scores[f2-1] += 5
                if (sol3[-1] - f2 < 3): poss_sol3_scores[f2-1] += 5
                if (sol4[-1] - f2 < 3): poss_sol4_scores[f2-1] += 5
                if (sol5[-1] - f2 < 3): poss_sol5_scores[f2-1] += 5
                if (sol6[-1] - f2 < 3): poss_sol6_scores[f2-1] += 5
                if (sol7[-1] - f2 < 3): poss_sol7_scores[f2-1] += 5
                if (sol8[-1] - f2 < 3): poss_sol8_scores[f2-1] += 5
                if (sol9[-1] - f2 < 3): poss_sol9_scores[f2-1] += 5
                if (sol10[-1] - f2 < 3): poss_sol10_scores[f2-1] += 5
                if (sol11[-1] - f2 < 3): poss_sol11_scores[f2-1] += 5
                if (sol12[-1] - f2 < 3): poss_sol12_scores[f2-1] += 5
                if (sol13[-1] - f2 < 3): poss_sol13_scores[f2-1] += 5
                if (sol14[-1] - f2 < 3): poss_sol14_scores[f2-1] += 5
            
            # if going UP 7 or more STs, add points if difference in fingers is less than 4
            elif (semitones > 6):
                if (f2 - sol1[-1] < 3): poss_sol1_scores[f2-1] += 5
                if (f2 - sol2[-1] < 3): poss_sol2_scores[f2-1] += 5
                if (f2 - sol3[-1] < 3): poss_sol3_scores[f2-1] += 5
                if (f2 - sol4[-1] < 3): poss_sol4_scores[f2-1] += 5
                if (f2 - sol5[-1] < 3): poss_sol5_scores[f2-1] += 5
                if (f2 - sol6[-1] < 3): poss_sol6_scores[f2-1] += 5
                if (f2 - sol7[-1] < 3): poss_sol7_scores[f2-1] += 5
                if (f2 - sol8[-1] < 3): poss_sol8_scores[f2-1] += 5
                if (f2 - sol9[-1] < 3): poss_sol9_scores[f2-1] += 5
                if (f2 - sol10[-1] < 3): poss_sol10_scores[f2-1] += 5
                if (f2 - sol11[-1] < 3): poss_sol11_scores[f2-1] += 5
                if (f2 - sol12[-1] < 3): poss_sol12_scores[f2-1] += 5
                if (f2 - sol13[-1] < 3): poss_sol13_scores[f2-1] += 5
                if (f2 - sol14[-1] < 3): poss_sol14_scores[f2-1] += 5
                if (f2 - sol15[-1] < 3): poss_sol15_scores[f2-1] += 5
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
            # solution 6
            if (semitones < minComf[reference_index_6]): poss_sol6_scores[f2-1] += 2*(minComf[reference_index_6] - semitones)
            elif (semitones > maxComf[reference_index_6]): poss_sol6_scores[f2-1] += 2*(semitones - maxComf[reference_index_6])
            # solution 7
            if (semitones < minComf[reference_index_7]): poss_sol7_scores[f2-1] += 2*(minComf[reference_index_7] - semitones)
            elif (semitones > maxComf[reference_index_7]): poss_sol7_scores[f2-1] += 2*(semitones - maxComf[reference_index_7])
            # solution 8
            if (semitones < minComf[reference_index_8]): poss_sol8_scores[f2-1] += 2*(minComf[reference_index_8] - semitones)
            elif (semitones > maxComf[reference_index_8]): poss_sol8_scores[f2-1] += 2*(semitones - maxComf[reference_index_8])
            # solution 9
            if (semitones < minComf[reference_index_9]): poss_sol9_scores[f2-1] += 2*(minComf[reference_index_9] - semitones)
            elif (semitones > maxComf[reference_index_9]): poss_sol9_scores[f2-1] += 2*(semitones - maxComf[reference_index_9])
            # solution 10
            if (semitones < minComf[reference_index_10]): poss_sol10_scores[f2-1] += 2*(minComf[reference_index_10] - semitones)
            elif (semitones > maxComf[reference_index_10]): poss_sol10_scores[f2-1] += 2*(semitones - maxComf[reference_index_10])
            # solution 11
            if (semitones < minComf[reference_index_11]): poss_sol11_scores[f2-1] += 2*(minComf[reference_index_11] - semitones)
            elif (semitones > maxComf[reference_index_11]): poss_sol11_scores[f2-1] += 2*(semitones - maxComf[reference_index_11])
            # solution 12
            if (semitones < minComf[reference_index_12]): poss_sol12_scores[f2-1] += 2*(minComf[reference_index_12] - semitones)
            elif (semitones > maxComf[reference_index_12]): poss_sol12_scores[f2-1] += 2*(semitones - maxComf[reference_index_12])
            # solution 13
            if (semitones < minComf[reference_index_13]): poss_sol13_scores[f2-1] += 2*(minComf[reference_index_13] - semitones)
            elif (semitones > maxComf[reference_index_13]): poss_sol13_scores[f2-1] += 2*(semitones - maxComf[reference_index_13])
            # solution 14
            if (semitones < minComf[reference_index_14]): poss_sol14_scores[f2-1] += 2*(minComf[reference_index_14] - semitones)
            elif (semitones > maxComf[reference_index_14]): poss_sol14_scores[f2-1] += 2*(semitones - maxComf[reference_index_14])
            # solution 15
            if (semitones < minComf[reference_index_15]): poss_sol15_scores[f2-1] += 2*(minComf[reference_index_15] - semitones)
            elif (semitones > maxComf[reference_index_15]): poss_sol15_scores[f2-1] += 2*(semitones - maxComf[reference_index_15])

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
            # solution 6
            if (semitones < minRel[reference_index_6]): poss_sol6_scores[f2-1] += minRel[reference_index_6] - semitones
            elif (semitones > maxRel[reference_index_6]): poss_sol6_scores[f2-1] += semitones - maxRel[reference_index_6]
            # solution 7
            if (semitones < minRel[reference_index_7]): poss_sol7_scores[f2-1] += minRel[reference_index_7] - semitones
            elif (semitones > maxRel[reference_index_7]): poss_sol7_scores[f2-1] += semitones - maxRel[reference_index_7]
            # solution 8
            if (semitones < minRel[reference_index_8]): poss_sol8_scores[f2-1] += minRel[reference_index_8] - semitones
            elif (semitones > maxRel[reference_index_8]): poss_sol8_scores[f2-1] += semitones - maxRel[reference_index_8]
            # solution 9
            if (semitones < minRel[reference_index_9]): poss_sol9_scores[f2-1] += minRel[reference_index_9] - semitones
            elif (semitones > maxRel[reference_index_9]): poss_sol9_scores[f2-1] += semitones - maxRel[reference_index_9]
            # solution 10
            if (semitones < minRel[reference_index_10]): poss_sol10_scores[f2-1] += minRel[reference_index_10] - semitones
            elif (semitones > maxRel[reference_index_10]): poss_sol10_scores[f2-1] += semitones - maxRel[reference_index_10]
            # solution 11
            if (semitones < minRel[reference_index_11]): poss_sol11_scores[f2-1] += minRel[reference_index_11] - semitones
            elif (semitones > maxRel[reference_index_11]): poss_sol11_scores[f2-1] += semitones - maxRel[reference_index_11]
            # solution 12
            if (semitones < minRel[reference_index_12]): poss_sol12_scores[f2-1] += minRel[reference_index_12] - semitones
            elif (semitones > maxRel[reference_index_12]): poss_sol12_scores[f2-1] += semitones - maxRel[reference_index_12]
            # solution 13
            if (semitones < minRel[reference_index_13]): poss_sol13_scores[f2-1] += minRel[reference_index_13] - semitones
            elif (semitones > maxRel[reference_index_13]): poss_sol13_scores[f2-1] += semitones - maxRel[reference_index_13]
            # solution 14
            if (semitones < minRel[reference_index_14]): poss_sol14_scores[f2-1] += minRel[reference_index_14] - semitones
            elif (semitones > maxRel[reference_index_14]): poss_sol14_scores[f2-1] += semitones - maxRel[reference_index_14]
            # solution 15
            if (semitones < minRel[reference_index_15]): poss_sol15_scores[f2-1] += minRel[reference_index_15] - semitones
            elif (semitones > maxRel[reference_index_15]): poss_sol15_scores[f2-1] += semitones - maxRel[reference_index_15]

            #
            #
            # RULE 3
            # compare minComf & maxComf for 1st & 3rd interval
            
            # changes this so it will calculate the score for 1st/3rd interval in the first round to narrow down more. (p=1)
            # then, it will skip this calculation for the next round, instead of doing it again with the same interval. (p=2)
            # after this, it will operate normally. (p>2)
            if (p>1):
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
                # solution 6
                if (semitones_1_3 < minComf[reference_index_1st_3rd_6]): poss_sol6_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_6] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_6]): poss_sol6_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_6])
                # solution 7
                if (semitones_1_3 < minComf[reference_index_1st_3rd_7]): poss_sol7_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_7] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_7]): poss_sol7_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_7])
                # solution 8
                if (semitones_1_3 < minComf[reference_index_1st_3rd_8]): poss_sol8_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_8] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_8]): poss_sol8_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_8])
                # solution 9
                if (semitones_1_3 < minComf[reference_index_1st_3rd_9]): poss_sol9_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_9] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_9]): poss_sol9_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_9])
                # solution 10
                if (semitones_1_3 < minComf[reference_index_1st_3rd_10]): poss_sol10_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_10] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_10]): poss_sol10_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_10])
                # solution 11
                if (semitones_1_3 < minComf[reference_index_1st_3rd_11]): poss_sol11_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_11] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_11]): poss_sol11_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_11])
                # solution 12
                if (semitones_1_3 < minComf[reference_index_1st_3rd_12]): poss_sol12_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_12] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_12]): poss_sol12_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_12])
                # solution 13
                if (semitones_1_3 < minComf[reference_index_1st_3rd_13]): poss_sol13_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_13] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_13]): poss_sol13_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_13])
                # solution 14
                if (semitones_1_3 < minComf[reference_index_1st_3rd_14]): poss_sol14_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_14] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_14]): poss_sol14_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_14])
                # solution 15
                if (semitones_1_3 < minComf[reference_index_1st_3rd_15]): poss_sol15_scores[f2-1] += 2*(minComf[reference_index_1st_3rd_15] - semitones_1_3)
                elif (semitones_1_3 > maxComf[reference_index_1st_3rd_15]): poss_sol15_scores[f2-1] += 2*(semitones_1_3 - maxComf[reference_index_1st_3rd_15])

            #
            #
            # TODO #5
            # add point if sequence [3,4,5] occurs -> add 1pt
            # add point if sequence [5,4,3] occurs -> add 1pt

            # TODO #4
            # [3,4] or [4,3] AND 3=white & 4=black -> add 1pt

            # TODO #4
            # thumb plays black key -> add 1pt
            # note before = white -> add 2pts
            # note after = white -> add 2pts

            # TODO #4
            # if thumb pass on the way down
            if (semitones < 0):
                if ((sol1[-1]==1) & (f2 != 1)): poss_sol1_scores[f2-1] += 1
                elif ((sol2[-1]==1) & (f2 != 1)): poss_sol2_scores[f2-1] += 1
                elif ((sol3[-1]==1) & (f2 != 1)): poss_sol3_scores[f2-1] += 1
                elif ((sol4[-1]==1) & (f2 != 1)): poss_sol4_scores[f2-1] += 1
                elif ((sol5[-1]==1) & (f2 != 1)): poss_sol5_scores[f2-1] += 1
                elif ((sol6[-1]==1) & (f2 != 1)): poss_sol6_scores[f2-1] += 1
                elif ((sol7[-1]==1) & (f2 != 1)): poss_sol7_scores[f2-1] += 1
                elif ((sol8[-1]==1) & (f2 != 1)): poss_sol8_scores[f2-1] += 1
                elif ((sol9[-1]==1) & (f2 != 1)): poss_sol9_scores[f2-1] += 1
                elif ((sol10[-1]==1) & (f2 != 1)): poss_sol0_scores[f2-1] += 1
                elif ((sol11[-1]==1) & (f2 != 1)): poss_sol1_scores[f2-1] += 1
                elif ((sol12[-1]==1) & (f2 != 1)): poss_sol2_scores[f2-1] += 1
                elif ((sol13[-1]==1) & (f2 != 1)): poss_sol3_scores[f2-1] += 1
                elif ((sol14[-1]==1) & (f2 != 1)): poss_sol4_scores[f2-1] += 1
                elif ((sol15[-1]==1) & (f2 != 1)): poss_sol5_scores[f2-1] += 1
            # if thumb pass on the way up
            elif (semitones > 0):
                if ((sol1[-1]!=1) & (f2==1)): poss_sol1_scores[f2-1] += 1
                if ((sol2[-1]!=1) & (f2==1)): poss_sol2_scores[f2-1] += 1
                if ((sol3[-1]!=1) & (f2==1)): poss_sol3_scores[f2-1] += 1
                if ((sol4[-1]!=1) & (f2==1)): poss_sol4_scores[f2-1] += 1
                if ((sol5[-1]!=1) & (f2==1)): poss_sol5_scores[f2-1] += 1
                if ((sol6[-1]!=1) & (f2==1)): poss_sol6_scores[f2-1] += 1
                if ((sol7[-1]!=1) & (f2==1)): poss_sol7_scores[f2-1] += 1
                if ((sol8[-1]!=1) & (f2==1)): poss_sol8_scores[f2-1] += 1
                if ((sol9[-1]!=1) & (f2==1)): poss_sol9_scores[f2-1] += 1
                if ((sol10[-1]!=1) & (f2==1)): poss_sol10_scores[f2-1] += 1
                if ((sol11[-1]!=1) & (f2==1)): poss_sol11_scores[f2-1] += 1
                if ((sol12[-1]!=1) & (f2==1)): poss_sol12_scores[f2-1] += 1
                if ((sol13[-1]!=1) & (f2==1)): poss_sol13_scores[f2-1] += 1
                if ((sol14[-1]!=1) & (f2==1)): poss_sol14_scores[f2-1] += 1
                if ((sol15[-1]!=1) & (f2==1)): poss_sol15_scores[f2-1] += 1
                

            # thumb pass with lower pitch = white&not thumb, upper = black&thumb -> add 3pts
    
        #
        #
        # COMPARE SCORES

        # DONE: initialize the temporary solution variables
        # expand to 10 possible solutions
        for a in range (0,5):
            temp_scores[a] = poss_sol1_scores[a]
        for b in range (5,10):
            temp_scores[b] = poss_sol2_scores[b-5]
        for c in range (10,15):
            temp_scores[c] = poss_sol3_scores[c-10]
        temp_sol_num = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
        temp_poss_sol_index = [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]
        
        # DONE: compare scores of all possible solutions & update temporary solution arrays
        for i in range (0,5):
            
            #
            # SOLUTION 1
            # if sol1[i] is the new best score
            if (poss_sol1_scores[i] < temp_scores[0]):
                for j in range (14,0,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new best solution
                temp_scores[0] = poss_sol1_scores.copy()[i]
                temp_sol_num[0] = 1
                temp_poss_sol_index[0] = i
            # if sol1[i] is the new 2nd-best score
            elif (poss_sol1_scores[i] < temp_scores[1]):
                for j in range (14,1,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 2nd-best solution
                temp_scores[1] = poss_sol1_scores.copy()[i]
                temp_sol_num[1] = 1
                temp_poss_sol_index[1] = i
            # if sol1[i] is the new 3rd-best score
            elif (poss_sol1_scores[i] < temp_scores[2]):
                for j in range (14,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 3rd-best solution
                temp_scores[2] = poss_sol1_scores.copy()[i]
                temp_sol_num[2] = 1
                temp_poss_sol_index[2] = i
            # if sol1[i] is the new 4th-best score
            elif (poss_sol1_scores[i] < temp_scores[3]):
                for j in range (14,3,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 4-th best solution
                temp_scores[3] = poss_sol1_scores.copy()[i]
                temp_sol_num[3] = 1
                temp_poss_sol_index[3] = i
            # if sol1[i] is the new 5th-best score
            elif (poss_sol1_scores[i] < temp_scores[4]):
                for j in range (14,4,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 5th-best solution
                temp_scores[4] = poss_sol1_scores.copy()[i]
                temp_sol_num[4] = 1
                temp_poss_sol_index[4] = i
            # if sol1[i] is the new 6th-best score
            elif (poss_sol1_scores[i] < temp_scores[5]):
                for j in range (14,5,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 6th-best solution
                temp_scores[5] = poss_sol1_scores.copy()[i]
                temp_sol_num[5] = 1
                temp_poss_sol_index[5] = i
            # if sol1[i] is the new 7th-best score
            elif (poss_sol1_scores[i] < temp_scores[6]):
                for j in range (14,6,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 7th-best solution
                temp_scores[6] = poss_sol1_scores.copy()[i]
                temp_sol_num[6] = 1
                temp_poss_sol_index[6] = i
            # if sol1[i] is the new 8th-best score
            elif (poss_sol1_scores[i] < temp_scores[7]):
                for j in range (14,7,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 8th-best solution
                temp_scores[7] = poss_sol1_scores.copy()[i]
                temp_sol_num[7] = 1
                temp_poss_sol_index[7] = i
            # if sol1[i] is the new 9th-best score
            elif (poss_sol1_scores[i] < temp_scores[8]):
                for j in range (14,8,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 9th-best solution
                temp_scores[8] = poss_sol1_scores.copy()[i]
                temp_sol_num[8] = 1
                temp_poss_sol_index[8] = i
            # if sol1[i] is the new 10th-best score
            elif (poss_sol1_scores[i] < temp_scores[9]):
                for j in range (14,9,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 10th-best solution
                temp_scores[9] = poss_sol1_scores.copy()[i]
                temp_sol_num[9] = 1
                temp_poss_sol_index[9] = i
            # if sol1[i] is the new 11th-best score
            elif (poss_sol1_scores[i] < temp_scores[10]):
                for j in range (14,10,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 11th-best solution
                temp_scores[10] = poss_sol1_scores.copy()[i]
                temp_sol_num[10] = 1
                temp_poss_sol_index[10] = i
            # if sol1[i] is the new 12th-best score
            elif (poss_sol1_scores[i] < temp_scores[11]):
                for j in range (14,11,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 12th-best solution
                temp_scores[11] = poss_sol1_scores.copy()[i]
                temp_sol_num[11] = 1
                temp_poss_sol_index[11] = i
            # if sol1[i] is the new 13th-best score
            elif (poss_sol1_scores[i] < temp_scores[12]):
                for j in range (14,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 13th-best solution
                temp_scores[12] = poss_sol1_scores.copy()[i]
                temp_sol_num[12] = 1
                temp_poss_sol_index[12] = i
            # if sol1[i] is the new 14th-best score
            elif (poss_sol1_scores[i] < temp_scores[13]):
                temp_scores[14] = temp_scores.copy()[13]
                temp_sol_num[14] = temp_sol_num.copy()[13]
                temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                # set the new 14th-best solution
                temp_scores[13] = poss_sol1_scores.copy()[i]
                temp_sol_num[13] = 1
                temp_poss_sol_index[13] = i
            # if sol1[i] is the new 15th-best score
            elif (poss_sol1_scores[i] < temp_scores[14]):
                # set the new 14th-best solution
                temp_scores[14] = poss_sol1_scores.copy()[i]
                temp_sol_num[14] = 1
                temp_poss_sol_index[14] = i
            
            #
            # SOLUTION 2
            # if sol2[i] is the new best score
            if (poss_sol2_scores[i] < temp_scores[0]):
                for j in range (14,0,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new best solution
                temp_scores[0] = poss_sol2_scores.copy()[i]
                temp_sol_num[0] = 2
                temp_poss_sol_index[0] = i
            # if sol2[i] is the new 2nd-best score
            elif (poss_sol2_scores[i] < temp_scores[1]):
                for j in range (14,1,-1):
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
                for j in range (14,2,-1):
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
                for j in range (14,3,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 4-th best solution
                temp_scores[3] = poss_sol2_scores.copy()[i]
                temp_sol_num[3] = 2
                temp_poss_sol_index[3] = i
            # if sol2[i] is the new 5th-best score
            elif (poss_sol2_scores[i] < temp_scores[4]):
                for j in range (14,4,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 5th-best solution
                temp_scores[4] = poss_sol2_scores.copy()[i]
                temp_sol_num[4] = 2
                temp_poss_sol_index[4] = i
            # if sol2[i] is the new 6th-best score
            elif (poss_sol2_scores[i] < temp_scores[5]):
                for j in range (14,5,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 6th-best solution
                temp_scores[5] = poss_sol2_scores.copy()[i]
                temp_sol_num[5] = 2
                temp_poss_sol_index[5] = i
            # if sol2[i] is the new 7th-best score
            elif (poss_sol2_scores[i] < temp_scores[6]):
                for j in range (14,6,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 7th-best solution
                temp_scores[6] = poss_sol2_scores.copy()[i]
                temp_sol_num[6] = 2
                temp_poss_sol_index[6] = i
            # if sol2[i] is the new 8th-best score
            elif (poss_sol2_scores[i] < temp_scores[7]):
                for j in range (14,7,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 8th-best solution
                temp_scores[7] = poss_sol2_scores.copy()[i]
                temp_sol_num[7] = 2
                temp_poss_sol_index[7] = i
            # if sol2[i] is the new 9th-best score
            elif (poss_sol2_scores[i] < temp_scores[8]):
                for j in range (14,8,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 9th-best solution
                temp_scores[8] = poss_sol2_scores.copy()[i]
                temp_sol_num[8] = 2
                temp_poss_sol_index[8] = i
            # if sol2[i] is the new 10th-best score
            elif (poss_sol2_scores[i] < temp_scores[9]):
                for j in range (14,9,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 10th-best solution
                temp_scores[9] = poss_sol2_scores.copy()[i]
                temp_sol_num[9] = 2
                temp_poss_sol_index[9] = i
            # if sol2[i] is the new 11th-best score
            elif (poss_sol2_scores[i] < temp_scores[10]):
                for j in range (14,10,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 11th-best solution
                temp_scores[10] = poss_sol2_scores.copy()[i]
                temp_sol_num[10] = 2
                temp_poss_sol_index[10] = i
            # if sol2[i] is the new 12th-best score
            elif (poss_sol2_scores[i] < temp_scores[11]):
                for j in range (14,11,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 12th-best solution
                temp_scores[11] = poss_sol2_scores.copy()[i]
                temp_sol_num[11] = 2
                temp_poss_sol_index[11] = i
            # if sol2[i] is the new 13th-best score
            elif (poss_sol2_scores[i] < temp_scores[12]):
                for j in range (14,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 13th-best solution
                temp_scores[12] = poss_sol2_scores.copy()[i]
                temp_sol_num[12] = 2
                temp_poss_sol_index[12] = i
            # if sol2[i] is the new 14th-best score
            elif (poss_sol2_scores[i] < temp_scores[13]):
                temp_scores[14] = temp_scores.copy()[13]
                temp_sol_num[14] = temp_sol_num.copy()[13]
                temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                # set the new 14th-best solution
                temp_scores[13] = poss_sol2_scores.copy()[i]
                temp_sol_num[13] = 2
                temp_poss_sol_index[13] = i
            # if sol2[i] is the new 15th-best score
            elif (poss_sol2_scores[i] < temp_scores[14]):
                # set the new 14th-best solution
                temp_scores[14] = poss_sol2_scores.copy()[i]
                temp_sol_num[14] = 2
                temp_poss_sol_index[14] = i

            #
            # SOLUTION 3
            # if sol3[i] is the new best score
            if (poss_sol3_scores[i] < temp_scores[0]):
                for j in range (14,0,-1):
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
                for j in range (14,1,-1):
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
                for j in range (14,2,-1):
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
                for j in range (14,3,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 4-th best solution
                temp_scores[3] = poss_sol3_scores.copy()[i]
                temp_sol_num[3] = 3
                temp_poss_sol_index[3] = i
            # if sol3[i] is the new 5th-best score
            elif (poss_sol3_scores[i] < temp_scores[4]):
                for j in range (14,4,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 5th-best solution
                temp_scores[4] = poss_sol3_scores.copy()[i]
                temp_sol_num[4] = 3
                temp_poss_sol_index[4] = i
            # if sol3[i] is the new 6th-best score
            elif (poss_sol3_scores[i] < temp_scores[5]):
                for j in range (14,5,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 6th-best solution
                temp_scores[5] = poss_sol3_scores.copy()[i]
                temp_sol_num[5] = 3
                temp_poss_sol_index[5] = i
            # if sol3[i] is the new 7th-best score
            elif (poss_sol3_scores[i] < temp_scores[6]):
                for j in range (14,6,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 7th-best solution
                temp_scores[6] = poss_sol3_scores.copy()[i]
                temp_sol_num[6] = 3
                temp_poss_sol_index[6] = i
            # if sol3[i] is the new 8th-best score
            elif (poss_sol3_scores[i] < temp_scores[7]):
                for j in range (14,7,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 8th-best solution
                temp_scores[7] = poss_sol3_scores.copy()[i]
                temp_sol_num[7] = 3
                temp_poss_sol_index[7] = i
            # if sol3[i] is the new 9th-best score
            elif (poss_sol3_scores[i] < temp_scores[8]):
                for j in range (14,8,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 9th-best solution
                temp_scores[8] = poss_sol3_scores.copy()[i]
                temp_sol_num[8] = 3
                temp_poss_sol_index[8] = i
            # if sol3[i] is the new 10th-best score
            elif (poss_sol3_scores[i] < temp_scores[9]):
                for j in range (14,9,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 10th-best solution
                temp_scores[9] = poss_sol3_scores.copy()[i]
                temp_sol_num[9] = 3
                temp_poss_sol_index[9] = i
            # if sol3[i] is the new 11th-best score
            elif (poss_sol3_scores[i] < temp_scores[10]):
                for j in range (14,10,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 11th-best solution
                temp_scores[10] = poss_sol3_scores.copy()[i]
                temp_sol_num[10] = 3
                temp_poss_sol_index[10] = i
            # if sol3[i] is the new 12th-best score
            elif (poss_sol3_scores[i] < temp_scores[11]):
                for j in range (14,11,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 12th-best solution
                temp_scores[11] = poss_sol3_scores.copy()[i]
                temp_sol_num[11] = 3
                temp_poss_sol_index[11] = i
            # if sol3[i] is the new 13th-best score
            elif (poss_sol3_scores[i] < temp_scores[12]):
                for j in range (14,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 13th-best solution
                temp_scores[12] = poss_sol3_scores.copy()[i]
                temp_sol_num[12] = 3
                temp_poss_sol_index[12] = i
            # if sol3[i] is the new 14th-best score
            elif (poss_sol3_scores[i] < temp_scores[13]):
                temp_scores[14] = temp_scores.copy()[13]
                temp_sol_num[14] = temp_sol_num.copy()[13]
                temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                # set the new 14th-best solution
                temp_scores[13] = poss_sol3_scores.copy()[i]
                temp_sol_num[13] = 3
                temp_poss_sol_index[13] = i
            # if sol3[i] is the new 15th-best score
            elif (poss_sol3_scores[i] < temp_scores[14]):
                # set the new 14th-best solution
                temp_scores[14] = poss_sol3_scores.copy()[i]
                temp_sol_num[14] = 3
                temp_poss_sol_index[14] = i

            #
            # SOLUTION 4
            # if sol4[i] is the new best score
            if (poss_sol4_scores[i] < temp_scores[0]):
                for j in range (14,0,-1):
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
                for j in range (14,1,-1):
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
                for j in range (14,2,-1):
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
                for j in range (14,3,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 4-th best solution
                temp_scores[3] = poss_sol4_scores.copy()[i]
                temp_sol_num[3] = 4
                temp_poss_sol_index[3] = i
            # if sol4[i] is the new 5th-best score
            elif (poss_sol4_scores[i] < temp_scores[4]):
                for j in range (14,4,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 5th-best solution
                temp_scores[4] = poss_sol4_scores.copy()[i]
                temp_sol_num[4] = 4
                temp_poss_sol_index[4] = i
            # if sol4[i] is the new 6th-best score
            elif (poss_sol4_scores[i] < temp_scores[5]):
                for j in range (14,5,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 6th-best solution
                temp_scores[5] = poss_sol4_scores.copy()[i]
                temp_sol_num[5] = 4
                temp_poss_sol_index[5] = i
            # if sol4[i] is the new 7th-best score
            elif (poss_sol4_scores[i] < temp_scores[6]):
                for j in range (14,6,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 7th-best solution
                temp_scores[6] = poss_sol4_scores.copy()[i]
                temp_sol_num[6] = 4
                temp_poss_sol_index[6] = i
            # if sol4[i] is the new 8th-best score
            elif (poss_sol4_scores[i] < temp_scores[7]):
                for j in range (14,7,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 8th-best solution
                temp_scores[7] = poss_sol4_scores.copy()[i]
                temp_sol_num[7] = 4
                temp_poss_sol_index[7] = i
            # if sol4[i] is the new 9th-best score
            elif (poss_sol4_scores[i] < temp_scores[8]):
                for j in range (14,8,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 9th-best solution
                temp_scores[8] = poss_sol4_scores.copy()[i]
                temp_sol_num[8] = 4
                temp_poss_sol_index[8] = i
            # if sol4[i] is the new 10th-best score
            elif (poss_sol4_scores[i] < temp_scores[9]):
                for j in range (14,9,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 10th-best solution
                temp_scores[9] = poss_sol4_scores.copy()[i]
                temp_sol_num[9] = 4
                temp_poss_sol_index[9] = i
            # if sol4[i] is the new 11th-best score
            elif (poss_sol4_scores[i] < temp_scores[10]):
                for j in range (14,10,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 11th-best solution
                temp_scores[10] = poss_sol4_scores.copy()[i]
                temp_sol_num[10] = 4
                temp_poss_sol_index[10] = i
            # if sol4[i] is the new 12th-best score
            elif (poss_sol4_scores[i] < temp_scores[11]):
                for j in range (14,11,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 12th-best solution
                temp_scores[11] = poss_sol4_scores.copy()[i]
                temp_sol_num[11] = 4
                temp_poss_sol_index[11] = i
            # if sol4[i] is the new 13th-best score
            elif (poss_sol4_scores[i] < temp_scores[12]):
                for j in range (14,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 13th-best solution
                temp_scores[12] = poss_sol4_scores.copy()[i]
                temp_sol_num[12] = 4
                temp_poss_sol_index[12] = i
            # if sol4[i] is the new 14th-best score
            elif (poss_sol4_scores[i] < temp_scores[13]):
                temp_scores[14] = temp_scores.copy()[13]
                temp_sol_num[14] = temp_sol_num.copy()[13]
                temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                # set the new 14th-best solution
                temp_scores[13] = poss_sol4_scores.copy()[i]
                temp_sol_num[13] = 4
                temp_poss_sol_index[13] = i
            # if sol4[i] is the new 15th-best score
            elif (poss_sol4_scores[i] < temp_scores[14]):
                # set the new 14th-best solution
                temp_scores[14] = poss_sol4_scores.copy()[i]
                temp_sol_num[14] = 4
                temp_poss_sol_index[14] = i

            #
            # SOLUTION 5
            # if sol5[i] is the new best score
            if (poss_sol5_scores[i] < temp_scores[0]):
                for j in range (14,0,-1):
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
                for j in range (14,1,-1):
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
                for j in range (14,2,-1):
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
                for j in range (14,3,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 4-th best solution
                temp_scores[3] = poss_sol5_scores.copy()[i]
                temp_sol_num[3] = 5
                temp_poss_sol_index[3] = i
            # if sol5[i] is the new 5th-best score
            elif (poss_sol5_scores[i] < temp_scores[4]):
                for j in range (14,4,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 5th-best solution
                temp_scores[4] = poss_sol5_scores.copy()[i]
                temp_sol_num[4] = 5
                temp_poss_sol_index[4] = i
            # if sol5[i] is the new 6th-best score
            elif (poss_sol5_scores[i] < temp_scores[5]):
                for j in range (14,5,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 6th-best solution
                temp_scores[5] = poss_sol5_scores.copy()[i]
                temp_sol_num[5] = 5
                temp_poss_sol_index[5] = i
            # if sol5[i] is the new 7th-best score
            elif (poss_sol5_scores[i] < temp_scores[6]):
                for j in range (14,6,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 7th-best solution
                temp_scores[6] = poss_sol5_scores.copy()[i]
                temp_sol_num[6] = 5
                temp_poss_sol_index[6] = i
            # if sol5[i] is the new 8th-best score
            elif (poss_sol5_scores[i] < temp_scores[7]):
                for j in range (14,7,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 8th-best solution
                temp_scores[7] = poss_sol5_scores.copy()[i]
                temp_sol_num[7] = 5
                temp_poss_sol_index[7] = i
            # if sol5[i] is the new 9th-best score
            elif (poss_sol5_scores[i] < temp_scores[8]):
                for j in range (14,8,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 9th-best solution
                temp_scores[8] = poss_sol5_scores.copy()[i]
                temp_sol_num[8] = 5
                temp_poss_sol_index[8] = i
            # if sol5[i] is the new 10th-best score
            elif (poss_sol5_scores[i] < temp_scores[9]):
                for j in range (14,9,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 10th-best solution
                temp_scores[9] = poss_sol5_scores.copy()[i]
                temp_sol_num[9] = 5
                temp_poss_sol_index[9] = i
            # if sol5[i] is the new 11th-best score
            elif (poss_sol5_scores[i] < temp_scores[10]):
                for j in range (14,10,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 11th-best solution
                temp_scores[10] = poss_sol5_scores.copy()[i]
                temp_sol_num[10] = 5
                temp_poss_sol_index[10] = i
            # if sol5[i] is the new 12th-best score
            elif (poss_sol5_scores[i] < temp_scores[11]):
                for j in range (14,11,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 12th-best solution
                temp_scores[11] = poss_sol5_scores.copy()[i]
                temp_sol_num[11] = 5
                temp_poss_sol_index[11] = i
            # if sol5[i] is the new 13th-best score
            elif (poss_sol5_scores[i] < temp_scores[12]):
                for j in range (14,2,-1):
                    # shift the other values
                    temp_scores[j] = temp_scores.copy()[j-1]
                    temp_sol_num[j] = temp_sol_num.copy()[j-1]
                    temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                # set the new 13th-best solution
                temp_scores[12] = poss_sol5_scores.copy()[i]
                temp_sol_num[12] = 5
                temp_poss_sol_index[12] = i
            # if sol5[i] is the new 14th-best score
            elif (poss_sol5_scores[i] < temp_scores[13]):
                temp_scores[14] = temp_scores.copy()[13]
                temp_sol_num[14] = temp_sol_num.copy()[13]
                temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                # set the new 14th-best solution
                temp_scores[13] = poss_sol5_scores.copy()[i]
                temp_sol_num[13] = 5
                temp_poss_sol_index[13] = i
            # if sol5[i] is the new 15th-best score
            elif (poss_sol5_scores[i] < temp_scores[14]):
                # set the new 14th-best solution
                temp_scores[14] = poss_sol5_scores.copy()[i]
                temp_sol_num[14] = 5
                temp_poss_sol_index[14] = i

            if (p>1):

                #
                # SOLUTION 6
                # if sol6[i] is the new best score
                if (poss_sol6_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol6_scores.copy()[i]
                    temp_sol_num[0] = 6
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol6_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol6_scores.copy()[i]
                    temp_sol_num[1] = 6
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol6_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol6_scores.copy()[i]
                    temp_sol_num[2] = 6
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol6_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol6_scores.copy()[i]
                    temp_sol_num[3] = 6
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol6_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol6_scores.copy()[i]
                    temp_sol_num[4] = 6
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol6_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol6_scores.copy()[i]
                    temp_sol_num[5] = 6
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol6_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol6_scores.copy()[i]
                    temp_sol_num[6] = 6
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol6_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol6_scores.copy()[i]
                    temp_sol_num[7] = 6
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol6_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol6_scores.copy()[i]
                    temp_sol_num[8] = 6
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol6_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol6_scores.copy()[i]
                    temp_sol_num[9] = 6
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol6_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol6_scores.copy()[i]
                    temp_sol_num[10] = 6
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol6_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol6_scores.copy()[i]
                    temp_sol_num[11] = 6
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol6_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol6_scores.copy()[i]
                    temp_sol_num[12] = 6
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol6_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol6_scores.copy()[i]
                    temp_sol_num[13] = 6
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol6_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol6_scores.copy()[i]
                    temp_sol_num[14] = 6
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 7
                # if sol6[i] is the new best score
                if (poss_sol7_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol7_scores.copy()[i]
                    temp_sol_num[0] = 7
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol7_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol7_scores.copy()[i]
                    temp_sol_num[1] = 7
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol7_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol7_scores.copy()[i]
                    temp_sol_num[2] = 7
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol7_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol7_scores.copy()[i]
                    temp_sol_num[3] = 7
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol7_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol7_scores.copy()[i]
                    temp_sol_num[4] = 7
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol7_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol7_scores.copy()[i]
                    temp_sol_num[5] = 7
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol7_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol7_scores.copy()[i]
                    temp_sol_num[6] = 7
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol7_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol7_scores.copy()[i]
                    temp_sol_num[7] = 7
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol7_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol7_scores.copy()[i]
                    temp_sol_num[8] = 7
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol7_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol7_scores.copy()[i]
                    temp_sol_num[9] = 7
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol7_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol7_scores.copy()[i]
                    temp_sol_num[10] = 7
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol7_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol7_scores.copy()[i]
                    temp_sol_num[11] = 7
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol7_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol7_scores.copy()[i]
                    temp_sol_num[12] = 7
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol7_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol7_scores.copy()[i]
                    temp_sol_num[13] = 7
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol7_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol7_scores.copy()[i]
                    temp_sol_num[14] = 7
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 8
                # if sol6[i] is the new best score
                if (poss_sol8_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol8_scores.copy()[i]
                    temp_sol_num[0] = 8
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol8_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol8_scores.copy()[i]
                    temp_sol_num[1] = 8
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol8_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol8_scores.copy()[i]
                    temp_sol_num[2] = 8
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol8_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol8_scores.copy()[i]
                    temp_sol_num[3] = 8
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol8_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol8_scores.copy()[i]
                    temp_sol_num[4] = 8
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol8_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol8_scores.copy()[i]
                    temp_sol_num[5] = 8
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol8_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol8_scores.copy()[i]
                    temp_sol_num[6] = 8
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol8_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol8_scores.copy()[i]
                    temp_sol_num[7] = 8
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol8_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol8_scores.copy()[i]
                    temp_sol_num[8] = 8
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol8_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol8_scores.copy()[i]
                    temp_sol_num[9] = 8
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol8_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol8_scores.copy()[i]
                    temp_sol_num[10] = 8
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol8_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol8_scores.copy()[i]
                    temp_sol_num[11] = 8
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol8_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol8_scores.copy()[i]
                    temp_sol_num[12] = 8
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol8_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol8_scores.copy()[i]
                    temp_sol_num[13] = 8
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol8_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol8_scores.copy()[i]
                    temp_sol_num[14] = 8
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 9
                # if sol6[i] is the new best score
                if (poss_sol9_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol9_scores.copy()[i]
                    temp_sol_num[0] = 9
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol9_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol9_scores.copy()[i]
                    temp_sol_num[1] = 9
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol9_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol9_scores.copy()[i]
                    temp_sol_num[2] = 9
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol9_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol9_scores.copy()[i]
                    temp_sol_num[3] = 9
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol9_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol9_scores.copy()[i]
                    temp_sol_num[4] = 9
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol9_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol9_scores.copy()[i]
                    temp_sol_num[5] = 9
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol9_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol9_scores.copy()[i]
                    temp_sol_num[6] = 9
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol9_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol9_scores.copy()[i]
                    temp_sol_num[7] = 9
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol9_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol9_scores.copy()[i]
                    temp_sol_num[8] = 9
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol9_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol9_scores.copy()[i]
                    temp_sol_num[9] = 9
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol9_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol9_scores.copy()[i]
                    temp_sol_num[10] = 9
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol9_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol9_scores.copy()[i]
                    temp_sol_num[11] = 9
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol9_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol9_scores.copy()[i]
                    temp_sol_num[12] = 9
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol9_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol9_scores.copy()[i]
                    temp_sol_num[13] = 9
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol9_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol9_scores.copy()[i]
                    temp_sol_num[14] = 9
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 10
                # if sol6[i] is the new best score
                if (poss_sol10_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol10_scores.copy()[i]
                    temp_sol_num[0] = 10
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol10_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol10_scores.copy()[i]
                    temp_sol_num[1] = 10
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol10_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol10_scores.copy()[i]
                    temp_sol_num[2] = 10
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol10_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol10_scores.copy()[i]
                    temp_sol_num[3] = 10
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol10_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol10_scores.copy()[i]
                    temp_sol_num[4] = 10
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol10_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol10_scores.copy()[i]
                    temp_sol_num[5] = 10
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol10_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol10_scores.copy()[i]
                    temp_sol_num[6] = 10
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol10_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol10_scores.copy()[i]
                    temp_sol_num[7] = 10
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol10_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol10_scores.copy()[i]
                    temp_sol_num[8] = 10
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol10_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol10_scores.copy()[i]
                    temp_sol_num[9] = 10
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol10_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol10_scores.copy()[i]
                    temp_sol_num[10] = 10
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol10_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol10_scores.copy()[i]
                    temp_sol_num[11] = 10
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol10_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol10_scores.copy()[i]
                    temp_sol_num[12] = 10
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol10_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol10_scores.copy()[i]
                    temp_sol_num[13] = 10
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol10_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol10_scores.copy()[i]
                    temp_sol_num[14] = 10
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 11
                # if sol6[i] is the new best score
                if (poss_sol11_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol11_scores.copy()[i]
                    temp_sol_num[0] = 11
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol11_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol11_scores.copy()[i]
                    temp_sol_num[1] = 11
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol11_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol11_scores.copy()[i]
                    temp_sol_num[2] = 11
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol11_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol11_scores.copy()[i]
                    temp_sol_num[3] = 11
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol11_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol11_scores.copy()[i]
                    temp_sol_num[4] = 11
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol11_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol11_scores.copy()[i]
                    temp_sol_num[5] = 11
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol11_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol11_scores.copy()[i]
                    temp_sol_num[6] = 11
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol11_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol11_scores.copy()[i]
                    temp_sol_num[7] = 11
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol11_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol11_scores.copy()[i]
                    temp_sol_num[8] = 11
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol11_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol11_scores.copy()[i]
                    temp_sol_num[9] = 11
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol11_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol11_scores.copy()[i]
                    temp_sol_num[10] = 11
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol11_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol11_scores.copy()[i]
                    temp_sol_num[11] = 11
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol11_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol11_scores.copy()[i]
                    temp_sol_num[12] = 11
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol11_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol11_scores.copy()[i]
                    temp_sol_num[13] = 11
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol11_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol11_scores.copy()[i]
                    temp_sol_num[14] = 11
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 12
                # if sol6[i] is the new best score
                if (poss_sol12_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol12_scores.copy()[i]
                    temp_sol_num[0] = 12
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol12_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol12_scores.copy()[i]
                    temp_sol_num[1] = 12
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol12_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol12_scores.copy()[i]
                    temp_sol_num[2] = 12
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol12_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol12_scores.copy()[i]
                    temp_sol_num[3] = 12
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol12_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol12_scores.copy()[i]
                    temp_sol_num[4] = 12
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol12_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol12_scores.copy()[i]
                    temp_sol_num[5] = 12
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol12_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol12_scores.copy()[i]
                    temp_sol_num[6] = 12
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol12_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol12_scores.copy()[i]
                    temp_sol_num[7] = 12
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol12_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol12_scores.copy()[i]
                    temp_sol_num[8] = 12
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol12_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol12_scores.copy()[i]
                    temp_sol_num[9] = 12
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol12_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol12_scores.copy()[i]
                    temp_sol_num[10] = 12
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol12_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol12_scores.copy()[i]
                    temp_sol_num[11] = 12
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol12_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol12_scores.copy()[i]
                    temp_sol_num[12] = 12
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol12_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol12_scores.copy()[i]
                    temp_sol_num[13] = 12
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol12_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol12_scores.copy()[i]
                    temp_sol_num[14] = 12
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 13
                # if sol6[i] is the new best score
                if (poss_sol13_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol13_scores.copy()[i]
                    temp_sol_num[0] = 13
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol13_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol13_scores.copy()[i]
                    temp_sol_num[1] = 13
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol13_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol13_scores.copy()[i]
                    temp_sol_num[2] = 13
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol13_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol13_scores.copy()[i]
                    temp_sol_num[3] = 13
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol13_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol13_scores.copy()[i]
                    temp_sol_num[4] = 13
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol13_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol13_scores.copy()[i]
                    temp_sol_num[5] = 13
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol13_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol13_scores.copy()[i]
                    temp_sol_num[6] = 13
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol13_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol13_scores.copy()[i]
                    temp_sol_num[7] = 13
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol13_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol13_scores.copy()[i]
                    temp_sol_num[8] = 13
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol13_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol13_scores.copy()[i]
                    temp_sol_num[9] = 13
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol13_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol13_scores.copy()[i]
                    temp_sol_num[10] = 13
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol13_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol13_scores.copy()[i]
                    temp_sol_num[11] = 13
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol13_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol13_scores.copy()[i]
                    temp_sol_num[12] = 13
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol13_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol13_scores.copy()[i]
                    temp_sol_num[13] = 13
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol13_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol13_scores.copy()[i]
                    temp_sol_num[14] = 13
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 14
                # if sol6[i] is the new best score
                if (poss_sol14_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol14_scores.copy()[i]
                    temp_sol_num[0] = 14
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol14_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol14_scores.copy()[i]
                    temp_sol_num[1] = 14
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol14_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol14_scores.copy()[i]
                    temp_sol_num[2] = 14
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol14_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol14_scores.copy()[i]
                    temp_sol_num[3] = 14
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol14_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol14_scores.copy()[i]
                    temp_sol_num[4] = 14
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol14_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol14_scores.copy()[i]
                    temp_sol_num[5] = 14
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol14_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol14_scores.copy()[i]
                    temp_sol_num[6] = 14
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol14_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol14_scores.copy()[i]
                    temp_sol_num[7] = 14
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol14_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol14_scores.copy()[i]
                    temp_sol_num[8] = 14
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol14_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol14_scores.copy()[i]
                    temp_sol_num[9] = 14
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol14_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol14_scores.copy()[i]
                    temp_sol_num[10] = 14
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol14_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol14_scores.copy()[i]
                    temp_sol_num[11] = 14
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol14_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol14_scores.copy()[i]
                    temp_sol_num[12] = 14
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol14_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol14_scores.copy()[i]
                    temp_sol_num[13] = 14
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol14_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol14_scores.copy()[i]
                    temp_sol_num[14] = 14
                    temp_poss_sol_index[14] = i

                #
                # SOLUTION 15
                # if sol6[i] is the new best score
                if (poss_sol15_scores[i] < temp_scores[0]):
                    for j in range (14,0,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new best solution
                    temp_scores[0] = poss_sol15_scores.copy()[i]
                    temp_sol_num[0] = 15
                    temp_poss_sol_index[0] = i
                # if sol5[i] is the new 2nd-best score
                elif (poss_sol15_scores[i] < temp_scores[1]):
                    for j in range (14,1,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 2nd-best solution
                    temp_scores[1] = poss_sol15_scores.copy()[i]
                    temp_sol_num[1] = 15
                    temp_poss_sol_index[1] = i
                # if sol5[i] is the new 3rd-best score
                elif (poss_sol15_scores[i] < temp_scores[2]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 3rd-best solution
                    temp_scores[2] = poss_sol15_scores.copy()[i]
                    temp_sol_num[2] = 15
                    temp_poss_sol_index[2] = i
                # if sol5[i] is the new 4th-best score
                elif (poss_sol15_scores[i] < temp_scores[3]):
                    for j in range (14,3,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 4-th best solution
                    temp_scores[3] = poss_sol15_scores.copy()[i]
                    temp_sol_num[3] = 15
                    temp_poss_sol_index[3] = i
                # if sol5[i] is the new 5th-best score
                elif (poss_sol15_scores[i] < temp_scores[4]):
                    for j in range (14,4,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 5th-best solution
                    temp_scores[4] = poss_sol15_scores.copy()[i]
                    temp_sol_num[4] = 15
                    temp_poss_sol_index[4] = i
                # if sol5[i] is the new 6th-best score
                elif (poss_sol15_scores[i] < temp_scores[5]):
                    for j in range (14,5,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 6th-best solution
                    temp_scores[5] = poss_sol15_scores.copy()[i]
                    temp_sol_num[5] = 15
                    temp_poss_sol_index[5] = i
                # if sol5[i] is the new 7th-best score
                elif (poss_sol15_scores[i] < temp_scores[6]):
                    for j in range (14,6,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 7th-best solution
                    temp_scores[6] = poss_sol15_scores.copy()[i]
                    temp_sol_num[6] = 15
                    temp_poss_sol_index[6] = i
                # if sol5[i] is the new 8th-best score
                elif (poss_sol15_scores[i] < temp_scores[7]):
                    for j in range (14,7,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 8th-best solution
                    temp_scores[7] = poss_sol15_scores.copy()[i]
                    temp_sol_num[7] = 15
                    temp_poss_sol_index[7] = i
                # if sol5[i] is the new 9th-best score
                elif (poss_sol15_scores[i] < temp_scores[8]):
                    for j in range (14,8,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 9th-best solution
                    temp_scores[8] = poss_sol15_scores.copy()[i]
                    temp_sol_num[8] = 15
                    temp_poss_sol_index[8] = i
                # if sol5[i] is the new 10th-best score
                elif (poss_sol15_scores[i] < temp_scores[9]):
                    for j in range (14,9,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 10th-best solution
                    temp_scores[9] = poss_sol15_scores.copy()[i]
                    temp_sol_num[9] = 15
                    temp_poss_sol_index[9] = i
                # if sol5[i] is the new 11th-best score
                elif (poss_sol15_scores[i] < temp_scores[10]):
                    for j in range (14,10,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 11th-best solution
                    temp_scores[10] = poss_sol15_scores.copy()[i]
                    temp_sol_num[10] = 15
                    temp_poss_sol_index[10] = i
                # if sol5[i] is the new 12th-best score
                elif (poss_sol15_scores[i] < temp_scores[11]):
                    for j in range (14,11,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 12th-best solution
                    temp_scores[11] = poss_sol15_scores.copy()[i]
                    temp_sol_num[11] = 15
                    temp_poss_sol_index[11] = i
                # if sol5[i] is the new 13th-best score
                elif (poss_sol15_scores[i] < temp_scores[12]):
                    for j in range (14,2,-1):
                        # shift the other values
                        temp_scores[j] = temp_scores.copy()[j-1]
                        temp_sol_num[j] = temp_sol_num.copy()[j-1]
                        temp_poss_sol_index[j] = temp_poss_sol_index.copy()[j-1]
                    # set the new 13th-best solution
                    temp_scores[12] = poss_sol15_scores.copy()[i]
                    temp_sol_num[12] = 15
                    temp_poss_sol_index[12] = i
                # if sol5[i] is the new 14th-best score
                elif (poss_sol15_scores[i] < temp_scores[13]):
                    temp_scores[14] = temp_scores.copy()[13]
                    temp_sol_num[14] = temp_sol_num.copy()[13]
                    temp_poss_sol_index[14] = temp_poss_sol_index.copy()[13]
                    # set the new 14th-best solution
                    temp_scores[13] = poss_sol15_scores.copy()[i]
                    temp_sol_num[13] = 15
                    temp_poss_sol_index[13] = i
                # if sol5[i] is the new 15th-best score
                elif (poss_sol15_scores[i] < temp_scores[14]):
                    # set the new 14th-best solution
                    temp_scores[14] = poss_sol15_scores.copy()[i]
                    temp_sol_num[14] = 15
                    temp_poss_sol_index[14] = i


                '''
                CONTINUE FROM HERE
                EXPAND EACH SOLUTION TO 15 AND THEN ADD 5 MORE AT THE END
                '''

        #
        #
        #
        #
        # COPY BEST 10 SOLUTIONS INTO TEMPORARY SOL ARRAYS (EXPAND)
        
        # set temporary sol1 to the best solution
        if temp_sol_num[0] == 1: sol1_temp = sol1.copy()
        elif temp_sol_num[0] == 2: sol1_temp = sol2.copy()
        elif temp_sol_num[0] == 3: sol1_temp = sol3.copy()
        elif temp_sol_num[0] == 4: sol1_temp = sol4.copy()
        elif temp_sol_num[0] == 5: sol1_temp = sol5.copy()
        elif temp_sol_num[0] == 6: sol1_temp = sol6.copy()
        elif temp_sol_num[0] == 7: sol1_temp = sol7.copy()
        elif temp_sol_num[0] == 8: sol1_temp = sol8.copy()
        elif temp_sol_num[0] == 9: sol1_temp = sol9.copy()
        elif temp_sol_num[0] == 10: sol1_temp = sol10.copy()
        elif temp_sol_num[0] == 11: sol1_temp = sol11.copy()
        elif temp_sol_num[0] == 12: sol1_temp = sol12.copy()
        elif temp_sol_num[0] == 13: sol1_temp = sol13.copy()
        elif temp_sol_num[0] == 14: sol1_temp = sol14.copy()
        elif temp_sol_num[0] == 15: sol1_temp = sol15.copy()

        # set temporary sol2 to the 2nd-best solution
        if temp_sol_num[1] == 1: sol2_temp = sol1.copy()
        elif temp_sol_num[1] == 2: sol2_temp = sol2.copy()
        elif temp_sol_num[1] == 3: sol2_temp = sol3.copy()
        elif temp_sol_num[1] == 4: sol2_temp = sol4.copy()
        elif temp_sol_num[1] == 5: sol2_temp = sol5.copy()
        elif temp_sol_num[1] == 6: sol2_temp = sol6.copy()
        elif temp_sol_num[1] == 7: sol2_temp = sol7.copy()
        elif temp_sol_num[1] == 8: sol2_temp = sol8.copy()
        elif temp_sol_num[1] == 9: sol2_temp = sol9.copy()
        elif temp_sol_num[1] == 10: sol2_temp = sol10.copy()
        elif temp_sol_num[1] == 11: sol2_temp = sol11.copy()
        elif temp_sol_num[1] == 12: sol2_temp = sol12.copy()
        elif temp_sol_num[1] == 13: sol2_temp = sol13.copy()
        elif temp_sol_num[1] == 14: sol2_temp = sol14.copy()
        elif temp_sol_num[1] == 15: sol2_temp = sol15.copy()

        # set temporary sol3 to the 3rd-best solution
        if temp_sol_num[2] == 1: sol3_temp = sol1.copy()
        elif temp_sol_num[2] == 2: sol3_temp = sol2.copy()
        elif temp_sol_num[2] == 3: sol3_temp = sol3.copy()
        elif temp_sol_num[2] == 4: sol3_temp = sol4.copy()
        elif temp_sol_num[2] == 5: sol3_temp = sol5.copy()
        elif temp_sol_num[2] == 6: sol3_temp = sol6.copy()
        elif temp_sol_num[2] == 7: sol3_temp = sol7.copy()
        elif temp_sol_num[2] == 8: sol3_temp = sol8.copy()
        elif temp_sol_num[2] == 9: sol3_temp = sol9.copy()
        elif temp_sol_num[2] == 10: sol3_temp = sol10.copy()
        elif temp_sol_num[2] == 11: sol3_temp = sol11.copy()
        elif temp_sol_num[2] == 12: sol3_temp = sol12.copy()
        elif temp_sol_num[2] == 13: sol3_temp = sol13.copy()
        elif temp_sol_num[2] == 14: sol3_temp = sol14.copy()
        elif temp_sol_num[2] == 15: sol3_temp = sol15.copy()

        # set temporary sol4 to the 4th-best solution
        if temp_sol_num[3] == 1: sol4_temp = sol1.copy()
        elif temp_sol_num[3] == 2: sol4_temp = sol2.copy()
        elif temp_sol_num[3] == 3: sol4_temp = sol3.copy()
        elif temp_sol_num[3] == 4: sol4_temp = sol4.copy()
        elif temp_sol_num[3] == 5: sol4_temp = sol5.copy()
        elif temp_sol_num[3] == 6: sol4_temp = sol6.copy()
        elif temp_sol_num[3] == 7: sol4_temp = sol7.copy()
        elif temp_sol_num[3] == 8: sol4_temp = sol8.copy()
        elif temp_sol_num[3] == 9: sol4_temp = sol9.copy()
        elif temp_sol_num[3] == 10: sol4_temp = sol10.copy()
        elif temp_sol_num[3] == 11: sol4_temp = sol11.copy()
        elif temp_sol_num[3] == 12: sol4_temp = sol12.copy()
        elif temp_sol_num[3] == 13: sol4_temp = sol13.copy()
        elif temp_sol_num[3] == 14: sol4_temp = sol14.copy()
        elif temp_sol_num[3] == 15: sol4_temp = sol15.copy()

        # set temporary sol5 to the 5th-best solution
        if temp_sol_num[4] == 1: sol5_temp = sol1.copy()
        elif temp_sol_num[4] == 2: sol5_temp = sol2.copy()
        elif temp_sol_num[4] == 3: sol5_temp = sol3.copy()
        elif temp_sol_num[4] == 4: sol5_temp = sol4.copy()
        elif temp_sol_num[4] == 5: sol5_temp = sol5.copy()
        elif temp_sol_num[4] == 6: sol5_temp = sol6.copy()
        elif temp_sol_num[4] == 7: sol5_temp = sol7.copy()
        elif temp_sol_num[4] == 8: sol5_temp = sol8.copy()
        elif temp_sol_num[4] == 9: sol5_temp = sol9.copy()
        elif temp_sol_num[4] == 10: sol5_temp = sol10.copy()
        elif temp_sol_num[4] == 11: sol5_temp = sol11.copy()
        elif temp_sol_num[4] == 12: sol5_temp = sol12.copy()
        elif temp_sol_num[4] == 13: sol5_temp = sol13.copy()
        elif temp_sol_num[4] == 14: sol5_temp = sol14.copy()
        elif temp_sol_num[4] == 15: sol5_temp = sol15.copy()

        # set temporary sol6 to the 6th-best solution
        if temp_sol_num[5] == 1: sol6_temp = sol1.copy()
        elif temp_sol_num[5] == 2: sol6_temp = sol2.copy()
        elif temp_sol_num[5] == 3: sol6_temp = sol3.copy()
        elif temp_sol_num[5] == 4: sol6_temp = sol4.copy()
        elif temp_sol_num[5] == 5: sol6_temp = sol5.copy()
        elif temp_sol_num[5] == 6: sol6_temp = sol6.copy()
        elif temp_sol_num[5] == 7: sol6_temp = sol7.copy()
        elif temp_sol_num[5] == 8: sol6_temp = sol8.copy()
        elif temp_sol_num[5] == 9: sol6_temp = sol9.copy()
        elif temp_sol_num[5] == 10: sol6_temp = sol10.copy()
        elif temp_sol_num[5] == 11: sol6_temp = sol11.copy()
        elif temp_sol_num[5] == 12: sol6_temp = sol12.copy()
        elif temp_sol_num[5] == 13: sol6_temp = sol13.copy()
        elif temp_sol_num[5] == 14: sol6_temp = sol14.copy()
        elif temp_sol_num[5] == 15: sol6_temp = sol15.copy()

        # set temporary sol7 to the 7th-best solution
        if temp_sol_num[6] == 1: sol7_temp = sol1.copy()
        elif temp_sol_num[6] == 2: sol7_temp = sol2.copy()
        elif temp_sol_num[6] == 3: sol7_temp = sol3.copy()
        elif temp_sol_num[6] == 4: sol7_temp = sol4.copy()
        elif temp_sol_num[6] == 5: sol7_temp = sol5.copy()
        elif temp_sol_num[6] == 6: sol7_temp = sol6.copy()
        elif temp_sol_num[6] == 7: sol7_temp = sol7.copy()
        elif temp_sol_num[6] == 8: sol7_temp = sol8.copy()
        elif temp_sol_num[6] == 9: sol7_temp = sol9.copy()
        elif temp_sol_num[6] == 10: sol7_temp = sol10.copy()
        elif temp_sol_num[6] == 11: sol7_temp = sol11.copy()
        elif temp_sol_num[6] == 12: sol7_temp = sol12.copy()
        elif temp_sol_num[6] == 13: sol7_temp = sol13.copy()
        elif temp_sol_num[6] == 14: sol7_temp = sol14.copy()
        elif temp_sol_num[6] == 15: sol7_temp = sol15.copy()

        # set temporary sol8 to the 8th-best solution
        if temp_sol_num[7] == 1: sol8_temp = sol1.copy()
        elif temp_sol_num[7] == 2: sol8_temp = sol2.copy()
        elif temp_sol_num[7] == 3: sol8_temp = sol3.copy()
        elif temp_sol_num[7] == 4: sol8_temp = sol4.copy()
        elif temp_sol_num[7] == 5: sol8_temp = sol5.copy()
        elif temp_sol_num[7] == 6: sol8_temp = sol6.copy()
        elif temp_sol_num[7] == 7: sol8_temp = sol7.copy()
        elif temp_sol_num[7] == 8: sol8_temp = sol8.copy()
        elif temp_sol_num[7] == 9: sol8_temp = sol9.copy()
        elif temp_sol_num[7] == 10: sol8_temp = sol10.copy()
        elif temp_sol_num[7] == 11: sol8_temp = sol11.copy()
        elif temp_sol_num[7] == 12: sol8_temp = sol12.copy()
        elif temp_sol_num[7] == 13: sol8_temp = sol13.copy()
        elif temp_sol_num[7] == 14: sol8_temp = sol14.copy()
        elif temp_sol_num[7] == 15: sol8_temp = sol15.copy()

        # set temporary sol9 to the 9th-best solution
        if temp_sol_num[8] == 1: sol9_temp = sol1.copy()
        elif temp_sol_num[8] == 2: sol9_temp = sol2.copy()
        elif temp_sol_num[8] == 3: sol9_temp = sol3.copy()
        elif temp_sol_num[8] == 4: sol9_temp = sol4.copy()
        elif temp_sol_num[8] == 5: sol9_temp = sol5.copy()
        elif temp_sol_num[8] == 6: sol9_temp = sol6.copy()
        elif temp_sol_num[8] == 7: sol9_temp = sol7.copy()
        elif temp_sol_num[8] == 8: sol9_temp = sol8.copy()
        elif temp_sol_num[8] == 9: sol9_temp = sol9.copy()
        elif temp_sol_num[8] == 10: sol9_temp = sol10.copy()
        elif temp_sol_num[8] == 11: sol9_temp = sol11.copy()
        elif temp_sol_num[8] == 12: sol9_temp = sol12.copy()
        elif temp_sol_num[8] == 13: sol9_temp = sol13.copy()
        elif temp_sol_num[8] == 14: sol9_temp = sol14.copy()
        elif temp_sol_num[8] == 15: sol9_temp = sol15.copy()

        # set temporary sol10 to the 10th-best solution
        if temp_sol_num[9] == 1: sol10_temp = sol1.copy()
        elif temp_sol_num[9] == 2: sol10_temp = sol2.copy()
        elif temp_sol_num[9] == 3: sol10_temp = sol3.copy()
        elif temp_sol_num[9] == 4: sol10_temp = sol4.copy()
        elif temp_sol_num[9] == 5: sol10_temp = sol5.copy()
        elif temp_sol_num[9] == 6: sol10_temp = sol6.copy()
        elif temp_sol_num[9] == 7: sol10_temp = sol7.copy()
        elif temp_sol_num[9] == 8: sol10_temp = sol8.copy()
        elif temp_sol_num[9] == 9: sol10_temp = sol9.copy()
        elif temp_sol_num[9] == 10: sol10_temp = sol10.copy()
        elif temp_sol_num[9] == 11: sol10_temp = sol11.copy()
        elif temp_sol_num[9] == 12: sol10_temp = sol12.copy()
        elif temp_sol_num[9] == 13: sol10_temp = sol13.copy()
        elif temp_sol_num[9] == 14: sol10_temp = sol14.copy()
        elif temp_sol_num[9] == 15: sol10_temp = sol15.copy()

        # set temporary sol11 to the 11th-best solution
        if temp_sol_num[10] == 1: sol11_temp = sol1.copy()
        elif temp_sol_num[10] == 2: sol11_temp = sol2.copy()
        elif temp_sol_num[10] == 3: sol11_temp = sol3.copy()
        elif temp_sol_num[10] == 4: sol11_temp = sol4.copy()
        elif temp_sol_num[10] == 5: sol11_temp = sol5.copy()
        elif temp_sol_num[10] == 6: sol11_temp = sol6.copy()
        elif temp_sol_num[10] == 7: sol11_temp = sol7.copy()
        elif temp_sol_num[10] == 8: sol11_temp = sol8.copy()
        elif temp_sol_num[10] == 9: sol11_temp = sol9.copy()
        elif temp_sol_num[10] == 10: sol11_temp = sol10.copy()
        elif temp_sol_num[10] == 11: sol11_temp = sol11.copy()
        elif temp_sol_num[10] == 12: sol11_temp = sol12.copy()
        elif temp_sol_num[10] == 13: sol11_temp = sol13.copy()
        elif temp_sol_num[10] == 14: sol11_temp = sol14.copy()
        elif temp_sol_num[10] == 15: sol11_temp = sol15.copy()

        # set temporary sol12 to the 12th-best solution
        if temp_sol_num[11] == 1: sol12_temp = sol1.copy()
        elif temp_sol_num[11] == 2: sol12_temp = sol2.copy()
        elif temp_sol_num[11] == 3: sol12_temp = sol3.copy()
        elif temp_sol_num[11] == 4: sol12_temp = sol4.copy()
        elif temp_sol_num[11] == 5: sol12_temp = sol5.copy()
        elif temp_sol_num[11] == 6: sol12_temp = sol6.copy()
        elif temp_sol_num[11] == 7: sol12_temp = sol7.copy()
        elif temp_sol_num[11] == 8: sol12_temp = sol8.copy()
        elif temp_sol_num[11] == 9: sol12_temp = sol9.copy()
        elif temp_sol_num[11] == 10: sol12_temp = sol10.copy()
        elif temp_sol_num[11] == 11: sol12_temp = sol11.copy()
        elif temp_sol_num[11] == 12: sol12_temp = sol12.copy()
        elif temp_sol_num[11] == 13: sol12_temp = sol13.copy()
        elif temp_sol_num[11] == 14: sol12_temp = sol14.copy()
        elif temp_sol_num[11] == 15: sol12_temp = sol15.copy()

        # set temporary sol13 to the 13th-best solution
        if temp_sol_num[12] == 1: sol13_temp = sol1.copy()
        elif temp_sol_num[12] == 2: sol13_temp = sol2.copy()
        elif temp_sol_num[12] == 3: sol13_temp = sol3.copy()
        elif temp_sol_num[12] == 4: sol13_temp = sol4.copy()
        elif temp_sol_num[12] == 5: sol13_temp = sol5.copy()
        elif temp_sol_num[12] == 6: sol13_temp = sol6.copy()
        elif temp_sol_num[12] == 7: sol13_temp = sol7.copy()
        elif temp_sol_num[12] == 8: sol13_temp = sol8.copy()
        elif temp_sol_num[12] == 9: sol13_temp = sol9.copy()
        elif temp_sol_num[12] == 10: sol13_temp = sol10.copy()
        elif temp_sol_num[12] == 11: sol13_temp = sol11.copy()
        elif temp_sol_num[12] == 12: sol13_temp = sol12.copy()
        elif temp_sol_num[12] == 13: sol13_temp = sol13.copy()
        elif temp_sol_num[12] == 14: sol13_temp = sol14.copy()
        elif temp_sol_num[12] == 15: sol13_temp = sol15.copy()

        # set temporary sol14 to the 14th-best solution
        if temp_sol_num[13] == 1: sol14_temp = sol1.copy()
        elif temp_sol_num[13] == 2: sol14_temp = sol2.copy()
        elif temp_sol_num[13] == 3: sol14_temp = sol3.copy()
        elif temp_sol_num[13] == 4: sol14_temp = sol4.copy()
        elif temp_sol_num[13] == 5: sol14_temp = sol5.copy()
        elif temp_sol_num[13] == 6: sol14_temp = sol6.copy()
        elif temp_sol_num[13] == 7: sol14_temp = sol7.copy()
        elif temp_sol_num[13] == 8: sol14_temp = sol8.copy()
        elif temp_sol_num[13] == 9: sol14_temp = sol9.copy()
        elif temp_sol_num[13] == 10: sol14_temp = sol10.copy()
        elif temp_sol_num[13] == 11: sol14_temp = sol11.copy()
        elif temp_sol_num[13] == 12: sol14_temp = sol12.copy()
        elif temp_sol_num[13] == 13: sol14_temp = sol13.copy()
        elif temp_sol_num[13] == 14: sol14_temp = sol14.copy()
        elif temp_sol_num[13] == 15: sol14_temp = sol15.copy()

        # set temporary sol15 to the 15th-best solution
        if temp_sol_num[14] == 1: sol15_temp = sol1.copy()
        elif temp_sol_num[14] == 2: sol15_temp = sol2.copy()
        elif temp_sol_num[14] == 3: sol15_temp = sol3.copy()
        elif temp_sol_num[14] == 4: sol15_temp = sol4.copy()
        elif temp_sol_num[14] == 5: sol15_temp = sol5.copy()
        elif temp_sol_num[14] == 6: sol15_temp = sol6.copy()
        elif temp_sol_num[14] == 7: sol15_temp = sol7.copy()
        elif temp_sol_num[14] == 8: sol15_temp = sol8.copy()
        elif temp_sol_num[14] == 9: sol15_temp = sol9.copy()
        elif temp_sol_num[14] == 10: sol15_temp = sol10.copy()
        elif temp_sol_num[14] == 11: sol15_temp = sol11.copy()
        elif temp_sol_num[14] == 12: sol15_temp = sol12.copy()
        elif temp_sol_num[14] == 13: sol15_temp = sol13.copy()
        elif temp_sol_num[14] == 14: sol15_temp = sol14.copy()
        elif temp_sol_num[14] == 15: sol15_temp = sol15.copy()

        # append new finger placements
        sol1_temp.append(temp_poss_sol_index[0]+1) # append new finger placement for sol1
        sol2_temp.append(temp_poss_sol_index[1]+1) # append new finger placement for sol2
        sol3_temp.append(temp_poss_sol_index[2]+1) # append new finger placement for sol3
        sol4_temp.append(temp_poss_sol_index[3]+1) # append new finger placement for sol4
        sol5_temp.append(temp_poss_sol_index[4]+1) # append new finger placement for sol5
        sol6_temp.append(temp_poss_sol_index[5]+1) # append new finger placement for sol6
        sol7_temp.append(temp_poss_sol_index[6]+1) # append new finger placement for sol7
        sol8_temp.append(temp_poss_sol_index[7]+1) # append new finger placement for sol8
        sol9_temp.append(temp_poss_sol_index[8]+1) # append new finger placement for sol9
        sol10_temp.append(temp_poss_sol_index[9]+1) # append new finger placement for sol10
        sol11_temp.append(temp_poss_sol_index[10]+1) # append new finger placement for sol11
        sol12_temp.append(temp_poss_sol_index[11]+1) # append new finger placement for sol12
        sol13_temp.append(temp_poss_sol_index[12]+1) # append new finger placement for sol13
        sol14_temp.append(temp_poss_sol_index[13]+1) # append new finger placement for sol14
        sol15_temp.append(temp_poss_sol_index[14]+1) # append new finger placement for sol15

        # copy over current solutions
        sol1 = sol1_temp
        sol2 = sol2_temp
        sol3 = sol3_temp
        sol4 = sol4_temp
        sol5 = sol5_temp
        sol6 = sol6_temp
        sol7 = sol7_temp
        sol8 = sol8_temp
        sol9 = sol9_temp
        sol10 = sol10_temp
        sol11 = sol11_temp
        sol12 = sol12_temp
        sol13 = sol13_temp
        sol14 = sol14_temp
        sol15 = sol15_temp

        # copy over scores and reset array
        scores = temp_scores
        temp_scores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        # set possible scores to be the current score for each solution
        '''
        poss_sol1_scores = [scores[0],scores[0],scores[0],scores[0],scores[0]]
        poss_sol2_scores = [scores[1],scores[1],scores[1],scores[1],scores[1]]
        poss_sol3_scores = [scores[2],scores[2],scores[2],scores[2],scores[2]]
        poss_sol4_scores = [scores[3],scores[3],scores[3],scores[3],scores[3]]
        poss_sol5_scores = [scores[4],scores[4],scores[4],scores[4],scores[4]]
        poss_sol6_scores = [scores[5],scores[5],scores[5],scores[5],scores[5]]
        poss_sol7_scores = [scores[6],scores[6],scores[6],scores[6],scores[6]]
        poss_sol8_scores = [scores[7],scores[7],scores[7],scores[7],scores[7]]
        poss_sol9_scores = [scores[8],scores[8],scores[8],scores[8],scores[8]]
        poss_sol10_scores = [scores[9],scores[9],scores[9],scores[9],scores[9]]
        '''
        poss_sol1_scores = [0,0,0,0,0]
        poss_sol2_scores = [0,0,0,0,0]
        poss_sol3_scores = [0,0,0,0,0]
        poss_sol4_scores = [0,0,0,0,0]
        poss_sol5_scores = [0,0,0,0,0]
        poss_sol6_scores = [0,0,0,0,0]
        poss_sol7_scores = [0,0,0,0,0]
        poss_sol8_scores = [0,0,0,0,0]
        poss_sol9_scores = [0,0,0,0,0]
        poss_sol10_scores = [0,0,0,0,0]
        poss_sol11_scores = [0,0,0,0,0]
        poss_sol12_scores = [0,0,0,0,0]
        poss_sol13_scores = [0,0,0,0,0]
        poss_sol14_scores = [0,0,0,0,0]
        poss_sol15_scores = [0,0,0,0,0]
        
    #
    #
    # print results for debugging
    print("#1 solution:")
    print("score =", scores[0])
    print("sol_num =", temp_sol_num[0])
    print("little lamb  =", little_lamb_chars)
    print("solution =", sol1)