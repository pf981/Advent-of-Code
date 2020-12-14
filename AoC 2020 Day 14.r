# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/14

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

install.packages("binaryLogic")

# COMMAND ----------

library(binaryLogic)

# COMMAND ----------

input <- "mask = 11110100010101111011001X0100XX00100X
mem[17610] = 1035852
mem[55284] = 229776690
mem[16166] = 12685380
mem[8340] = 16011
mask = 0X1X0X010101011X10X101000X0001110100
mem[968] = 15992
mem[32758] = 7076
mem[30704] = 1701
mem[33719] = 58012
mem[20818] = 25927237
mem[16718] = 46485
mask = 111001111X0X0X101X111X1X001XX0011010
mem[2115] = 14848
mem[42753] = 617
mem[56076] = 9933868
mem[19106] = 43503
mem[10073] = 32909
mem[40830] = 1959686
mask = X11X00000XX1011X10000X01110000X0001X
mem[41605] = 13245557
mem[6571] = 7973763
mem[46231] = 28527162
mem[44901] = 163334644
mask = 0101XXX1X10XX1101011110000000010010X
mem[53492] = 357272
mem[32816] = 35015
mem[6965] = 11280352
mem[27745] = 160101
mem[26728] = 1260
mask = 1XXX0100XX1X0X10101100011101101X0111
mem[22010] = 28123044
mem[42154] = 82539
mem[54914] = 22078
mem[7185] = 436
mem[58583] = 25334197
mask = 11110010X001011010X1XX010XX0110001XX
mem[62397] = 9570559
mem[49595] = 15491062
mem[21644] = 9478776
mem[19853] = 31023
mask = 001110000101011X1111100XX1111000X111
mem[62345] = 1200300
mem[34309] = 115943357
mem[23144] = 873
mem[36010] = 954
mem[6857] = 645222
mask = 0011X101110X10101111000X010X00100000
mem[12284] = 570
mem[44849] = 48293
mem[48549] = 489763617
mem[51371] = 1151
mask = 01X0X10101000XXX10111010011010XX0X10
mem[17699] = 14190020
mem[32796] = 84255743
mem[62003] = 1426
mem[18906] = 353
mem[38218] = 615297
mask = 0X0101010111XXX01011010111XX01100010
mem[26389] = 62531634
mem[12404] = 1034263
mem[49398] = 1006
mem[22929] = 313056
mem[16164] = 1694664
mem[19077] = 53452
mask = 0X1XXX0X010101101X1110XX101010X01010
mem[38381] = 18385
mem[2319] = 552
mem[60857] = 1931
mem[41219] = 19301038
mem[9073] = 85077
mask = 00010000010XX1X01000110101100X000111
mem[10385] = 227941
mem[31042] = 151514106
mem[22360] = 168649336
mask = 0110010X0100XX10001X11X1X11100XX0X11
mem[40411] = 8140928
mem[3859] = 2742
mem[45449] = 4317450
mem[17740] = 1337381
mem[19338] = 6605990
mem[22407] = 53051
mem[42292] = 550664
mask = X1110XX00X0101101011XX0X101110001111
mem[59509] = 304929
mem[43817] = 14977
mem[39410] = 439
mem[38730] = 34567670
mem[31862] = 8027039
mem[60857] = 5209
mask = X11X0000X1X101X010110XX011111011X011
mem[28472] = 14882
mem[50099] = 1135
mem[58921] = 980796
mem[50737] = 36974
mem[54167] = 22140347
mem[2139] = 22934
mem[13202] = 136157
mask = X1X001X1010001X0X0111100101110X0X101
mem[911] = 8925
mem[652] = 183714641
mem[58633] = 5186611
mem[41763] = 29030
mask = 011X01010010001110110X0X1100000000X1
mem[47324] = 8124
mem[31660] = 355290
mem[19624] = 1760
mem[32635] = 27873924
mem[45190] = 439446159
mem[1090] = 428
mask = XX10000X00011X1X1011010X0001110X0101
mem[40622] = 1839170
mem[45103] = 108379641
mem[29222] = 187252
mem[42753] = 2592089
mem[46615] = 4466791
mem[22416] = 6619543
mask = X0X101X10X000010XXX10110111011011101
mem[42154] = 3271203
mem[10355] = 89584861
mem[14447] = 383415
mask = 1X000X001X100X10X0X1X01X1101X0110101
mem[40691] = 1490354
mem[6162] = 601597339
mem[62819] = 15727
mem[48596] = 8589566
mem[46732] = 56337
mem[35437] = 1568988
mask = 00X0X10X01010110X0111X0XX01100001111
mem[43285] = 75734
mem[41605] = 46442
mem[7672] = 667983
mem[29222] = 9835
mem[34949] = 3945167
mask = 01X00101X101001010X1100X0X11X110X101
mem[8617] = 182201
mem[33667] = 11585659
mem[57414] = 235257
mask = 0111010001010XX01X11XX1011XX101X1011
mem[19633] = 3970
mem[10580] = 6454804
mem[22445] = 12328278
mem[22131] = 70709
mem[31438] = 870851666
mem[46279] = 638924631
mem[20402] = 311245
mask = 0110000101X1X11010111X001111X1000111
mem[2405] = 733626
mem[27649] = 150996
mem[45000] = 13156617
mask = 01X10X0X01X10110101101X1X1X00100011X
mem[44304] = 5130
mem[25804] = 264101480
mem[896] = 1445
mem[20949] = 386031115
mem[24951] = 9889
mem[51040] = 3708234
mask = 00100X01010101101111100010XX0100X1XX
mem[31907] = 15551
mem[1218] = 1034
mem[17073] = 359232
mask = 010100010101X1101X11011X010001XXXXX0
mem[11137] = 1499158
mem[59509] = 262392
mem[6988] = 14863
mem[28213] = 554
mem[7044] = 68
mask = 01100101X1XX0X10X01110X1001X00X00X11
mem[22674] = 3230
mem[35891] = 3585
mem[3551] = 15928515
mem[36206] = 104461320
mem[22167] = 1161073
mask = 01X1X00X01010X1010111X010XX00011X101
mem[17360] = 494
mem[34415] = 3766044
mem[8898] = 846638
mem[48368] = 500781
mask = 011001010X0X001X0X101X010X100101100X
mem[60679] = 10414
mem[34463] = 11
mask = 01100100010XX11X1X0X0000001111010011
mem[40952] = 1659
mem[27502] = 2916485
mem[7436] = 211741
mem[58641] = 944726
mem[58633] = 46218913
mask = 010110000101011X101101X0111110X00X11
mem[3042] = 13844
mem[49701] = 56163826
mask = 011001X00101011010X1100010X11X011X11
mem[38067] = 7299191
mem[31130] = 116061
mem[2139] = 63458254
mem[4521] = 1237
mask = 0111X000X1010110101X011100100100011X
mem[21329] = 642
mem[41123] = 28058
mem[29555] = 4111
mem[15009] = 3801745
mem[49595] = 317
mem[56642] = 126724425
mem[29388] = 19214321
mask = 1101X1X0X11X101011X01X11X0111X001X01
mem[20118] = 21164480
mem[39432] = 508
mem[39859] = 958
mem[36851] = 196470
mem[26907] = 97849565
mask = XX10000011110X001011XX0010X110100001
mem[34234] = 17652327
mem[16028] = 80890944
mem[54559] = 64040
mem[25194] = 41593756
mask = 001110000101X1101XX1000X10110000110X
mem[33667] = 916652067
mem[2405] = 1244
mem[63718] = 292918
mem[29526] = 711465
mem[24951] = 1884
mem[22360] = 167190303
mask = 1100000000111X11101X0110X00010X00100
mem[6620] = 2734891
mem[64584] = 215747822
mask = 01X00X000100101000X11000X01110100X01
mem[56211] = 3278176
mem[40364] = 340370
mem[23555] = 27655
mem[42471] = 227213
mask = 1X10X1111101X110X011X000X0X0X10011X0
mem[6829] = 110833304
mem[15624] = 23686
mem[59705] = 5391933
mem[10724] = 32064
mem[14827] = 6939
mask = X1X1100001010X111011101X00110X000010
mem[50595] = 719945
mem[1480] = 39227195
mem[52615] = 124668762
mask = 01100XX1110X011XX01100001011X1X10X10
mem[58924] = 3492
mem[16850] = 584
mem[61283] = 289490093
mem[20396] = 55247
mem[12216] = 9844180
mem[12216] = 14974951
mask = 00X00101010101X010111000101XX0100001
mem[4778] = 4486654
mem[24826] = 1334889
mem[30412] = 685
mem[424] = 40892660
mem[19019] = 87071
mem[58641] = 13743890
mask = 011100XXX10101101X0X00010001011100X0
mem[10355] = 392450
mem[20082] = 23264
mem[25220] = 1800190
mem[59108] = 141835
mem[58233] = 543
mem[48973] = 863
mem[54167] = 28960
mask = 1110X0000001X11010110000X1011XXX1010
mem[52783] = 2071776
mem[60857] = 108259027
mem[37356] = 2641268
mem[21950] = 47481758
mem[52557] = 7700825
mask = 0X11010XX10X001011110010111000101001
mem[58111] = 244589936
mem[41399] = 42658
mem[27306] = 237040
mem[4122] = 1592
mask = X1X00X0111110110101XX1001001X0010X10
mem[6801] = 34789897
mem[59447] = 10675177
mem[28987] = 666686
mask = X110000X000110X11011111000X11100010X
mem[424] = 2927
mem[30920] = 894899
mem[1670] = 305032596
mask = 0111X01000X1X1101011001X111000011010
mem[29811] = 632621
mem[40046] = 51323
mem[55593] = 6182
mask = 01100011100XX11X00X110X011110XX10101
mem[58803] = 484311
mem[49237] = 12281
mem[46823] = 1332
mem[24356] = 1277234
mem[42561] = 1938
mem[14991] = 8909
mask = 0111X00000X101101X11101010111X001111
mem[8482] = 2735
mem[36657] = 64651206
mem[3842] = 157
mem[60137] = 483271
mem[5610] = 709
mask = XX1X00X00X01X11010111X001101110X1111
mem[22416] = 27971815
mem[19192] = 7861
mem[51678] = 25016
mask = 011XX1111101XX101111001X001110010000
mem[64535] = 155
mem[38057] = 669
mem[8482] = 29767095
mask = 00100X000X010X10X111100X11100110X101
mem[38067] = 10211
mem[37762] = 11637
mem[34706] = 44902
mask = 0X11001100110XXX1011011X10X10X01100X
mem[26809] = 2100865
mem[60446] = 25094
mem[43745] = 461971
mem[24321] = 28927
mem[7984] = 355769146
mem[9488] = 1910
mask = 0X1001X1X10X0X1010111X10X011X01X1111
mem[51678] = 2889
mem[46700] = 214866595
mem[40992] = 4945733
mem[25409] = 172376952
mask = 0110011111X100101X11000XX110X0001X0X
mem[11587] = 9651
mem[41265] = 61660
mem[1822] = 6155
mem[29303] = 250909900
mem[59145] = 51920318
mask = 01X1X0X0X1010110101100101111100X0001
mem[33719] = 2071728
mem[24951] = 108
mem[12284] = 369552742
mem[55012] = 53272268
mem[31862] = 3576
mem[5950] = 460151
mem[55978] = 53697916
mask = XX1100000X01011010X1100011X01000X110
mem[61606] = 1036
mem[6477] = 81209
mem[2187] = 6526467
mask = 111000X011110100X011X0XXX11X10110X01
mem[25194] = 7338343
mem[16563] = 225968
mem[51983] = 30985431
mask = 0X000100010101101X11100X00011X111011
mem[34309] = 434429
mem[16850] = 476433401
mem[63015] = 181118
mask = X110001011X1010X1011010X1011X01100X0
mem[19081] = 237103716
mem[24300] = 10640
mem[23963] = 430607
mask = 0111XXXX001101101011000011XX00X01XX1
mem[26941] = 27590
mem[31862] = 20472
mem[4020] = 3134353
mem[55543] = 1761762
mem[45048] = 1024489921
mask = 11100111X10X111XX0X1000010111110101X
mem[48596] = 3587524
mem[2018] = 451398
mem[54298] = 121634159
mem[26371] = 5517119
mem[57585] = 1825
mask = 0111X00X0011X11010X10X100100X1100000
mem[44281] = 1515553
mem[36633] = 1289
mem[30077] = 12046281
mem[55362] = 226809
mem[48993] = 794317
mem[58968] = 241
mask = X110010101100X10101110100011000XX001
mem[22929] = 2072990
mem[22931] = 336
mem[31880] = 119168961
mem[3859] = 49656496
mem[45103] = 296484159
mask = XX11000001011110100101100X0X01100101
mem[41219] = 826
mem[38539] = 22527609
mem[40238] = 29540
mem[34813] = 4305171
mem[51640] = 4302332
mem[44070] = 1373134
mask = 011X0000X101011010011111X01X10101011
mem[40884] = 256867181
mem[56234] = 2181222
mem[5950] = 68826
mem[1760] = 88028804
mem[50704] = 5302105
mem[24366] = 442
mem[10147] = 127227597
mask = 0110X1100101X1101011X111100X0X0XX010
mem[21956] = 121736133
mem[25007] = 3174
mem[42616] = 925004
mem[1670] = 3018
mem[46932] = 2981988
mask = X1110011001XXXX01011011X1X1100011X01
mem[61283] = 521975
mem[27640] = 322
mem[62514] = 153670214
mem[23951] = 14226595
mem[9549] = 2336533
mem[11888] = 827772
mask = 1101X100XXX1X010111000XX0001000X10X1
mem[16797] = 22808
mem[48021] = 2258240
mem[12370] = 185157105
mask = 01110X0X00XX0X1X10110100X10X01000010
mem[4594] = 93
mem[57388] = 665641765
mem[1345] = 361710791
mem[37543] = 1730
mem[57136] = 388716965
mem[42524] = 553
mem[13403] = 637623155
mask = 0110X1X0X101011X10110110100101011110
mem[16512] = 3631
mem[11337] = 203803846
mem[2504] = 336583240
mem[12269] = 4069068
mask = 01XX001111001110101100001X01000100X0
mem[33661] = 6490
mem[30704] = 128919282
mem[41797] = 22490
mem[8134] = 38294563
mem[63208] = 12103
mask = 11X00X0000X1XX1X101100010000010011XX
mem[24951] = 3275742
mem[23998] = 1551
mem[19972] = 5727596
mem[17337] = 205937438
mem[41952] = 53261
mem[64651] = 26734
mask = X11001111101XX101X110X001011100X0X1X
mem[57388] = 441426
mem[11337] = 336
mem[8515] = 381065399
mem[49625] = 1066556272
mem[54274] = 7650
mem[8575] = 15426
mem[18302] = 216253866
mask = 1X0X00X000X11X1110110100110111X1X101
mem[6256] = 17076091
mem[7973] = 5554062
mem[39859] = 1429203
mask = 0X110001011101101X1111101001XX000110
mem[38807] = 351
mem[28213] = 22387
mem[26591] = 76518875
mem[15712] = 12048675
mask = 01X1XX00010101101011X111XX1010XX1011
mem[9073] = 789
mem[39859] = 919291385
mem[18302] = 347
mem[41224] = 4579691
mem[41167] = 19132842
mem[424] = 158741911
mask = X110010X0100X010X0100X00XX111001X011
mem[28822] = 66019
mem[46209] = 2719
mem[35264] = 1826
mem[60137] = 389000
mask = 01010001X101X11010110X111111X1000001
mem[16591] = 62860121
mem[10737] = 1180
mem[31130] = 16000
mem[34880] = 584
mem[6800] = 39
mask = 0111X000X1XX11101001010X00110010011X
mem[5501] = 31780835
mem[31862] = 6009
mem[49129] = 91037
mem[7935] = 15099
mem[44839] = 31518815
mask = 0101000101011110X1110111000001XXX000
mem[14827] = 1206371
mem[62398] = 1062
mem[50952] = 1253562
mem[32584] = 22533969
mem[9662] = 2590
mask = 01100X111X0X1110XX111X000X1101000001
mem[40142] = 107915
mem[10580] = 4884244
mem[2187] = 1020
mask = 11X100XX1001X1X0101X01X1001X11111100
mem[19551] = 54829
mem[18208] = 627039
mem[18032] = 3423
mem[24162] = 301557348
mem[35891] = 1206
mask = 01100111110100X0XX1X1011XXX100101000
mem[9695] = 368318059
mem[9916] = 30083984
mem[9903] = 866066456
mem[3360] = 434642
mem[3609] = 2437
mask = 0XX1X000010XX1X0100X1010X10100X00111
mem[64662] = 5845
mem[20000] = 2302117
mem[21056] = 11248
mem[641] = 200833516
mem[46678] = 3506929
mask = 0X100111111100101111110X01110X00010X
mem[59199] = 1984963
mem[43784] = 7811709
mem[49701] = 3967
mem[11888] = 790487
mask = 111X00000101111010010X10001101XX11X0
mem[51082] = 222096294
mem[50595] = 121297
mem[27424] = 268132
mem[9473] = 200971
mem[42941] = 1604
mask = 0X11010X1X00X01011110010111XX010X00X
mem[44304] = 31572
mem[14907] = 1066531
mem[34745] = 91393
mem[1617] = 124090
mem[25898] = 49692
mask = X11X01000X010X111X1X10100000010X10X0
mem[12953] = 62465686
mem[24718] = 15597133
mem[20124] = 4930329
mask = 0X11010000X10X1010110111XX00X1XX101X
mem[12426] = 694
mem[2226] = 70693
mem[6332] = 3693756
mask = 0111100000110XX010X11000X1X111011010
mem[42447] = 86599788
mem[62694] = 50365
mem[59239] = 4355782
mem[12523] = 14292673
mem[52756] = 2685769
mem[54978] = 207845
mem[17699] = 366567692
mask = 011001011111X0XX101100000X10X0X01011
mem[8186] = 1183
mem[6181] = 8087
mem[61605] = 3505
mem[46678] = 85544
mem[40046] = 5212041
mem[28835] = 3272650
mask = 011100000101X11010X1011X10X1XX00X011
mem[55012] = 105058
mem[52202] = 26295
mem[59657] = 2809
mask = X1X10100X101XXX0X110001110001XX01001
mem[45682] = 323588
mem[49237] = 58065
mem[41032] = 27927
mem[35647] = 280
mem[47892] = 252817
mem[29350] = 15075
mask = X11100X0010X01X010111101001100000010
mem[34234] = 10472
mem[14531] = 102821
mem[49081] = 3626197
mem[62940] = 630043
mem[4115] = 453716952
mask = 0111010001XX0110111X0101100X1X10101X
mem[911] = 198069
mem[5550] = 42378
mem[27566] = 13692
mem[13890] = 46764242
mem[11669] = 66225421
mem[54529] = 652599152
mask = X11X01X00X01011X10110110X00X100X10X0
mem[7236] = 3301
mem[10580] = 971
mem[51284] = 232016
mem[13784] = 33278200
"

# COMMAND ----------

# input <- "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# "

# COMMAND ----------

# input <- "mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# "

# COMMAND ----------

process_segment <- function(segment_lines) {
  mask <- segment_lines[[1]] %>% str_replace("mask = ", "")

  segment_lines[-1] %>%
    as_tibble() %>%
    extract(value, c("address", "value"), "mem\\[(\\d+)\\] = (\\d+)") %>%
    transmute(
      address = as.integer(address),
      value = as.integer(value),
      mask = mask
    )
}

# COMMAND ----------

input_lines <- read_lines(input)

# COMMAND ----------

mem <- map_dfr(
  split(input_lines, cumsum(str_detect(input_lines, "^mask = "))),
  process_segment
)
display(mem)

# COMMAND ----------

# strtoi doesn't work because it can't handle integers this big
binary_str_to_dec <- function(x) {
  x %>%
    str_split("") %>%
    map(as.integer) %>%
    map(function(y) reduce(y, ~.x * 2 + .y))
}

# COMMAND ----------

result <-
  mem %>%
  mutate(
    value_bin = as.binary(value, n = 36),
    
    mask_1 = mask %>% chartr("X", "0", .) %>% binary_str_to_dec() %>% as.binary(n = 36),
    mask_0 = mask %>% chartr("1X0", "110", .) %>% binary_str_to_dec() %>% as.binary(n = 36),
    
    masked_bin = pmap(lst(value_bin, mask_1, mask_0), ~(..1 | ..2) & ..3),
    masked = map_dbl(masked_bin, as.double) # Can't use integer because it's too big
  )
result

# COMMAND ----------

result$masked

# COMMAND ----------

answer <-
  result %>%
  group_by(address) %>%
  slice(n()) %>%
  ungroup() %>%
  summarise(answer = sum(masked)) %>%
  pull(answer)
format(answer, scientific = FALSE)

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

# mask <- "X01X0"

# COMMAND ----------

expand_mask <- function(mask) {
  replacement_grid <- expand.grid(
    rep(list(c("0", "1")), str_count(mask, "X")),
    stringsAsFactors = FALSE
  )
  
  reduce(
    replacement_grid,
    str_replace,
    pattern = "X",
    .init = mask
  )
}

# COMMAND ----------

result <-
  mem %>%
  mutate(
    value_bin = as.binary(value, n = 36),
    
    mask = map(mask, expand_mask)
  )
result

# COMMAND ----------

df <-
  result %>%
  unnest(mask) %>%
  mutate(
    address_bin = as.binary(address, n = 36),
    mask = mask %>% binary_str_to_dec() %>% as.binary(n = 36),
    address_final = map2(address_bin, mask, ~(.x | .y))
  )

# COMMAND ----------

df

# COMMAND ----------

# as.double(df$address_final[[1]])

# COMMAND ----------

# df$address_final
df %>%
  mutate(address_final = map_dbl(address_final, as.double)) %>% pull(address_final) %>% unique()

# COMMAND ----------

a=  df %>%
  mutate(address_final = map_dbl(address_final, as.double)) %>%
  group_by(address_final) %>%
  slice(n()) %>%
  ungroup() %>%
  pull(value)

# COMMAND ----------

format(sum(a), scientific = FALSE)

# COMMAND ----------

# 1702907407523 too low

# COMMAND ----------

answer <-
  df %>%
  mutate(address_final = map_dbl(address_final, as.double)) %>%
  group_by(address_final) %>%
  slice(n()) %>%
  ungroup() %>%
  summarise(answer = sum(value)) %>%
  pull(answer)
format(answer, scientific = FALSE)

# COMMAND ----------

answer

# COMMAND ----------

# MAGIC %md ## Scratch

# COMMAND ----------

result %>%
  mutate(
    mask_bin = map(mask, as.binary)
  )

# COMMAND ----------

str_count(mem$mask, "X") %>% table()

# COMMAND ----------

2^9 * 63

# COMMAND ----------

result <-
  mem %>%
  mutate(
    value_bin = as.binary(value, n = 36),
    
    mask_1 = mask %>% chartr("X", "0", .) %>% binary_str_to_dec() %>% as.binary(n = 36),
    mask_0 = mask %>% chartr("1X0", "110", .) %>% binary_str_to_dec() %>% as.binary(n = 36),
    
    masked_bin = pmap(lst(value_bin, mask_1, mask_0), ~(..1 | ..2) & ..3),
    masked = map_dbl(masked_bin, as.double) # Can't use integer because it's too big
  )
result

# COMMAND ----------

expand_mask("X01X0X")

# COMMAND ----------

rep(list(c("0", "1")), str_count(mask, "X"))

# COMMAND ----------

reduce(
  expand.grid(list(c("0", "1"), c("0", "1")), stringsAsFactors = FALSE),

  str_replace,
  pattern = "X",
  .init = "X01X0"
)

# COMMAND ----------

"X01X0" %>% str_count("X")

# COMMAND ----------

"X01X0" %>% str_replace("X", "0")

# COMMAND ----------

str_replace

# COMMAND ----------

sr = expand.grid(list(c("0", "1"), c("0", "1")), stringsAsFactors = FALSE)

# COMMAND ----------

?expand.grid

# COMMAND ----------

v = expand.grid(list(c("0", "1"), c("0", "1")), stringsAsFactors = FALSE)
v

# COMMAND ----------

str_replace("X01X0", pattern = "X", replacement = v[[1]])

# COMMAND ----------

reduce(
  expand.grid(list(c("0", "1"), c("0", "1")), stringsAsFactors = FALSE),

  str_replace,
  pattern = "X",
  .init = "X01X0"
)

# COMMAND ----------

reduce2(
  expand.grid(list(c("0", "1"), c("0", "1")), stringsAsFactors = FALSE),

  ~str_replace(.y, .x, pattern = "X")
)

# COMMAND ----------

str_replace(
  str_replace("X01X0", pattern = "X", replacement = v[[1]]),
  pattern = "X", replacement = v[[2]]
)

# COMMAND ----------

reduce2(
  expand.grid(list(c("0", "1"), c("0", "1")), stringsAsFactors = FALSE),

  ~str_replace(.y, .x, pattern = "X")
)

# COMMAND ----------

str_replace

# COMMAND ----------

?reduce

# COMMAND ----------

str_replace("X01X0", pattern = "X")

# COMMAND ----------

expand.grid(list(c("0", "1"), c("0", "1")), stringsAsFactors = FALSE) %>%
  map(str_replace, string = "X01X0", pattern = "X")

# COMMAND ----------

expand.grid(list(c("0", "1"), c("0", "1")), stringsAsFactors = FALSE) %>%
  map(str_replace, string = "X01X0", pattern = "X")

# COMMAND ----------

expand.grid(list(c(0, 1), c(0, 1), c(0, 1)))

# COMMAND ----------

expand.grid(c(0, 1), c(0, 1), c(0, 1))

# COMMAND ----------

mask_address <- function(address, mask) {
  
}

# COMMAND ----------

address_masked = mask_address(address, mask)

# COMMAND ----------

mem