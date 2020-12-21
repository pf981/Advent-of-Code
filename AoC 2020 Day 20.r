# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/20

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Tile 1621:
.#.##...#.
#..#..#.#.
#.#..#..##
.....#..#.
.#..#...##
#....#...#
.#........
#.#.#....#
...#...#..
.#..#....#

Tile 3671:
..#.#.###.
#.##....##
#.........
##..#.#...
#..###....
..#.#....#
##..###..#
..#......#
.........#
......###.

Tile 2803:
#.#.#..#..
#.....#...
...##..###
#.#.....##
#...#..#.#
..#...##.#
..#...#..#
####.#..##
#..##....#
#..#.##.#.

Tile 1531:
####.#####
.###...###
##..#..#.#
##.#..#..#
#....#..##
##.#....#.
#.#.##....
....#..#..
#...#.....
##....#...

Tile 1811:
#.#...#..#
##....#.##
#...##.#..
#..##.....
.#.#.....#
##..#.....
##.#......
..#...##..
.#.##....#
##...##..#

Tile 2143:
##.###.#.#
#..##.##..
###.......
..##.#...#
#.......#.
#.#....##.
...#..####
..##...#.#
#.#..#.##.
#.#.#...##

Tile 2887:
.......##.
#..#..#..#
....#.....
...#..##..
..#.......
#...##..##
..#...##..
#.....#.##
##..#..##.
#...#.####

Tile 3511:
.#.##....#
#.#...##.#
#...##.###
....#.....
..#......#
.###.#..#.
#.........
#.#....###
.......#.#
#..#######

Tile 3911:
.#..#.###.
#...#.##..
.#..#...##
##.#.##.##
....#.#..#
...###....
.....#...#
...##..#..
###.#.#.#.
##.....#.#

Tile 3821:
#####..#..
##..#.....
....##.#.#
#....#....
#...##.#.#
#........#
####......
#.#.#....#
....######
..#...###.

Tile 3539:
#####.##..
#........#
####.#....
.##..#.#.#
#.....#...
#.#......#
##...###.#
.#..#.....
#.#.......
...#...#..

Tile 3251:
....#..##.
.###.#...#
#..#.....#
...#.....#
..#.......
.##..#...#
#.......##
#.....#...
....#..#.#
######.#.#

Tile 2677:
.#...#...#
...#.###..
......##..
#.##.##...
#.#...#.##
#..#####..
......##..
......##.#
#..#..#...
..##.####.

Tile 3011:
#.#..#..##
#.###..#..
#..#..##..
#.#..#...#
##...#####
....#..###
.#..#..#.#
..#...#..#
##.##..#.#
.#.##.....

Tile 1489:
#...##.###
#.#..#....
#.....#..#
##..#.....
...#....##
.##.##.#.#
#.#......#
#........#
....#.....
##.#.#####

Tile 3769:
.....####.
##....####
###....#.#
.##..#.#.#
..........
##....####
#...#..#..
...#.....#
##.#.....#
#...##.###

Tile 2293:
.#..#.#...
####......
##...#....
###.#.#...
.##.##...#
......#.#.
##.....#..
#..#.##.##
.##....##.
.#.....#..

Tile 3947:
.#.#...##.
..........
..#...##.#
..###..#.#
##...#.###
.#..#..#..
#.#....#..
....#.#..#
.#....####
######..#.

Tile 1223:
#..#####.#
###..#..##
##.###....
...##.#...
..#.##.#..
##.###...#
...#..#.##
...#..#...
.#....#..#
#..####...

Tile 3331:
#.....##..
##..###.#.
.##.#...#.
.##..#.#..
#......#..
...#.....#
###.#.#...
.##......#
#..#......
...#...###

Tile 3691:
#..#..#.##
......#..#
#.#..##..#
###.......
#.#....##.
##.#..##..
#......#..
..#.......
...#.#..#.
#..#......

Tile 1289:
#.......#.
##.##....#
####......
.#..#.#..#
#.#.#..###
#..#......
##.#####..
.#........
##.##....#
##.#######

Tile 2857:
.#.#..#.##
.....#.#..
#..#...#..
.##...#..#
##..#..#.#
#..#..#..#
...#......
#.#.#.....
##...#....
....#.##..

Tile 3559:
#.##..##..
..#.##.###
##..#....#
#.#..#..#.
##.####..#
.....#...#
#....#....
##..#.##..
#..#.....#
###.##..##

Tile 2633:
...#.#..##
##.......#
#...##..#.
#.#....#.#
.........#
...#.....#
.#.##....#
...#..#...
#.#.##....
..#..##...

Tile 1973:
#.#.....#.
#.......#.
#....#....
.#.#...##.
.........#
#.......#.
...#.##..#
.##...#...
##..#..#..
####..##.#

Tile 1373:
#####.#..#
##.##..###
#.####...#
..###.#...
....##...#
#...#....#
##.#....##
.......#..
##.#.##.#.
#.###.##.#

Tile 1759:
.#.....##.
#.#..#...#
....###..#
........##
....#.....
.....#..#.
#...#....#
.#..#...#.
...#.#.#..
##...#..##

Tile 1213:
#....###.#
###...##.#
.#.....#.#
#......##.
.#...#.##.
.##.......
....##...#
#.........
.........#
#.....#.##

Tile 2341:
#.....#.#.
...##.#..#
.....##..#
......##.#
#...#....#
..#...###.
..##.#.#.#
.#.#....##
.#.....###
.#.#...##.

Tile 3547:
####.#.#.#
...###...#
#..#.##...
##..#.#...
#....#.#.#
.#.......#
.#.#......
###.....#.
#.#....###
.#.##.#...

Tile 2003:
#####.####
...#..#..#
.#.......#
#.#.#...##
.#.#.#..#.
#......#..
...#..#...
.#...#.#..
#........#
####.###..

Tile 2861:
#..##.##..
..#.#....#
....##.#..
##........
#.........
##.....#.#
##.....##.
####.....#
###..#####
.........#

Tile 3697:
#..##.####
.....#....
#.#.#.#.#.
#.##...###
..##.....#
.#.......#
.##.......
#.#..#...#
.#.###.#..
####.####.

Tile 3929:
.#.##..#.#
##.#....##
....#.#..#
....#.#.#.
##........
...#..#...
###....#.#
#........#
.###.##.##
###..#####

Tile 3527:
#.#.#...#.
####.#....
......#...
.##......#
.#......##
.##.#.#.##
#..#......
#.....#...
.#........
..#..####.

Tile 1777:
.#..#...##
#....###..
..#..##.##
..##...#..
....#.#...
#...##.#..
#..##.#..#
...##.....
.#....#..#
.#..#..###

Tile 1543:
......#...
.#...##...
#...#..#.#
..........
#..##....#
..#.#...##
...#.####.
##....#...
...#..####
.#.#..####

Tile 2063:
##....#...
#.....#...
###.##...#
......#..#
...##..#..
###.#.....
##.....##.
#..#.##...
##.###..##
#....###..

Tile 1181:
#.##...###
####.#....
.........#
####..##.#
.....#..#.
.......#..
..###....#
##..##....
#.#...#..#
.#.#.#...#

Tile 3491:
#...###.##
..##..#.##
.......##.
..........
.....#..#.
#..#......
##....#.#.
...##...#.
..###.....
..#.##..#.

Tile 1873:
...#.....#
...#.#..#.
##.#......
.#...#.###
#.#.#..#..
.....###.#
#..#..#...
....#.....
.....#.#.#
######...#

Tile 2579:
.####...#.
#..#..#..#
.....#...#
#.#..#...#
#.....##..
......#..#
#......##.
.#...##...
.#...##...
.##.####..

Tile 1481:
.#.#.#####
..#.#.##..
.###...#.#
...##.....
..#.#.#.#.
.#.......#
##.#....#.
#.#...#...
.###..#...
......##.#

Tile 2417:
.#..#..#.#
.#.#.....#
.###..##.#
#.#.#.....
#....#.###
..#..#....
#....#.#..
####....##
..#.#...##
....######

Tile 3581:
..##.....#
.....##..#
#.........
#....##..#
#..#....#.
#.....#..#
.#..#.#.#.
...#......
.....##..#
#.........

Tile 3593:
#.##.###..
###.....##
##.#....#.
###.#....#
###....#.#
#.#..#..##
......#.##
...#....#.
.#...#..#.
..#####..#

Tile 3167:
#...#.#.#.
......#.##
##.##.#.##
#...#.##.#
....#...#.
..#....##.
...#...##.
...##..#..
....#.##.#
##.#....#.

Tile 1439:
...##..###
#.#......#
..#..###.#
....#.#...
#.........
......#..#
..#.#.#..#
##.#.#....
..#...#..#
#.###.#...

Tile 1249:
..#.##...#
#.#......#
.......#..
##.#.#.#.#
.#..#..#..
..#.#..#.#
.....##.#.
#........#
..#..##.##
..#..#####

Tile 2687:
##...##...
###.###.#.
#...###..#
.#.......#
....#.#...
.....#####
##.#####..
#....#....
..#.####.#
##....#.#.

Tile 2693:
..#..#..#.
....#..###
....##....
.#.##.....
.#..###...
..##.#....
#.........
....##.##.
..#..#....
.#.#......

Tile 1741:
.#.###..##
......####
#.......##
#.#......#
##..#...#.
##.....#.#
#..#......
..##.#..##
#..#......
#.#..###.#

Tile 3413:
...####.#.
.#..#.##..
#....#.##.
##.#.....#
##.###..##
.......###
.#....###.
#....##..#
##.####..#
....#.###.

Tile 3191:
.....####.
##.##..#..
.##.#.##.#
.......###
....####..
.#.#..#.#.
...#...#..
##..#..#.#
...#..#...
..##..#.#.

Tile 2897:
#.#######.
...#....#.
#.....##.#
###.#...#.
##.#####.#
..#.##..##
#.##......
##.#.##..#
#.#....#..
#.##.#.###

Tile 2017:
##.##...##
#...#.##..
#..#.#...#
.##.......
##.......#
##..#.#..#
##.#.#.#.#
..........
..........
..######.#

Tile 2939:
#...##.##.
.....#.##.
....#.#...
#.#......#
.#.....#.#
.........#
###.....##
......#..#
#..#..##..
.##..#.##.

Tile 1753:
#...#.#.##
.#...#...#
###..#.###
#..##....#
#..#......
#.##...#..
..#...#...
#..#......
.#.......#
....#.#.##

Tile 3229:
#..####.#.
#.....#..#
......##..
#.#...##.#
#...#...##
#.#....#.#
.#..##..#.
#..#.....#
#..##.....
.#.#.#..##

Tile 1367:
####.....#
...#.##...
...#...#..
.#.###..#.
.........#
.#........
..........
.#...###.#
##........
...##..#.#

Tile 2851:
..#.#...##
#.....##.#
.##.#..#.#
#...###..#
###...#...
....#..#.#
..#.......
#.....#...
...#.#...#
.###..#..#

Tile 2357:
....##.#.#
###...#.##
####..##.#
#.####...#
#...##...#
#.#......#
#..##.#.#.
#.#....#.#
.###...#..
####..#.##

Tile 1697:
#..#.#.##.
.......#..
...##....#
##........
....#....#
##.#.....#
.##......#
#....#..#.
##.##...##
#....#...#

Tile 1571:
#.###...#.
##..#..#..
.........#
...#.#.#..
#........#
#..##.#...
##...##.#.
..........
....#.#...
.##.....#.

Tile 3323:
#.#.#..###
#...#...##
.......#.#
#.##......
..#.#..##.
#.......#.
....####.#
....##...#
..##....##
######.###

Tile 3461:
#....##.#.
....#.....
#......##.
##.....##.
#..#...##.
.#.......#
##.#......
..........
.....#..##
.....#.###

Tile 2719:
.#.#.#....
..#..#.##.
..##...###
..#..#...#
##.......#
.#........
.##..#....
..##..#...
..#....#..
.#.#.#..#.

Tile 3359:
.###...#.#
.....###.#
#..####.#.
.....##..#
..#.#...#.
#.#..###..
..#....#.#
....#.#..#
.....#..#.
#.###.#..#

Tile 3803:
.####.#..#
...#...###
.......##.
.......##.
#..#..#..#
##...#....
....##....
##........
..#..#####
..#..##...

Tile 3019:
##..###.#.
..#.......
##..#.##.#
##......#.
#......#..
#.#....#..
.###.###.#
#..#.##..#
###.##.#.#
.###.###.#

Tile 2791:
......#.#.
#....#....
##...#####
....##....
#.....##.#
..##......
#.#...#..#
...##...#.
..##....#.
##.##..#..

Tile 3881:
#....##..#
...#..#..#
.###..#..#
...#....##
#...#..#.#
#.#.#..#.#
#..##.....
...#......
#.#....#..
.#..##.###

Tile 2087:
.#..#.#...
###....###
.###..#.##
........##
###.##..##
...#...#.#
#...#....#
##..#....#
#..####.#.
##..#####.

Tile 1789:
######.#..
........#.
..#...##.#
.#.......#
.#...#....
#..#.#..##
#####.#..#
#...###..#
.#.#....##
####.##.#.

Tile 2539:
#.###.#..#
..#..#...#
##.##.#...
#.....##..
#..##..#..
..###.##.#
#..###...#
.###.#.#..
#...#.....
..###.##..

Tile 2111:
####..###.
#....###..
..#.....##
#....##.##
#.....#...
#..#.#....
...#..####
##..##..#.
##.....#.#
#.#...#.#.

Tile 1433:
#.....#..#
.#.###.#.#
.#...#.#.#
.......###
#..##.#...
.#...##.#.
#..#....##
#......#..
....#..#.#
..#.#..##.

Tile 1667:
..##......
#..#....#.
.##.#..#.#
.....#....
#.#.##..#.
...##.....
..#.#....#
#.#..#...#
...#...##.
....#....#

Tile 2389:
.#.#...#..
.#.......#
.....#....
#...###..#
..........
.#........
.#.###.#.#
#....#..#.
..#......#
##...#...#

Tile 1069:
...###..##
...#.....#
##......##
....##....
..#..##..#
##..#..#.#
##.#.#.#.#
.#..###..#
#.#.......
.#.#.#....

Tile 1103:
..###.##..
...##..#.#
#....##..#
....#..#.#
#....#.#..
###....###
..#...##..
..##.....#
#........#
.####..#..

Tile 3761:
....#.##..
###.......
#...#.....
..##.#...#
#........#
.###......
...#..#...
...#.#.#..
#....#.#.#
....#...#.

Tile 2473:
........##
.#.#..#...
.#........
.####.#.##
##..##...#
##.....#..
###.#..#.#
..........
.#.#..##.#
..#....#.#

Tile 1987:
...#..#.#.
......#...
#....#.###
..#....#..
..#..##..#
........#.
#..#.....#
...#..#..#
.......#.#
...###.##.

Tile 1187:
..#.#.#..#
##.#...##.
#......#.#
....#....#
..##...#.#
#..#..#.##
..........
..##...#.#
...####..#
.#.#.#####

Tile 2699:
###.#.##.#
.#.#####.#
.#..#..#..
.###....##
..#..##..#
.....#...#
..........
#...##...#
#.........
##..#..#.#

Tile 3643:
..##...#..
#..#..#.##
#.###.####
..##..##..
......#...
##.##..#..
...#.##.##
....#..#.#
##..#....#
#....#...#

Tile 3463:
..###.##.#
......##.#
#........#
......##.#
##.......#
##..#..#.#
##.......#
##......#.
##.#.##...
.###..#.##

Tile 1117:
#.#.##....
..#..#.###
.#..#.....
...#.#....
........#.
##.###...#
..#..#.#.#
....#..#..
..#.#....#
..#.#..#..

Tile 1163:
.##.##..##
....#..#..
##..#..#..
#..#.....#
#..#.....#
..#.##....
...#.#....
..###..#.#
...#...#.#
###.######

Tile 3557:
#.#....#..
....####.#
.#....####
..#...###.
#......#..
.......#..
##....#...
##.....#..
...#..#.#.
...###.#..

Tile 2467:
.####....#
.#.#..##.#
####......
......#.#.
#.#....#.#
##.....#..
..#....#.#
..#.##...#
.#.....###
#...##.##.

Tile 1471:
.###..#.##
##.#...##.
.#...#....
....##..#.
........#.
##....##.#
###..##.#.
#....###.#
##.....##.
#..#..##.#

Tile 3931:
#....#..##
#...#..#..
.#..######
#.###...#.
....#.##.#
#.#...####
#....#..#.
....##.#..
#..#..####
#.#.#.....

Tile 2029:
##.#.#####
#.#......#
#...##...#
#...#.....
#..##.....
#.....##.#
....##....
..##.#.###
###.#.###.
..####.##.

Tile 1913:
#..###.###
.......###
.#..#.####
.#..#.#...
..#.......
.#....###.
.###..#.#.
#....#..#.
#.#..#.#..
.#..#.#.#.

Tile 2213:
..#.##.###
......###.
..#..#...#
#..#..#.##
#....###..
...#....#.
#.##.#..#.
##.#...#..
.##....###
####.#..#.

Tile 1511:
###.#...##
.##.....#.
.##...#..#
...##.##..
#.#..#.#.#
##...###.#
###..#.###
.##.##..#.
#......#..
###.....##

Tile 2243:
#..#.#...#
##...#....
.....#.#.#
....##..#.
#..######.
.#..#.##..
#.........
...#.##.#.
.#.......#
.##...#.##

Tile 3701:
...#######
#..#...##.
...####..#
..#..#...#
##........
#.....#..#
##..#.#...
##.#.##.#.
.##.......
###.#...##

Tile 3137:
.#.####...
#..#.#...#
.......#.#
#..#.....#
#.....#...
#...###.##
.###...#.#
##......##
#.#....#.#
##...####.

Tile 2437:
#...#..###
.#.#....#.
....#...#.
.......#.#
#.#...##.#
###..#...#
#.##..#...
....#.....
#.#.#.##..
.#.#.#.###

Tile 1009:
..#.#.#...
...#..##..
##...##..#
........##
##...###.#
#....#...#
..#..#...#
..####.###
#.........
####..#..#

Tile 2399:
..####.#..
###..#....
#..#..##..
...#.#....
##.##.....
##.###..#.
##..##..##
###....#.#
..#......#
#.###..##.

Tile 2843:
.....#....
......#...
.##.#....#
..#....#..
.##.....##
.#...##.#.
####..##..
.##....##.
....##...#
#..###...#

Tile 1193:
##.....###
.......#..
.#...#.#..
#.#...#.##
..#.....##
.#.....#..
#...#....#
##.#..#.#.
##.....#.#
#..#.....#

Tile 1951:
###......#
..........
..........
#####.....
#.##..#...
.........#
##.##.....
#.#..#.##.
.#...#...#
..#.###...

Tile 1879:
#...#.....
.#.......#
###.......
#####.....
#..#.#....
...###.##.
#.......#.
#.#......#
.#..##....
..#.##.###

Tile 3469:
..####...#
#...#...#.
......###.
........#.
####.....#
#...#...#.
...#....##
#..#..#..#
..#...##.#
#####..#.#

Tile 2161:
####.####.
###...#.##
.##...#...
#..#...#..
##...##.#.
#.........
#...##...#
....#.#..#
..#.##..##
#.......##

Tile 2083:
##.##.#..#
#.##.#..#.
...#.....#
##.#.##.#.
.....#..#.
#.......#.
...###.#.#
....##...#
#.##.#...#
##.#...###

Tile 2089:
#.#.###.#.
#..##.....
.....#...#
#.........
.##...####
#...##...#
.#.......#
....#...##
#..##....#
.....##.#.

Tile 1051:
#.....##.#
.....##.#.
#...#....#
.#.#......
........#.
.......#..
##....#.##
#.......##
#........#
####.##.#.

Tile 3347:
....##.#..
#.#.#..#.#
##........
..#....#..
##...##...
.##.#.....
#........#
#..###....
.....#...#
##.##.#..#

Tile 2927:
#.##......
...#..#.##
.#.#.#.##.
..........
##....#...
##.#...#..
....##.##.
#....#.#..
..#.....#.
##.###.#..

Tile 1301:
#..##.#.#.
#.#......#
..#...#..#
##....#..#
#.........
.......#.#
....##.#..
#..#.###..
..#.######
...###.###

Tile 2459:
#..###....
...###.###
##........
##..#..#..
##.#.##.##
#.##.#..#.
#..##..##.
.#...##..#
#........#
..#.######

Tile 1583:
.#.#..#..#
#.#.#....#
.##.......
.........#
#....#....
##...###.#
#.#.......
.........#
#...#....#
#.###..#.#

Tile 3533:
.#.##.#..#
.#.......#
........#.
.#...#...#
#.........
.......#.#
...#...#..
##..#..#.#
...#.###..
.###..####

Tile 1993:
#.####..#.
..##.#.#.#
.#.#......
.#........
..#.......
#.##..#..#
##..#.....
.#.##..#..
........#.
.#.#.###.#

Tile 3853:
..#.####.#
##....##.#
..#......#
....#.....
.....#.##.
......#..#
..#..#.#.#
##....#...
###.#..##.
##...#.#.#

Tile 2113:
#..#.#.#.#
#.....#.##
#.....#..#
.##....#.#
##.#.#####
#..#......
...#...#..
...#.#..##
.......##.
..##....##

Tile 3319:
####.#..##
##....#.#.
#.......#.
......#..#
####...##.
..........
##.....#..
..#..#..##
#...#.....
.##..#...#

Tile 3847:
...##..#.#
..#.##...#
...#..####
#..#.#.#..
#........#
#....##..#
#....#..##
.#.#.##.##
.####.....
#....##..#

Tile 1283:
..##..###.
##.......#
#.#.#.....
.#.#....#.
..#..#....
#...#.....
##.......#
.##.#...##
##.####...
##..#..###

Tile 2957:
#.####.#.#
#..#..##..
#..###...#
#.#..#.#..
#.......#.
#.#..#...#
######....
#.......##
#...#...#.
.##..#.##.

Tile 1097:
.###.#.###
#......##.
#........#
....#...#.
..##..#.#.
#....#..##
.###...##.
..##.#...#
#..#.####.
#.#.......

Tile 1399:
#.###..###
#...##.###
....#.#...
#...##.#..
..#...#..#
#...###...
.......#..
..#.#.#...
...##...#.
...##..##.

Tile 1451:
#.#...#.#.
#........#
#.#....#.#
###.#.....
....##....
.##.#..#..
.#.####..#
..#..###.#
...#...#.#
#...##.#.#

Tile 1559:
#..#.#.###
......#...
.....#..##
#.........
##..#.....
...#...#..
##.#.#....
.....#.##.
#...#.#.#.
...#####..

Tile 3391:
#.#.#.#..#
##..#.....
.#...###..
......#..#
#.#.....#.
...#..#...
.#......#.
.......#..
.....#.#.#
#.#.#.##.#

Tile 2423:
#.#.#....#
#......#..
#.#.#.#.##
...#.#.#.#
....#.#.#.
.......#..
.##.....#.
.........#
#.#..#...#
...##..##.

Tile 2297:
.....#####
#..#......
#...#.....
##...#.#..
.......##.
#.......#.
###....###
..#.....#.
.....##...
##.##.###.

Tile 2011:
#######...
#.#...#.#.
...##..#..
...##..#.#
......#..#
#..#.....#
...#.#....
....#.#...
..#.###..#
#.#####.#.

Tile 1049:
#.#...#...
.......###
#..#.#..##
##.......#
.#.###...#
##....#...
...#.##...
........#.
...#..#.#.
##...##.##

Tile 3943:
..#...####
...#.##...
#.#.###...
.#...###.#
....#.##..
.##...#..#
####.....#
####.##.#.
##...#....
.##.#...#.

Tile 2039:
#####.#..#
#.#....###
.....#....
##.....#.#
.......#..
#......#..
..#...#..#
#.#...#...
..##...#..
##.#######

Tile 1297:
.#..##.###
#.....#..#
###..##..#
.##..#..##
...#......
#..#....##
..#......#
...##.#..#
....##....
#..###.#..

Tile 1597:
.#..#.##..
###......#
#...##...#
.#.#....##
...##.##..
#.###....#
###.#.....
..#....#.#
...##....#
###.##....

Tile 1319:
...#.##..#
#.#####...
..........
.#..#..#..
#...#.#.#.
.#.##..#..
###.......
#...#.##..
...#.....#
##.#####.#

Tile 2333:
#..##..##.
...#...#.#
..##.#....
#....#.##.
..##..##.#
..##..###.
...##.#..#
.....#.#.#
#......#.#
########..

Tile 1423:
#.##..##..
#.##.....#
#.#..##...
##.#####..
...#.#..#.
.#..#.#.#.
#.##....##
...###..##
#.#.#...#.
#..##.###.

Tile 1303:
.#########
##..#....#
..#.#.####
..........
#...#.....
#.#..#...#
###.#.....
.##.#....#
#.#.#..#..
##..##..#."

# COMMAND ----------

input <- "Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."

# COMMAND ----------

to_binary <- function(x) sum(2 ^ (which(x == "#") - 1))

parse_tile <- function(x) {
  l <- read_lines(x)
  
  tile_id <- parse_number(l[[1]])
  
  m <- str_split(l[-1], "") %>% unlist() %>% matrix(ncol = nchar(l[[2]]), byrow = TRUE)
  
  tibble(
    tile_id = tile_id,
    north = to_binary(m[1,]),
    east = to_binary(m[,ncol(m)]),
    south = to_binary(m[nrow(m),]),
    west = to_binary(m[,1])
  )
}
parse_tile(tiles[[1]])

# COMMAND ----------

tiles <-
  input %>%
  str_split("\n\n") %>%
  unlist() %>%
  map_dfr(parse_tile)
tiles

# COMMAND ----------

borders

# COMMAND ----------

graph square arrangement