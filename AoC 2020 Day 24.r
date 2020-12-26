# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/24

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "eeeseswneenwnwenwseeeee
swswnwswswneswswneeswswswswseswsww
sweswwnwseswnwewnwseewseeneneswww
swnwsweseneenweeseswseseeswseenese
nwsenwsewnesenenwnenwnwnewnwswwwswne
ewseeeeeswnee
nenwwwwwnwwwnewwwsewnwwswwww
neneeenenwnenwnesweneneeswneneenee
wnewsewwswnwswwsew
seswseseswnwseseseeseseswswswswseswswswnwse
swwweswweswseswseneseseseswseneswse
weeswnwswnenwseenenweswnwwenwnwwsw
seseeseneseeeeseseseewnwseeeesee
seseswseswseswseseeseseswsesewneseswsese
eseeeenenewneeneew
neneswswswnwswenwesewswwswwswswwe
nwnwnwnwnwnwneswnwnenenenwnw
wseseseseweseseweeseenese
wswwwswwwwnwswnwseswwnewwwswsew
eswnweneeesweenweeenweeeswwe
seseseseseseeseswseseseeseeseeneee
swsenwseseeeseseeseneswsewseeseesese
nwneswwnenwneneneneneneneenwsenenwneenenw
swswswsweswswswswswswswswswswswswswwsw
swswnwseswswswwswwwwswswsw
wnewseswwswwwwswwenwwswswwwwwsw
seseswsweseseswseswseswswseenwswsewswswsw
seseneseswseswswseswswsesenwseneneswsew
nwnwnenwnwnenenwsenwnwnwnenwnwenwnwnwnwsw
sweeeeneeneeneneneeneneene
nenenesweeneeeeneeneneneneenwnene
swnwneneneswenenesewnenene
neeneeenenenenenenesweneneeneee
nweesesesesweseseseesesewsesesesesese
seseseneseesesesenwswsesesesesesesesesese
neseswseesesenwseswseneeseseseneseseswsw
nwnwnwwwsenenenwseswnwnwnenwnenwnesenwsese
neswsewswswswswswswswswwswswswswwwsww
nwnwnwnwnwwnwnwswwnwwewnwwwwww
nenwswneswnenenenwneneswnenenenwnesenwnenee
sesesesesewseseswseseseseseseesesesese
eeeneswesenwneseeeneneneneeewne
neseswnesesenwseseswsesewseweseswese
seseseneseswseseseswsesesesesewsesesesenw
seswswnenwseseneseenwsesese
neswwwnwsenenwwnewwnwsenewswnwww
neneswneswnwswnwwswseswswswwswwswswesw
nwnwneenwnwnwnwwwnwswnwnwenenwnenenw
nwwwnwwnwnwseseenwnwwnwnwnwnwwsenw
nwnwnwsenwnwnwnenwnwnwnwnwnwnenenwnenenw
sweseswenwseewnweeeseenesenwsee
nenenenenenenenenwneseneeneneneneswnenene
wswswsweenweenwneswswnwnwnwneseew
swswswnwswsweswwswswswswswseeswswswsww
nwnwnwnwnwnwnwnenenenwnwnwnwwnwnwnwsene
wewwswnwnwswwnwwnwwnenwwewnwnwnw
nweeeeeeeeeeeswneseneeseew
wwwwewwwnwwnwnwnwswnwwwww
wwnwwwwwwwwwwwwwewseww
nenwnenwnenewnwnenwnenenwnenwnenenenwnwse
swswswswseseswnewwnwswswswwneswswnew
ewwwwnwwwwwwwwwwwwswwww
senesesewwswswnwwneeww
wnwswnwewewswwseeswwwwenww
weenenwwwsewneneneseeswneseesenesw
seseswwneswswesewswswwsweswnwnwswnwne
nenenenenenenenenenenenenenenenenwneswne
nwnewnwnwnenwsenenwnenwnwsewnenwnenene
nenwswenwnwwnwwnwneseenwnenwsenenesene
nenwwwnwswnwwseenwnwwsewnwwwwnww
wseswswswseseneswenewenwseseneswswwnw
neneneneswenenenewnenenenwneneeneene
nwnenwnwnenenenenenwnwnwneeneswnw
newnenwnewseneneneeneneseneneneneew
wnwnwwnenwnwswwnwwnwnwnwnwwnesewnww
eneneneenenwwneneeneneneswnenenenenene
sweenwnesenewswwswwswwsewwswnwswsenw
swwswnwwswwseseswwswswnwswswswswnwswse
swseneseeeeesewseesese
swwswswswewsweneswswswseswswwnewseswsw
sesesenwweneseneseswneswwwesesesee
wnwnwnwnwswwwsenwnewnwwnwnwenwwwse
nwnwwnwnwnwnwenwnwnwswnenwnwnwnwnwwse
swseeseseeeeeeeeeenweeeesee
neseneneeenewnenenwswwneseneeswneswnw
neeneeeneneeseneeneewneweneeee
seseswswswseseseswsenew
eeeeseeeeseenweeesweseseenwe
ewenwseswneneeenwseswwnwnwweswe
swwnwnwwsewneswnenwewnwwnwsenwnesw
nwnwnwnweneeneseesewwwswnwswnwneee
swswwwwswswneswseweewwnwwwswwswsw
neneneneneneneneneneneneneneneneneneswne
swseswseswswseseseswswswseswsewsesenenwsw
neswnwswseswswswseswwswwswwneswswswswsw
weneneneneeeeenwneneewneeneeese
nenenenwnwnenwneneneswnenwnwneenwnenwne
sweseweneseswnwnwenesenenwnenwnwwnenene
ewewsweswweswswswnesenwneswnwsew
seseseseseseseseseseseseseneseseseseswsew
nwnwswnwnwnwnenwnenwnwnwnenwnwenwnwnwnwnw
nwnwsesenwnwnwnwnwnwneswnesewnwsenwnww
neenenwnenenwwnwnenenenenwnwnenenwnene
nenwneenwwneseneneswneseseneenewnenese
sewnwswseswnenewwwwseweswwwnww
enwnwneswnwnwnwnwnwnwnwnwnwnwnwwnwnwnwe
neneeneneneewseneeneeneneneenenene
swseseeswseswswswswswseswswswswswswsww
nwseseenwswswwswsenenweswnewswnwswe
wswwwwwwwwswnwswwswwswwwew
eeeneeeenweeneneeenesene
eenwnewswswwswswnwnwswenewnenwnwse
neneeneneneenenewnenenenenenenenee
neesenwnwseswseeeseesesewesesewee
nwnwnwnwenwnenenenenewne
eswnwsenewwnweswwnwsewwwnwwnenew
swswswswswswsewswswseswseswseseswneswswse
seneeneneenwneenwsenenewnenesenenene
swswswswswwswwswswswneeswswswnwseswwwsw
ewwnenwneswswswswneswneenewswse
seswnwnwnwnwnwnwnwswnewnenwnenwenenenwne
nwnwnwnwnwnwnwnweenwnwswwnw
nenenenenenenwneneneseneneenewnenwnew
eeeeeewseeeeeeese
eswsewnewwnwsweneeeeeeenenwe
wnwwwwwnwwnwwwwwsewwwwww
senwseesenesweseenwweeesenewesee
seswswswswsweswswswswneswswweswswnwnw
eeeseweeseeeneeweeeeeeeee
nwnwnenwneswnenenwneenwnwnwnenwnwnwnene
nesenesweeswnenweeneneenenenwseeenw
nwnwnwnwnwnwnwnwnwnenwnwneseewnwnwnwnw
seseeseeeseseseeseeseeswnweseee
neeswwnenewswwnwneseswsewneweseesw
nwwswnewwnwnwnwneswnwnwnwwnwnwnwnwnw
wswwnewswswswnewswwswseneswsw
nwnwnwswnwnwnwnwwnwwnwwnwnwnwseenwnwnw
swewnwwnewwwnwnwwnwnwseeseenw
swswswswseswswswswneswswswswswseswsw
neeneswneneenwswneswnenenwenewseneew
enwnwnwwwnwswenwnwnwnwnwnwnwwswnwnw
nenenwnenenwnwnenenwnwnwnwnwnenwnwnwnwse
nwnwsesenwnewnenenwnwnwnwwnwnweseswnww
swenwwsenwsewewwnwwwwwwneesww
wswnwnwnwnwnwwwwwenww
seseseseseswseeseseswseseseswsesenwswse
wnwsenewwwwnwwwwswwwww
seesweeweeeweeeeeeeneee
nwwnwswwewwwwwnwwwwnwwwww
nenwnwnewnwnwnwsewnwnwsewwnenwnwnwsesesw
neenwsenewnenesenwnwnwsesenenwnenenwnwsw
swswswswswswswseswneswswseswsw
wneenwnwseneeneswnweseswsewsenenwnee
swseswswswswswseswseswswswswswneswswswsw
wswswswnwswseswwswswsw
swswsesweswswswswneswswwse
neswweeneewseneenenewseenenwesenw
swwwweeseseswnwneenwnwwsewwwnwse
neneneeneneeeneneneswneenwnwesweswe
wnwnwnwsewwwnenwwwwnwwew
nwswnesenwseseswseneeswse
nwnwnwnwnwnwnwenwnwnwnwwnwnwwnwswww
nwnenenwswnenwnwswnenenwnesenenenwsenenwe
senwnewseenesweswneseseeesesesesesesesw
eneneeweeneeeeeeeeeeeee
eseeeeseseseseseeweseseseeseee
wwsewwwswwwwwnewswswwwwww
enwsweswsenwnwswswswswnweswswswseswswsw
sesenwseswswsesewseseswseseseswseeneswse
eweenwesweeewnwweewesesee
seswseenwwnwsweswneeseswsesese
seswneswswsewnwsweswnwwneswneswwswwse
nwwnwswwnewnwnwnwnwnwnwnwnwwnwnwnwnw
swswwwneneswwwwww
nwswwsewnwnwswnwnwwswsweneneseenewnwe
senwnwnenenwnwnwenwswnenwewswswswnwsw
swwswswswswwswswswwswswswewswwwsw
swsesewseseseseswseneswsesesesesesesesese
ewseeeeswseseeeeeeeseeenwse
nwnwnwnwnwnenwnwnesenwnenwsenwswnwnwnwnw
nenenwwnenenenwnwnwnwnenwseenwnewnene
wswwswwnwwsesewswswswswswswwwswwswne
seenwweseseswnewenesenenenwswwnwnwe
swswwseswewnewswwwweesenwswwswsw
nwwnwenwwswnwnwnwnwwnwwnwwnwnwnwew
wswswsenewswwswswswswswswwwswswsww
wwwwnwnwnwnwnwnwewwnewwnwnwswwnw
eswnesewseeeesesweenesenwnwseseseenw
eswseseseeneseenwnesewwseeseswwsese
esenesesesesenwswsesweswnwswweswsesese
nwseesweeeewnwnwswewee
nwwnwnenenenenwsenenwnwnwnwnenwnwnenenw
wsenwnenwnwesenewnenwnwsw
swswswneswswwswswswswseswwswswswswswswsw
eeseweseseswseeseseseeesenwsewee
nenenenwseneneneneneswenewsewswnenene
eeneewswseswnenenenwnwswnwnwenwswnwswne
swwnwnwwsweseewswwswnewwwswsesww
swwseseswswswseeswsewswneseswswswsese
neseseswwswsesesenwseseseseseswesesesese
eewesweeeswseeswnweenwwnenwne
swswswswseswnwswwswwswwwswnewsesww
nenwnenesenewnenenenewneneneneneneeswnee
wsweswewwswswseseswewnweseswenw
nwnwwnwwwwsewwsewnwwnewnwnewnw
seneeenwneeeeswneeseneeeenwswe
swnwsenwnwneseseswseseneseseswwseeeswse
nwnwnewewenenwnwnwnenwnenwnwnwnwnwnw
neseneweenewneneeeeenenwneenenene
ewseneneenenenenwneneneseeneswenenw
nwnenenwnwnwnenwnwsenwnwnwnwnwsenwnwnwnw
swwswswwwwswwwnenwswswsweswswwwsw
eeseeeeneeenenwneneeeeenewsww
seseeeeeeeeeeswneseeseseeese
nesenewenwneeneneenenenene
nwsesenwseewwweseseseseseeswswswneene
swneswswwwwseeswwwwwwwsewwnwnw
senwswseenwseswseswswseseswswswseeseswsese
swseswswswseswnesesesweswswseneseswnwsew
eeeweseeneeenweeeneenesenene
eseeseseeseesenweseseeenwswsesee
enwneeneeenenesweneneneenenenenenene
swswswswswewswwswswswseeswswswswswsw
sesewswwnweseswnesesesesesewneswsese
nenenenwswnwenwsweeeeeneneneneese
nwneswenwwwwenesewsenwwnwnwnenwsww
neenwseseeseseseseswewnwnesewseswnee
neneweneneneeswneneneneneneenenenenese
sewneneeneneneneeneneeneneneneeenene
nwnwwwwwsenwnwnwnwwsewenwsene
eswsenwnweeeseseswseeeeweee
seeeseseseeseseseseseeeeeeew
neeeeseeenwneweeneesee
nwswnwwenwnwnwnenwnenenwsenenene
eneneneneenweneneweseneneneseswenene
nesweeseeneseeswweweenenwseese
nwwnwwwnwnwwnwenwswnw
swswswwnenwswwswwwswesweswnwswwsesw
nwsesenwnwnwnwwnwnwwnenwnwnwnwneenww
wnwsewwsenwwwnweeewwewnesww
nwnesenwseenesesesenesenenwwnwsenwwwwse
nwnwnwnwnwnwnwneneenwsenwnwnwwnwnwnwnwnew
sewsewwwnwnwnwnwnwwwnwnwnwnwnwnww
ewnenewweswswwewneweeeneee
swnwnenwnwnwnwnwnwnwnwnwnwnwswnwnwnenwnw
nwsenwnwwseneenenwnwnwnwnwnwnwnwnwnww
senwnwsenesenwnwneneswnenenesewnwswnenwnw
senweenweeeesweseswnwewenesee
wwewwnwwwwnwwnwwwwwwwswee
seswsenwsesesesesesesesese
nwnwwwewwnwwwwnwwwwwwwww
seeeeeeeeeseeeeseswseseeseenw
swwswswswswesweswswswswwswnwswswswe
eneneeeswneeeeneeeeeeeeenw
nenenwneeneneseneseneneneneenenwnwnewsw
neeenwewseneenwneswnesenewswneneeene
ewseseseseseseswneswseswswnwseswsesesese
nwnwnwwnesenwnwnwnwnwnwwnwnwnwwwww
nenweneeesweeeeeswewseswnwswe
weswswswswwwswswwwwswswswswswww
nenwsesesenweesesenwwnweseseswsenwse
seeeeeseeenwseeseswseeeseesesene
wnwnenenwsenwwnwweewnwwee
seeseseseesesesesenwsesesesesesesesee
wewswwwwwneswwww
sesenwseseseseseseseseseseseeseseswsese
seeneewsenweswesewwnwseseswswnwsesw
wnwnwswnwnwenwnwwnwnwnwneneswnwsw
seseseesesenesewesese
ewneeenweseseesesweeseseeseseseese
neneneseneneneneneneneneeeeneswnenenewne
senenwnwnwnwnwenwnwnwnwnwwnwnwnwneswe
wsweenweeseweeeenw
nenweesesesewsweeenwse
neneeneeneneneneneswneeneeeeenee
swenenenwneneneneneneeswnwneneneneneee
neenwneseneeenenewneweswneseenwnesw
swwsenewswneswnwswwwwswswwwwwse
nenwwswnewneseseswwsewwwnwwwwww
nenwswnwnwnwnwnwnesesenwnwnwwnwwnwnwnwne
wwswwwneswwswnwwwnewwwswwwse
neeswseseseseswwseneseeseeseseesesenee
nwnewnwneneneeneseneenenenenenewnene
nwsewsweseweeswwsenwnwwnwneenesw
eeeeseseeeseeseneswsee
nwnwnwnwwnwwnwwnwnwnwnwwwwwswnew
ewenenenenenenenenenenenenenenesenenene
nwnwnwwwnwnwnwwwwwwwewnwnwnww
nenenwneseseneseeswnenwwwwsenesenwnw
eeeneeenweneesenwseesweswseew
wswwneeenwnwnenwsenwswnwwnwwsesew
eeeeesewsesenweeseseeeese
eneesesesenweeneneswwnewnenenw
nenwswewenesenenenwseneneseeeenwnene
nwesenwsenwswnwnwnwnwnwnw
nwnwnwwnwwsenwnwnwnwnwnwwnwnwwnw
swneneswswswswseswswswswswswswswswswsww
neswnewnwnwewwwwwwswwwwnewsese
newwwwswwsewwnwnwwnwnwwwnewnw
seswseseneseswwsewseswseseswsenesesese
swswneenenenenwnenenenenenwnenenenenwnesenw
sesesewseeseseseseswwseseseneseeeneese
eeseneswsenenwwnwnenesewnenwnwnwswnw
wnenwneneneneneneneseneneenenesesenew
nwenwnwnwnwwnwnenenwnwnwnenenwnwnwnwne
nesenewsenenewnenesewnenenwnenenenene
wnwnwnenenwnwsenwwnwnwsenwnwnwnwnwnwnwne
nesewnwswwwwswwewwswew
wneweneeneeneneseewswwnenenewee
wwswwnwseswswweswwwwswwswswnwsesw
swswwswswswswneswswneseswwneseswswwswswsw
wwneseswwwwswe
nwsenwnenwnwnenenwnenene
nenenenwnenenenenwnenwsw
seswnwseswnwswneswswswsesweswswswnwsesw
swneswnesewnewwwswswwwwnwswww
swswnewwswswswswwswswswswswwswswwse
swweswswswswnweswneeswnwseswswswnwsw
swseswnesesesewneswwswneswnwseneswsenw
sewwnwwnwnwwwsenenwnwswwwsenewwwne
neneswneeenenweneswneneneswwneeenenene
swseswsweseseswsenenwnwwswswseswseneesw
nwenesenwsenenenwneswsweswnwnewesenw
swneneenwnwseneeeswneneeneweenene
swswswswwseswswseseseneswsweswseswswseswnw
eesweenesweeeeeeenwweeeee
nwnewneswwseneswswswwswseneswneseswsw
eseeenweeeseseenwnweseeeswese
neenwnwswnenenwenwnenwnenenenewnwnwnwnw
neeeneneeeneenewsenenenweneneesw
seseseseswwswswseseseseswswswswswswnee
senwswsewseswseswseseseswseseesesesenesese
swsweswswswwswwswswswswswswnwswsweswsw
neeewnewneesewseeneneenenwesene
nwnwenweswnwweseeesesweeneeseesenw
sewwwwwwnwwwwww
nwwneenwnwneswwenwnwnwnwneswswnwnwswnw
esesweeeeneeeeneeeewseseeesee
swsewenenenwneeseswwnewsenwneneene
nenenwnwnwnenwnwenenwnenwsenwnenwnwnenenesw
seseeswseneswswseseseswsweswwsesewsw
esesenewnwnwwwswnwnewwnewnwwsew
wnenwwswwswwswswswswwwswswwseesw
senenenwnenenenenenenenenenenenenwnene
swseneswswseseswswsweseswswwnwswsesese
wewwswwnwwwnwewwnwwswwsewsww
swswewsesweswseswseswswnwswnwswenwswse
neeeeeneeeeneeneenesweneenee
swseseseseswswsenwseseswseseseeseseseswse
swnwnwnwwwnwnenwnwesenwnwwnwnwnwnwnwnww
swneswwesesewswwwswwswswwswswwnenwsw
nwswnwsesenweeseswwswseswseswesenwse
swwnwwnwnwwnwnwwnenwnwnwwnwnwwnww
wneeswsenwswseseswwesw
neeenenwsweneseesweenenweeneeee
nwneeswseneswnwsenwnwsenwnwnwnenwnwnenw
sewwwsewswenwswswnwnw
wnwnwnwwenwnwnwnwnwsenwnwnenwwsw
wwswswwswwwwwwswswe
eeeneeeeeeseneeenweenewnee
neeesenenenewneeneeneneneenwnesw
wwwnewseewnwwwewwwwwwnwwse
seseseseseesewsesesesesese
eseeeeweeneeeseesese
swswswswnwwwwwwwwswwnewneswese
seswsesenwsenwnwsweseswswwseseswseese
swswswswseswswnwswswewswswswswswswswsw
eseeseeneewesewenweeeeseeesw
nwenwseneswswwswswnwseswseswwneswsweesw
wnwsewsesenenwneseswnenenwnw
nwnwnwsewswnwnwwwnwwnenwnwwnw
ewwnwnwnweswenwsenwwsesenwnwsenwewnw
eseeeeeweeeswneeseewenwneee
neswswswewswseswnwswseswswsw
wwnwwnwswenwnwwnwnwnwnwnesesewewne
nenenwnwnwnwneweneneneenenenenwnwnww
wneeeneeneneneeneeneeeneenenesee
swwwnwswswwnewswsweswwwswswswswwsw
eeeseseseseseewsewseeseseneewsese
wnwenwnwwenwnwnwwwnwsewwnwse
eswneewseseeseswneeseenww
wwnenwwwswnwnwswwwnwwwwwewww
neswnwswnwwswwwnwneeneswswwnwnewnw
swseneswseswnwwsenwswwnwswseswnesesene
nwswnwnwnwnwswwnwnenesenwnwnenwnwnw
swswnewswwwswswwwwwswswww
nenenenenenenewnenenenesenenenenenenene
wwswnwwneswwswwwwsewswswwwswswsew
eseeweeeeeseeseneeeesesesese
eeeeeseeesweenenwneeenweeee
swsewsesesenwnwseseneseseeneseeseswese
eeeenwseeeeeneenene
eweesenwseewne
nwnenwnewneseenewswsewsenwnwnwneswnesenw
esweeswseseneseeseeeseeeeeene
enwnenwnwnwenwwnenwwnweseswswnwnwnenwne
eenesenwnesenenenenwneneewnenwswsene
seswseseewewseseseseseesewseseswswnw
nwnwwnwenwnwnwnwnwwnweseswnwnwwnwnw
neseswswswswsesenwnwnwwsenwneseswwwsewe
sewwwwwnwwwnenwnwnwwwwwnwnw
wwwewswewswwwwswwwwwwwsw
swseeswseseneeeseeenwneneswewswne
neeswwnwneenenwnenesenwenewnenenewne
swwwwswwseswswwswswswswnewswwswsw
nwnwnwwwnwnwnwewewwswnwnwnwwnww
swswswswswswswswswswswwswswswswwswswne
weswswswnwweswneswswswswseswswenwswswnw
nenenwnenenwnenwnesenwsewnenenwnenenenenw
nwswnwnwsenwnwnwneewwseseswnwnwseneenw
seswneseseswneseswnwseewsewse
senwseeeseeeseseseseeseseseseesesw
enenwsewnwsewwnwnwswnewwwnwnewsw
wwswwwnwwsewnewnwnewww
nwswneseneswnwsweswswwswswswswnweenwesw
swwswweswswswswswswsweseneswneswwww
wewswwwwwwnwwwwwwnwnwwww
neswwwnwwswwseswswwswsewnwswwswwsw
nenwneneneneswnenesenenenenesenenwnwne
wseseseseseeseeeseseeesenew
swseenwnenenwswnwnwwsweenwneneseenenw
eeswsenewneseweeeswsesesesewnwnesese
nwseeeswseswwwnenesenwseswwseesesesesw
nesewnenenenenenene
wnwwnwwnwwnenwewwnwwwnwnwnwnwswse
neneneneswnenenenene
nwnwnwnwnenwnwneeswenwnewnwnwneenewnwne
eeeeneeeeneneneneeenwneswneswenwne
nenwnenwwnenenwenenwnenwenwneneswnene
nwnwnwwnewwwnwwwsewnwwwwwnwwnw
weswswsesweswneswnwswswswswswsweswsww
neneeneewneneneneeneswnenenenenenene
wswwwwnwnewwwwswswnwswsewsewsw
swswsenwseswseswnweswsesesesesesesesesese
nenwnwnwneneenenenenenewnwnwnenenesenene
swseswswwswsenenwseswswseswswseseswswsese
swswsesweswneswswswewnesenwseswnene
nenesweenesenenenenwnwneswnenwswsenwnwnw
wewsewswseswwnewswwnwwnwwswwwsw
nenwnwsenwswnwnwwnesenwnwnwnwnwnwenwne
sesenweseeseseseseneeseseeseseswsese
seweswwwnesenwwnwnwnw
sweseseseswneewsenweseneseeseesee
neneneeeeeneneneenenenenenenenewnew
nwewneswsweenwsesewesenesewneesw
eseseseseenesenwseeseeeew
nwswswseeswswseswseswswswseseseseseswswse
nwnwwnwnenenenwenenenenenenwneenenenenwsw
neseswswseseswswsewseseseseseseneswsesw
seswswswseswswnwseswswswswswswswswswsenese
wseswwnwewnwnwwwwwsweswnewnwenew
sewwswwneswwwwswwwenewwwswew
swseswswseseneseseswswsewseswseswseswsw
wsesesewseseeeseseesesesesesesesesee
nwnwnenenenwnenwnenenenenwnenenenwsenwnw
senenwswnweseswnenweneswwsw
neeeseeeneeneneneneenwnenenesenwe
nwwnwnwneswnwwnwswnwenwnwnwnwnwwnenwe
seseswewseswswnwneneseseneswswsewwsesw
nenewneeneswneeneneneseneneeneenene
neneeeneeeeeeeeneeeeewene
wnwwenewnwnwnwnwwnwnwnwwnwnwswsenwsenw
wwsewwswnwwwwwwswwwwww
swsweseeswsenwseseneweswswswwswswsesese
nwwnwnwnenwnwnwsenwnwnwnenwnwswnwnenw
sweswswswnwswneneneenwswswswswswsesww
neenewnwnwnenwnenenenewnwneneenwnwnw
nwnenwnwnenenwwseenwnewnenenene
nenenesenwswnenenenwnenwneneneenenwne
neeneeneweneeneeeneeenwese
swwneswnwswwsewswneswswseswswwswswnesw
swseseseseseseseeesesesenwseseseesese
nenweswseswswwsewswswnwnewwnwnesesew
swseswseseswswneneswswsenesese
nwseswsesesenwsesenwnwsenweseewwsese
neseeneeneneeeenenenenenenenewnew
nweweenwnwewseseseseesesese
esenwwnwswnenwwseeswswewnwswenesesese
neenwnwneseseseewneenesewnenenenenew
nwnwnwnwnenwnwnwnwnwnwswenwnwnenwswnwnwnwnw
swnwseswseeswnwswsw
wenweeseneswneswnwnwwneswseneneseswsw
nenenewnenenenenenenenenesenwnenenenwnene
seswnenwseeseswwseesenwswseseeeee
eeeneeeeweneneeeeeeeewee
eeeeeeneesweeeeeenweeee
eeneneeneeneeneenwneseeeneeene
wwwwsewwwwwwwnwwswewnwwsww
wwwewswwwnwnwnwnwwwwwnww
senwswsewwneseneswnenewwwenwwe
seeesesweseseneswnwseesewseeseew
swwneewwswswwswwwswswwswnewwww
swswwswswswwseswneswswwwwwwwswswsw
sewnwswwnwewnwwwwnenwnwnwnwewsewne
nenwnwnwnwwnwnwneswnwnwnwnwswnwnwnwnwnw
eweseneenwneenewneeeeneenewse
nwwwwwsewsenwwnwnwwweswnwswnwnee
eeeeeseeseesweenweseeeeeee
eneenesenewnenenenenwenenesenenenene
wwwwwwnwwwwwseewwwwwwww
nwnwwwnwnwwenwwwwwwnwwswwnwww
swnesesesesesewseseseseseseseseseesesesew
nwnwnwnwnweswswnenwnenenenenwnwnwnenwnw
wwwwnwnewnesewwseswwenwsewwnwnw
sewwwwwsewswwwnesewwnwwwwwwne
swswnwswswswnwswwswswswswwseweswswsw
wwnwswwwwwwwwseseewwnwnwnwww
nwnwswnwnwnwnwnenenenwnwnenenwnenenwnesw
eeeeeneeseenwesweneweneene
nenwwnwwwwnwwewwwwwsewseswwnw
nwwswswswnwwwsewwewwwweswwe
seswswwwswswnwwnwswweswweswsenwnw
nwnenenenenenwneneneswnenwnenenenenenene
neeesweeeenesweeeeeeseeee
eswswseseseswswswswswweenewnwswseswsw
eeseseseeseesesesesenwswseseneseesw
seeeeseseeeeeswenwseseesesesesese
neneenenwneneswnenwneneseenwnenesenenene
senwnwnwnwnwnwnwnwnwnwnwnwnwnwnwnwnwnwnw
neeenenenenenenenenweesweenenene
wwwnewwwwwwwwwwwwwwswwse
eeeeseeeeeeneesweseee
seswswnwwswseswswswswswwswnwswwswww
eseseeseeneesweswseseeesesesesenw
seseeseeenweeswesenesesesenesewe
seneseseseseseseswseeesesesesesesenwwenw
seeeeeeeeweseeeeeeeeee
neenwneneneeeneneeeneneneneeneeswne
wwwwwwwwwwwwwwnwwnwwe
seseneseseseswsenwswswswseseswsenwseswsesw
wwswwwnenwwwenwnwsesesweswwwwnw
wwwwwswwwnwwsewnwwnenwnwnwnewse
neneneneeewneneneneeseeneneneswee
nwnwnwnwnwnwnwenwnwwnwnwswwnwnwnw
nwseeneseseeeseeseenweswsweeesese
eswneneenenenwnenenwneneneneneneswswnwswnw
seswseseswswswswswneswswswseswseswsesese
eswnwneeseewenesweneseneeeenwnenw
wnwnwnwnwnwnwwnwwnwnwnwsenwnwnwnwnwnw
swwswwwwswneswwwwwwswwwwnesw
seseewswweswenwswsenwswnenwswswneeene
swswswswseeswseswswswenwswwswewswseew
senwnenwswswswswseewswwnewswswsenesw
eneneneeeeeeweneeeneeesewneee
nwnwnwnwnwnwnwnwnwwwsewwnw
wwsesewsenesweneneseeeseswnwnesew
eeneneesweeeseswwneeseseeeeew
senesewwenwneswsenweeswswsenwswswnesw
nwnwwnwnwnwnwwwnwwnwwnwnwnwwsewne
seswseseswseswswswneseneseswswwseswsese
sesesesesesesesesesesesesesenwsesesesese
seeseeeeeweeeee
sesesenwsesesenenewseswswseseseseseseenw
nwnwwewwwnwswnwnwwnwwwwwnwww
wwnwnwnwnwnwnwwnwnwswenwnwnw
neneneneneneseneneneeneneneenenenwnene
wwnwsenwnwnwnwnwnenwnwnwnwnwnwnwwnww
newnwnesewnwsewsenenwswnwnwnwnwnwnwnwnwnw
senwsenwnwnwnwnenesewnenwnwnwnese
eseseseseseseseesesesesenw
neseesewsenwseseswseseseenwnew
swneswwswseswswswseneswnwseseswwseseswse
wwwewwnwwwwnwwwwnwwwwww
nenenesenenwnenwneneneswnwnenenwnenenenw
"

# COMMAND ----------

input <- "sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"

# COMMAND ----------

tiles <- input %>% read_lines() %>% str_extract_all("(e|se|sw|w|nw|ne)")
tiles

# COMMAND ----------

# Directions are e, se, w

# COMMAND ----------

paths <-
  tiles %>%
  enframe(name = "path_id", value = "direction") %>%
  unnest(direction) %>%
  mutate(
    d = ifelse(direction %in% c("e", "se", "sw"), 1, -1),
    direction = case_when(
      direction == "w" ~ "e",
      direction == "nw" ~ "se",
      direction == "ne" ~ "sw",
      TRUE ~ direction
    )
  )
paths

# COMMAND ----------

paths %>%
  group_by(path_id, direction) %>%
  summarise(d = sum(d)) %>%
  pivot_wider(id_cols = path_id, names_from = direction, values_from = d) %>%
  count(e, se, sw) %>%
  filter((n %% 2) == 1) %>%
  nrow()

# COMMAND ----------

# 322 wrong. too low

# COMMAND ----------

# 564 too high