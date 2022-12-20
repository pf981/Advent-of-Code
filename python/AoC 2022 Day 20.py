# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/20

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 20: Grove Positioning System ---</h2><p>It's finally time to meet back up with the Elves. When you try to contact them, however, you get no reply. Perhaps you're out of range?</p>
# MAGIC <p>You know they're headed to the grove where the <em class="star">star</em> fruit grows, so if you can figure out where that is, you should be able to meet back up with them.</p>
# MAGIC <p>Fortunately, your handheld device has a file (your puzzle input) that contains the grove's coordinates! Unfortunately, the file is <em>encrypted</em> - just in case the device were to fall into the wrong hands.</p>
# MAGIC <p>Maybe you can <span title="You once again make a mental note to remind the Elves later not to invent their own cryptographic functions.">decrypt</span> it?</p>
# MAGIC <p>When you were still back at the camp, you overheard some Elves talking about coordinate file encryption. The main operation involved in decrypting the file is called <em>mixing</em>.</p>
# MAGIC <p>The encrypted file is a list of numbers. To <em>mix</em> the file, move each number forward or backward in the file a number of positions equal to the value of the number being moved. The list is <em>circular</em>, so moving a number off one end of the list wraps back around to the other end as if the ends were connected.</p>
# MAGIC <p>For example, to move the <code>1</code> in a sequence like <code>4, 5, 6, <em>1</em>, 7, 8, 9</code>, the <code>1</code> moves one position forward: <code>4, 5, 6, 7, <em>1</em>, 8, 9</code>. To move the <code>-2</code> in a sequence like <code>4, <em>-2</em>, 5, 6, 7, 8, 9</code>, the <code>-2</code> moves two positions backward, wrapping around: <code>4, 5, 6, 7, 8, <em>-2</em>, 9</code>.</p>
# MAGIC <p>The numbers should be moved <em>in the order they originally appear</em> in the encrypted file. Numbers moving around during the mixing process do not change the order in which the numbers are moved.</p>
# MAGIC <p>Consider this encrypted file:</p>
# MAGIC <pre><code>1
# MAGIC 2
# MAGIC -3
# MAGIC 3
# MAGIC -2
# MAGIC 0
# MAGIC 4
# MAGIC </code></pre>
# MAGIC <p>Mixing this file proceeds as follows:</p>
# MAGIC <pre><code>Initial arrangement:
# MAGIC 1, 2, -3, 3, -2, 0, 4
# MAGIC 
# MAGIC 1 moves between 2 and -3:
# MAGIC 2, 1, -3, 3, -2, 0, 4
# MAGIC 
# MAGIC 2 moves between -3 and 3:
# MAGIC 1, -3, 2, 3, -2, 0, 4
# MAGIC 
# MAGIC -3 moves between -2 and 0:
# MAGIC 1, 2, 3, -2, -3, 0, 4
# MAGIC 
# MAGIC 3 moves between 0 and 4:
# MAGIC 1, 2, -2, -3, 0, 3, 4
# MAGIC 
# MAGIC -2 moves between 4 and 1:
# MAGIC 1, 2, -3, 0, 3, 4, -2
# MAGIC 
# MAGIC 0 does not move:
# MAGIC 1, 2, -3, 0, 3, 4, -2
# MAGIC 
# MAGIC 4 moves between -3 and 0:
# MAGIC 1, 2, -3, 4, 0, 3, -2
# MAGIC </code></pre>
# MAGIC <p>Then, the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value <code>0</code>, wrapping around the list as necessary. In the above example, the 1000th number after <code>0</code> is <code><em>4</em></code>, the 2000th is <code><em>-3</em></code>, and the 3000th is <code><em>2</em></code>; adding these together produces <code><em>3</em></code>.</p>
# MAGIC <p>Mix your encrypted file exactly once. <em>What is the sum of the three numbers that form the grove coordinates?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''-5901
-7708
678
-2850
-5950
6948
-1831
-8497
-5624
-5511
-9065
7906
9614
9115
9936
-461
153
3041
-4184
-3106
1541
-2141
-8114
-9869
-8052
492
-4161
-6779
-3912
-8279
-2772
-6401
8938
-4438
-850
-3408
4159
7928
6629
-9397
32
-9652
5803
-2920
4632
1628
6637
144
-8252
9807
-9228
7880
9916
-2761
-9355
-205
-7891
-9753
-6802
4921
-9588
528
-8118
4921
8622
-6445
5571
-7384
-321
-85
-5370
-2001
6294
-4611
4861
3194
-2826
4303
5697
2549
-609
8170
6459
-1042
-7130
-3530
5399
-3040
4421
-7592
-8421
-6001
-2486
3264
11
4318
24
-6462
-7486
-2854
8364
3594
9425
-9899
-722
8987
-5100
-9081
-6948
7933
7799
4769
1169
7640
9464
-5476
1263
-6016
3026
652
-2773
3554
4999
-2825
-7284
-8926
2380
2639
-8352
-6215
8777
9042
6648
-8326
3941
-7736
2521
-8685
8242
5287
-7975
-3369
6437
-8031
3394
-4299
-8470
4975
-3167
-1061
-6982
-9351
392
-134
7092
-6686
7587
5939
-6479
-3970
5629
4931
1574
3875
1858
4855
-7985
4964
8846
-9716
-9933
-5665
-4769
-2658
-8446
-4114
7700
632
5793
-917
6898
-7310
8465
771
3609
8257
-1010
8914
4363
-4978
-6855
5597
-1795
9450
6113
6340
-9927
9843
8311
7146
-9416
9288
2254
6855
7147
-9539
9645
-9330
5399
6304
-1516
-3039
7666
-2913
7095
-1935
-5668
-1491
-8995
-5394
-2398
-7611
6737
-9007
4889
-9523
-8733
6132
-4043
-8857
549
6273
335
9468
-8475
4260
-8624
-7936
9128
1362
-1082
-4733
-455
-4726
2764
-944
-7685
-1142
2574
1100
-472
-2640
-4561
2062
4033
-1808
7060
4515
-6476
-6804
-8512
-4024
4068
6973
2318
7323
4989
-3894
5783
-2630
9346
1824
-2721
4840
-3359
-6297
-8461
8770
-138
-6433
7054
-2224
9550
1556
-4086
-3332
-2524
9521
-6152
7649
-2171
-8208
6492
1299
-6256
8915
5162
5436
-1495
-1973
-2001
1850
9987
-2085
5786
-5540
-6509
-3620
-3581
7530
201
-45
6636
-2408
-5600
3059
4624
-123
1100
-1230
8848
-3421
-8574
-3680
8268
9556
8106
5236
-9997
4508
1004
-9853
6540
1885
-5585
-2524
765
-1908
-6859
-6632
-7787
4093
464
8855
7464
-2499
-1824
-7052
-6880
-1037
-5539
-7914
-7613
4012
-8411
3461
-9767
-3965
-8816
-1568
6480
7786
921
1755
-3651
-2771
-3472
2417
817
7291
-6894
-833
-7022
6469
1203
4785
-6860
2122
2192
-402
1033
8495
-8339
-8816
-2522
8832
-1433
-5238
-6286
3999
-2678
-5246
-6810
-2218
7695
8676
-3616
-3980
-1006
2066
9046
-2110
1224
8753
6338
483
6893
6674
5573
9902
-8347
8957
-4583
-8993
2680
-1845
-84
-3745
-2550
877
-3138
1402
-3443
1815
1911
-2417
3977
-4672
-8093
-1965
884
1770
1823
-6254
-2378
3334
-5839
-6099
9046
6514
-6381
-3091
8457
-7125
-3543
549
6389
-1896
9410
-9853
-1389
-1762
2099
174
-9881
9221
-7035
6375
-5251
-4013
-596
1504
-923
8170
-6000
-5876
7019
-2098
6602
-8819
-405
-8964
-4848
-5633
1591
-7117
-7292
-9966
4159
7731
-8452
-7807
-7056
-8202
-3648
-7744
4363
-2275
6797
9565
4470
1377
2294
-2703
-7056
7278
8607
4256
-9350
892
3226
3275
-7819
6262
6884
-3137
9049
2507
8835
-4374
-5136
3702
4761
-9629
-4085
1440
-6004
1926
1602
5249
-1379
-1288
-4217
-8840
1718
8642
-5628
-8545
-6506
-7775
1604
9699
8491
-218
6855
1082
-9935
-7601
-4230
8727
6279
-3374
-7278
146
-8245
4995
2324
-6040
-9551
7429
9042
1126
5426
8702
-6494
-9457
4908
9109
3124
7375
1345
-178
-7708
-7519
-6476
9653
5481
-3323
-9165
-7289
-6284
9243
2515
-7601
-4413
1239
3637
-1252
3989
4939
6454
-4201
4747
-3337
-1951
-7275
2795
6455
-296
2574
-491
-6345
-6794
-1415
4019
1173
-5337
-9366
-3003
-6638
7781
-3261
-3438
3222
-729
3991
8959
263
-1896
4294
2591
9530
-3059
-9922
-9652
7356
1253
-2171
-265
4391
-1372
-9488
-9457
-4004
245
-5596
256
9925
8866
-7404
-8543
2388
-5814
-758
4954
9094
2991
5042
-6969
-8267
6547
-3537
7589
4173
6053
75
8313
-5289
7986
-2192
-3941
4954
9882
7436
-7060
-8749
-6852
6669
8618
9150
-4357
-5816
372
-6563
-3408
-3279
9530
1017
7755
-6850
9374
-5289
-134
4871
4179
3434
-4055
-5056
-7502
4627
-2954
7474
-2061
1185
-4249
97
-4345
9700
-8216
-7213
-7211
516
6726
-8017
-1984
-2606
8148
3566
8684
-7853
-3723
-1368
347
-8709
-2024
-5251
3483
-2650
-4002
-2606
-4912
-6915
3320
585
-7708
6409
-5380
-1729
-6001
7978
6644
5317
303
-8639
-1973
8875
8734
-9404
101
-1356
659
-6127
1908
-5006
2947
-8375
8831
2911
-3810
-260
-3166
5412
679
-944
4212
1352
8064
8517
4259
5709
-4230
2432
-727
-7071
7561
-4421
8105
-32
9371
-2866
-5931
7270
-3876
-1573
7525
4740
-6014
7968
6144
7062
-2175
5434
-740
-8679
9211
4830
-5537
-209
9058
-6358
-4495
1057
3110
-7494
-6653
-7683
8561
-920
5532
-7650
7608
-5384
-3066
7300
4218
5388
7466
1925
3550
3351
1201
-8306
7093
9867
438
9996
1834
6988
-2341
3335
9391
-8755
4372
2348
-1897
9684
-8351
2970
7019
646
-2587
2138
-2417
7951
-8462
5697
-9900
-3581
-225
-4566
-4844
-8964
-4673
1773
2217
7202
-4602
8014
-8092
-8267
-3840
4067
7399
4999
-3405
7237
-1273
-5456
9450
7027
-5680
-8190
6345
-5773
-300
238
8491
260
4634
9182
-806
-4790
-895
8491
-6943
-8608
2833
-9196
-4858
8174
-159
-6749
461
4981
5416
345
-5418
6746
8155
6224
-4586
4485
-4490
-4560
-4666
2767
-4783
-6103
3047
-6307
5811
-1763
579
-3848
-3063
4632
5930
2077
5222
-479
2457
6225
-5380
-6802
1998
201
9824
5821
7160
5117
-6686
969
-4379
-1092
1717
3098
1179
6743
-4415
8612
-1004
-6980
8671
-178
-7509
2513
285
6384
-9098
3251
-3652
914
-5081
-5269
-9529
315
4843
396
-1221
-8317
6352
6333
7370
-5523
-4202
7479
9469
6254
1121
-433
-1762
613
-7838
3835
-3810
48
7554
-168
-8895
6627
-4934
-7239
4164
-3219
598
4631
-329
-2381
8767
1605
3593
8201
-2979
-7057
8895
-8652
7575
-6030
5273
-7209
-7560
4489
9144
9579
-2711
-3923
3902
2524
-4769
678
5996
5071
5575
-4747
-5910
6356
516
-5955
-46
8561
-1874
5345
2435
-1536
9236
-4063
258
-8277
-6554
7700
-6861
-8250
1061
-3767
5733
-1063
8807
-9784
-9527
4455
-4560
4670
-4189
4670
-444
-5895
-9779
5418
-1202
8006
-8601
-4417
-6539
-605
7256
-6734
-5901
365
6968
-2158
8148
-6854
762
1092
4666
2718
4286
-4055
3488
-695
7440
5239
149
-4519
1926
-669
-5152
-3755
5478
7654
-2182
-7310
4949
-7914
4901
-4701
6985
3670
-1875
-9861
4818
2211
-6973
676
9325
-5474
-795
-2158
-2502
-9050
1057
8279
-1780
-1257
9930
-6956
-2034
-7393
7913
1207
2254
182
-5910
-7380
4048
-1923
-9908
4632
-7458
8492
-4848
6341
-9618
-5759
-9708
7627
-1769
629
-32
-5614
-2938
8528
7259
1010
-5938
1314
-9660
-6357
-3230
-7580
-2761
-9462
6432
5377
8313
3401
4537
7764
2046
-3016
-3530
3226
3503
-4560
2385
1192
9013
-3167
-9474
-2085
5662
-513
284
-3147
-820
7105
2482
6267
-8227
8124
5752
2507
743
-9972
-6188
-9418
9386
5403
3730
1364
-3379
-6202
-5954
-8803
-1877
-4360
-5754
-8090
-2542
8656
1621
-5628
-6910
3780
-1845
1186
6296
-5671
9888
-390
7820
-5767
2709
1608
-1656
1267
-183
-218
-3471
8474
4931
2492
-6657
8492
-3342
6363
-2954
4559
7382
99
1823
-6491
-2254
4563
4508
-554
-1039
7615
-5585
8051
-7471
-2025
-2659
-3800
-3763
5573
263
-9422
-7217
-8639
1683
8147
-9503
6539
2641
-8892
9520
892
4880
-46
7095
535
1558
3761
7781
4238
9109
-7547
-5226
-5692
-2205
2585
5253
-1874
1103
-1058
-1351
2767
4566
-7034
-177
9303
-4690
5739
4666
-1050
-6856
-5550
-9069
7794
8957
-5996
3046
6781
6544
5545
-3145
6604
8442
1738
-4963
-9925
-3299
-7721
926
-5550
-9354
-2944
644
-1210
2899
9374
3640
-7073
-1222
-9714
9860
-2938
-3266
8978
8475
480
-1546
-4288
741
-8243
2585
9022
8619
-1499
7632
4736
-1226
-1893
-2341
3553
-7137
-8740
582
7126
4142
-6006
-8211
9069
7764
-2185
1294
-6872
4769
1280
2716
745
1224
7824
2524
6454
-4803
6296
8553
-8487
1281
7231
-6415
7946
8561
-8734
8778
-6416
-3336
-698
-3606
-2202
-6919
-3328
-1096
-668
8383
4401
3786
2272
6932
6424
-9493
2873
-2827
8580
3394
-3979
-6885
412
1569
8988
-1190
-5706
-1657
-2909
-1024
309
-4389
-8083
-2773
-9139
295
748
1369
-899
-7071
8915
-7861
1462
750
-8093
-7367
9950
1574
7339
5254
1064
-8997
-250
8363
5616
6033
2261
7276
-5193
-80
-3619
-5337
3517
-1218
-5055
-2275
7806
-7494
-3284
5526
-4299
6501
-6426
-2535
-4035
4752
-9353
-8969
-802
501
4211
3172
4149
-6547
-9531
-6948
-1695
-4396
3356
9883
618
-7320
9061
-5063
-7839
9862
-438
5305
4791
-5168
-772
6038
-5646
-6686
4280
5917
-9536
-1504
-3089
6113
-4009
7928
1315
-3742
-6043
2482
-4547
1926
1230
4276
6075
-3537
-7130
2343
3041
-1943
-6854
3428
-2275
303
-7484
-1832
8698
9677
-3713
-4254
9192
1407
-1544
7210
-4858
-3263
3811
-6566
-9714
2601
7744
4842
-423
8975
5388
-3614
-3248
-6576
1211
-7177
3108
1056
-9069
2080
7875
8490
-1719
-111
1946
1040
-7582
114
6247
-1024
-5895
1377
-1891
-5168
-9069
3352
-8044
9144
-6052
2849
9925
3172
4932
762
7968
-4762
-8458
-974
7049
-7980
-8816
7089
-8886
644
-3818
-1732
8219
3594
6341
671
-6112
-3613
6126
4245
1499
3852
-2134
2145
-352
-2626
-2175
2274
8482
-5986
8687
-1929
6462
-8701
4531
8228
-323
3361
-3688
-2039
4390
8806
1824
467
-4341
-6386
-4636
-2395
2689
-9708
7242
9468
-8227
-3761
1149
-5228
9022
-9377
7722
-7683
-2837
4243
-1210
5186
-48
-5859
5222
2884
3966
-6506
-1273
-5725
7504
4925
3717
-7936
-352
8961
5503
6460
-6208
948
5912
-7344
3055
-4560
-2284
3279
5279
7834
78
3251
-3856
-1892
-6779
652
-6832
1179
-6455
1146
-9450
-6181
5218
8772
8077
4390
-2144
283
7313
8174
-8164
2425
6991
-1152
-2290
7520
-8458
6586
1923
-8031
-1191
6880
5400
-2395
-5773
7523
-6664
-7267
-2916
1243
9653
-9902
5786
6964
8758
-1792
4806
7715
4690
7555
727
-8806
2997
-8211
-7366
7313
5713
8744
676
-2778
9983
2534
9653
-3091
483
-2385
1301
3911
-3439
-8315
-4857
-592
-8057
6212
3284
5215
2077
7633
-2192
1169
-407
-3711
111
-5658
-1491
7420
-2389
7940
-3165
-6785
687
-8497
-9933
-3040
-178
-3779
-8876
-7388
-5692
-4348
-8099
-6682
-6358
5189
655
3947
-7402
6158
7382
1216
3186
5122
-6888
2752
7389
-121
-78
3881
2577
-6080
-1176
6638
366
-3446
-794
9644
-3001
-2019
1392
6309
3029
6588
4515
-2581
-7623
-4904
3182
-4175
2016
6628
-8352
-1491
31
5479
-7914
3116
-4053
8232
6276
-5758
-4245
9526
-2085
-8502
-9642
-5868
-1686
-9924
4635
-3397
-1969
-9258
-9877
-1932
5045
-1729
7810
8223
5889
-1090
-9098
-5455
-7764
9773
7452
2516
-4201
-5525
5752
-6943
4747
3184
5901
-8286
-9790
-2837
6053
6309
-7828
-695
1216
6361
-7073
4930
3104
-3742
5403
7092
-9354
8439
-4114
-9253
2908
-7933
4769
-7693
2007
-6287
1110
-2997
8936
8956
-5683
9445
2877
6583
-8473
3422
-9922
-9592
-2988
-6599
-8462
3180
-9980
-5606
9469
9367
3993
682
-727
3142
1284
9447
-3771
-1656
-1727
-6287
5564
9949
3759
9109
-8840
-6948
3427
-9776
-9462
5948
3281
3525
5385
5682
4861
-2841
8506
8389
-2862
-8286
3041
6839
4054
34
3639
-2262
8965
5109
5605
-5512
921
-1935
3937
-175
4259
7518
9325
5189
-7796
5197
-1246
460
-4036
-8675
-2260
8545
9332
9709
-7679
3360
7413
3550
4613
6251
-5092
-1289
-390
-8114
9475
7954
-7250
1067
1402
-8169
-9700
978
-2640
-5025
-1594
4060
-6111
-8762
9127
-8458
-8057
9425
-4923
3484
3337
7721
-2683
-6045
-8886
1753
-5554
356
-6748
1558
9001
9645
-3056
-5337
6290
8956
7615
-9493
1255
-1523
6130
563
1349
3853
6954
-8999
2449
8866
-5816
-2208
-8406
-4822
9888
-8093
3279
2513
-7543
626
4783
-2954
1804
-6932
309
7763
-3165
9451
-2843
3172
-8964
-4333
-6940
8404
-7641
-2384
-4606
-5714
4519
9142
-5825
1098
9862
1255
8988
-6433
-8125
7676
-8154
3522
-7308
8536
-4397
-7052
2732
-167
4494
-790
7095
8492
8196
-9396
-821
6247
596
-733
-5107
-9430
-8059
8263
-1557
8976
6603
4159
-590
989
-4679
5615
-2683
2318
-8267
-590
-4401
-3498
-2827
5110
8976
5082
5041
-9997
874
2331
-5967
-4728
5254
-596
-8420
9290
-5348
-8058
9128
-8299
-2392
6343
9802
5704
-2667
-6800
-4173
-5423
-6080
-2107
88
-9214
-8716
-6263
5705
-6287
-7399
-9052
-6022
-8373
-1195
5376
-539
-7196
-7657
-2790
8148
-8368
1458
4949
-4156
1126
1284
6671
-1050
-5127
4741
-3084
-1023
-3613
4965
5949
-6787
-47
-4175
-5837
-4029
-6469
-7823
2826
-3359
7474
8193
2968
1650
2492
3172
-4360
7425
991
6855
262
5248
-2429
-7872
3178
3743
-1184
3456
4619
7991
-3026
2051
6583
-4100
5767
-6215
9100
-5348
-6548
7539
-6932
3366
-6867
-8303
-1042
-87
-1018
-3484
-1973
-5910
2003
7834
7749
-9383
-480
2228
6612
-5819
8727
6792
6103
-1379
-2441
-32
4313
6877
948
-7559
-253
204
-604
-358
7205
4113
7906
5189
7146
-4248
8907
-1614
-8125
-5532
1976
2658
-766
-8964
3869
8256
-1230
-7936
-7868
351
-6416
-2085
8833
8332
6147
9333
-772
3805
-7764
-5632
5204
-5671
-1249
-6624
1877
11
-6742
6496
967
6607
-5695
-8683
4940
-5625
1305
2889
-7580
-3443
6612
-9370
7552
-6859
2077
-9935
2452
7912
8674
-6147
1345
-1281
6365
4465
-7732
1153
-3593
-9309
9581
-3529
8117
372
1439
-1744
-4268
-2909
5260
201
5608
5404
7151
8340
-3824
9596
6586
1031
-8819
-8809
2820
2208
-5895
-1849
8565
2635
4000
8502
6136
9400
1349
4741
-2812
-1897
-3991
4508
4503
3745
7845
9860
-2425
-3236
4870
2708
2014
-5251
-8345
-1929
-6329
6502
8390
676
-5814
-8044
-9623
-4188
7014
1324
7138
-1832
-9383
-9980
7991
-6914
4902
-3827
-3753
-5168
4944
-9698
8649
-9876
-1426
3807
1825
-7445
3465
-3824
8760
-1388
2806
-7116
-4444
-6503
-6043
6258
4146
2279
8238
-7074
5532
7587
-4495
-4210
4968
7000
2618
-8297
8522
6444
8005
-7430
-7104
773
-8546
5672
-7125
-7553
5200
-6914
771
8988
-918
-4494
-3451
-8104
9332
-2123
-5067
8942
-8487
-7310
4921
-6726
8093
2853
2228
4945
2916
3401
-9221
9461
1395
8000
6566
-3065
-1252
6627
-3248
7834
-4739
7842
-6982
-4606
-4210
2046
-191
3898
-6210
468
8439
-4692
-4173
1016
-7839
-4212
-1165
6251
9172
-5366
-6498
6113
6746
-721
-8318
306
-2533
8612
-3147
6462
4605
-5206
892
9303
-4255
7798
-4036
-9309
-4619
-3114
-188
-9182
9923
7123
2668
-3146
1203
-4357
-3239
1440
6059
4511
-8395
-4170
-4600
8333
315
9464
-8458
6872
-7211
-8034
-8205
-5229
-6281
6007
5706
-9511
-3775
-9965
-4183
7057
-9624
4318
-391
3713
-1729
3706
4211
7784
-3471
1149
2453
-985
-3599
4810
-2064
-134
5597
7055
8642
9447
-3669
6247
-6616
8966
9517
-6530
8265
-6452
1593
5492
-7993
1911
8100
3205
-5619
-3818
-6634
-2232
-5803
-7143
-3980
-9922
-1004
5611
-5700
6190
-9908
1104
-7004
2446
4435
-5296
-2855
-7685
7261
-6726
-7038
6340
6895
-3410
1757
-8892
9475
-7960
6549
2880
-5012
-9186
4556
1517
-1543
-8321
2067
6246
-7057
7241
-7239
2254
7049
6491
-6810
8655
3890
-5193
-6004
671
-8800
2729
-7272
-7548
-9587
9626
-3872
-4054
-5539
-3147
-1634
-2293
-6069
55
3866
-111
-1027
8410
-8912
-9396
-84
-3248
2919
9761
5995
-3106
8637
-8243
3247
1402
4290
-7358
-4184
1649
2964
5697
878
7197
-9456
5936
5189
8430
-5489
8612
-5935
-5793
1087
2981
-7839
-1878
6859
-4982
-7189
7968
-1081
5198
4954
9551
4840
-5413
1673
9615
1345
8093
-9917
-2100
-5251
4931
-4948
-9054
-1664
-1092
-1967
-6647
8380
-6496
-3359
-2202
9581
-3235
-2915
6948
5841
-8545
93
-9391
-8753
2144
-2332
5777
9252
-281
9343
-4996
8423
8543
-7917
-1125
6476
-6034
-6416
-7422
-30
-2376
7734
7428
-4265
1556
9546
771
-1165
-5025
-283
-5866
759
-5268
7035
-302
5492
-5486
2455
-976
8423
-4894
-1598
364
-199
4927
6220
9288
9855
-4635
990
-1572
-4376
-2944
3673
1455
-2639
-3716
-5155
-3267
5102
8744
5588
8977
-6701
-642
257
-5885
-4172
-4908
-2332
-7807
4232
-7208
2880
-8240
950
-2524
-1435
4297
9452
9800
-9354
9519
-9593
-7300
-1634
-71
-1568
4831
2430
9138
2668
-7494
2975
7517
-5876
3139
3131
-2384
-7984
3413
-5767
-7785
-292
-944
1203
9436
4821
5673
4422
2211
9170
8106
3264
6289
3421
2790
7093
-6900
-2550
-1892
35
-4790
-7048
5923
-6867
3312
8094
6437
9247
9042
2452
-8656
-6940
-5368
1033
2324
-4173
5608
7151
-6779
-3321
4720
396
1804
-7708
9949
1700
-1681
4259
8832
7783
8000
-5432
4842
7342
-185
-3424
-5525
2718
9608
4670
3475
-2916
-2185
6013
2630
7625
7824
-5755
-8691
-5574
6860
1528
3046
-4359
396
4515
2062
1087
5376
-5773
-1965
3031
-3239
-1693
7496
3328
4865
6374
5992
8612
-5455
5540
-8190
-5439
-755
-3474
-7517
2858
-7285
-9899
-6319
-8888
-2944
-4162
5853
9170
-3982
-1992
-5472
-4173
8174
3640
-3963
1582
8492
3220
4391
-707
5556
1786
-883
-2244
-2075
-4207
1814
7096
1750
-7380
-1301
3708
6114
3753
6025
7500
-5614
-6804
5479
3638
-6729
1239
6653
-2384
-8304
4968
-7405
-6286
8385
-5017
-9931
5004
9168
6947
2330
-3947
3581
3753
-3429
9046
2315
-657
9306
-6032
2279
-1150
1217
-1521
-5618
7060
3241
6863
5556
9061
-2478
-7395
3358
7930
-2971
2846
-6834
4634
-339
-3590
2794
-8089
-4162
6701
9674
142
6247
8368
2059
9677
4791
9203
-8193
-8147
449
7035
-2374
1349
9654
-3337
4465
7764
9282
-8296
5655
1296
-2155
9517
-2698
-8394
-273
7003
-7988
2907
-6057
6737
-3374
1823
-5019
6375
5146
-2814
-911
-1182
-8809
2997
5573
-8261
-4592
3770
5922
-2630
1261
-5368
3615
6737
-7370
4747
7915
-3130
5407
-8886
-382
-3667
-5683
-9362
7944
-2610
4008
7170
3550
-1747
-4514
-8206
3098
-1195
-7267
-1891
5247
3640
6656
3772
-3114
-6624
-8185
4093
8148
-930
-3998
6489
2580
7978
-6244
1523
6276
3072
501
-362
8501
-9784
5952
-2542
5306
7577
-3121
5404
-1835
9345
-2655
-8115
6909
-461
-2366
-6988
4954
8100
-7908
8667
-8897
-7482
5522
5527
-2370
-2021
909
-1523
-4317
1179
-7679
7375
-2463
1834
8580
-387
7108
7355
-4527
5786
1683
-3471
1850
-1891
-5421
1217
2795
-4377
2276
-895
7525
-8631
7008
-1911
-278
-1533
4811
-3882
-6856
8481
6760
4466
-3894
5758
-9931
-7208
-9559
-3424
5365
-5789
676
-3448
-5325
4449
-9052
5462
9019
-1608
-806
4822
7333
4720
4066
260
-6099
-8941
1048
-3898
3175
-4954
-7217
-9714
-652
8928
3055
-8720
3558
-7696
6815
99
-2156
-2478
-954
-517
454
-6284
-2205
3779
-9513
1823
6832
2046
6025
8988
-3371
-5931
3873
-1211
1149
4797
-9527
-3279
5459
-1135
4634
-5665
7940
745
5193
3596
9469
731
-8945
-4754
-8226
-2232
-9877
7298
6627
-6882
-7774
-7806
7615
7699
5885
5895
5494
-3858
9888
-8286
9435
5248
2911
-6649
812
-1597
3131
899
2145
6931
1074
9761
4205
-2010
267
-7212
3553
1386
5015
393
4465
-405
-7861
-4599
2055
-8525
3320
4030
-1598
7824
261
-452
-3641
-8537
-3439
4710
-6186
-5816
-6248
4769
9591
-7856
6643
-6940
3267
769
2668
-3838
4404
-2505
-4361
753
-1238
-1593
-7523
8593
24
5055
6893
7358
7358
7876
4693
5963
2865
362
5292
-3932
6279
-1182
6725
6985
9371
-2122
869
6514
8630
2870
-4159
-2141
-5396
5228
1548
-7960
-3459
7968
3522
6190
-1149
-4666
-8738
-1040
5758
-13
-8800
4785
-2107
7817
-7685
-2899
671
2728
4964
4968
-6491
-2843
885
9221
7196
-3236
1365
-7301
-5127
4071
-9418
9183
-372
1372
-1151
8748
-2225
-8013
2598
7272
7824
488
-2977
-1957
-7032
4710
-3610
-6321
678
-197
7545
-3568
9324
-5444
-2262
3337
4575
9069
-1064
-9054
-9457
4404
1554
5196
5202
2766
915
-9922
-4904
5168
338
1449
9699
-6216
-9715
8938
-8729
1854
626
309
1828
3153
-6152
441
-1441
-6814
-4632
-790
-9599
5813
8238
-3521
-5214
-9536
-6814
1016
8493
3691
3902
-803
98
2165
-1193
-1828
-1195
4519
-2055
-4143
1770
7235
5380
-2025
9022
4471
-3539
4725
1058
-9908
1712
-6337
-3321
-8317
-3567
-8407
-8348
8900
-1879
2090
8105
3483
-1456
-467
-5758
-8244
7624
7032
-9040
5196
4927
-944
-3938
4975
-7980
-3428
-4609
-3011
-923
-5269
-6127
3176
4523
258
-642
-2460
2717
-6990
-3195
-6425
6469
-7872
8092
-6437
5324
-3161
-4004
-8424
799
8789
-7713
3172
-1541
-637
-3265
1161
378
-609
-5554
-695
-1634
-4388
7444
-8506
-835
2156
5189
-6437
6257
9920
-9876
1224
-2509
-6077
1922
-1681
5811
-9430
3459
-8155
-4415
3691
2254
-2202
-3382
-2542
-2571
4794
1801
6586
4169
-474
1871
6985
-5268
6061
4640
-2778
-1430
-2016
-6616
5254
-6219
2087
-8431
9069
4008
1281
821
-4596
4741
2276
-9997
-5211
1318
-2685
969
-5328
626
1765
-5650
9714
-9270
9985
8210
8684
-2127
9333
3166
1114
-539
5069
-764
6005
6829
-8590
681
6583
3759
8310
7986
3780
7360
2077
-1919
-196
4956
-9253
2986
-226
6212
-1507
-7474
6168
6843
-8539
-4336
-3108
-8553
-806
-3537
1104
4966
-4857
1542
-7780
-6734
9879
4159
-1343
6992
7759
3282
-8475
-3574
-5155
-3779
-2675
1903
1176
-6913
5207
-372
8796
-7030
4632
-3752
43
-3524
-474
2789
-4514
3180
3433
-9853
8187
-1923
6182
3376
-9354
-178
-1372
-6045
-6578
258
9763
6341
1440
-6616
83
-832
6035
8389
2841
-3399
-8916
-6664
-4002
-5699
-8261
7272
8006
8167
9243
-8311
4404
-6496
8021
441
-2747
1656
8097
1428
-433
-735
8777
8633
-6253
-6409
8288
-3263
-6097
-1598
9930
-6235
9122
7013
-2171
-2258
-110
-4824
-6104
7315
8033
-2207
2709
-8894
2922
5090
8491
1177
-4119
6729
7175
2961
4511
-4494
-7552
-2208
3380
3747
6715
-3753
-2778
-787
322
-5152
-6040
-7975
9236
-7224
-6717
-5456
1466
-8216
-9995
-4781
6134
-8496
-846
-2728
-5155
5786
-5100
-923
1144
579
412
-3669
-1729
7545
4378
2080
3204
-5885
-6254
7139
-4835
8184
-8826
3428
1824
-5203
8976
1984
-7787
5132
-3844
-8155
-9531
-5619
-5238
-3239
5280
-7079
4339
-5273
6837
-698
-1364
-2235
7274
5408
9352
-5109
-461
-6440
8705
1191
6018
7155
-9761
3767
-5050
-3405
-2876
-7780
7517
-8375
6529
-7030
-2614
6340
4316
-9475
7265
-2812
-9536
1179
-5626
-4335
7500
-8747
-8661
4748
-4599
7345
-3036
-695
-9551
-9253
-9168
8938
-7494
4745
-2055
8232
-1288
2499
-1426
-920
-5559
9469
8878
8501
-2899
908
7589
-7942
-6929
-7922
-719
9447
-3379
-6188
-1591
4699
-7300
9338
307
6583
4855
0
838
4012
5869
1507
-6173
-3161
-7625
9875
8766
7593
380
9400
153
-4319
-785
-2312
6339
8738
2406
-3871
9919
-621
-1676
-8088
-8254
-7220
4325
-2981
-366
-7370
1958
-2156
-8710
-9927
-2397
-9063
-6855
1823
-6355
2956
4703
8536
-5996
7979
5803
7633
-7510
338
-2708
-3405
-6867
-7290
-8564
-548
-6415
-5859
-4421
-9430
9316
5005
-9061
-1114
-6264
8727
-8553
-7045
5552
-4690
-6216
9286
7845
3780
436
1346
-7486
7004
-6535
5015
-7177
-572
7273
-2566
7385
4989
3935
-684
4931
8014
-9864
-4801
9497
6288
-5117
-4843
-1222
-739
4358
3312
-1835
-7352
9400
-766
-5104
-8451
-5100
9522
9803
-5370
-390
-1602
7364
-7948
-3991
-5095
1057
345
-3587
6859
-2542
2630
-1474
-9133
4981
-8744
36
908
-2387
4164
-8157
7254
1317
-6972
-2182
-617
-8557
-7276
-6966
6931
-5238
7820
4631
-7143
-258
4613
-4003
2165
1677
4745
-8949
5222
2120
-5773
-5665
-4415
-30
-1388
-6699
2637
7320
9075
2152
-7868
-2550
-8540
-8921
821
9286
4412
-9593
-5587
2347
4426
7750
-6861
-7563
7155
-7910
-4730
8379
-6814
-1438
-1309
3875
-3488
7014
-798
1920
1423
4730
-276
-3241
-6814
-9480
2997
-5639
-5483
9810
-4681
-1708
2368
-8661
7110
-8735
9099
11
-1214
7428
-9683
-1699
-7557
2443
1650
-7290
6313
1093
-8487
969
-3958
-8615
-3722
6893
-5825
3837
1656
1540
-2524
93
-7489
-905
3946
8653
8831
8868
-9539
-6749
-4590
6117
4573
7491
-5868
-5489
6477
-9002
7231
-2258
6309
-2471
2651
-1819
219
203
7256
2852
-9052
5107
6825
-4032
7127
-6562
7122
8238
-7984
-4619
5965
3747
2352
6315
-8118
6529
8959
9155
9525
-9403
-6476
-5396
1075
-1376
4559
-2771
-4305
904
-8205
-9738
-4972
7940
4263
-8816
9514
-5120
-1762
-1811
7583
545
6751
-5262
4763
-6287
-1852
1060
9557
-767
6921
2543
8979
7055
9594
6404
-9779
3595
6160
8305
-2422
3835
-6055
5883
7903
-4769
8618
-8981
-6776
-2773
-8376
-2837
2149
8653
-2436
-405
6447
-7293
8905
7719
-5337
-1807
-7250
-4771
-7769
-9357
-4200
7377
5704
-6896
3533
-7891
-3801
-300
-290
6541
4602
4968
-3066
-8029
-7568
2194
-944
1396
-1692
2880
8009
8186
-4170
6788
4668
8407
2105
1386
-1474
-6948
-6402
-8173
8541
-2185
-3634
9298
7202
-4963
2184
4166
-3677
-1923
-4869
-8543
-1897
-8032
9517
5805
-9931
-7853
4784
-1669
-8407
1464
3320
-1744
-7861
-5957
-3265
-1309
7181
2833
-766
5653
247
6942
7191
6743
5456
-4981
6265
-8539
-1758
-8981
9049
9921
1355
1604
-8945
-6337
7477
-2625
-8462
-6366
5491
8471
917
5340
3501
9951
-7723
4715
8443
-5446
1136
-1626
-9990
-8451
9711
2062
-7315
3935
2557
-8720
4598
-9045
-5537
2767
-2644
6502
-4002
-8504
7940
-3752
-2693
-3529
-822
-205
-8803
6028
2783
-9737
3413
8133
2682
7345
9236
7398
-5910
4061
-6983
2575
-7160
5713
8879
4767
5597
-5938
8781
-3742
-6167
-2290
-9767
1851
8210
2473
-1682
-9798
-5380
8228
-4635
-5909
8724
-4356
9158
-5784
-1747
4259
9013
8619
4012
7290
-2085
4889
-3464
4640
-3006
-3195
5632
-9309
-3471
-9128
24
9515
-877
1669
-4833
-5348
-2518
9410
-717
9949
-3872
6068
-9362
-8764
-7284
-3368
3663
-5509
9005
9980
-8964
-5134
-9965
-9317
4355
-7316
8536
1736
4124
-3106
3624
-8755
-7764
-6099
-5675
-2088
-6971
2323
6507
-7819
-2634
-8348
-199
-7708
-3371
811
911
745
-8076
-1587
-7923
-3535
-1796
8870
2830
-2169
-3281
-5607
-358
1712
-9230
6507
9638
-7797
-4981
-917
5098
6035
8253
1559
927
-9457
-3860
7345
5090
-657
3284
4949
1595
5957
-2121
-3069
4970
-3844
-7412
6970
6126
-7690
-2848
7472
5901
-1598
4068
9005
-3871
8148
7842
-7403
8783
2066
-1840
-163
-9098
-8347
-8232
-8997
-6034
8272
-1937
-6429
-5220
-8832
5483
1355
-9660
-1504
1858
-3716
-8407
8947
8471
-6664
-1366
-5086
9821
-568
-5825
7666
2365
-1290
-2526
-3718
6340
-513
-7310
1389
-8857
-3844
8821
8251
-8155
7967
-9602
6348
1540
8640
-1147
-9662
-4162
-5473
-2997
-6651
-1970
-3844
-5789
950
67
7814
967
6893
-3264
5411
-7309
-7894
-4548
2856
-5166
-8374
4256
7785
8774
258
-9548
7170
95
-5241
-452
-6579
3543
6874
-952
-3837
7282
3970
-7285
-4529
-6867
-1207
296
-4004
8389
4083
4931
-8039
4470
-7988
1886
7464
9809
-5030
-3279
-3297
-8647
8343
-3704
-5646
2797
9821
-7079
-2535
5713
6725
-474
3323
-250
9444
-8006
-6030
-2222
-5957
-4905
-1608
-3661
-1273
1220
5258
3323
-6733
-4274
-5633
-6923
-5628
-7267
4238
3708
9370
9061
-2332
8308
-5481
-2461
8077
9554
-2915
-2509
5978
-8093
-9660
1654
-53
6310
-1811
7096
3691
-3404
-6915
-5692
1749
448
-1212
4755
-12
-6943
9377
7986
1928
5277
-180
-7311
-2378
-4893
6735
-8722
-5238
5247
-5055
5388
-7272
-2634
-9554
1460
-4162
8728
5855
133
-9655
-2667
7845
-2851
-3174
-2395
-3949
6607
-3836
384
-4728
2398
6828
-1513
-5758
-4228
5662
-3642
3503
-5585
8805
-833
2324
-7489
-8352
1582
7824
-2263
-7987
-1010
9380
6447
-6476
246
3178
-3640
2739
7731
319
9098
9832
5759
-1357
9821
1057
-5350
-2721
6579
719
3999
7752
1726
-7547
-221
3320
6897
-4812
2599
-2081
-4587
7074
8788
-8693
-9019
-6787
5288
-6512
2313
5812
6653
8213
-8247
-6715
-5571
-1174
2795
805
7676
-3078
-7038
-5503
4451
-3294
-5835
-5191
2288
-1149
358
7799
8216
2452
5722
-7723
4834
6839
7986
5069
1873
3301
7721
5670
-7519
5053
-8185
-9558
5532
-952
987
-513
-3406
8857
6690
6735
-5680
-5168
279
-2758
4801
-9383
4968
1795
-7311
-8964
-564
8956
-8173
-6034
-2812
3037
-8439
9040
3371
3444
6193
-7272
1926
8653
-1896
-9160
7871
-1190
-554
2041
-3422
-7143
-5778
-6397
5558
-9546
8287
-5289
-7861
3021
3220
1909
1997
-1252
6596
5218
5134
6462
-9050
-1386
5249
-3613
4523
6276
1725
4831
-281
7978
6996
-9853
-4692
7158
1749
2991
3320
-7641
4185
6241
-6014
-7125
-8916
1402
-2739
9720
9147
4738
-4858
-1738
960
2795
-8567
-6512
2555
-9618
-4426
-7432
2705
7681
-700
191
1726
5260
-2676
-3616
-3883
1143
-5566
654
6007
1385
2947
-4679
9410
-8153
-9318
527
2046
4129
5301
2450
-110
-273
1849
-8948
2789
6612
3083
3961
-5462
6620
7069
5553
-2379
-2254
7819
-4834
3866
1983
9124
5320
8207
252
4293
-4634
9389
129
2395
1673
-3276
-5891
4797
1233
9113
-4707
-1835
-8819
7139
-3188
-122
-3812
-1991
-7035
-8150
8013
-7038
1528
8772
-1806
-1576
8891
-7293
1652
7077
9497
4188
676
1369
-3101
-580
-1513
1083
6894
-3470
7154
7057
790
8493
284
-2230
2889
7319
2368
6528
4124
-1030
-9815
9581
2708
-921
5088
-5647
8653
1081
-4438
9698
9075
-4701
-6188
550
-5178
6972
5751
-5840
8364
4624
-7838
9831
-5625
8506
1646
6388
-3950
3737
4452
-1539
1503
-9652
-3530
-8314
4110
-8039
8170
-3321
67
-642
-6954
-568
4220
1534
5813
-7057
-639
-414
7495
-8766
-5153
-8882
6715
9869
4744
6160
8767
-7083
1907
7181
-7253
-1794
-5095
-3406
1019
-107
-5886
5189
1114
-3411
-4401
3175
1766
1804
7165
6115
-8946
9150
6592
-4665
2704
2956
-2061
-9658
-5238
7991
-2784
2119
730
8978
-2263
2446
-427
3514
9243
-2057
-2098
7721
-2524
-4288
-7876
6874
-8520
7781
7274
1192
-7910
-944
-3076
-4457
-4827
9944
-7644
-4469
-522
-4189
3713
-9558
4930
-8422
8043
9222
591
2853
7500
-9546
-3025
-1573
-2995
-4954
8724
-2077
-270
-8623
9215
-8185
7288
8000
-1937
-2222
-3241
5856
-4068
39
-6195
9300
-7489
-85
-2932
8671
892
-4202
-8731
-3335
3932
-7035
-382
-5620
7495
6821
144
4598
3226
2912'''

# COMMAND ----------

import collections

def mix(deque):
  for i in range(len(deque)):
    while deque[0][1] != i:
      deque.rotate(-1)

    num, _ = deque.popleft()
    deque.rotate(-num)
    deque.appendleft((num, i))

start_deque = collections.deque((int(num), i) for i, num in enumerate(inp.splitlines()))
deque = start_deque.copy()
mix(deque)

nums = [num for num, _ in deque]
zero_i = nums.index(0)
answer = sum(nums[(zero_i + di) % len(nums)] for di in [1000, 2000, 3000])
print(answer) # 2 seconds

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The grove coordinate values seem nonsensical. While you ponder the mysteries of Elf encryption, you suddenly remember the rest of the decryption routine you overheard back at camp.</p>
# MAGIC <p>First, you need to apply the <em>decryption key</em>, <code>811589153</code>. Multiply each number by the decryption key before you begin; this will produce the actual list of numbers to mix.</p>
# MAGIC <p>Second, you need to mix the list of numbers <em>ten times</em>. The order in which the numbers are mixed does not change during mixing; the numbers are still moved in the order they appeared in the original, pre-mixed list. (So, if -3 appears fourth in the original list of numbers to mix, -3 will be the fourth number to move during each round of mixing.)</p>
# MAGIC <p>Using the same example as above:</p>
# MAGIC <pre><code>Initial arrangement:
# MAGIC 811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612
# MAGIC 
# MAGIC After 1 round of mixing:
# MAGIC 0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153
# MAGIC 
# MAGIC After 2 rounds of mixing:
# MAGIC 0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153
# MAGIC 
# MAGIC After 3 rounds of mixing:
# MAGIC 0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459
# MAGIC 
# MAGIC After 4 rounds of mixing:
# MAGIC 0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306
# MAGIC 
# MAGIC After 5 rounds of mixing:
# MAGIC 0, 811589153, -1623178306, 1623178306, -2434767459, 3246356612, 2434767459
# MAGIC 
# MAGIC After 6 rounds of mixing:
# MAGIC 0, 811589153, -1623178306, 3246356612, -2434767459, 1623178306, 2434767459
# MAGIC 
# MAGIC After 7 rounds of mixing:
# MAGIC 0, -2434767459, 2434767459, 1623178306, -1623178306, 811589153, 3246356612
# MAGIC 
# MAGIC After 8 rounds of mixing:
# MAGIC 0, 1623178306, 3246356612, 811589153, -2434767459, 2434767459, -1623178306
# MAGIC 
# MAGIC After 9 rounds of mixing:
# MAGIC 0, 811589153, 1623178306, -2434767459, 3246356612, 2434767459, -1623178306
# MAGIC 
# MAGIC After 10 rounds of mixing:
# MAGIC 0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153
# MAGIC </code></pre>
# MAGIC <p>The grove coordinates can still be found in the same way. Here, the 1000th number after <code>0</code> is <code><em>811589153</em></code>, the 2000th is <code><em>2434767459</em></code>, and the 3000th is <code><em>-1623178306</em></code>; adding these together produces <code><em>1623178306</em></code>.</p>
# MAGIC <p>Apply the decryption key and mix your encrypted file ten times. <em>What is the sum of the three numbers that form the grove coordinates?</em></p>
# MAGIC </article>

# COMMAND ----------

deque = collections.deque((num * 811589153, i) for num, i in start_deque)
for _ in range(10):
  mix(deque)

nums = [num for num, _ in deque]
zero_i = nums.index(0)
answer = sum(nums[(zero_i + di) % len(nums)] for di in [1000, 2000, 3000])
print(answer) # 20 seconds
