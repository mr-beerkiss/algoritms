""" quick_sort.py """
def quick_sort(alist):
    """ Provides the quick sort algorithm on the supplied list """
    def partition(alist, p, r):
        """ partitions the supplied array on position r """
        q = p
        for j in range(p, r):
            if (alist[j] <= alist[r]):
                alist[q], alist[j] = alist[j], alist[q]
                q += 1

        alist[q], alist[r] = alist[r], alist[q]   
        return q

    def quick_sort_helper(alist, p, r):
        """ lamba function that actually performs the recursive call """
        if (p < r):
            q = partition(alist, p, r)
            quick_sort_helper(alist, p, q-1)
            quick_sort_helper(alist, q+1, r)

    quick_sort_helper(alist, 0, len(alist)-1)
    

def test_program():
    """ test the program """
    # Can't test the partition function directly since it is a lamda!
    # in_list = [9, 7, 5, 11, 12, 2, 14, 3, 10, 4, 6];
    # ex_list = [5, 2, 3, 4, 6, 7, 14, 9, 10, 11, 12];
    # q = partition(in_list, 0, len(in_list)-1);
    # assert in_list ==  ex_list, "Expected %r but got %r" % (ex_list, in_list)
    # assert q == 4, "Expected parition key to be %d but got %d" % (4, q)

    in_list = [5, 4, 1, 3, 2]
    ex_list = sorted(in_list)
    # quick_sort(in_list, 0, len(in_list)-1)
    quick_sort(in_list)
    assert in_list == ex_list, "Expected %r but got %r" % (ex_list, in_list)

    in_list = [27, 8, -11, 3, 0, 89, -66]
    ex_list = sorted(in_list)
    # quick_sort(in_list, 0, len(in_list)-1)
    quick_sort(in_list)
    assert in_list == ex_list, "Expected %r but got %r" % (ex_list, in_list)

    in_list = [880, 375, -91, 550, 637, 412, 541, 114, -273, 120, -549, -666, 944, -960, -209, 232, -809, 263, -466, -795, -407, -579, 161, -515, 782, -552, -702, 685, -217, -210, -410, -340, 586, 625, 117, 887, 971, 177, -214, -374, 937, 650, -394, 818, -792, 323, -253, -774, 855, 307, -513, -783, -819, 651, 79, 455, 898, -900, 147, 957, -117, -898, 805, 197, -389, -398, -903, 969, -834, -972, -630, 931, 123, 529, -400, -436, -116, 684, 982, -417, 458, 979, -129, -63, -228, -570, -853, 399, 840, 676, -887, -351, 159, -334, -30, 841, 222, -107, -451, 173, 704, 345, -879, -104, -225, 61, -782, -742, 835, 336, -497, 634, -755, -188, -877, -10, 302, 267, 534, -638, -858, -558, 417, -247, 44, 279, 124, -575, 590, 878, 582, -595, -814, -278, 39, 783, -557, -831, -246, -31, 592, 780, -915, -799, 233, -745, 342, -70, -97, 387, -102, -298, -110, 986, -431, -118, -265, 547, 837, -320, 294, 613, 517, -276, -309, -323, -937, 614, 915, 562, -60, -80, 844, 779, -424, 974, 711, 567, 129, -348, 958, 63, 672, -321, 270, 243, -69, 576, 744, -135, 98, 587, -238, -862, -523, -893, 187, -51, 81, 956, -239, -943, -537, 746, -826, -690, 285, 721, 406, 771, 851, 444, -598, -427, 103, -583, -307, -490, 499, -751, 237, -543, 51, -452, 890, 953, -148, -412, 827, -328, -723, 96, -33, -85, 367, 481, -213, -878, 349, 23, -618, -84, 758, 189, -227, -237, 698, 899, -759, 595, -881, 19, 27, -401, -462, -324, -551, -564, -429, 902, -712, -531, -44, 717, 870, -777, -846, 0, -808, -242, 281, -865, 362, -474, 778, 274, -138, -126, 138, -650, -541, 448, -95, 767, -965, 658, -727, 807, 739, -652, -615, -581, 47, 330, 70, 301, 502, -461, 109, -187, 45, 277, -649, -306, -171, -989, -369, -378, -789, -949, 141, -299, -660, -505, 732, -668, -768, 552, -269, 122, -697, 26, -734, -470, 531, 155, -857, 610, 823, -824, -101, -659, -752, 224, 168, -844, -291, -159, -195, 255, -776, -450, 559, -93, -891, -901, 535, -337, 929, 530, 130, -375, -930, 871, -121, -920, -243, -934, -995, 87, 450, 733, 490, -856, -316, -528, -186, -979, -434, -78, -510, -956, 219, 442, -66, 364, -216, -358, -354, 497, -428, 925, 409, -58, 907, 906, 166, -331, 295, 378, -957, -675, -477, 217, -662, -18, -206, 447, 242, 332, -133, -764, 932, 642, 43, -911, -122, 947, -507, 950, 54, 847, -245, -749, -478, 803, 389, 796, -330, -524, 180, 936, -606, -787, 16, 476, -408, 724, 195, 445, -362, -699, -544, 759, -563, -816, -96, -338, 34, -491, -713, -721, -106, -167, -322, 71, -335, 600, 623, 666, 374, -395, 171, 697, -297, -399, 390, 454, -83, 848, -718, 752, -797, 430, -845, 810, -261, -366, 523, -396, -821, -591, -521, -585, -610, -661, -441, 731, -295, -670, -780, -538, -750, 540, -757, 320, 501, -936, 781, 656, -488, -415, 628, 165, 701, -704, 422, 620, 104, 414, 73, 933, -166, 804, 785, 306, -823, -923, 741, 75, 22, -997, -833, -113, -700, 327, 983, 525, -173, 95, -607, 127, 981, -53, 370, 809, 149, -636, 483, -308, 142, 413, -13, -367, 314, -852, 801, -922, 228, -47, -81, 72, 745, -499, -863, -592, -411, -205, -746, 3, -455, -886, 829, -46, -142, -533, -535, 518, 419, -38, -732, -114, -646, -714, 184, -182, 690, -318, 776, -346, -781, 491, 250, 638, -953, -35, 30, -231, 683, 273, -817, 204, -869, 603, 882, 828, -769, 328, -203, 313, -200, 700, -935, 170, -719, -685, 505, -536, -710, 680, -867, -151, 503, -409, 353, 584, -385, -512, 675, 384, 984, 69, -604, -859, -140, 573, -569, 910, -49, -801, -518, 719, 952, 111, -11, 321, 181, 178, 756, -617, -571, -4, -848, 978, -448, -678, -837, 885, 908, 549, 960, -17, -420, -683, -487, 9, -629, 257, 593, -829, 154, -559, -501, -589, 176, 826, -508, 446, 137, -942, -255, -775, 862, 276, 736, -270, 718, -263, -383, 145, -397, -698, 188, 988, -183, 52, 770, -19, -976, -602, -484, -422, 449, -64, -540, -141, 546, 37, -715, -271, -744, -836, -500, -249, -202, 511, 153, -7, 636, 429, 357, -950, 924, 346, -861, -139, 789, 688, -74, -391, 964, -766, -168, 710, -14, 556, 816, 548, -165, -993, 116, -611, -927, -677, 215, -637, -197, 304, -460, 917, 868, 773, -229, 317, 312, 653, 318, -907, 266, 492, 319, 585, 463, -587, -498, -71, -131, -485, -435, -868, -248, -506, -517, 126, -928, -996, 662, 825, -933, -418, 821, 110, 13, -169, -402, 975, -632, 867, 470, 337, 453, 258, 763, -382, -682, -553, 935, 865, 192, -703, 480, -180, 198, -277, 380, 563, 659, 5, 926, 820, -530, -22, 474, 875, -108, 369, -883, 580, 74, -254, -665, 553, -387, -55, 859, -971, 4, 962, -850, 229, -440, -577, -370, 386, -686, -902, 498, 806, -737, -1, 340, 494, -778, 987, -145, 632, 972, 657, -421, 179, 911, 713, 373, 7, 423, 568, -287, -899, -526, 443, -312, -639, 664, 834, -738, -917, -599, 686, 661, 240, 100, -522, -458, -741, -516, -574, -65, 175, 459, -360, -390, 845, 288, -32, -332, 976, -612, 668, 227, 186, 143, -520, -386, 749, -838, 326, -696, 764, 162, -779, 738, -292, -722, 873, -763, -476, 151, -656, 77, 371, 798, 886, 574, -208, -561, -36, -233, -463, -416, 478, 472, -889, -99, -361, -669, 462, -86, -274, -963, 536, 808, -890, -822, -673, 461, 510, 252, -828, -855, 742, -628, 786, 945, 194, 133, -973, 167, -403, -190, -555, -181, -368, -640, 418, 532, -162, -504, 874, -841, -627, -926, -293, 790, -339, -144, -705, -438, 196, 268, -975, -234, 86, 670, -25, -651, -207, 598, -603, -161, 208, -860, -3, 941, 766, -909, 200, 212, 416, 275, -355, 846, 624, -572, 89, -532, 388, 822, -305, -772, -609, 709, -406, -109, 608, 516, 428, 815, 843, -818, 963, 66, -674, 309, -496, 594, 150, 919, -419, 118, -241]
    ex_list = sorted(in_list)
    quick_sort(in_list)
    assert in_list == ex_list, "Expected %r but got %r" % (ex_list, in_list)
    
    print("All tests have passed")

test_program()