# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/12

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "L90
N5
L180
L180
S4
F21
W4
S1
R270
F18
S4
F44
R90
N5
F18
E5
R270
F1
L90
W5
N4
W5
F37
R90
S1
W2
S1
L90
W5
R90
N1
W2
L180
L90
E3
N1
L90
F30
E4
N2
E2
F76
R90
W4
S3
R90
F2
L90
S3
R180
N5
E4
L90
W4
F1
N2
E1
F8
R90
F88
R180
F60
W2
R90
E3
N3
W5
F56
S1
E5
F5
L90
E4
N3
R90
E2
F34
W4
L90
F100
W4
L90
F40
L90
F51
E5
F52
N1
F45
W2
N2
F56
N2
W3
R180
F14
N3
L90
N2
F18
L180
E1
R90
N2
E3
L180
S5
F87
L90
F32
E1
F92
N1
W3
F89
E2
N1
R90
W1
F9
E1
F74
S1
L270
S1
F99
L90
W1
R90
F78
L90
W4
S2
R180
E3
S4
L90
F78
E5
L90
S5
W2
R90
N1
E5
F33
W1
R180
S1
W4
N1
F69
S5
R90
N5
F89
L90
W1
F91
L90
F19
E5
L90
F53
L90
S5
L90
S4
W1
S2
L180
F3
N5
N5
F78
E3
S1
L180
F79
L90
W4
R180
W3
N4
W5
F84
S4
L180
S1
S3
E2
S4
R90
N1
E5
S4
W4
R90
F44
R90
E5
S5
W1
N4
F37
N2
F41
R90
F58
L90
F5
R90
W4
L90
F45
N4
F48
S1
E2
S1
R90
F30
W2
L90
F53
L90
W5
R90
N2
E1
S3
F29
N5
L270
S2
F87
S4
F86
S4
R90
W5
F59
N2
F35
L90
W5
N3
E3
L90
S2
E2
N2
L90
R90
N5
L270
N5
R90
N4
E2
S3
W2
F55
E4
S1
L90
W3
S4
F95
W5
E2
R90
S3
F54
L90
N5
F69
R90
N1
W3
N4
F49
N4
E5
S2
W5
S5
R90
N1
F76
S5
E4
S5
L90
N2
R90
F68
L90
S1
R90
F67
L90
N3
E1
F51
S1
F94
S3
E5
N3
F76
R180
F53
R90
R90
F96
L270
N1
R90
E3
L90
F57
S5
F39
N2
F95
R270
W1
S4
N5
N4
F5
L90
F83
L180
E4
F82
N5
R90
F52
L90
F13
N5
R90
L90
F10
N5
F80
E4
L180
N1
R90
E1
R180
E5
F25
S3
L180
F29
N1
W1
F20
W1
R180
F56
E5
S2
L90
F67
N4
W3
E2
R180
E1
F16
F59
R180
E5
F21
E2
R90
N4
E5
S5
E3
L90
W1
L90
E2
S3
R90
F59
W4
F44
S2
W1
S1
N5
W1
S3
E1
N3
R90
E2
F39
R90
F2
E1
N5
W5
F24
E3
L90
S3
E2
F57
E2
R90
F12
R90
N2
W3
L180
N4
F78
R180
N4
F92
L90
L180
N2
W4
R90
F7
S4
E3
S4
E1
S4
L180
S2
F81
E5
L90
F3
N4
F39
S2
W4
F28
R90
F75
W1
S3
W5
S1
F67
E3
F62
R90
N3
R180
W2
F67
S2
W1
L90
L90
S2
E3
R90
N5
S4
F14
R180
N2
R90
W3
L180
F37
W1
S4
E1
F45
W4
S5
L180
S2
W1
L90
N4
R90
F44
S1
E3
S4
W5
N4
W4
R270
S1
W3
L90
R90
F95
N1
R90
S1
F48
L90
F53
E2
R180
N5
F46
W5
F98
S3
F81
N5
F98
N4
F67
S1
E1
F10
R90
F66
W3
N1
L180
N1
F27
F54
W2
F3
R90
F68
E2
E4
F30
L90
F62
S2
L90
F99
R90
F48
E4
S4
F96
W4
N5
W5
F44
F90
N1
L90
F68
N4
W1
F83
S5
E1
N3
R90
W4
N5
F59
R90
L180
W2
F14
L90
N1
F58
R90
E2
L90
S5
F30
R90
F17
W1
F29
E3
R90
S3
R90
W1
N2
S3
W2
S2
R90
W2
N2
L90
W1
F55
S3
W4
R180
N3
W1
L90
F59
E5
L90
L180
F70
W1
F41
L180
S5
F22
S5
L270
F11
R90
S3
W2
N4
R90
W5
R180
F17
R90
F99
L180
F26
R90
W5
R180
S5
F28
N5
W1
N5
F100
S4
E2
L270
N4
F100
S1
R180
F81
S5
W5
L180
F1
R90
W5
L90
R90
N4
F69
W5
L180
F68
S5
F21
E4
L180
W3
S3
R90
E3
R90
E2
R90
F19
N3
R90
F81
S1
R90
F1
N1
L90
R90
W1
S4
F93
W5
F31
W1
N1
W1
F59
L180
W5
S4
L90
S1
R270
N1
R90
S3
R90
W2
R90
W2
R180
F83
S3
R90
F99
R90
F25
S2
F81
F33
F55
R90
F40
N5
L90
N5
E5
F56
L180
S2
F52
E4
F99
S2
E1
L180
F47
S3
W4
W3
L90
N1
F26
R90
W5
R90
W5
L90
E2
N1
F35
L90
S3
F20
W5
F29
L90
S2
W4
L180
N5
F27
L90
F80
S1
L90
R180
F37
"

# COMMAND ----------

# read_lines(input) %>% keep(str_starts, "R|L") %>% unique() %>% sort()

# COMMAND ----------

# input <- "F10
# N3
# F7
# R90
# F11
# "

# COMMAND ----------

directions <-
  read_lines(input) %>%
  as_tibble() %>%
  extract(value, c("action", "value"), "(.)(\\d+)") %>%
  mutate(value = as.numeric(value))
directions

# COMMAND ----------

result <- 
  directions %>%
  mutate(
    facing = cumsum(case_when(
      action == "L" ~ value,
      action == "R" ~ -value,
      TRUE ~ 0
    )),
    delta_north = case_when(
      action == "N" ~ value,
      action == "S" ~ -value,
      action == "F" ~ value * sin(facing / 180 * pi),
      TRUE ~ 0
    ),
    delta_east = case_when(
      action == "E" ~ value,
      action == "W" ~ -value,
      action == "F" ~ value * cos(facing / 180 * pi),
      TRUE ~ 0
    )
  )

# COMMAND ----------

abs(sum(result$delta_north)) + abs(sum(result$delta_east))

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

# # TESTING
# input <- "F10
# N3
# F7
# R90
# F11
# L180
# F11
# L90
# F7
# S3
# F10
# "

# directions <-
#   read_lines(input) %>%
#   as_tibble() %>%
#   extract(value, c("action", "value"), "(.)(\\d+)") %>%
#   mutate(value = as.numeric(value))
# directions

# COMMAND ----------

wp_changes <-
  directions %>%
  mutate(
    wp_delta_north = case_when(
      action == "N" ~ value,
      action == "S" ~ -value,
      TRUE ~ 0
    ),
    wp_delta_east = case_when(
      action == "E" ~ value,
      action == "W" ~ -value,
      TRUE ~ 0
    )
  ) %>% 
  add_row(wp_delta_north = 1, wp_delta_east = 10, .before = 1)
wp_changes

# COMMAND ----------

# for (i in which(wp_changes$action %in% c("L", "R"))) {
#   cur_wp <- wp_changes %>% slice(1:i) %>% summarise(wp_north = sum(wp_delta_north), wp_east = sum(wp_delta_east))

#   x <- cur_wp$wp_east
#   y <- cur_wp$wp_north
  
#   v <- paste0(wp_changes$action[i], wp_changes$value[i])
#   if (v %in% c("L180", "R180")) {
#     new_x <- -x
#     new_y <- -y
#   } else if (v %in% c("L270", "R90")) {
#     new_x <- -y
#     new_y <- x
#   } else if (v %in% c("R270", "L90")) {
#     new_x <- y
#     new_y <- -x
#   }
  
#   wp_changes$wp_delta_north[i] <- new_y - y
#   wp_changes$wp_delta_east[i] <- new_x - x
# }

# COMMAND ----------

for (i in which(wp_changes$action %in% c("L", "R"))) {
  cur_wp <- wp_changes %>% slice(1:i) %>% summarise(wp_north = sum(wp_delta_north), wp_east = sum(wp_delta_east))

  x <- cur_wp$wp_east
  y <- cur_wp$wp_north
  
  v <- paste0(wp_changes$action[i], wp_changes$value[i])
  if (v %in% c("L180", "R180")) {
    new_x <- -x
    new_y <- -y
  } else if (v %in% c("L270", "R90")) { # FIXME: TEST - these signs r90 and l90 are swapped nhere
    new_x <- y
    new_y <- -x
  } else if (v %in% c("R270", "L90")) {
    new_x <- -y
    new_y <- x
  }
  
  wp_changes$wp_delta_north[i] <- new_y - y
  wp_changes$wp_delta_east[i] <- new_x - x
}

# COMMAND ----------

# for (i in which(wp_changes$action %in% c("L", "R"))) {
#   cur_wp <- wp_changes %>% slice(1:i) %>% summarise(wp_north = sum(wp_delta_north), wp_east = sum(wp_delta_east))

#   x <- cur_wp$wp_east
#   y <- cur_wp$wp_north

#   r <- sqrt(x^2 + y^2)
#   theta <- atan(y / x)

#   theta_change <- ifelse(wp_changes$action[i] == "R", -1, 1) * wp_changes$value[i] / 180 * pi
#   new_x <- r * cos(theta + theta_change)
#   new_y <- r * sin(theta + theta_change)
  
#   wp_changes$wp_delta_north[i] <- new_y - y
#   wp_changes$wp_delta_east[i] <- new_x - x
# }

# COMMAND ----------

 "L180" "L270" "L90"  "R180" "R270" "R90" 

# COMMAND ----------

result <-
  wp_changes %>%
  mutate(
    wp_east = cumsum(wp_delta_east),
    wp_north = cumsum(wp_delta_north),
    
    ship_delta_east = case_when(
      action == "F" ~ value * wp_east,
      TRUE ~ 0
    ),
    ship_delta_north = case_when(
      action == "F" ~ value * wp_north,
      TRUE ~ 0
    ),
    
    ship_abs_east = cumsum(ship_delta_east),
    ship_abs_north = cumsum(ship_delta_north)
  )

# COMMAND ----------

display(result) # FIXME: The bug is in turning left/right

# COMMAND ----------

result %>% tail(1) %>% with(abs(ship_abs_east) + abs(ship_abs_north))

# COMMAND ----------

# 44534 too high

# COMMAND ----------

# 41212

# COMMAND ----------

# MAGIC %md ## WIP

# COMMAND ----------

for (i in which(wp_changes$action %in% c("L", "R"))) {
  cur_wp <- wp_changes %>% slice(1:i) %>% summarise(wp_north = sum(wp_delta_north), wp_east = sum(wp_delta_east))

  x <- cur_wp$wp_east
  y <- cur_wp$wp_north
  
  v <- paste0(wp_changes$action[i], wp_changes$value[i])
  if (v %in% c("L180", "R180")) {
    new_x <- -x
    new_y <- -y
  } else if (v %in% c("L270", "R90")) {
    new_x <- -y
    new_y <- x
  } else if (v %in% c("R270", "L90")) {
    new_x <- y
    new_y <- -x
  }
  
  wp_changes$wp_delta_north[i] <- new_y - y
  wp_changes$wp_delta_east[i] <- new_x - x
}

# COMMAND ----------

 "L180" "R180" 
"L270" "R90" 
"R270" "L90"  

# COMMAND ----------

 "L180" "L270" "L90"  "R180" "R270" "R90" 

# COMMAND ----------

# MAGIC %md ## Scratch

# COMMAND ----------

result %>% tail(1) %>% with(abs(ship_abs_east) + abs(ship_abs_north))

# COMMAND ----------

# 105124 too high

# COMMAND ----------

  cur_wp <- wp_changes %>% slice(1:i) %>% summarise(wp_north = sum(wp_delta_north), wp_east = sum(wp_delta_east))

  x <- cur_wp$wp_east
  y <- cur_wp$wp_north

  r <- sqrt(x^2 + y^2)
  theta <- atan(y / x)

  theta_change <- ifelse(wp_changes$action[i] == "R", -1, 1) * wp_changes$value[i] / 180 * pi
  new_x <- r * cos(theta + theta_change)
  new_y <- r * sin(theta + theta_change)
  
  wp_changes$wp_delta_north[i] <- new_y - y
  wp_changes$wp_delta_east[i] <- new_x - x