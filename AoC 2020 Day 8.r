# Databricks notebook source
library(tidyverse)

# COMMAND ----------

input <- "acc -8
jmp +5
acc +0
acc +44
acc +42
jmp +324
acc -17
jmp +1
acc -17
jmp +51
acc -13
acc +4
jmp +1
nop +608
jmp +274
acc -17
jmp +169
acc +28
nop +508
jmp +1
jmp +570
acc +22
acc -14
jmp +377
acc -13
acc +27
jmp +474
acc -5
jmp +1
acc +12
jmp +37
jmp +184
acc +36
acc +32
acc -8
jmp +465
acc -13
acc +18
jmp +169
acc +20
acc +26
acc +23
jmp +333
jmp +584
acc +9
acc +28
acc +28
nop +571
jmp +143
acc +39
acc +39
acc -16
jmp +361
acc +48
acc +3
acc +15
nop +4
jmp +504
acc +6
jmp +285
acc +26
acc +33
jmp +1
acc +36
jmp +577
acc +36
jmp +6
nop +498
acc +42
jmp +496
acc +10
jmp +74
acc +17
acc +16
acc +30
jmp +254
acc -3
acc +16
acc -2
nop +106
jmp +541
acc -15
jmp +579
jmp +165
acc +22
acc -6
acc +29
acc -19
jmp +342
acc -19
jmp +340
acc +13
acc +25
acc +29
jmp +269
acc -14
acc +27
acc +41
acc +49
jmp +181
nop +350
jmp +1
nop +437
acc +34
jmp +494
acc +19
acc +2
acc +44
jmp +558
acc +10
jmp +44
nop +4
nop -80
nop +540
jmp +16
acc +28
jmp +14
acc +13
nop +399
acc +29
nop -60
jmp -6
acc +41
acc +30
jmp +232
acc +28
nop +495
acc +15
acc +48
jmp +157
nop +483
jmp -59
acc +5
acc +30
acc +30
acc +2
jmp +349
acc +11
acc +27
acc +1
jmp +367
acc +8
acc +45
acc +11
jmp +171
jmp -113
acc +48
jmp -38
acc +12
jmp +145
acc +8
nop +29
nop +319
jmp +154
nop +166
jmp +395
nop +15
jmp +237
acc +22
acc +3
acc +42
acc +1
jmp +288
jmp -63
nop +489
acc +33
jmp +247
jmp +1
acc -8
acc +9
jmp +413
acc -17
acc +3
acc +3
jmp +432
nop -17
acc +36
nop +198
acc +45
jmp +109
nop +242
acc +40
acc +11
jmp +448
jmp +437
acc +3
acc +49
acc +27
jmp +221
nop +158
jmp +143
acc +50
jmp -70
acc +46
acc +8
acc +35
acc -3
jmp +104
acc +11
acc +0
jmp +34
nop +132
jmp +425
jmp +219
acc -12
acc +48
jmp +21
jmp +434
acc +30
acc +1
acc +40
jmp +435
jmp +132
acc +40
jmp +236
jmp +179
jmp -149
acc +25
acc +40
acc -9
acc +49
jmp +445
nop +399
acc -14
nop +374
acc +0
jmp +152
acc +39
nop +322
acc +49
nop +117
jmp -19
acc +24
jmp +385
acc +17
acc +39
acc +44
acc -8
jmp -58
acc -18
nop -76
jmp +66
acc +14
jmp +427
acc +11
acc +47
acc +9
jmp +1
acc +42
jmp -7
acc -16
acc -13
jmp +409
acc +1
acc +35
acc +34
jmp +371
acc +24
acc +46
acc -4
jmp +367
acc +19
acc +27
acc -8
acc +41
jmp -184
nop -185
acc +23
acc -8
acc +35
jmp -9
acc -7
nop -101
nop +121
acc +37
jmp -72
acc +24
jmp +1
nop -124
jmp +163
acc +37
acc -12
jmp +331
acc -12
acc +1
jmp +232
jmp -233
jmp -72
acc +28
jmp +169
acc +43
acc +18
nop +108
jmp -184
acc -4
acc -10
nop +317
acc +48
jmp +173
nop +45
jmp -73
acc +35
jmp +198
acc -15
acc +46
acc +31
jmp +41
nop +169
jmp +1
nop -92
nop -271
jmp -113
jmp +1
nop -42
jmp +42
nop -283
acc +22
nop +200
jmp -17
jmp +1
acc +49
nop +35
nop -185
jmp +298
acc +1
jmp +1
nop +301
acc +19
jmp -34
jmp +163
jmp +1
acc +49
jmp -115
jmp -62
acc +8
acc +5
acc -6
jmp -146
acc -4
nop -202
acc +47
jmp -114
acc +8
jmp +57
acc +37
jmp +61
jmp +267
acc +2
acc +28
nop -20
jmp -186
acc +24
nop +269
acc +48
acc +45
jmp -22
acc +11
acc +36
jmp -267
acc +7
nop -45
nop -231
jmp +32
nop +220
acc +19
jmp -250
acc +33
jmp -169
acc +45
acc -13
acc +0
acc +44
jmp +6
acc +42
jmp +84
acc +48
jmp -332
jmp +213
acc -16
acc +31
acc +17
acc +3
jmp -75
jmp +1
acc +11
acc +4
jmp -271
acc -12
nop +97
nop +11
jmp -43
acc +30
jmp +1
jmp +49
jmp -379
nop -51
acc +0
acc -8
nop -191
jmp -346
jmp -255
acc +2
acc +21
acc -16
nop +217
jmp -30
acc +31
jmp -270
jmp -324
jmp +130
acc +49
nop +179
jmp -37
acc +11
acc +15
acc +29
acc +17
jmp -237
acc +47
acc -13
acc +6
jmp +169
nop +54
acc -12
jmp -233
nop +33
acc +17
acc +14
acc +21
jmp -275
acc -8
acc +1
nop +229
jmp +1
jmp +119
jmp -193
nop +217
jmp +95
acc -2
acc +1
acc +41
jmp -332
acc +44
nop -343
acc +23
jmp -165
acc +7
acc -12
nop -339
jmp +9
nop -390
acc -17
acc +43
jmp -138
nop -247
acc +42
acc +0
jmp +170
acc +48
jmp -139
acc +6
acc +13
acc +35
jmp -85
nop -117
jmp -307
acc +25
acc -10
acc -14
acc +0
jmp -355
jmp +102
acc -8
acc +47
acc +36
jmp +42
acc +33
acc +17
acc +46
jmp -331
jmp +1
acc -11
jmp +1
acc +27
jmp +147
acc -14
nop -28
acc +32
jmp -482
acc +11
nop -390
jmp -485
acc -12
acc +37
acc +33
acc +28
jmp -32
acc +42
acc -11
jmp -460
acc +36
acc +6
acc +39
jmp +80
nop +123
acc -13
jmp -97
acc +25
acc +46
acc +13
nop -450
jmp +84
acc +3
nop -260
jmp +1
acc +22
jmp -510
acc -4
acc +17
acc -19
jmp -420
acc -14
acc +26
acc +29
acc +17
jmp -458
acc -10
acc +23
nop -2
jmp -196
acc -5
jmp -416
acc +49
jmp -165
acc +4
acc +7
acc +20
nop -217
jmp +103
jmp +5
acc -1
acc +2
jmp +1
jmp +84
acc -14
jmp -518
jmp +1
acc +30
acc +21
jmp -202
nop -18
jmp -344
jmp -88
nop -472
acc -5
acc +13
jmp -295
nop -315
acc +41
nop -317
jmp -299
nop +105
jmp -86
acc +7
jmp -226
nop -277
acc +21
acc +13
acc +47
jmp -283
acc -11
acc -1
jmp -408
acc +47
nop -553
acc +37
acc -11
jmp -468
acc +43
nop -299
acc +40
acc +2
jmp -275
acc +24
acc -14
acc +13
acc +36
jmp -249
acc +35
jmp -45
acc +47
acc +31
acc -19
jmp -151
jmp -33
acc +6
jmp -160
jmp -553
acc +25
jmp +1
nop -267
jmp -430
acc +23
nop +63
acc +37
jmp -434
nop -579
jmp +11
acc +25
acc -17
acc +22
acc +27
jmp +15
jmp -546
acc -4
acc +41
acc +0
jmp -261
acc +20
jmp -404
jmp -408
acc +26
jmp -464
acc +34
nop -80
acc -12
jmp -43
jmp -410
acc -13
acc -3
jmp -310
nop -433
acc -7
acc -11
acc +9
jmp -29
nop -564
acc -5
acc -16
acc +36
jmp -587
jmp -115
acc +24
acc +35
nop -638
jmp -573
acc +31
acc +14
jmp -609
acc +25
acc -10
acc +18
jmp -308
acc +25
acc +33
acc +21
acc -12
jmp -172
nop -37
acc +12
jmp -316
acc +41
acc +14
jmp -415
acc +40
jmp -112
jmp -613
acc +26
nop -151
jmp -471
acc +50
acc +16
nop -119
acc +46
jmp +1
"

# COMMAND ----------

# input <- "nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# "

# COMMAND ----------

instructions <-
  input %>%
  read_lines() %>%
  as_tibble() %>%
  separate(value, c("op", "value"), " ") %>%
  mutate(value = parse_number(value))

instructions

# COMMAND ----------

accumulator <- 0
visited <- c()
i <- 1

repeat {
  instruction <- instructions %>% slice(i)
  if (i %in% visited) {
    break
  }
  
  visited <- c(visited, i)
  
  if (instruction$op == "acc") {
    accumulator <- accumulator + instruction$value
  }
  
  if (instruction$op == "jmp") {
    i <- i + instruction$value
  } else {
    i <- i + 1
  }
}

# COMMAND ----------

accumulator

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

try_instructions <- function(instructions) {
  accumulator <- 0
  visited <- c()
  i <- 1

  repeat {
    instruction <- instructions %>% slice(i)
    if (i %in% visited) {
      return(NULL)
    }

    visited <- c(visited, i)

    if (instruction$op == "acc") {
      accumulator <- accumulator + instruction$value
    }

    if (instruction$op == "jmp") {
      i <- i + instruction$value
    } else {
      i <- i + 1
    }
    
    if (i == nrow(instructions) + 1) {
      return(accumulator)
    }
  }
}

# COMMAND ----------

try_instructions(instructions)

# COMMAND ----------

unlist(map(which(instructions$op == "nop"), function(i) {
  updated <- instructions
  updated$op[i] <- "jmp"
  try_instructions(updated)
}))

# COMMAND ----------

unlist(map(which(instructions$op == "jmp"), function(i) {
  updated <- instructions
  updated$op[i] <- "nop"
  try_instructions(updated)
}))