# Databricks notebook source
inp = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

# COMMAND ----------

inp = '''seeds: 304740406 53203352 1080760686 52608146 1670978447 367043978 1445830299 58442414 4012995194 104364808 4123691336 167638723 2284615844 178205532 3164519436 564398605 90744016 147784453 577905361 122056749

seed-to-soil map:
0 699677807 922644641
4174180469 3833727510 120786827
1525682201 2566557266 229511566
3280624601 3954514337 340452959
2228029508 2796068832 310221139
3621077560 3280624601 553102909
2120836342 592484641 107193166
1982514669 227320902 138321673
1755193767 0 227320902
922644641 1622322448 603037560
2538250647 365642575 226842066
2765092713 2225360008 341197258

soil-to-fertilizer map:
1916776044 145070025 3464138
1920240182 0 145070025
706160141 2208005933 115191764
2898492924 830275742 87027483
3489083348 3344594558 103871907
2985520407 148534163 415139950
821351905 917303225 327392865
1148744770 1517236949 182706102
295069722 3448466465 411090419
1816984891 3244803405 99791153
4282585972 4292886644 2080652
3592955255 563674113 266601629
4266462972 4158154511 16123000
1331450872 1244696090 272540859
2715943131 3062253612 182549793
4284666624 4174277511 10300672
4158154511 4184578183 108308461
1603991731 1995012773 212993160
2065310207 2411620688 650632924
0 1699943051 295069722
3400660357 2323197697 88422991

fertilizer-to-water map:
3585244197 3493316345 482900943
2871272496 878061687 456215665
3477664135 4187387234 107580062
845559238 15587711 56716031
121711204 2918313406 409174755
1639718746 0 15587711
530885959 2603640127 314673279
902275269 2435903232 167736895
2635221133 72303742 236051363
1070012164 308355105 569706582
1699846244 1334277352 935374889
4279315086 3477664135 15652210
1655306457 2269652241 44539787
109056711 2423248739 12654493
0 2314192028 109056711
4068145140 3976217288 211169946

water-to-light map:
3841742547 3016842841 17384315
2875021919 2637593760 185450069
3413635232 3588265685 87508205
1311241677 236307150 54007684
3349161906 4276682782 18284514
896790030 1355845673 34430118
3060471988 3835573209 145836645
2741184131 3675773890 133837788
1387754847 947687177 15489861
3785944618 2057196631 55797929
2006585491 2931426646 85416195
3873217816 3809611678 25961531
1667765627 643929130 34884144
2092001686 2434956599 202637161
1001898651 158618769 77688381
3899179347 2253048950 181907649
1786416461 377140410 101956748
0 833901414 113785763
1403244708 479097158 56815029
3859126862 3034227156 14090954
747996464 678813274 31450438
869173795 963177038 27616235
3268502638 2006585491 50611140
113785763 0 148879571
262665334 1511505797 386606610
1187603975 710263712 123637702
3319113778 3987361499 30048128
3367446420 2885237834 46188812
931220148 990793273 15913032
1460059737 1006706305 120880314
1079587032 535912187 108016943
3645890228 2112994560 140054390
3206308633 2823043829 62194005
1888373209 148879571 9739198
3501143437 3443518894 144746791
779446902 1127586619 89726893
947133180 1217313512 54765471
2481910976 4017409627 259273155
1365249361 1390275791 22505486
4087038641 3048318110 207928655
1702649771 1272078983 83766690
649271944 1412781277 98724520
2294638847 3256246765 187272129
4081086996 3981409854 5951645
1580940051 290314834 86825576

light-to-temperature map:
2659452899 3773423191 23529065
1010417677 1830019321 229964714
1506263997 1764304095 65715226
3017023682 3993999178 103632805
3758361154 3931294907 62704271
2513441862 2529586713 106552791
3821065425 3163657189 7959671
3410504451 3191697730 271334719
2500616406 3150831733 12825456
2065874786 2636139504 257698620
4142272690 2382216135 108163002
1377732678 1378901025 61208694
91217027 248578952 8927711
2463617376 3879075083 36999030
3982807123 2315058258 67157877
2323573406 2065874786 97274446
958870382 916323074 51547295
3868386197 3579887474 114420926
931392999 1351423642 27477383
2942753127 3694308400 74270555
1812734437 168620508 79958444
3301364949 2163149232 3197696
2420847852 2166346928 42769524
3829025096 3111470632 39361101
2619994653 2490379137 39207576
1571979223 1523548881 240755214
2927532333 3916074113 15220794
3125500723 4097631983 175864226
1438941372 10080856 67322625
2049903179 0 10080856
3304562645 2209116452 105941806
1976132043 1277652506 73771136
2659202229 3171616860 250670
4256036535 3463032449 38930761
1240382391 257506663 137350287
0 77403481 91217027
3120656487 3768578955 4844236
100144738 967870369 309782137
409926875 394856950 521466124
2682981964 4273496209 21471087
2704453051 3501963210 77924264
2802207515 2893838124 125324818
3681839170 3796952256 76521984
4250435692 3873474240 5600843
1892692881 1440109719 83439162
4049965000 3019162942 92307690
2782377315 3171867530 19830200

temperature-to-humidity map:
1281293605 2434144353 57731817
3534843655 3623804479 36539813
1516028925 367078655 499627624
3340374639 3427302148 25514722
1176213912 2491876170 105079693
3872645852 3827818849 188531931
508302359 1375008638 300832898
0 866706279 508302359
4146417618 3475254801 148549678
4083438506 3660344292 62979112
3365889361 3745584127 82234722
4061177783 3723323404 22260723
2015656549 1675841536 348405327
1056134836 246999579 120079076
3448124083 3452816870 22437931
3321587434 3408514943 18787205
3470562014 4016350780 64281641
3571383468 3321587434 86927509
1339025422 2024246863 177003503
809135257 0 246999579
2364061876 2596955863 115651453
3658310977 4080632421 214334875
2479713329 2201250366 232893987

humidity-to-location map:
2408792839 708984436 12070437
3916327360 4103567762 90492800
2136669394 2902458135 226099404
1414655297 721054873 722014097
2462136308 3514619416 2467233
1254861475 3327498132 98562162
2362768798 569836962 46024041
4185175199 3916327360 8885363
421054090 234463197 201173738
2497827912 1550759989 35404865
849065671 0 224309687
37059832 615861003 93123433
4006820160 3925212723 178355039
2863253575 1705311678 653833074
622227828 1443068970 107691019
2464603541 2869233764 33224371
1353423637 3128557539 61231660
1073375358 3426060294 47286090
2725544642 3189789199 137708933
26906322 224309687 10153510
2420863276 3473346384 41273032
729918847 1586164854 119146824
2533232777 2676921899 192311865
0 2359144752 26906322
1120661448 435636935 134200027
130183265 2386051074 290870825
'''

# COMMAND ----------

import re
seeds, *maps = inp.split('\n\n')
seeds = [int(x) for x in re.findall('\d+', seeds)]
maps = [[[int(x) for x in re.findall('\d+', line)] for line in m.splitlines()[1:]] for m in maps]


# COMMAND ----------

s = []
for seed in seeds:
    for mapping in maps:
        for dest_start, source_start, range_len in mapping:
            if source_start <= seed < source_start + range_len:
                seed = dest_start + (seed - source_start)
                break
    s.append(seed)
min(s)

# COMMAND ----------



# COMMAND ----------

# Greedy?

# COMMAND ----------

# Smallest outcome
min((dest_start, source_start, range_len) for dest_start, source_start, range_len in maps[-1])
# location is [0, 26906322)
# humidity is [2359144752, 2359144752+26906322)

# COMMAND ----------

for mapping in maps[::-1]:
    print(min((dest_start, source_start, range_len) for dest_start, source_start, range_len in maps[-1]))

# COMMAND ----------

seeds

# COMMAND ----------

for i in range(0, len(seeds), 2):
    print(seeds[i:i+2])

# COMMAND ----------

def overlap(start1, end1, start2, end2):
    """how much does the range (start1, end1) overlap with (start2, end2)"""
    return max(max((end2-start1), 0) - max((end2-end1), 0) - max((start2-start1), 0), 0)

# COMMAND ----------

# import functools


# @functools.cache
# def get_smallest_range(i, in_start, in_range_len):
#     print(f'{i=} {in_start=} {in_range_len=}')
#     if i == len(maps):
#         return in_start

#     output_ranges = [] # (out_start, out_range_len) pairs
#     for dest_start, source_start, range_len in maps[i]:
#         if source_start + range_len <= in_start or source_start >= in_start + in_range_len:
#             print(f'{dest_start=} {source_start=} {range_len=} no overlap')
#             continue # No overlap
        
#         # Assume overlap
#         if source_start == in_start: # Source starts at input start
#             overlap_start = in_start
#             overlap_range_len = min(range_len, in_range_len)
#         elif source_start < in_start: # Source starts to left
#             overlap_start = in_start
#             overlap_end = min(source_start + range_len, in_start + in_range_len)
#             overlap_range_len = overlap_end - in_start
#             print(f'{dest_start=} {source_start=} {range_len=} overlap type1: {overlap_start=} {overlap_range_len=}')
#         else: # Source starts to right of input start (still inside input)
#             overlap_start = source_start
#             overlap_end = min(source_start + range_len, in_start + in_range_len)
#             overlap_range_len = overlap_end - in_start
#             print(f'{dest_start=} {source_start=} {range_len=} overlap type2: {overlap_start=} {overlap_range_len=}')
        
#         overlap_start = overlap_start - source_start +  dest_start

#         #overlap_start, overlap_range_len = ...
#         output_ranges.append((overlap_start, overlap_range_len))

#     outputs = [get_smallest_range(i + 1, out_start, out_range_len) for out_start, out_range_len in output_ranges]
#     print(f'{outputs=}')
#     return min(outputs) if outputs else float('inf')

# # get_smallest_range(0, in_start=79, in_range_len=14)
# get_smallest_range(0, in_start=82, in_range_len=1)


# # starting_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
# # result = []
# # for in_start, in_range_len in starting_ranges:
# #     result.append(get_smallest_range(0, in_start, in_range_len))
# # result


# #print(min(result))

# COMMAND ----------

import functools


@functools.cache
def get_smallest_range(i, in_start, in_range_len):
    # print(f'{i=} {in_start=} {in_range_len=}')
    if i == len(maps):
        return in_start

    output_ranges = [] # (out_start, out_range_len) pairs
    for dest_start, source_start, range_len in maps[i]:
        if source_start + range_len <= in_start or source_start >= in_start + in_range_len:
            # print(f'{dest_start=} {source_start=} {range_len=} no overlap')
            continue # No overlap
        
        # Assume overlap
        if source_start == in_start: # Source starts at input start
            overlap_start = in_start
            overlap_range_len = min(range_len, in_range_len)
        elif source_start < in_start: # Source starts to left
            overlap_start = in_start
            overlap_end = min(source_start + range_len, in_start + in_range_len)
            overlap_range_len = overlap_end - in_start
            # print(f'{dest_start=} {source_start=} {range_len=} overlap type1: {overlap_start=} {overlap_range_len=}')
        else: # Source starts to right of input start (still inside input)
            overlap_start = source_start
            overlap_end = min(source_start + range_len, in_start + in_range_len)
            overlap_range_len = overlap_end - source_start # overlap_range_len = overlap_end - in_start
            # print(f'{dest_start=} {source_start=} {range_len=} overlap type2: {overlap_start=} {overlap_range_len=}') # Bug in here

            #dest_start=0 source_start=69 range_len=1 overlap type2: overlap_start=69 overlap_range_len=2
            #dest_start=70 source_start=70 range_len=10000000000 overlap type2: overlap_start=70 overlap_range_len=13
        
        overlap_start = overlap_start - source_start +  dest_start

        #overlap_start, overlap_range_len = ...
        output_ranges.append((overlap_start, overlap_range_len))

    outputs = [get_smallest_range(i + 1, out_start, out_range_len) for out_start, out_range_len in output_ranges]
    #print(f'{outputs=}')
    return min(outputs) if outputs else float('inf')

maps = [[[int(x) for x in re.findall('\d+', line)] for line in m.splitlines()[1:]] for m in inp.split('\n\n')[1:]]
for m in maps:
    m.sort(key=lambda e: e[1])
for m in maps:
    if m[0][1] != 0:
        m.insert(0, [0, 0, m[0][1]])
    
    last_val = m[-1][1] + m[-1][2]
    m.append([last_val, last_val, 10_000_000_000])
    #i in range(len(m)):
    
    for i in range(len(m) - 1):
        end = m[i][1] + m[i][2]
        start = m[i+1][1]
        if end != start:
            m.append((end, end, start - end))

    m.sort(key=lambda e: e[1])
        
# maps


# get_smallest_range(0, in_start=79, in_range_len=14)
# get_smallest_range(0, in_start=82, in_range_len=1)


starting_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
result = []
for in_start, in_range_len in starting_ranges:
    result.append(get_smallest_range(0, in_start, in_range_len))
result


print(min(result))

# COMMAND ----------

print(min(result)) # 60756547 TOO HIGH

# COMMAND ----------

4917124<60756547

# COMMAND ----------

starting_ranges

# COMMAND ----------

get_smallest_range(0, 79, 14)

# COMMAND ----------

z = [get_smallest_range(0, 55+i, 1) for i in range(13)] # So INDIVIDUALLY (length 1) numbers are fine. There is a problem when it's a RANGE

# COMMAND ----------

get_smallest_range(0, 55, 13)

# COMMAND ----------

get_smallest_range(5, 68, 13) # This is where it goes bad

# THIS IS DEFINITELY THE BUG - HOW IS 13?? dest_start=70 source_start=70 range_len=10000000000 overlap type2: overlap_start=70 overlap_range_len=13

# COMMAND ----------

get_smallest_range(0, 68, 1) 

# COMMAND ----------

z

# COMMAND ----------

# THIS IS A BUG
# dest_start=0 source_start=69 range_len=1 overlap type2: overlap_start=69 overlap_range_len=2

# COMMAND ----------

get_smallest_range(0, 55, 13)

# COMMAND ----------

i=6 in_start=0 in_range_len=2
i=7 in_start=0 in_range_len=2

# COMMAND ----------

get_smallest_range(6, 0, 2) 

# COMMAND ----------

maps[7]

# COMMAND ----------

# i=7 in_start=74 in_range_len=13

# COMMAND ----------

get_smallest_range(7, 74, 13)

# COMMAND ----------

result

# COMMAND ----------

maps

# COMMAND ----------

get_smallest_range(3, in_start=84, in_range_len=1) # 84 water goes to 77 light
# i=5 -> 4 temp
# i=5 -> 46 humidity

# COMMAND ----------

maps[1]

# COMMAND ----------

maps

# COMMAND ----------

get_smallest_range(0, in_start=79, in_range_len=14)

# COMMAND ----------

starting_ranges

# COMMAND ----------

maps

# COMMAND ----------

maps[0]
