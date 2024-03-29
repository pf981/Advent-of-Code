# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 13: Transparent Origami ---</h2><p>You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.</p>
# MAGIC <p>Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:</p>
# MAGIC <pre><code>Congratulations on your purchase! To activate this infrared thermal imaging
# MAGIC camera system, please enter the code found on page 1 of the manual.
# MAGIC </code></pre>
# MAGIC <p>Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of <a href="https://en.wikipedia.org/wiki/Transparency_(projection)" target="_blank">transparent paper</a>! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:</p>
# MAGIC <pre><code>6,10
# MAGIC 0,14
# MAGIC 9,10
# MAGIC 0,3
# MAGIC 10,4
# MAGIC 4,11
# MAGIC 6,0
# MAGIC 6,12
# MAGIC 4,1
# MAGIC 0,13
# MAGIC 10,12
# MAGIC 3,4
# MAGIC 3,0
# MAGIC 8,4
# MAGIC 1,10
# MAGIC 2,14
# MAGIC 8,10
# MAGIC 9,0
# MAGIC 
# MAGIC fold along y=7
# MAGIC fold along x=5
# MAGIC </code></pre>
# MAGIC <p>The first section is a list of dots on the transparent paper. <code>0,0</code> represents the top-left coordinate.  The first value, <code>x</code>, increases to the right.  The second value, <code>y</code>, increases downward.  So, the coordinate <code>3,0</code> is to the right of <code>0,0</code>, and the coordinate <code>0,7</code> is below <code>0,0</code>. The coordinates in this example form the following pattern, where <code>#</code> is a dot on the paper and <code>.</code> is an empty, unmarked position:</p>
# MAGIC <pre><code>...#..#..#.
# MAGIC ....#......
# MAGIC ...........
# MAGIC #..........
# MAGIC ...#....#.#
# MAGIC ...........
# MAGIC ...........
# MAGIC ...........
# MAGIC ...........
# MAGIC ...........
# MAGIC .#....#.##.
# MAGIC ....#......
# MAGIC ......#...#
# MAGIC #..........
# MAGIC #.#........
# MAGIC </code></pre>
# MAGIC <p>Then, there is a list of <em>fold instructions</em>. Each instruction indicates a line on the transparent paper and wants you to fold the paper <em>up</em> (for horizontal <code>y=...</code> lines) or <em>left</em> (for vertical <code>x=...</code> lines). In this example, the first fold instruction is <code>fold along y=7</code>, which designates the line formed by all of the positions where <code>y</code> is <code>7</code> (marked here with <code>-</code>):</p>
# MAGIC <pre><code>...#..#..#.
# MAGIC ....#......
# MAGIC ...........
# MAGIC #..........
# MAGIC ...#....#.#
# MAGIC ...........
# MAGIC ...........
# MAGIC -----------
# MAGIC ...........
# MAGIC ...........
# MAGIC .#....#.##.
# MAGIC ....#......
# MAGIC ......#...#
# MAGIC #..........
# MAGIC #.#........
# MAGIC </code></pre>
# MAGIC <p>Because this is a horizontal line, fold the bottom half <em>up</em>. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:</p>
# MAGIC <pre><code>#.##..#..#.
# MAGIC #...#......
# MAGIC ......#...#
# MAGIC #...#......
# MAGIC .#.#..#.###
# MAGIC ...........
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>Now, only <code>17</code> dots are visible.</p>
# MAGIC <p>Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at <code>0,0</code> and <code>0,1</code>). Because the paper is transparent, the dot just below them in the result (at <code>0,3</code>) remains visible, as it can be seen through the transparent paper.</p>
# MAGIC <p>Also notice that some dots can end up <em>overlapping</em>; in this case, the dots merge together and become a single dot.</p>
# MAGIC <p>The second fold instruction is <code>fold along x=5</code>, which indicates this line:</p>
# MAGIC <pre><code>#.##.|#..#.
# MAGIC #...#|.....
# MAGIC .....|#...#
# MAGIC #...#|.....
# MAGIC .#.#.|#.###
# MAGIC .....|.....
# MAGIC .....|.....
# MAGIC </code></pre>
# MAGIC <p>Because this is a vertical line, fold <em>left</em>:</p>
# MAGIC <pre><code>#####
# MAGIC #...#
# MAGIC #...#
# MAGIC #...#
# MAGIC #####
# MAGIC .....
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>The instructions made a square!</p>
# MAGIC <p>The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, <code><em>17</em></code> dots are visible - dots that end up overlapping after the fold is completed count as a single dot.</p>
# MAGIC <p><em>How many dots are visible after completing just the first fold instruction on your transparent paper?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''802,891
773,324
1125,3
910,718
433,626
1310,809
840,799
415,74
346,306
1203,817
793,877
18,194
120,554
1016,887
437,238
249,730
212,66
955,457
873,656
607,155
311,820
98,824
769,639
547,172
1059,596
320,273
676,457
698,491
661,535
718,803
212,28
366,642
862,563
298,295
1011,493
370,779
1118,416
1285,576
760,703
22,466
87,570
391,84
1115,737
331,155
1126,773
684,485
334,733
1288,816
681,576
268,191
375,152
142,266
604,596
836,451
763,396
758,140
323,739
851,381
301,877
1261,371
410,116
248,677
502,687
724,565
858,43
430,376
63,117
776,564
612,331
1197,191
331,610
1250,878
460,158
1267,511
719,187
644,838
333,402
470,799
567,379
249,58
1250,68
288,252
1242,117
1007,654
1222,845
1041,519
80,788
206,115
594,530
25,241
643,875
432,191
537,232
263,551
758,717
251,596
62,131
944,611
334,161
659,535
949,40
918,387
679,584
20,437
1044,829
89,252
55,4
851,79
266,513
1262,878
388,206
448,872
945,103
224,327
480,522
228,51
179,663
959,576
241,406
800,210
1044,152
118,677
1248,131
107,15
656,361
1272,731
209,423
1190,106
1082,51
221,716
25,576
1158,655
534,330
1004,880
3,359
1092,23
82,408
45,438
442,866
602,494
1083,814
661,135
269,519
321,178
666,838
952,861
687,530
140,479
1158,522
218,107
349,446
857,481
584,584
1186,627
918,497
102,177
435,767
887,313
266,206
1136,541
1140,173
704,430
787,551
514,31
326,743
634,569
1056,606
1178,264
423,313
316,166
654,501
1285,352
385,453
704,28
864,329
370,227
1179,551
20,549
99,586
1036,400
617,453
1124,740
678,18
97,705
228,70
738,330
1086,376
1069,854
962,327
922,740
1158,186
731,570
1124,708
798,677
388,152
606,430
279,739
179,638
1096,74
527,261
1158,708
435,654
796,31
910,372
820,757
1036,494
435,319
22,18
797,672
656,393
224,791
146,796
386,199
684,35
1131,638
546,107
179,784
989,716
1053,579
361,854
741,358
393,396
455,149
1183,334
1059,74
234,372
377,859
195,135
1179,595
1211,590
258,441
632,620
663,315
1253,599
749,567
875,767
1010,28
760,191
480,372
960,516
1193,570
780,122
68,777
591,707
1082,163
1235,52
880,70
102,269
1303,579
228,731
644,15
743,379
1047,791
1164,796
107,77
918,61
98,180
1287,766
38,88
80,554
1242,453
335,756
160,77
1183,633
1119,353
512,714
112,372
388,812
87,122
259,805
388,490
262,397
5,135
580,789
430,518
440,64
922,737
1212,70
0,85
1169,670
393,498
1235,298
1009,94
890,746
500,477
377,390
191,681
550,373
1104,22
309,523
1261,483
1119,289
343,105
1069,406
120,106
131,807
922,152
1235,148
940,115
567,603
366,611
180,219
426,714
249,282
453,413
1216,777
403,74
894,768
214,382
924,423
1170,863
20,457
1032,268
935,152
862,872
75,52
266,812
470,95
716,154
1130,684
796,414
1108,851
436,107
842,634
975,579
964,434
344,852
758,306
800,684
1263,742
1299,19
1130,675
140,414
144,684
1048,173
947,73
584,310
592,803
582,288
924,689
25,149
231,133
1098,380
840,456
966,115
1267,383
107,655
408,780
726,310
108,3
288,88
1170,480
308,882
503,231
157,247
321,716
113,703
848,416
180,451
152,298
913,91
681,696
902,780
363,821
42,128
875,799
415,372
243,873
597,841
897,58
328,295
1252,471
120,564
421,567
987,807
1101,232
899,873
219,799
266,65
301,800
569,596
967,820
579,74
475,256
944,546
738,784
663,138
70,63
719,707
1228,564
884,731
195,513
335,138
1223,772
288,59
426,395
257,579
517,254
1246,609
453,481
840,266
736,486
808,207
15,7
303,128
917,396
98,714
626,485
792,866
89,364
70,136
1310,85
469,443
448,564
647,756
719,329
858,346
989,135
356,491
1000,779
977,402
960,722
241,506
1179,343
1190,788
319,315
345,371
415,820
124,478
1082,731
266,152
234,746
212,514
830,74
1047,777
1186,346
274,494
363,261
1000,563
430,70
288,194
852,586
870,74
862,51
1305,135
1031,379
300,812
234,592
42,42
1015,82
683,885
1169,84
667,19
726,63
975,138
383,890
683,9
1151,423
1168,714
1096,294
222,191
146,98
1159,187
1203,351
743,772
1116,288
234,522
405,730
900,116
1235,842
411,469
540,380
361,152
1052,441
490,154
1033,259
607,742
363,745
425,189
375,805
1135,691
186,186
716,269
703,600
1004,569
206,51
840,95
627,885
214,858
1021,103
823,516
396,453
924,205
42,766
1088,821
398,63
1130,219
855,143
1091,575
967,522
694,358
435,879
796,303
562,750
1230,554
984,743
569,88
3,162
10,431
780,346
20,325
802,796
433,268
1290,549
634,457
728,288
510,449
99,308
1098,66
1067,873
345,84
1210,875
1288,18
435,369
574,786
388,154
802,236
566,49
1218,144
192,478
1111,149
202,346
631,310
309,371
803,336
743,603
689,628
1043,255
1061,826
514,210
1048,61
944,806
1108,43
1071,372
638,180
1307,535
994,166
378,858
704,464
949,742
82,486
1048,397
206,563
413,806
1164,98
344,115
842,740
1136,820
514,414
366,252
919,329
108,252
594,364
321,807
278,250
1062,385
550,191
224,376
1098,828
1009,800
387,507
172,417
897,88
195,759
131,299
940,667
1163,876
5,359
181,791
731,324
388,404
1086,327
736,106
310,563
174,820
140,863
75,148
957,800
776,106
62,763
398,831
1088,546
1108,100
155,26
1026,563
164,137
830,522
323,162
127,334
676,773
758,754
398,735
572,116
120,788
117,794
961,672
769,255
1208,269
596,504
954,528
289,847
426,742
629,653
574,106
736,277
263,777
1178,630
92,750
299,493
209,232
705,147
1014,301
855,149
405,58
1044,65
503,635
537,324
1007,310
58,471
597,151
147,784
1263,155
440,830
1203,879
1002,882
1203,77
366,806
951,82
1290,457
271,442
716,826
565,252
932,204
954,483
924,695
492,309
1228,486
1235,827
1169,810
1031,739
912,63
1101,662
392,833
1303,586
793,17
693,453
316,728
1088,191
227,814
964,306
527,633
373,701
934,626
249,164
1282,409
124,627
579,148
698,122
764,107
416,768
634,549
1173,472
654,395
1047,117
1001,810
1115,513
1190,554
1087,194
661,807
1022,835
216,494
385,285
629,696
263,117
546,227
152,74
1009,17
497,247
131,595
857,413
1126,438
344,779
378,690
1168,180
708,494
1034,718
951,364
835,558
798,180
1056,718
567,324
1211,308
954,366
922,404
905,58
592,579
1116,630
1218,808
1272,806
862,330
723,581
797,222
1250,157
716,812
835,256
895,74
541,639
351,128
959,878
940,43
388,42
1072,320
862,42
1131,663
152,655
1247,859
1183,261
377,483
694,194
426,163
512,441
147,22
587,581
612,212
137,640
522,264
345,362
1310,533
932,690
612,213
18,700
1213,705
514,479
925,823
400,718
1179,147
142,180
448,22
266,240
159,516
154,417
20,264
966,779
934,644
1076,302
1056,288
64,509
175,411
1163,448
378,158
842,186
626,859
92,144
979,854
800,642
701,456
884,742
348,567
1235,746
1022,59
135,737
346,460
918,507
1307,827
1178,712
651,359
428,105
1115,381
49,479
1299,875
730,789
596,639
463,737
828,417
1007,128
654,499
1206,73
326,151
489,357
452,346
508,763
354,364
218,787
966,563
1131,231
514,415
862,778
676,569
359,140
584,383
915,805
914,117
830,372
405,612
1001,523
965,810
1017,152
1285,149
1031,600
932,288
708,400
487,378
1295,455
880,824
979,40

fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6'''

# COMMAND ----------

import collections


def do_fold(dots, along, position):
  result = set()
  max_x, max_y = [max(dim) + 1 for dim in zip(*dots)]
  max_x = position if along == 'x' else max_x
  max_y = position if along == 'y' else max_y
  
  for y in range(max_y):
    for x in range(max_x):
      if (
        (x, y) in dots or
        (along == 'x' and (2 * position - x, y) in dots) or
        (along == 'y' and (x, 2 * position - y) in dots)
      ):
        result.add((x, y))

  return result


dots, folds = inp.split('\n\n')
dots = {tuple(int(coord) for coord in line.split(',')) for line in dots.splitlines()}
folds = [(lhs[-1], int(rhs)) for lhs, rhs in [line.split('=') for line in folds.splitlines()]]

answer = len(do_fold(dots, *folds[0]))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><span title="How can you fold it that many times? You tell me, I'm not the one folding it.">Finish folding</span> the transparent paper according to the instructions. The manual says the code is always <em>eight capital letters</em>.</p>
# MAGIC <p><em>What code do you use to activate the infrared thermal imaging camera system?</em></p>
# MAGIC </article>

# COMMAND ----------

for along, position in folds:
  dots = do_fold(dots, along, position)

max_x, max_y = [max(dim) + 1 for dim in zip(*dots)]
for y in range(max_y):
  for x in range(max_x):
    print('#' if (x, y) in dots else ' ', end='')
  print()

# COMMAND ----------

answer = 'UCLZRAZU'
print(answer)
