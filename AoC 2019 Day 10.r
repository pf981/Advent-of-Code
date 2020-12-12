# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/10

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "#.#................#..............#......#......
.......##..#..#....#.#.....##...#.........#.#...
.#...............#....#.##......................
......#..####.........#....#.......#..#.....#...
.....#............#......#................#.#...
....##...#.#.#.#.............#..#.#.......#.....
..#.#.........#....#..#.#.........####..........
....#...#.#...####..#..#..#.....#...............
.............#......#..........#...........#....
......#.#.........#...............#.............
..#......#..#.....##...##.....#....#.#......#...
...#.......##.........#.#..#......#........#.#..
#.............#..........#....#.#.....#.........
#......#.#................#.......#..#.#........
#..#.#.....#.....###..#.................#..#....
...............................#..........#.....
###.#.....#.....#.............#.......#....#....
.#.....#.........#.....#....#...................
........#....................#..#...............
.....#...#.##......#............#......#.....#..
..#..#..............#..#..#.##........#.........
..#.#...#.......#....##...#........#...#.#....#.
.....#.#..####...........#.##....#....#......#..
.....#..#..##...............................#...
.#....#..#......#.#............#........##...#..
.......#.....................#..#....#.....#....
#......#..###...........#.#....#......#.........
..............#..#.#...#.......#..#.#...#......#
.......#...........#.....#...#.............#.#..
..##..##.............#........#........#........
......#.............##..#.........#...#.#.#.....
#........#.........#...#.....#................#.
...#.#...........#.....#.........#......##......
..#..#...........#..........#...................
.........#..#.......................#.#.........
......#.#.#.....#...........#...............#...
......#.##...........#....#............#........
#...........##.#.#........##...........##.......
......#....#..#.......#.....#.#.......#.##......
.#....#......#..............#.......#...........
......##.#..........#..................#........
......##.##...#..#........#............#........
..#.....#.................###...#.....###.#..#..
....##...............#....#..................#..
.....#................#.#.#.......#..........#..
#........................#.##..........#....##..
.#.........#.#.#...#...#....#........#..#.......
...#..#.#......................#...............#
"

# COMMAND ----------

# input <- ".#..#
# .....
# #####
# ....#
# ...##
# "

# COMMAND ----------

asteroids_str <- read_lines(input)

# COMMAND ----------

asteroids <-
  asteroids_str %>%
  str_c(collapse = "") %>%
  str_split('') %>%
  unlist() %>%
  matrix(ncol = nchar(asteroids_str[[1]]), byrow = TRUE)
asteroids

# COMMAND ----------

coords <- which(asteroids == "#", arr.ind = TRUE) %>% as_tibble() %>% set_names("y", "x") %>% mutate(y = nrow(asteroids) - y)

# COMMAND ----------

ggplot(coords, aes(x, y)) + geom_point()

# COMMAND ----------

result <-
  crossing(a=coords, b=coords) %>%
  as.list() %>%
  bind_cols() %>%
  #filter(!(x == x1 & y == y1)) %>%
  mutate(
    slope = (y - y1) / (x - x1),
    d = (x - x1)^2 + (y - y1)^2
  ) %>%
  group_by(x, y, slope) %>%
  arrange(d) %>%
  slice(1) %>%
  ungroup() %>%
  count(x, y) %>%
  arrange(desc(n))
result

# COMMAND ----------

ggplot(result, aes(x, y, label = n)) + geom_point() + geom_label()

# COMMAND ----------

result$n[[1]]
#> 303

# COMMAND ----------

# MAGIC %md ### Tests

# COMMAND ----------

find_max_asteroids <- function(asteroids_str) {
  asteroids_str <- read_lines(asteroids_str)
  asteroids <-
    asteroids_str %>%
    str_c(collapse = "") %>%
    str_split('') %>%
    unlist() %>%
    matrix(ncol = nchar(asteroids_str[[1]]), byrow = TRUE)
  
  coords <- which(asteroids == "#", arr.ind = TRUE) %>% as_tibble() %>% set_names("y", "x") %>% mutate(y = nrow(asteroids) - y)
  
  result <-
    crossing(a=coords, b=coords) %>%
    as.list() %>%
    bind_cols() %>%
    # filter(!(x == x1 & y == y1)) %>%
    mutate(
      slope = (y - y1) / (x - x1),
      d = (x - x1)^2 + (y - y1)^2
    ) %>%
    group_by(x, y, slope) %>%
    arrange(d) %>%
    slice(1) %>%
    ungroup() %>%
    count(x, y) %>%
    arrange(desc(n))
  result
  
  lst(answer = result$n[[1]], result = result, p = ggplot(result, aes(x, y, label = n)) + geom_point() + geom_label())
}

# COMMAND ----------

library(testthat)

# COMMAND ----------

test_that("example map 1 works", expect_equal(find_max_asteroids("......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
")$answer,
  33
))

test_that("example map 2 works", expect_equal(find_max_asteroids("#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
")$answer,
  35
))

# COMMAND ----------

test_that("example map 1 works", expect_equal(find_max_asteroids("......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
")$answer,
  33
))
  expect_equal(
    find_max_asteroids("#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
")$answer,
    35
  )
  expect_equal(
    find_max_asteroids(".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
")$answer,
    41
  )
  expect_equal(
    find_max_asteroids(".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
")$answer,
    210
  )
})

# COMMAND ----------

find_max_asteroids("......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
")$answer

# COMMAND ----------

find_max_asteroids(".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
")

# COMMAND ----------

find_max_asteroids("#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
")$answer