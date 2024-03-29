# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 18: Settlers of The North Pole ---</h2><p>On the outskirts of the North Pole base construction project, many Elves are collecting <span title="Trade wood for sheep?">lumber</span>.</p>
# MAGIC <p>The lumber collection area is 50 acres by 50 acres; each acre can be either <em>open ground</em> (<code>.</code>), <em>trees</em> (<code>|</code>), or a <em>lumberyard</em> (<code>#</code>). You take a scan of the area (your puzzle input).</p>
# MAGIC <p>Strange magic is at work here: each minute, the landscape looks entirely different. In exactly <em>one minute</em>, an open acre can fill with trees, a wooded acre can be converted to a lumberyard, or a lumberyard can be cleared to open ground (the lumber having been sent to other projects).</p>
# MAGIC <p>The change to each acre is based entirely on <em>the contents of that acre</em> as well as <em>the number of open, wooded, or lumberyard acres adjacent to it</em> at the start of each minute. Here, "adjacent" means any of the eight acres surrounding that acre. (Acres on the edges of the lumber collection area might have fewer than eight adjacent acres; the missing acres aren't counted.)</p>
# MAGIC <p>In particular:</p>
# MAGIC <ul>
# MAGIC <li>An <em>open</em> acre will become filled with <em>trees</em> if <em>three or more</em> adjacent acres contained trees. Otherwise, nothing happens.</li>
# MAGIC <li>An acre filled with <em>trees</em> will become a <em>lumberyard</em> if <em>three or more</em> adjacent acres were lumberyards. Otherwise, nothing happens.</li>
# MAGIC <li>An acre containing a <em>lumberyard</em> will remain a <em>lumberyard</em> if it was adjacent to <em>at least one other lumberyard and at least one acre containing trees</em>. Otherwise, it becomes <em>open</em>.</li>
# MAGIC </ul>
# MAGIC <p>These changes happen across all acres <em>simultaneously</em>, each of them using the state of all acres at the beginning of the minute and changing to their new form by the end of that same minute. Changes that happen during the minute don't affect each other.</p>
# MAGIC <p>For example, suppose the lumber collection area is instead only 10 by 10 acres with this initial configuration:</p>
# MAGIC <pre><code>Initial state:
# MAGIC .#.#...|#.
# MAGIC .....#|##|
# MAGIC .|..|...#.
# MAGIC ..|#.....#
# MAGIC #.#|||#|#|
# MAGIC ...#.||...
# MAGIC .|....|...
# MAGIC ||...#|.#|
# MAGIC |.||||..|.
# MAGIC ...#.|..|.
# MAGIC 
# MAGIC After 1 minute:
# MAGIC .......##.
# MAGIC ......|###
# MAGIC .|..|...#.
# MAGIC ..|#||...#
# MAGIC ..##||.|#|
# MAGIC ...#||||..
# MAGIC ||...|||..
# MAGIC |||||.||.|
# MAGIC ||||||||||
# MAGIC ....||..|.
# MAGIC 
# MAGIC After 2 minutes:
# MAGIC .......#..
# MAGIC ......|#..
# MAGIC .|.|||....
# MAGIC ..##|||..#
# MAGIC ..###|||#|
# MAGIC ...#|||||.
# MAGIC |||||||||.
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC .|||||||||
# MAGIC 
# MAGIC After 3 minutes:
# MAGIC .......#..
# MAGIC ....|||#..
# MAGIC .|.||||...
# MAGIC ..###|||.#
# MAGIC ...##|||#|
# MAGIC .||##|||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC 
# MAGIC After 4 minutes:
# MAGIC .....|.#..
# MAGIC ...||||#..
# MAGIC .|.#||||..
# MAGIC ..###||||#
# MAGIC ...###||#|
# MAGIC |||##|||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC 
# MAGIC After 5 minutes:
# MAGIC ....|||#..
# MAGIC ...||||#..
# MAGIC .|.##||||.
# MAGIC ..####|||#
# MAGIC .|.###||#|
# MAGIC |||###||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC 
# MAGIC After 6 minutes:
# MAGIC ...||||#..
# MAGIC ...||||#..
# MAGIC .|.###|||.
# MAGIC ..#.##|||#
# MAGIC |||#.##|#|
# MAGIC |||###||||
# MAGIC ||||#|||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC 
# MAGIC After 7 minutes:
# MAGIC ...||||#..
# MAGIC ..||#|##..
# MAGIC .|.####||.
# MAGIC ||#..##||#
# MAGIC ||##.##|#|
# MAGIC |||####|||
# MAGIC |||###||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC 
# MAGIC After 8 minutes:
# MAGIC ..||||##..
# MAGIC ..|#####..
# MAGIC |||#####|.
# MAGIC ||#...##|#
# MAGIC ||##..###|
# MAGIC ||##.###||
# MAGIC |||####|||
# MAGIC ||||#|||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC 
# MAGIC After 9 minutes:
# MAGIC ..||###...
# MAGIC .||#####..
# MAGIC ||##...##.
# MAGIC ||#....###
# MAGIC |##....##|
# MAGIC ||##..###|
# MAGIC ||######||
# MAGIC |||###||||
# MAGIC ||||||||||
# MAGIC ||||||||||
# MAGIC 
# MAGIC After 10 minutes:
# MAGIC .||##.....
# MAGIC ||###.....
# MAGIC ||##......
# MAGIC |##.....##
# MAGIC |##.....##
# MAGIC |##....##|
# MAGIC ||##.####|
# MAGIC ||#####|||
# MAGIC ||||#|||||
# MAGIC ||||||||||
# MAGIC </code></pre>
# MAGIC <p>After 10 minutes, there are <code>37</code> wooded acres and <code>31</code> lumberyards.  Multiplying the number of wooded acres by the number of lumberyards gives the total <em>resource value</em> after ten minutes: <code>37 * 31 = <em>1147</em></code>.</p>
# MAGIC <p><em>What will the total resource value of the lumber collection area be after 10 minutes?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "|....|....||.##|.|.|.##.|....|..#|#|#.#|.#|#|....#
.#...#.#....#|..#.#||........|.#.#.###.|.#||##..#.
....|..#####...|.##.#.|.|.|||.|#...|..|....##|#.||
|..#..|..#|#|.....#..|.....#........#....|..#..#..
..#|##..##..#.........|##.|..#.|.|....|#.||#.##...
.......|...|#..####.|#..#.||...|#.......|..|.|.#|#
....|||............|..#|.#..|.|.|...|...........|.
.|##.|.|...#...|||..#.#.##.|.#.|..||#.#....#......
.#..#|....#...#.#..|..#.#...#..|#||....#...#||#..#
#|...||.|#.#.|..##|..#..|......|..|....|#.|##.....
#.#|...##.|..##...||#.|..#|.|..|.|..#....#....#|..
##|||...##.....#|..||.||..|...#.###|.#..#.#..||.##
#|.|...|#...#..#.........#..#.##..#.|##.|.|.#####.
#.#..|.#.#.#|...#....|.|##.|....#..|#....|.#.#....
........|##.|...|...|....#..#..|..|#....#..#|#.|..
...#|.|.......||.|..#..|..#....|||#|.|........|##.
...##|.....|...|.#|.|.|.#|..##|..|#...#|||..#.#.|.
...|...#..|....#...###||##..|..#|.|..##|.#.||.....
...........#.|#..#.#|.|.#.#.......||.#..|.....#..#
.#..#.#....#|.|###...##..#.##|.|#..|....|#....#|.#
.#|....|.|..#..#.....#.#.|...#.....||.|.......#|.#
.|#...#.##...||||.#..#.....|#.||#.#....#|#...#|...
..#...#.#.|...#|.......#|##|.|.#.||.#|.#...|#.....
.......#....###|....||......|....|.....##.|.|.|...
|.|.|.|.#.#..##......#..|..##.#....#.#|....#.|..#.
.|...||...#.##..#..||...##..|.|.#.#.|.|....#......
....|......|..|.|.##.#.|.#.||........|.|#|.#.|..#.
.#.#...#...||..|.......||#.#|..|#||||..#|......|..
|||#.|#.|.##.#....#.#.|||||.....||.||.||.#|.##|#.#
........#|.|##..##.|......#||.|.#......#.....##.##
..||..#|.|.#..|#...#.....|..|#.||.#.|#.|#...#.|...
|#..#...|....|.........|.|##.#..#|##||#...#..#.|#.
...##..#.#..#|...#.|##...#....#....#|...#|..|.|.#.
.#|.......#|.||#..||#.#..|#.|.|..#.#..|..|..#..|..
#.|#.#|...|.#.#|..#..|...|#||#|.|#........|....|..
|.|||.|.|##||...|.|#..#|||.#.###||.#|.###...#....#
.##....#..|#.........#.|..|..||.#|..#|##|.#.....##
.....|#.#...|....#......||..|...|...#.....#.||..##
#|.|#..##.....|##....|.#.#.||.|.......||#.#.#..|#.
.#...#|.#.#||...|#..##.|..##.|.#|.||##.|.......||.
.|...#..|..#.##.#|||#####|.|....|#..###.|#.#..|.#|
...##.....||..|......|.#|.|.|.|.|..#.......##.|#..
|...|..|.#|..#|##.##...|.#|.#|#.......|.#.|#||.|..
.|..######......#|.#...#.#.|.#|...#..|....|..|..||
|#.#.#..|.|#|....##.||....#...#..|....#.|||.|##.|.
#|...#.#||..|...|.....###|.#....#|....|#...|..#.#.
..#|.||..#..#.......##...#|..#.##..#....||.|.|.##|
.||#.##.###..#|...........#....#|.#..#.##.|#.#...#
.##|##..#.|#.|......#..|#...#.....#.|.|#|...|.|...
..#.....##..#.#|#.#.....|#...#..|.#.|.|#|....#..|.
"

# COMMAND ----------

m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

# COMMAND ----------

get_adjacent_squares <- function(m, row, col) {
  c(
    tryCatch(m[row - 1, col - 1], error = function(e) NULL),
    tryCatch(m[row - 1, col + 0], error = function(e) NULL),
    tryCatch(m[row - 1, col + 1], error = function(e) NULL),
    tryCatch(m[row + 0, col - 1], error = function(e) NULL),
#   tryCatch(m[row + 0, col + 0], error = function(e) NULL),
    tryCatch(m[row + 0, col + 1], error = function(e) NULL),
    tryCatch(m[row + 1, col - 1], error = function(e) NULL),
    tryCatch(m[row + 1, col + 0], error = function(e) NULL),
    tryCatch(m[row + 1, col + 1], error = function(e) NULL)
  )
}

step <- function(m) {
  trees <- m
  lumberyards <- m
  trees[] <- 0
  lumberyards[] <- 0
  
  for (row in seq_len(nrow(m))) {
    for (col in seq_len(ncol(m))) {
      adjacent_squares <- get_adjacent_squares(m, row, col)
      trees[row, col] <- sum(adjacent_squares == "|")
      lumberyards[row, col] <- sum(adjacent_squares == "#")
    }
  }
  
  new_m <- m
  new_m[m == "." & trees >= 3] <- "|"
  new_m[m == "|" & lumberyards >= 3] <- "#"
  new_m[m == "#" & !(trees >= 1 & lumberyards >= 1)] <- "."
  
  new_m
}

simulate <- function(m, minutes) {
  for (i in seq_len(minutes)) {
    m <- step(m)
  }
  m
}

# COMMAND ----------

result <- simulate(m, 10)

answer <- sum(result == "|") * sum(result == "#")
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>This important natural resource will need to last for at least thousands of years.  Are the Elves collecting this lumber sustainably?</p>
# MAGIC <p><em>What will the total resource value of the lumber collection area be after 1000000000 minutes?</em></p>
# MAGIC </article>

# COMMAND ----------

minutes <- 1300
result <- m
ntrees <- integer(minutes)
nlumberyards <- integer(minutes)
for (i in seq_len(minutes)) {
  result <- step(result)
  ntrees[i] <- sum(result == "|")
  nlumberyards[i] <- sum(result == "#")
}

# COMMAND ----------

df <-
 tibble(ntrees, nlumberyards) %>%
 mutate(
   x = row_number(),
   resource_value = ntrees * nlumberyards
 )

df %>%
 select(-resource_value) %>%
 pivot_longer(-x) %>%
 ggplot(aes(x, value, col = name)) +
   geom_line() +
   theme_minimal()

# COMMAND ----------

df %>% filter(x >= 1000) %>% print(n = 100)

# COMMAND ----------

answer <- df %>% filter(x == 1000 + ((1000000000 - 1000) %% 28)) %>% pull(resource_value)
answer
