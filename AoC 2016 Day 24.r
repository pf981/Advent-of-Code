# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 24: Air Duct Spelunking ---</h2><p>You've finally met your match; the doors that provide access to the roof are locked tight, and all of the controls and related electronics are inaccessible. You simply can't reach them.</p>
# MAGIC <p>The robot that cleans the air ducts, however, <em>can</em>.</p>
# MAGIC <p>It's not a very fast <span title="The Brave Little Air Duct Cleaning Robot That Could">little robot</span>, but you reconfigure it to be able to interface with some of the exposed wires that have been routed through the <a href="https://en.wikipedia.org/wiki/HVAC">HVAC</a> system. If you can direct it to each of those locations, you should be able to bypass the security controls.</p>
# MAGIC <p>You extract the duct layout for this area from some blueprints you acquired and create a map with the relevant locations marked (your puzzle input). <code>0</code> is your current location, from which the cleaning robot embarks; the other numbers are (in <em>no particular order</em>) the locations the robot needs to visit at least once each. Walls are marked as <code>#</code>, and open passages are marked as <code>.</code>. Numbers behave like open passages.</p>
# MAGIC <p>For example, suppose you have a map like the following:</p>
# MAGIC <pre><code>###########
# MAGIC #0.1.....2#
# MAGIC #.#######.#
# MAGIC #4.......3#
# MAGIC ###########
# MAGIC </code></pre>
# MAGIC <p>To reach all of the points of interest as quickly as possible, you would have the robot take the following path:</p>
# MAGIC <ul>
# MAGIC <li><code>0</code> to <code>4</code> (<code>2</code> steps)</li>
# MAGIC <li><code>4</code> to <code>1</code> (<code>4</code> steps; it can't move diagonally)</li>
# MAGIC <li><code>1</code> to <code>2</code> (<code>6</code> steps)</li>
# MAGIC <li><code>2</code> to <code>3</code> (<code>2</code> steps)</li>
# MAGIC </ul>
# MAGIC <p>Since the robot isn't very fast, you need to find it the <em>shortest route</em>. This path is the fewest steps (in the above example, a total of <code>14</code>) required to start at <code>0</code> and then visit every other location at least once.</p>
# MAGIC <p>Given your actual map, and starting from location <code>0</code>, what is the <em>fewest number of steps</em> required to visit every non-<code>0</code> number marked on the map at least once?</p>
# MAGIC </article>

# COMMAND ----------

install.packages("combinat")

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "###################################################################################################################################################################################
#.........#...#.............#...#3#.#.....#...........#.........#.#...#.......#.#.#...#...#.................#...........#.#...#.#.......#.......#.......#...#...#.....#.....#.....#
#.#.#.#.#.#.#########.#.#.###.#.#.#.###.###.#.###.#.#.#.###.#.###.#.#.#.#.#####.#.#.#.#.#.#.###.#.#.#.#.#.#.#.###.#.#.###.#.#.#.#####.#.#.#.###.#.#.#.#.#.###.#.###.###.###.###.#.#
#...#...#...#.......#...#.#.#.....#...#.....#.........#.......#.#...#...#.#.............#...#.......#.#.#...#.#.....#.......#...#.....#...#...........#...#...#.#...............#2#
#.###.#.#.#####.###.###.#.#.#.#.###.#.#.#####.#######.#.###.###.#.#.#.#.#.#####.###.###.#.#.#####.#.###.#.###.#.#.#.#.#.#######.#######.#.#.###.###.###.#.#.#.#.#.#.###.#.###.#.###
#.......#.........#.#.#...#...#...#.....#.#.............#.....#...#.......#.#.....#...#...#.......#.............................#.#...#...#...#.....#...#.......#.......#.......#.#
#.###.#.#.#########.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#####.#.#.#######.#.#.#.#.#.#.#####.#.###.#.#####.#.###.###.#.#.###.###.#.#.#.#####.#.###.#.#.#.#######.###.#.#.#.###.###.#
#...#.#...#...#...#...#.#...#.....#...#...........#.....#.........#.#...#...#...#.#...#.......#...#.#.....#.#.....#...#.#.......#.#.#.......#.......#...........#.#.#...#.#.......#
#.#.#.###.###.#.#.#######.#.#.#.#.#.#.###.###########.#.#.#####.###.#.#.#####.#.#.#.#####.###.#.###.#####.###.#####.#########.#.###.#.###.#.#.#.#.###.###.#.#####.#.#.#.#.#.###.#.#
#.......#.......#...........#...#.#...#.............#.#.#...#...#.....#...#...#.#...#...#.......#.#.#.#...#.....#.#.#.........#...#...#.....#.#...........#.#.......#.#.#...#...#.#
#.#.#.###.#####.#.#####.#.###.#.#.#.###.#.#.#.###.###.#.#####.###.#####.#.#.#####.#.#.#.#######.#.###.#.###.#####.#.#####.#.#.#####.#.#.#.#.###.#.#######.#.#.#.###########.#.#.#.#
#.#.#.....#.#1..........#.#...#...#.....#.........#...............#.#...#.....#...#.......#...........#.#...#.#.....#.............#.............#.....#...#.....#...#.....#.#.....#
#.#.###.#.#.#####.#.#.#.###.#####.#.#.#.###.###.#.#.#.#####.#.#.###.#.#.#####.#.#.#.#.#.#.###.#.###.#.#.#.#.#.#.###.#.#.#####.###.###.###.#.#.#.###.#.#.#.#.#.###.#.#.#####.#####.#
#...#...#.#...#.#.#.#.#.......#.....................#.#...............#.......#.#...#.#.#.....#.#.#...#...#.#.......#.....#.#...#.........#.#.#...#.........#.............#.....#.#
#.###.###.###.#.#.###.#.#####.#.#####.###.###########.###.#.#.#####.#.#.#.###.###.#.#.#.#.###.#.#.#.#.###.#.###.#.#########.#.#.#.#.###.#.#.#.#.#.#.#.#.#.###.###.#####.#.#####.###
#.....#.#.......#.#.#.....#...#.......#...#.#...#.............#.#.#.....#.........#...#.#.........#.#.#.#...#.#...#...#.......#.....#.#.....#.#.#.......#.#...#.#.....#.......#...#
#.#.###.#.#######.#.#.#.###.#.###.###.#####.#.#.#.#.###.###.###.#.#.#####.#.#####.#.#.#.#.#.#########.#.#.#.#.#.#.#.#.#.###.#.###.#.#.###.###.#.#######.#.#.#.#.#.###.#.#.#.#.###.#
#.#.#.......#...#...#.#.#.#.....#.....#...#...#.....#...#...#...#...........#...........#.........#.#.....#.....#.......#...#...#...#.#...#.#.#.........#...#.....#.#...#.#.....#.#
#.#.#.#####.#.#.#.###.###.#.#.#####.#.###.#.#.#####.#.#####.#.#.#.#####.###.#.#.#.#.###.#.#.#.#.#.#.#.###.#.#####.###.###.#.#.#.#.#.#.#.#.#.###.###.#.#######.#####.###.#.###.###.#
#.#.......#.#...#.#...#.#.#.......#...#.....#.........#.....#.#.....#...#...#.#.#...#.....#...#...#...#.....#.......#.#.#...#.#.........#...#.#..4#.#.#.#.#.....#.....#.........#.#
#.###.#.#.#.###.#.#.###.#.#######.#.#.###.#.###.#.#.#.#.#.#.###.#####.#.###.#######.#####.###.#.#.#.#.#.###.#.#####.#.#.#.#.#.#.#.#.#.#.#.#.#.#######.#.#.#.#.#.#.#.#.#.#.###.#.#.#
#0#...#.#.#.....#...#...#.#...#...#...#...#.......#.#.#.....#...#...#...#...#...#...#.........#.......#...#.......#...#...#...#.......#...#...............#.....#...#...#...#.#...#
###.#.#.###.###########.#.#####.###.###.###.###.###.#.###.#.#.#.#.#.#.#.#.#.#.###.#.###.#.#.#.#####.#.#.#.#.#.#.#.#.#.#.#.###.#####.#.#####.#.#.#.#####.#.#.#####.#####.#.#.#.#.###
#...#.#...#.......#...#...........#...#.....#...#...#.#.........#.....#.#...#.......#.....#.#.#.........#.........#...#.#.#...#.#.....#.....................#...............#.....#
###.#.#.#.#.#.###.#.#.#.#.#######.#.#.###.###.#.#.#####.###.###.###.###.#.#.#.#.#######.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#.#####.###.#######.###.###.#.###.###.###.###.#.#.#
#...#.............#.#...........#.#.#.....#.....#.......#.#.....#...#.........#.....#.......#.....#...#.....#...#.......#...#...#.#.........#...#...........#.......#...#.......#.#
###.#.#########.#.#.#####.#.#.#.#.#.#.###.#.#######.#.#.#.#.#.#####.#.#.#.#####.#.#.#.#####.#######.#.#.#.#.#.#####.#.#.#.#####.#.#.###.#######.#######.#.#.###.#.#.#.#.#.#.###.#.#
#.#...............#.#.......#.....#.................#...#.#.#.......#...#.......#.#.#...#.#.......#...#.....#.....#...#.#.......#.#.#.....#.....#.....#.#...#.#...#...#.#...#.#.#.#
#.#.#.###.#.#.#.#.#.#.#.#.#.#########.#.#.#.#.#.#.#.#.#.#.#.###.#.#.#.###.#.#.#.#.#.###.#.#.###.#.#.###.###.#.#.#####.#####.#####.#.#.#.#.#.#.###.#.#.#.###.#.#.#.#.###.#.#.#.#####
#...#.#.....#...#.............#.#.#.#.........#.#...#.#.....#.......#...#.#.#.....#.......#...#...#...........#.....#.#.......#...#...#.#.........#...#...#.....#.......#...#.....#
###.#.#.#.#.#.#.###.#.###.#.###.#.#.#.#.###.#.###.#.#.#####.###.###.#.#.#.###.#.#.###.###.###.#.#.#.#.###.#####.###.#####.#.#.###.###.#####.#####.#.#.#######.###.###.###.#.#.#.#.#
#...#.#.....#.........#.......#.#...#.......#...#...#...........#.....#.......#...........#.......#...#...#.....#.....#...#.......#.#.#...#.#.....#.........#.....#...#.#...#.#...#
###.###.###.###.#.#####.###.#.#.#.#.#.###.###.###.###.#.#####.#.#.#.#.###.#.#.###.#.###.###.#.#.###.###.#.#.#.#.#.#.#.#.#.#.#.#.###.#.###.#.###.#.#.#####.#.#####.#.#.#.#####.#.#.#
#.#.#...#.#.#...................#.......#.#.#.#.#.....#.#.#.....#...#.......#.#...#.......#.....#...#.....#...#...#.#...#...#.........#...#...#...........#.........#.#..5#...#...#
#.#.#.###.#.###.#####.#.#.###.#.#####.#.#.#.#.#.#.###.#.#.#.#######.###.#.#.#.#.#.###.#.#.#.###.#.#####.#.#.#.#####.#.###.#.#.###.###.#.###.#.#.###########.#.#######.#.#.#.###.###
#...#.#.#...#.#.................#.#.....#.#.........#.....#.#.#...#.#.........#...#.#...#.#.........#...#...#.....#.#.#.#.....#...#.#.....#.#.............#.#...#.#.#.....#...#...#
#.#.###.#.#.#.#.#.#.#.#.###.###.#.#.#######.#######.###.#.#.#.###.#.#.#####.###.###.#####.#.#####.#.#.#.#.#.#.###.#.#.#.#.###.#.#.#.#.#.#.#.#####.#.#.#.#.###.#.#.#.#.#####.###.#.#
#...#.....#.....#.....#.#...#...#...............#...#...#...#.....#...#.#.....#.#.#...#...#.#...#...#.....#...#...#...................#.........#...#.........#.#...#.......#...#.#
###.#.###.#.#.#.###.#.#.#.#.#.###.###.#.###.###.#.###.#.#######.#.#.#.#.#.#####.#.#.#.#.#.###.#.#.#.#####.#.#.###.#.#######.#######.###.#######.#.#.#.#.###.###.###.#.#.#.#.#.#.#.#
#.....#7..#.#.#...........#.#...#.........#.....#.#.#...#.....#.............#...#...#...#.#.#...#.......#...#.....#.#.......#.#.....#...#...#...#...#...#...#.#.....#.#.......#.#.#
#.#.#.#.#.#.#.#.#.#.###.#####.#.#############.#.###.#.#.#.#.###.###.#######.#.#.###.#.###.#.###.#######.###.###.#.#.###.#.#.#.#.#.###.###.###.#.#.###.#.#.#.#.#.#.###.#.###.#.#.###
#...#.....#.#...#.#.....#.....#...#...#.......#6#.......#.#.......#.#.........#...#.#.....#.....#.#.......#.#.......#.......#.....#.....#.....#...#.#.#.#...#.#...#.#...#...#.#.#.#
###################################################################################################################################################################################
"

# COMMAND ----------

# input <- "###########
# #0.1.....2#
# #.#######.#
# #4.......3#
# ###########
# "

# COMMAND ----------

m <-
  input %>%
  read_lines() %>%
  str_split("") %>%
  simplify2array() %>%
  identity() %>%
  t()
m

# COMMAND ----------

visited <- m == "#"
visited

# COMMAND ----------

pois <- m
pois[] <- m %in% seq(from = 0, to = max(m), by = 1)
class(pois) <- "logical"
pois

# COMMAND ----------

pois_df <-
  which(pois, arr.ind = TRUE) %>%
  as_tibble() %>%
  add_column(name = m[which(pois, arr.ind = TRUE)])
pois_df

# COMMAND ----------

# Get shortest path from any POI to any other POI

# COMMAND ----------

combinations <-
  crossing(
    pois_df %>% rename_all(~str_c("from_", .)),
    pois_df %>% rename_all(~str_c("to_", .))
  ) %>%
  filter(to_name > from_name)
combinations

# COMMAND ----------

shortest_distance <- function(from_row, from_col, to_row, to_col) {
  rows <- c(from_row)
  cols <- c(from_col)
  ds <- c(0)
  v <- visited
  
  repeat {
    i <- which.min(ds)
    row <- rows[i]
    col <- cols[i]
    d <- ds[i]
    
    rows <- rows[-i]
    cols <- cols[-i]
    ds <- ds[-i]
    
    for (new_pos in list(c(row - 1, col), c(row + 1, col), c(row, col - 1), c(row, col + 1))) {
      if (v[new_pos[1], new_pos[2]]) next
      v[new_pos[1], new_pos[2]] <- TRUE
      
      if (new_pos[1] == to_row && new_pos[2] == to_col) return(d + 1)
      
      rows <- c(rows, new_pos[1])
      cols <- c(cols, new_pos[2])
      ds <- c(ds, d + 1)
    }
  }
}

# COMMAND ----------

distances <-
  combinations %>%
  mutate(
    d = pmap_dbl(lst(from_row, from_col, to_row, to_col), shortest_distance)
  ) %>%
  {bind_rows(
    mutate(., lookup = str_c(from_name, "-", to_name)),
    mutate(., lookup = str_c(to_name, "-", from_name))
  )}
distances

# COMMAND ----------

get_total_distance <- function(poi_seq) {
  inner_join(
    tibble(lookup = str_c(poi_seq, "-", lead(poi_seq)) %>% head(-1)),
    distances
  ) %>%
    pull(d) %>%
    sum()
}

# COMMAND ----------

answer <-
  distances$to_name %>%
  unique() %>%
  combinat::permn() %>%
  map(~c("0", .)) %>%
  map_dbl(get_total_distance) %>%
  min()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Of course, if you leave the cleaning robot somewhere weird, someone is bound to notice.</p>
# MAGIC <p>What is the fewest number of steps required to start at <code>0</code>, visit every non-<code>0</code> number marked on the map at least once, and then <em>return to <code>0</code></em>?</p>
# MAGIC </article>

# COMMAND ----------

answer <-
  distances$to_name %>%
  unique() %>%
  combinat::permn() %>%
  map(~c("0", ., "0")) %>%
  map_dbl(get_total_distance) %>%
  min()
answer
