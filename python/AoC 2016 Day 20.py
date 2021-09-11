# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/20

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 20: Firewall Rules ---</h2><p>You'd like to set up a small hidden computer here so you can use it to <span title="I'll create a GUI interface using Visual Basic... see if I can track an IP address.">get back into the network</span> later. However, the corporate firewall only allows communication with certain external <a href="https://en.wikipedia.org/wiki/IPv4#Addressing">IP addresses</a>.</p>
# MAGIC <p>You've retrieved the list of blocked IPs from the firewall, but the list seems to be messy and poorly maintained, and it's not clear which IPs are allowed. Also, rather than being written in <a href="https://en.wikipedia.org/wiki/Dot-decimal_notation">dot-decimal</a> notation, they are written as plain <a href="https://en.wikipedia.org/wiki/32-bit">32-bit integers</a>, which can have any value from <code>0</code> through <code>4294967295</code>, inclusive.</p>
# MAGIC <p>For example, suppose only the values <code>0</code> through <code>9</code> were valid, and that you retrieved the following blacklist:</p>
# MAGIC <pre><code>5-8
# MAGIC 0-2
# MAGIC 4-7
# MAGIC </code></pre>
# MAGIC <p>The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are <em>not</em> allowed. Then, the only IPs that this firewall allows are <code>3</code> and <code>9</code>, since those are the only numbers not in any range.</p>
# MAGIC <p>Given the list of blocked IPs you retrieved from the firewall (your puzzle input), <em>what is the lowest-valued IP</em> that is not blocked?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''420604416-480421096
172102328-195230700
613677102-639635955
1689844284-1724152701
3358865073-3365629764
1333423844-1344930397
2519115700-2535290065
698684483-723211151
979757052-1003200781
4165068842-4190472815
2020267004-2045214369
2979897715-3004836346
2110213890-2115506975
2970017340-2973461626
2236378365-2258142409
3423992974-3426380317
1462489107-1490036931
2189940955-2198476022
2417413696-2430182746
3624276792-3633790184
1005063612-1009015074
1061038892-1061410454
2276099915-2310172070
1202572862-1215598809
1783724555-1785267178
1262810964-1264200367
592924330-594021870
1981502514-2001291898
3639371125-3691832997
751455858-758389721
575870144-588215938
2707934395-2711294609
2271125072-2271532092
723211153-745881341
291750706-293834948
3846273818-3846421786
1798292566-1840652756
907920869-908496244
2979008391-2984333350
3120502195-3140695376
1316734884-1323407408
4013388816-4015102290
4211041074-4243535195
3264591092-3270165984
1356324132-1369836240
3500337320-3511856741
2675082203-2680516758
269092398-286582232
9214023-16864642
3496293771-3507984426
789173169-790658193
1589657426-1592447273
3018889533-3040428852
3190582871-3209497449
2582019510-2592221443
452701865-462658183
581072273-585497818
2885687081-2887027444
405199391-406037773
1926405498-1961345770
1591447330-1595803034
2075061753-2117082859
2738757089-2739984421
1758742902-1766649306
1598451138-1603784829
904873440-933144524
743128701-751089192
2946510215-2953128493
4258067806-4258357961
2162946809-2194271963
2502065462-2529412983
1794208357-1812728725
2399604728-2399751734
2675639614-2686964361
1243509131-1261449357
1334629713-1360716911
490307573-506198210
3865783894-3882438935
1355288427-1356825096
4080632471-4085694027
1069989320-1079328173
1261530547-1263095027
1864453415-1864536898
500660752-513276733
859810764-865812062
4054243009-4055337105
795048590-839560602
2708730392-2712322515
3642043390-3653718654
2350724230-2355301182
663974525-698684482
734062708-734919764
2004656983-2006812551
987361385-989501665
3621608802-3622545302
1133546243-1135802698
147516310-150573031
2271038167-2271338460
3912004191-3947848898
2301820906-2338108229
2361989797-2363651982
3867365-5819500
3702314080-3703559974
4134127328-4135370466
756306610-770493891
2079529322-2090642509
3981814383-3992802961
4031189022-4042698219
1560502437-1565573103
408025952-414757361
137808459-150920914
3393581407-3411447948
2151896844-2162946807
4201010521-4201471695
3713302577-3725874062
142387170-154849830
2166232094-2205567227
3291340751-3298984606
938375497-943547413
4055961596-4110367884
136677359-137609692
3037464396-3044180771
2691576247-2691980924
1009015076-1045645521
789113477-790592023
899519940-911794289
2137437783-2155776766
1399083500-1402900021
1469947218-1479256900
2944855925-2953686693
2910064491-2920533014
144173340-148094230
2360899146-2362380838
2013535209-2049558890
1109489564-1124585673
2756379565-2767828753
1060568096-1073644115
1691100485-1728041197
1592871439-1600233767
1516639981-1518466748
2098130915-2098541161
3704291842-3706581331
962586078-1003763244
527697837-533713889
1856931843-1873776214
2399693233-2399917980
2055406323-2063623078
240041628-275447727
1513843540-1521844727
1648487379-1649719916
2087056931-2102042862
3717079814-3719847466
1500211877-1510297315
407413483-415066321
3596458788-3618072868
218197655-228951780
643659026-656047997
1603704290-1614650204
2358880422-2366638177
3004836348-3015765511
3046845638-3046851095
3305333257-3307471995
2401731427-2405370552
4017360677-4027723482
557056664-575870142
609440078-615655979
1139493162-1151170381
428962141-483384245
2293357845-2334971307
3091700546-3119568633
1864347502-1864482912
1749751448-1750782554
420140812-420604414
1317387394-1324899402
3623998911-3629315327
4150451309-4152623876
434323808-454005042
1858560120-1864845209
2009686203-2018214121
605094405-611343970
4256094197-4258455116
1177692263-1227426205
4011096895-4014427778
39304785-47673299
498903368-524596608
605553131-610691072
3048424158-3066041482
153238649-154812518
1317950434-1324244958
3355309684-3360596455
2409598473-2428168849
2946469763-2949510201
543235050-544883779
1079837788-1081762723
3600722024-3622452566
4257178957-4258853576
1922845451-1979527610
1162924278-1217904821
1854156984-1867582222
2573163840-2578960281
1159211723-1163517189
1490036932-1500211875
482764386-488744315
235990048-265498430
1714315712-1724421861
958737616-962586076
790658195-851798647
2019736814-2021017547
2162802-8327007
787368380-789171975
3467221232-3469771790
3416813106-3439834312
906735025-908389759
64489226-70116603
1908532718-1922845449
1234754192-1245016567
3287320754-3296095689
3031537491-3039742613
3769892977-3785548652
1645238060-1655418015
612066331-620597775
2905104738-2920311121
2014785668-2022435799
3844301667-3844798343
2828382380-2863199622
2676931732-2682206642
171451625-218197654
2153052343-2156659109
610691073-636761246
2604642896-2615712599
1589965559-1603704289
2935029177-2942217574
186697135-187447861
1986224726-1986550701
770493893-789113476
3557491384-3562596711
2898302199-2920593201
934606912-955515749
1855368372-1872942514
2570443173-2571696675
186869593-188420012
1029668904-1048703657
3284676192-3295161434
3955266215-3977053319
2476141495-2479329360
4276025347-4283606977
534415917-569504381
2263536298-2268109489
1200129331-1210019228
3971350693-3990304290
489813454-495749644
1743364359-1768398619
3924729773-3931294732
105847925-111482255
794582284-818505469
1811415389-1838855885
1890243027-1898852651
1986067335-1986471617
104143552-106052965
772703103-776359533
3911720342-3933921905
395790945-398705617
2258142410-2267980008
613561861-616915116
3310135636-3330660281
2061419260-2061539636
2624281089-2626673183
1877477043-1884442706
2933979446-2949991401
543661669-563658372
197557686-226037744
613176712-618285697
4265278830-4278950571
3556799964-3560580457
1116126837-1122976017
1187703503-1205238834
983871724-1001238917
3887842382-3903790188
2641349279-2643172883
3583057749-3587680646
2601030398-2608486868
4157885743-4168988833
1162830362-1167726097
2514929623-2525222702
3291107480-3295972867
2151518630-2154613192
3046851552-3046878017
325969068-334085941
189084100-189886055
3650880042-3683085757
2453733029-2471942669
1662489961-1666626344
44287139-49449042
1400982930-1421830420
2546953607-2554587873
2639634659-2672001824
641036962-646629131
1236906461-1244507638
1331784152-1367083336
506198211-527697835
255997224-260755488
2588563930-2611385666
3599734818-3614926593
2285367719-2289556931
1088850011-1109811497
3586236383-3589929173
2399595142-2399763869
1385676603-1390665612
3513146704-3513797148
2738224131-2740166097
2869889938-2880215300
2005865698-2011251487
3046872422-3055338791
2940602932-2944294443
3711823219-3713306331
327670367-327738352
2793738-2841656
3807120966-3836270308
3711433856-3712911001
592896405-592954516
688452447-718340962
2063048458-2068052789
4162162406-4167839641
2049558892-2064994876
20968691-38549168
2497497428-2510517683
1583336096-1589657424
1143974607-1155771407
2381952303-2397368087
2009571163-2013286329
942853383-944865487
951722030-952400166
200197723-215328622
3106021045-3120502193
4140023055-4149617577
1668895062-1671431568
2626673185-2653038422
1841289175-1846422485
335754679-386244011
4062044458-4068497802
331356502-332799273
3307471997-3371549847
2018475560-2021933871
150920915-171451623
2194931559-2195514567
4089933248-4090707368
4157463945-4165762209
4100746531-4104107984
3411013858-3416813104
3374946441-3393581406
2552376718-2552429766
725947111-751643934
2473774976-2490564633
3566405121-3581497459
2683823262-2693090640
2734605142-2742827358
3441986164-3442398493
1524044927-1541206072
4254311927-4257287997
2411062371-2425081809
3666577856-3698298724
440803690-480698287
1614650206-1663590083
4257850447-4258201271
2637194180-2658593345
1269282838-1312761281
2522666665-2525818042
141503475-143914340
364934589-385277316
24026223-27879741
3557755338-3564098914
2943664323-2954588780
1571687539-1572996177
957113399-959367378
3585168986-3592657057
1356305980-1369637926
3630349604-3639371123
2570730499-2575580881
2459213065-2486172460
814620199-829988953
1983439516-1984861942
3800496806-3833569562
2841657-3867364
1706481656-1713944571
454683370-473903295
2697862561-2701781892
1451637419-1454646761
501104716-523461517
3304490686-3306418502
3846192081-3846304020
4191662000-4235899383
4096574372-4111227622
480421097-485653417
3762938052-3790582378
701786054-705861635
1214808315-1215006746
364434099-382831881
3713276399-3714579266
1336679025-1347883722
1979527611-1979886571
2090642510-2129888576
3624144511-3633098213
2097515227-2098217363
1851357581-1859249610
3021641379-3030459043
860720178-867061373
4053454232-4055923518
591971809-592927822
899570088-914232296
3171743426-3178833535
1767780850-1769461322
1648285748-1664437761
2756023351-2772357724
1841385621-1851357579
1764427585-1768013247
3968976986-3979761882
204898529-205069325
1192059065-1225447718
204967480-205140904
3191614963-3205521380
2687221525-2690406018
3713502419-3714707176
859460566-860824071
2761514667-2765543032
3357906031-3364349724
3275219921-3282195064
3391484605-3394594750
406732797-420140811
4273899514-4281205511
3083762422-3113295478
2193854781-2195333482
4203706684-4251257733
384194709-397192696
3591265505-3596458786
1102914397-1124045826
2310172071-2344149963
3066041483-3069828748
2635666365-2641585945
1060740916-1061127459
3774707512-3782147573
1743737707-1779166247
246638755-280110373
851798648-859460564
605075197-611133696
2293962494-2298136342
3460740393-3471166317
3280182044-3284676190
14791161-17348573
2691399120-2691637915
1728558700-1733098513
3461545676-3473725502
3751769544-3774673277
772066259-780246746
3356968359-3362991077
1605924820-1613022664
4015102292-4053454231
4206207007-4214797098
1335854520-1363709511
823795603-854558918
3290449369-3304490685
2540570240-2570730498
749722515-756306609
3442398495-3465001104
4229168442-4235745839
150802546-151838496
1380772851-1392292807
4190472817-4203706683
1466784263-1498319230
50105778-54260393
0-2793737
2956453641-2979008390
2552426525-2553141195
3069828750-3083762421
2800389226-2809306363
2275201948-2301909928
670647362-674039479
2639146472-2642836023
3846421788-3895249037
326561664-329333434
188182835-189612566
4253790781-4254533752
1804500603-1806558363
2405370554-2428432104
3608464545-3623946707
2353553540-2360491647
1325917396-1352060617
3577002908-3585168985
1864487525-1877898802
2535505356-2540570238
2012841949-2013535208
4122773972-4147066021
2221253241-2227916854
3996989806-4013388815
1118808237-1118876034
406730726-412027046
2830200680-2841462745
4009639150-4012108169
3387543681-3395550318
2412794571-2444576238
1022924735-1024398890
643270862-663974523
907974347-909753482
4148481231-4151899399
2061333796-2061422413
3844115908-3844704314
296503398-319176563
2743436711-2744991704
1024231444-1050533093
2976066221-2982350583
3913440938-3921340086
2546064716-2552639130
647510635-649788184
1861939256-1878905542
1119182827-1127962138
4176776277-4185432506
1728041199-1736154206
1905044208-1915920572
1860265438-1881626361
2934389290-2943526097
1068791968-1074539223
3124236778-3149982255
286582234-304243327
2100258789-2123748546
3432475911-3432766967
82082661-88073370
2327755908-2338617065
734803505-734970787
4225862764-4241303856
1352060618-1372691007
2552301217-2552408303
3873980245-3908789488
734733934-734933525
913241510-934606910
1746136669-1783130039
3478455269-3482503593
2300261034-2307782855
3248901770-3254155181
651662856-660523209
1118827933-1118873914
3495324533-3508390070
3614090639-3630342601
4152623878-4165068841
4251257735-4252768738
740064940-744628705
2663526-7317845
3173018368-3173033650
840243299-850630387
874982768-893955653
4195369814-4215042523
3712999015-3713605711
3167305950-3179505229
68345070-74894937
3467499056-3471357060
623795984-626879791
533357402-536413407
3551720149-3555281211
3933921906-3941710756
1732833292-1736931431
1172618521-1194746246
2011668991-2019214712
4173423213-4185833738
4129967821-4130008117
2025432624-2029847095
1663590084-1670239922
1677571493-1698026005
1167726098-1232818725
3785872097-3790663631
3140695377-3166258968
2971784945-2974988576
538998996-562454834
4225819511-4229474556
610567638-613651106
2462186480-2480650826
75973934-91434042
2688408664-2707934393
228951782-267685402
1783130040-1784614561
1872942515-1880846327
1262147457-1263932136
4024512115-4053495116
579938959-585172735
602874206-610295015
403990885-414323983
1730191207-1736990500
3623946708-3627097897
1350246834-1362835856
232836175-284581763
1569378906-1570007725
3026358814-3033526682
1636906011-1655244443
1346904336-1351608843
363534678-372420875
3465001105-3471897467
3934746154-3952361164
7208229-13983082
3469317144-3474090343
4280938719-4290730270
2020957337-2022484776
1692136283-1719643620
4032740692-4053771021
2972345930-2975812534
140067848-159037627
3630086418-3634626029
3252572678-3274451634
77141551-85341019
692066237-700847528
3552713357-3558885449
3075915215-3085817045
4162664504-4169419288
124626946-135046727
1884442708-1905044207
3703243550-3704832207
2220909545-2224015721
2692074751-2692885915
1069864185-1073578735
2691786564-2692864691
1737853571-1745347739
95461456-115187423
143224398-144838969
2138286928-2151694571
867061374-882471488
983262449-1001173152
4129969371-4130354697
3470641201-3487201657
2051110734-2064915382
747750272-758258548
3333190532-3365085965
3015765512-3029456808
3265304770-3277560812
546123550-551416184
3622334530-3628645995
1927820889-1967493838
3871603105-3889565720
529055056-557056663
2061323456-2061416792
614047849-615723475
1421830422-1438217488
893955655-899822408
2836598019-2847622397
3513797149-3566405119
2073594551-2086857816
3848735454-3851859716
2350779348-2362218008
1157368724-1159211721
1472023233-1491740523
409000134-412025522
973866742-991888713
1668403284-1669772137
499560567-510329898
267685403-276025076
1214847765-1215067953
2969721904-2972007967
585291343-591565800
1232818727-1248762127
2829953392-2835562942
3581151256-3592382743
3138701074-3144007132
1411308101-1412230389
2005544666-2044382522
3588499596-3590044644
409649298-412147889
2729008724-2746584170
2271068854-2273711594
3908832580-3914932215
335104351-395790944
1473266198-1475735364
91434044-136650095
2061500256-2061621366
3046851992-3046857394
1045645522-1053843281
3062437124-3066285848
2953128494-2956453639
2287457295-2292066307
670003013-672161332
999493075-1005063611
2468468433-2475614015
1784620864-1794208355
1840652757-1842609020
2736112937-2745142809
445972682-455985981
1400181442-1408982387
2727005736-2744339492
1372691009-1399083499
1258925192-1259447558
3572543625-3573210768
2855143621-2872648483
3524287180-3550477388
2401321114-2401936589
188464419-190820937
873632167-889945153
6333787-9214022
866108152-883525080
588215939-596870293
6123882-6333786
1945222555-1965326766
1450943271-1455273678
1071513900-1075274877
4066257746-4107013454
3743897533-3750360675
2210516312-2243489046
739672099-743664201
1190706188-1231785159
1541206073-1552994486
3512385624-3513610248
4004909328-4014105124
1552994488-1583336095
2691601784-2692559045
2959924467-2960061300
2065049768-2073594549
2928347959-2948232651
2737697310-2739140372
3440216783-3442065814
137081234-137703805
1455284245-1455810565
1261449358-1261530545
3839728048-3846372390
4054367050-4055961594
3439834313-3441586831
608984617-613222255
499254004-518922214
2175403815-2205135632
1454597594-1455393440
693379909-700041190
1736154207-1737853569
4010049861-4012151447
3836393111-3838773709
1506443565-1527056312
334384992-335104349
3432143787-3438801061
600863019-608705787
136650096-136849627
3836270310-3838516660
3746890560-3764006100
791648716-794185505
987754526-999694763
2099169385-2119583372
641698158-648180068
3460880474-3481616563
3813294403-3818142124
1317229673-1321947166
2017066792-2036619196
1169805608-1194307388
702695743-722588266
19217566-33973125
32718247-42062630
210053297-217544318
3911504558-3933321555
3975617006-3984996156
551283440-558238333
1127962140-1141935253
1136611230-1157368723
2379700479-2401127625
54260395-75973933
1952020827-1967209978
1264200368-1316734882
1397096904-1403128933
1258173114-1259068731
989260243-995310756
1799866888-1833669063
137517987-137808457
3730940245-3762938051
2963015846-2980970857
600863799-603995952
338151951-378904722
3027117516-3030869045
2785828139-2786645836
1079328174-1079992013
1053843283-1069416181
1060967066-1061236944
3487201659-3496293770
3347750745-3362523105
1338305534-1352171648
1438217489-1462489105
4197364536-4222741711
3189733030-3234111514
451903598-461106580
2097704515-2099471338
304243328-325969066
2086846158-2113069670
2545746395-2547066650
3895249038-3906283534
895659434-904873439
1856927180-1866112900
2775894269-2810724921
1324244959-1325601021
846667177-848199595
3505699661-3506197363
871734319-878294262
4258853578-4294967295
3880214909-3895480719
1986216334-1986348856
742290938-753736254
3234111516-3258189066
3383899774-3396452612
3501809450-3512385622
3378934393-3392160599
3079010157-3098817100
1803429736-1805049104
2166530895-2176167104
1317292508-1322866502
1832462772-1847638033
333679750-334384991
72032218-76605612
17348575-50105777
484459786-489813452
3046849434-3046856389
3467134484-3473562579
2803678490-2810293665
3794709054-3822236055
3186979605-3189733029
2695314106-2700550784
1699535593-1705619603
2237090616-2240620274
1448226508-1452768177
2397634923-2402113900
3900871909-3908832578
4277179118-4284467979
869824885-875039223
3193444038-3195088604
2098172269-2099552847
3166258970-3174350156
3713306332-3730940243
3790663633-3807120965
3193807148-3198905625
2686964362-2695658937
3046846149-3046946514
605656762-611150528
3489750890-3497886462
397630917-403990883
3074826378-3080783127
492235894-493663068
642025801-643219257
788627002-789236451
3084604998-3115741036
3371549848-3374946439
3874793389-3876408934
1139585817-1143207799
3174350157-3186979603
639635957-642849593
1597646197-1612855132
1382702163-1398831616
684158166-713176675
1894143091-1917115741
2089306322-2114752226
2578960283-2621599896
1532015022-1546127235
1324354899-1325917394
2416646543-2437368922
2269877523-2275201946
1992225975-2000270993
640306549-643270861
3044180773-3051507071
2775774779-2793333778
1691451382-1692811369
939103383-944332736
1888996559-1920171303
2268109491-2269877522
2215835480-2260579751
602969274-607505129
1604071710-1613863780
3050099422-3052240627
3628771809-3629905363
3875733031-3886920632
1079554232-1083825209
4121927827-4137657636
1185125973-1212455950
3691832998-3711433854
3128913327-3142493871
4136061085-4148481230
183514025-223274420
1692066643-1696528120
666994178-678090088
2754770797-2759197512
3628299759-3628932735
596038993-600863017
2166543044-2179778402
787127754-788139041
2552150503-2552363008
3258189067-3269060433
2282238677-2289889500
2833059982-2837278958
2887027445-2928347957
2012405876-2032624685
787098717-787195228
1468456416-1495861617
1677947927-1720886831
2345295255-2357276476
3982867112-3996989804
3952361166-3982867111
2822115640-2865481783
748108837-753342957
3838773710-3843041501
2129888578-2151896843
859599485-871063826
3258061263-3260134830
3333184176-3370719083
4252768739-4258730892
2621599897-2626383698
3691176288-3710040996
3294271054-3294614974
1297573835-1313952886
1689064095-1727538616
4111227623-4121927825
3377701672-3394223952
3457691408-3475080606
1439643724-1454465680
2050656519-2065049767
3915610103-3945886566
451360431-486638413
1979886573-1992225974
1081566438-1088850009
2656393854-2668773976
3294056463-3294326494
3242916477-3253418464
1341083507-1344391028
2110664130-2123875999
2049746107-2050500846
3841089640-3844211293
3837279464-3842572520
2865481784-2885687079
2271061510-2272621997
2269988720-2270241311
1202018544-1229602920
2712322516-2753492383
1257333433-1258706059
2653038423-2675082201
955515750-959548963
1285036550-1301703071
2769057410-2775774777
2428432105-2446718114
2446718116-2468468432
2344149965-2353553539
1427316534-1430111473
2205135633-2210516310
2753492385-2769057409
1886236958-1909206855
465545077-470595473
4270417833-4279802697
1516656167-1519514351
2810724922-2822115638
1992340399-2004656981
1109811498-1124752055
1390540334-1390759638
3377856394-3382045950
2366638179-2397634922
1118808079-1118848239
5926527-6123881
1671674170-1691100484
5819501-6106336
2490564635-2514000009
311106391-314727280
314059640-315255926
4010827162-4011730305
4010139590-4011598075
1803265906-1803834597
2497969870-2535505355
1671431570-1689108789
151189360-154214893'''

# COMMAND ----------

def solve(ends, max_allowed = 4294967295):
  i = 0
  count_allowed = 0
  first_allowed = None
  
  while i <= max_allowed:
    new_end = max(end for start, end in ends if start <= i)
    if new_end <= i:
      first_allowed = first_allowed or i
      new_end = min((start for start, end in ends if start > i), default=max_allowed)
      count_allowed += new_end - i
    i = new_end + 1
  
  return first_allowed, count_allowed

first_allowed, count_allowed = solve([[int(x) for x in line.split('-')] for line in inp.split('\n')])

answer = first_allowed
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><em>How many IPs</em> are allowed by the blacklist?</p>
# MAGIC </article>

# COMMAND ----------

answer = count_allowed
answer
