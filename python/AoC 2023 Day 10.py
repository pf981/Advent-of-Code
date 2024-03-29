# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/10

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 10: Pipe Maze ---</h2><p>You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.</p>
# MAGIC <p>You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "<a href="https://en.wikipedia.org/wiki/Hot_spring" target="_blank">Hot Springs</a>" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.</p>
# MAGIC <p>The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.</p>
# MAGIC <p>Scanning the area, you discover that the entire field you're standing on is <span title="Manufactured by Hamilton and Hilbert Pipe Company">densely packed with pipes</span>; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).</p>
# MAGIC <p>The pipes are arranged in a two-dimensional grid of <em>tiles</em>:</p>
# MAGIC <ul>
# MAGIC <li><code>|</code> is a <em>vertical pipe</em> connecting north and south.</li>
# MAGIC <li><code>-</code> is a <em>horizontal pipe</em> connecting east and west.</li>
# MAGIC <li><code>L</code> is a <em>90-degree bend</em> connecting north and east.</li>
# MAGIC <li><code>J</code> is a <em>90-degree bend</em> connecting north and west.</li>
# MAGIC <li><code>7</code> is a <em>90-degree bend</em> connecting south and west.</li>
# MAGIC <li><code>F</code> is a <em>90-degree bend</em> connecting south and east.</li>
# MAGIC <li><code>.</code> is <em>ground</em>; there is no pipe in this tile.</li>
# MAGIC <li><code>S</code> is the <em>starting position</em> of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.</li>
# MAGIC </ul>
# MAGIC <p>Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is <em>one large, continuous loop</em>.</p>
# MAGIC <p>For example, here is a square loop of pipe:</p>
# MAGIC <pre><code>.....
# MAGIC .F-7.
# MAGIC .|.|.
# MAGIC .L-J.
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>If the animal had entered this loop in the northwest corner, the sketch would instead look like this:</p>
# MAGIC <pre><code>.....
# MAGIC .<em>S</em>-7.
# MAGIC .|.|.
# MAGIC .L-J.
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>In the above diagram, the <code>S</code> tile is still a 90-degree <code>F</code> bend: you can tell because of how the adjacent pipes connect to it.</p>
# MAGIC <p>Unfortunately, there are also many pipes that <em>aren't connected to the loop</em>! This sketch shows the same loop as above:</p>
# MAGIC <pre><code>-L|F7
# MAGIC 7S-7|
# MAGIC L|7||
# MAGIC -L-J|
# MAGIC L|-JF
# MAGIC </code></pre>
# MAGIC <p>In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to <code>S</code>, pipes those pipes connect to, pipes <em>those</em> pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including <code>S</code>, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).</p>
# MAGIC <p>Here is a sketch that contains a slightly more complex main loop:</p>
# MAGIC <pre><code>..F7.
# MAGIC .FJ|.
# MAGIC SJ.L7
# MAGIC |F--J
# MAGIC LJ...
# MAGIC </code></pre>
# MAGIC <p>Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:</p>
# MAGIC <pre><code>7-F7-
# MAGIC .FJ|7
# MAGIC SJLL7
# MAGIC |F--J
# MAGIC LJ.LJ
# MAGIC </code></pre>
# MAGIC <p>If you want to <em>get out ahead of the animal</em>, you should find the tile in the loop that is <em>farthest</em> from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps <em>along the loop</em> to reach from the starting point - regardless of which way around the loop the animal went.</p>
# MAGIC <p>In the first example with the square loop:</p>
# MAGIC <pre><code>.....
# MAGIC .S-7.
# MAGIC .|.|.
# MAGIC .L-J.
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>You can count the distance each tile in the loop is from the starting point like this:</p>
# MAGIC <pre><code>.....
# MAGIC .012.
# MAGIC .1.3.
# MAGIC .23<em>4</em>.
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>In this example, the farthest point from the start is <code><em>4</em></code> steps away.</p>
# MAGIC <p>Here's the more complex loop again:</p>
# MAGIC <pre><code>..F7.
# MAGIC .FJ|.
# MAGIC SJ.L7
# MAGIC |F--J
# MAGIC LJ...
# MAGIC </code></pre>
# MAGIC <p>Here are the distances for each tile on that loop:</p>
# MAGIC <pre><code>..45.
# MAGIC .236.
# MAGIC 01.7<em>8</em>
# MAGIC 14567
# MAGIC 23...
# MAGIC </code></pre>
# MAGIC <p>Find the single giant loop starting at <code>S</code>. <em>How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''.F-7F-..|-F-|F---7J7FLF-7F|FJ-LJ.7--F7-|77.|7J.FFLF7-FJ7.J-7-|.J.7.F7L7..FF.|F--F--|J-FFJFL7F7-LJFF-.7F|7.FF|7FF7FL7L--F--77-7F7.7.-F-J.JFLF
FF-.F|-FLJJ.77F|F|-J77|---.7JLJLFJF-|7.F-7-F7.FFJLJ|.LF7-.|L7.J7LJ.L7FLFF7J|.F|.LJ-|.|.L7F.LFJ.||||FF|FLL--|L-J7--J|J7L||FJ-JLJL-JJ.L7J-L|7J
.|.FF7-LJ|.FJF-77|FJ|||-L|-L-FJ7F-|-LF-L7|FJL7J-F7FFF7FJ.J-.LJ.F|J7.LJ.|L.||L7JF|.7J7.7.|L-FJ7LL-JJ7FJ7.LL7J7LFJFLF--F|JF|-|.-JJJ7L7-||7F---
FF-F7JF|FFF..L-|-|JF-JF7LJ7.F7--JLJ..LFFJ||F-J|F777L|-7J-7|7|7.FJ-77..LL--7|7F7F|-J|77.FL-7FL-JJ|7JL-L-|7F|7JJLF77L|-7|.FJ-L7|J.LL-FF7F-77|J
F|...FFJLLJFFLJ|JJJ|.LL77-L7LJJ.|L|-|-FL7LJL7JF7JL|.|7||.LF|-|FJJF|F7FJ.FJ|LF||F7.-FFJ-LJ|FJ.L---J.|L.L77-JJ|7|||--L7|J-.F7|.F7F7|FJ|F|J-F..
--F-L|J..L.F77.L7--JL.L|L7F|J..FJFF-J7|FL-7FJF77JF7J..JJ-FJL-JF|.FFJLJLFF-F-F||||7L|LFFJF-7.7FL|.LL7|FFJL7JFF7F|L|-JJJ|.FL-L777L-.7L7FF7.|7|
F7J.|.L|7.J7|FL.|.|.L|7|J--7-7-L.F|J|F77|FJL-JL7-||L77LLF-J-|-F..FL7.F-LJ7FF7||||F77JLJLL.J7.L-JFF.LJL7-|L|FL-FJF77|.FF-LJ.||J.FF7|FLLJL7.FJ
FJ|F|FFLJ7L-L77L|-FF.|LJF7-L-77.7-|-FJL7FJF7F-7L7||7L|...|-LLL|7FF.LFFF.LF7|LJLJLJ|-7|.|7..J----F77.JF-JL--7JLFJFLJF-7J.L77FF.L-J|LJJ.F|JFJ|
J.L--77|.|7|L|7|J7|.FF|7||7-|||7|-J|L-7LJFJLJFL-J|L-7|-F-7.F7JFFF-7--7-F-J|L-7F7F-JFJL-FJ--J7FJ.J||J|F|7LFJ||-L--7-7JJ.F-7-7.FJ.L|J|||J.F7J7
|F.F|.7-|JLF7|.J7-77JF7F777.LJ|7L..F|FL-7L7F7F7.FJF-J-7|J|-||J.FJFJ7F7JL-7L77||LJF-7..F|J.|.F.F7FFF.-F77.7F-F77-F77L|77..L-7-.L-7L-LLLJLLJL7
F7FL77|FLFL|LF7|J-|FFJLJL---77LF7LF7F7F-JFJ|LJL7L7L7JJFJ-JFF--7L7|FFJ|7-LL7|FJL7FJFJ7-F7..F7F-J|F7J7J||J--7L|L7FJL77F-|F7|FF-7-|J|L|7|-JJ|FL
F-JJL--|7|.L7-J|LLF7L--7F---J-||F||LJ||F-JFJF--JFJFJ77F77F7L7FJFJL7L7|F7F7||L7FJL7L7F7||J7||L7FJ|L7F7||77||-L7|L-7L-7JLJL7JJJ.|J||||FJ7--FF7
F7..7JLL7FL.|-JJJL|L77|||77||7F-7FJF7LJL-7|FJF7FJFJJF7LF-JL-J|FJF-JFJLJ||LJ|J||F7|FJ|LJ|.L|L-J|L|FJ|||L7LFF-7||F7|F-J77LF7JJL|7.|JJ-.F-.|.FJ
7---F7|.FJJF7777.|L7L7FJ|F7-F7|FJL-JL-7F-J||L||L7L--J|7L----7||FJ|FJF--JL-7L-JLJ|||7L-7L7.|F--JFJ|FJ||FJ-FL7||LJLJL-7L7L||JFFF77|JJ.LJ7FL-|J
|F-7F--7FF7|J|FL.F|L7|L7||L7|||L7F7F7FJL7L||FJL7|F7F7|F----7||||F-JFJF-7F7L--7F-J|L7F7L7|FJL7F7|FJL7LJL77LFJLJF7F7F-JF77||7F7||7LL.-LJFFJF7|
J7F-J7.F|J7JFJLJ7LF7||FJ||FJ||L7||||||F7|FJLJF-J||LJLJL---7LJLJ|L7FJJL7||L---JL-7L7||L-JLJF7||LJL7FJF--J77|F--JLJ|||FJL7||FJ||L7.FFJ.-J--L-7
.L|JF77LJF-.JF-JLFJ|||L7|||FJ|FJ||LJ|||LJL7F-JF7|L7-FJ|F77|F7F-JFJL-7FJ|L-----7FJFJLJF7F-7|LJ|F--JL7L-7F7FJL---7|LJFJF7||||FJ|FJ.|7FL..|7|L|
--L-F.J|.--J-J7F7L7LJL-JLJ||FJL7|L-7LJL7F7||LFJ|L7|F7|FJL7|||L7||F--JL7L-7F7F-JL7L-7FJLJFJ|F-JL-7F-JF-J||L7F--7L--7L7||LJLJL-J|F--777F-7-FFJ
||L7-7JF7L-JF|F7F-JF7F-7F7LJL7||L7|L--7||LJ|FJFJJ|||L7L7FJLJ|FJFJL7JF7|F-J||L7F7L--J|F7|L-JL-7F-JL-7|FFJL-JL-7L---JFLJL7F-----J|F-J7--FLJLL7
.LJL.LJL|-L-F7||L7FJLJF||L--7L7|FJF7F7|LJF-J|FJ|FJ|L7L7|L7F7||FJF-JFJLJL-7|L7LJL---7LJL--77F-JL7J.FJL7L--7F7FJ-F-7F7F7FJ|F7F7F-JL7L|-7J.--LL
7JFJ77FF|-JL|||L7LJF7F7||F--JFJ||F||||L-7L7FJ|F7L7|L|FJ|FJ|||LJFJ|FJF----JL7L7F-7F7|F----JFJF--JJFJF-JF7FJ|LJF7|FJ||||L7||LJ||F--J7L-.||.F-J
|LJ-L-J7JJJ.||L7L--JLJ|||L--7|FJ|FJ|||F7|FJL7||L7|L7|L7||FJ|L-7|F7L7|F-7F7FJFJL7LJLJL----7L7L7F7FJFJF7||L7L7L||||FJ||L7|LJF-J|L-7F-7|FFJLJ||
|F-FLL7|...FJ|7L---7F-JLJF--J||FJL7LJ||LJ|F7|||FJL7||FJ|LJFJF7|LJL7|||FJ||L7L-7L7F7F7F---JL|FJ|||FJFJ|||JL7L7||||L7LJFJ|F-JF7|F-J|FJ----.F--
7JFL77J.-F-L7|F7F7FJ|F-77L--7LJ|F-JF-JL-7||||LJ|F-J||L7L-7L-J|L-7FJ|LJL7||FJF7L7LJLJ||JF7F7|L7|LJL7|FJ||F-JFJ|||L7|F7L-JL--JLJL--J|JJ|7J.J||
F-|F|F-7L|-FJLJLJLJFJ|FJF7F7|F-JL-7|JF77|||||F-JL-7||FJF7|F--JJFJL7L7F-J|||FJ|FJJF--JL-JLJ|L7|L-7FJ|L7||L-7L7|||FJLJL7F--7F7F7F---J77L-.--7J
|--J-J7LFF-L------7|7|L7||||||F7LFJL7||FJLJ||L-7F7||||J|||L7F--JF-JFJ|F-J|||FLJF7L7F--7F--JFJ|F-JL7|FJ||F7L7||LJL7LF7|L-7||LJ|L----777L7LFJ.
.FLJLLF-F-7F---7F7|L7L7||||||LJL7L-7|||L--7||F-J|LJLJ|FJ||FJL--7|F7|FJL7FJ|L-7L||7LJF-JL-7FJFJ|F7FJ|L-JLJ|FJLJF7FJFJLJF-JLJF-JF7F--J-|JF-L-J
|-J.-7.LL7|L--7LJ||FJ.|LJLJ|L--7L--JLJL7F7|LJL7FL---7||FJ|L-7F-JLJLJL7FJ|L|F-JFJ|F-7|F7F-JL7|.||LJFL--7F7|L7F7|LJJL-7FJ7F7FL--J|L---7JF|FJLJ
F7---F-F7||F7FJF7LJL-7L---7|FF7L----7F7LJLJF7FJF7LF-JLJ|7|F-JL-7F----JL7L-J|F7L7|L7|LJ|L-7FJL7||F-7F7J|||L-J|LJF7.F-JL--JL7F--7|F7F-J-JL-.L|
L7.|.|.|LJLJ|L-J|F7F7L---7||FJ|F-7F7LJL7F-7|||FJL7L-7F-JFJL-7F7||F7|F7FJF--J||FJ|FJ|F-JF-J|F-J||L7LJL7LJL7F7L-7|L7L-7F7F7FJ|F-JLJLJLL|7L7|F7
LJ7L-7FL7F-7|F--J|LJ|F--7LJ|L7|L7||L7LFJL7LJLJL-7|F-JL7LL7F-J|LJLJL7|LJFJ.F7||L7|L7|L-7L-7||F7||FJF--J|F7LJ|F-J|FJF7||LJLJ.||F7F7F7-F-7-L-JJ
--77L-F-J|FJLJF7FJF-J|F-JF7L7||FJLJFJFJF7L7F7F-7||L-7FJF7||FFJF7F--J|F7L7FJ|||FJ|FJ|F7|F-J|||LJ|L7|F7F7||F7|L7FJ|FJ||L-7F-7|LJLJ|||.|FJF|FJ|
J|.F--|F7|L--7|LJFL--JL--JL7|||L7F7L7L7|L-J||L7|||F7||FJ|||FJFJLJF7-LJ|FJL7|||L7|L7||||L-7||L-7L7||||||||||L7||FJL7||F-J|FJ|F--7LJL-JL-77..F
LF-.LFLJ||F-7LJLF7JF7F7F---JLJL7LJ|FJFJL7F7||FJ||LJ|||L7|||L7|F7FJ|F7FJ|F7|LJL7|L7|||||F-J||F7|FJ|||LJ||LJL-J|||F7||||F7|L-JL7-|F-7F7F-JJ-FJ
.F-7-7.LLJL7|||FJL-JLJ|L------7|7FJL7L-7|||||L7||F-J||J||||-|||||FJ|||FJ||L--7||FJ||||||F7|||||||||L-7|L-7F-7LJLJLJLJLJLJF7F7L7|L7||||-J..77
FLF|7LFJ-|F|L7FJF7F7F7|7F7F7JFJL7L-7L-7||||||FJLJ|F7|L7|||L-J|||||FJ|||FJL7F7|LJ|FJ|||||||||||||FJL7FJ|F-JL7L7F-7F--7F7F7|LJL-J|FJLJLJ.L77JF
F7FL|.||.LFJFJL-JLJLJ|L-JLJL7L-7L-7L-7||||LJ|L7F-J|LJFJ||L-7FJ||||L7|||L-7LJ||FFJ|7LJ|||||||||||L7J|L7LJF--JF||FJ|F7LJLJ||F7F7FJL-7.J.L.|L77
LF.LJ-|-F-L7|F7F7JF7J|F7F-7FJF7L7FJF-JLJ||-FJFJ|F7|F-JFJ|F7|L7||||FJ|||F-JF-JL7L7|F7-||||||||LJ|FJFJFJF7L---7||L7LJL--7FJLJ|||L---JJ-JLFF|L-
FF7.F.|.F7J||||||FJL-J|LJFJL-JL-JL7L---7LJFJFJFLJ||L7FJFJ|||FJ||||L7|||L-7|F7FJFJLJL7||||LJ|L-7|L7L7L7|L----JLJJL-----JL7F7LJL7F-7JL-J.FJJ-J
FL|-JJ7F||FJLJLJ|L-7F7L7FJF----7F7L----JF-JFJF7F-J|L|L7L7|LJL7|LJL7||||F7|LJ|L7|F-7FJ||||F-JF-J|FJ||FJ|F---------------7|||F-7LJFJF-J|.F|FF|
FJLFJ|F-JLJF---7|F-J|L7|L7|F7F7LJL-----7|F7|FJ|L-7L7|FJ|||F--JL-7FJ|||||LJF-JFJ||F|L7||||L7FJF-J|F-JL7||F--------------JLJLJF|F7L77F-7JJ|-LF
L.L|F-L7F-7|F--JLJF-JLLJLLJ|LJL--7JF---JLJLJL7L--JFJ|L-7||L-7F7FJL7|||LJF-JF7L7|L7|FJLJ||F|L7L-7|L7F-JLJL--------------7F-7F-J||FJJL-J|7|7F|
.F--|LFLJ-||L-7F-7|F7F7FF--JF7F-7L-JF7LF7JF-7L---7|FJF7|||F-J|||JFJ||L-7L-7||FJ|FJLJF-7||FJFJF-JL7LJ7F7|FF7F7F-7F7F----J|FJL--JLJ|LJ7.7FLJ-7
LLL-J7L7L-LJF-J|FJ||LJL7|F--JLJFJF--JL7|L7|FJF---J|L-JLJLJ|F7||L7L7|L7FJF-J|||7|L---JFJ||L7L7|F-7|F--JL7FJLJ|L7LJ|L-----JL7-|77F-7-JFF-7-F7-
|L|-JL|7|L|.L--JL7|L7F7|LJF---7L7L7F--J|FJ|L7L---7|F7F---7LJ||L7L7|L7|||L-7|||FJF---7|.LJ-|FJ|L7||L---7|L--7L-JF7L-------7L-7F7L7L7JLL-J--JJ
7|F7|FJ77-F------J|LLJ|L--JF-7|J|FJL---JL-JFJFF7FJLJLJF7FJLFJ|F|FJL7||L7F-J|||L7L--7LJF7F-JL7L-JLJF---JL--7L---JL-------7L--J|||L7L7FLL|7LFJ
7-FJLJ.F77L7F7F-7FJF--JF--7|FJL-J|F--7F---7L--J||F7F7FJ|L-7|FJFJL7FJ|L7|L7FJLJJL7F7L--J|L-7FJF7F7FJF--7F-7L---7F7F-7F-7FJF7F7||7FJFJ-.F-L7|7
L|||.|-LL-|LJ||FJ|FL---JF-J||F7F7|L-7|L--7|F7F7|||||LJ-L7FJLJ-L7FJL7|FJ||||LF7F-J||F7F7|F-JL7|||LJFJFFJL7L-7F7LJ|L7||JLJFJLJLJL-JFJF|-L|FJJJ
77|7-J-|FFL7FJ|L7L7|F---JF7|LJ||||F-J|F-7|||LJLJ|||L7JF7||F----J|F7LJL7|FJL7|LJF7|||||||L---J||L-7|F7L7FJF-J||F7L-JLJF7FJF-7F7F--JLJ|FFF-L|J
LF7|F-7F-JFFL-JJ|FJFJF7F7|LJF-J|LJL-7|L7|||L---7||L7L7||LJL-7F-7LJL7F-J|L7FJ|F7|||||||||JF7LFJL7FLJ|L7LJFJF7|LJ|F7F7FJLJFJ.LJLJF77JL-7-F7.|.
.LL-JJ.FJ7LLL-|LLJ-L-JLJ||F7L-7|F---JL-JLJ|F7F7||L7L7LJL--7FJ|-L7F-JL-7L7LJ7||LJ||||||||FJL7|F-JF-7L7|F7L-JLJF-J|LJLJF--JF7F7F7|L7.||JLL7-L7
JF|J.L7|.7-LLF-7F7FF7F--J||L-7LJL--7LF7F7JLJLJLJL-J-|F----JL7|F-JL---7L7L--7||F-J|||LJLJL-7|||F7L7|FJ||L--7F-JF-JF---JF7FJ||||||FJ7|JFF7-J.7
.LJJFLLL---|-L7LJ|FJ|L--7||F7L-----JFJLJL------7F7F7LJF---7FJ||F7F7F7L7L7F7||||F7|LJF-----JLJLJL-J|L7|L--7LJF7L7FJF-7-|||FJ|||||L7F7-|--J-F-
|J.F|-JJJLF77FL-7|L7|F--J|LJL-7F7F-7|F--7F7F7F7LJLJL--JF--J|FJ|||||||FJF||LJ||||||F-JF----7F--7F-7L-JL7F7L--JL-JL7|FJFJLJL-JLJLJFJ||FL.|.-7L
|7FJLF7L|F.L|7F7|L7|||F--JF---J||L7LJL77LJLJLJL7F-7F---JF7FJ|FJ||||||L7FJL7FJ|||LJL7FJF--7||F-J|LL---7||L---7F7F7LJL7L7F7F---7F7L-JL7J7FF7|J
JJ-LF|-77.FF7FJ|L7LJ|LJF-7L-7F7|L-JF-7L-------7|L7||F7F7||L-JL7|||LJ|FJL7FJ|FJLJJF-J|FJF7LJ|L-7|F----JLJF--7LJLJ|F--JFJ|LJF7-LJL----J7L-FJ7J
|-L-J.L|LJF||L7L7L-7L7FJFJF7LJ||F--JLL--------JL-J|LJLJLJL-7|L|||L77||JFJL7LJF---JF-JL7|L7FJF-J||F-7F7F-JF7L---7|L-7FJFJFFJ|F------7|F.|JLJ7
L.LL7J-JFFFJ|-L7|F7L7|L7|FJL-7LJL--7L|F7F7JF--7F7FL7F-7F--7L-7LJL7L7||7L7FJ|-L7F-7L7F-J|FJL7L-7|LJ-LJ||F-JL----JL-7LJFJ-FJFJ|F--7F7|-J7F--J-
|-F-||7F--JFJF-JLJL7||F||L--7L7F7F7L7FJ||L7|F-J||F7LJJLJF7L--JF7||FJ||7FJL-7.LLJJL7|L--J|F-JF-J|F7F7FJ|L-7F------7|F7L-7|FJFJL7J||LJ|7FJ|.LJ
.JJ7LFLL7F7|JL--7F7LJL-JL-7-L7LJLJL-J|FJ|FJ|L--JLJL7F7F-JL----J|FJL7LJ-L7F-J7.LL-JLJF---JL7.L--J|LJ|L-JF7||F7F---JLJL7FJ||||F7L7|L7LL-J.JF|J
|--7|.L.LJ|L-7F7LJL---7F7FJF7L-------JL-JL-JF------J||L7F------JL-7|J|LL|L-7-|F--FF-JF--7FJF---7L-7|F7FJLJ||LJF7F---7LJFJL-J||FJL7|||||F.FFF
F.||-|7.F7L-7LJL7F7F7|LJ||-|L---7F7F7F7F---7L7F7F7LFJL-JL-----7J|.||L|7L|F7|-JJJ.LL--JF7LJLL--7L-7|||||F--JL7FJLJF--JF-JF-7FJLJJFJ|J77-7FL7J
LJ-FFJJ.||F7L--7LJ|||F--JL7L7F-7LJLJ|||L-7LL-J|LJL7|F--7F-----J-L7LJ7-|JLJ||.LJ|F|LFF7||F77F-7L-7||LJLJ|F--7LJF-7L---JF7L7|L--7-L7|-FL---L-J
7F-J|7.FJLJL-7FJF7LJLJF7F7L7LJFJF7F7LJ|F7L----JF-7LJL-7|L------7LFJ|.-JJLLLJ7L-7-F--JLJLJL-JFJF7|LJF--7|L-7|F7L7L-----J|FJL7F7L7.LJ7-7J|F|.L
.|L|F-7L----7|L-JL7F7FJLJL7L7FL7|LJL-7|||F7F-7FJFJF-7FJL--7F---JFL7-7.F--|-JJFL.LL--7F-----7L-JLJF-JFFJ|F-JLJ|FJ|F-7F7-LJF7LJL7L77J|J7-77|.|
L.|J|FJFF---J|F--7LJ|L7LF7L7|F7LJF7F7||||||L7|L7L7L7|L---7LJF--7F7J7FFJ7F7|J.|.|JLF7LJ7F7F7L7F7F7|F-7L-JL---7LJF7L7LJL--7|L--7|FJ-.F-JJFJF-J
|.7|L7JFJF7F7LJF7L--JFJFJL-J|||F-JLJLJ||||L7||FJFJFJ|F7F-JF7L-7LJ|J7FF-J7|L--L77F-JL---JLJL-J|LJLJL7L7F-----JJFJL-JF-7F7LJF--JLJL|7|.FF--J-|
J.LLJF7L-JLJL-7|L7F7FJFJF--7LJLJF--7F7LJLJ7LJ|L7L-J.LJ|L-7|L7FJF-J-7LJ-JL|L--77FL7F7F---7F7F7|F-7F7L7|L-----7FJF7F7|7LJL-7L---77F7LL-F7J7.F7
L.|L-|L7F7JF--J|FJ||L7L7|F-JF7F-JF7LJL77F77F7L-JF--7F7L--JL7LJFJ||-L-J7.F-.|--7FFJ||L7F-J|||||L7LJL-J||F----J|FJLJLJF---7L----JF-7JLJLJ.FFLJ
JF|FLL7|||FJF-7|L7||FJLLJ|F7|||F-JL---JFJL-JL7F-JF7|||F77JF|F7L-77-F7L-FF.FF7.--|FJL-JL7FJ||||FL--7F7L-JF7F7||L----7|F--JF--7-F7-L-.7--7J7JJ
LL|FF7||||L7|FJL7|||L7F7FLJ||||L7F---7.|F----JL7FJ|||LJL7FFJ|L--J7-|J7LL-.LJ--..LJF----J|F||||F---J|L--7|LJL-JF----J|L---JF-JFJL77LFJ-||J|J7
|LLFJLJLJL-J|L7FJ||L7||L---J||L7||F--JFJL----7FJL7LJL7F7L7L7L7F7F7J.FFFJL-JJ|LJ-L|L-7F7FJFJ|LJL----J-F7LJF----JF--7||F----J.FJF7L-7J.FF|-L-J
|7.L-7F--7F-JFJL7LJ-LJL-7F--J|FJLJL---JF7F7F-J|F-JF-7||L-J-L7||LJ|J-FJ|7F|..F7JJLLF-J|LJ7L-JF----7F7FJL--JF----JF7L-JL---7-FJFJ|F-J|LJ7LJJ.L
.FLLL||F-JL-7L-7L-7F-7F7LJF--J|F7F-----JLJLJF-JL-7L7|||LF7F-JLJF-JFF7JLL7|F-7J|||LL--JF-7F7.L-7F7LJLJF-7F-JF--7FJ|F7F7F-7L-JFJJLJ.|7|||.F-7|
F-.L.LJL7F7FJF-JF7|L7LJL7FJF--J|||F------7F7|F--7L-JLJL7|LJF7F-J|7L||F7JL77.LLF--J|LFLL7|||F-7LJL----JLLJF-JF7LJFJ|LJLJ|L-7FJ7.F7FF-F7|F-F|J
L|.|7|FFJ|||JL7FJ||-L--7|L-J.F7||LJF7F7F-J|||L-7L7F7F-7LJF7||L--77J|LJ|-F7F-FFLJ|-F-7F-JLJLJFJF7F7F---7F-JF-J|F7L-JF7F---7|L-7FJ|FF7|L7-7FJ7
.|.-7-F|FJ|L77LJJ||F---JL----JLJL--JLJLJF7|||F-J.LJLJ7|F-JLJ|F-7L77L-7|.LLJF-77JFFL7|L-7F7F7L-JLJ|L--7|L--JF-J|L-7.|LJF7FJL--JL7L-JLJFJF7.J7
L7.|-F-J|FJFJJ-LLLJL7F7F7F---------7F-7FJLJLJL---7F7F7LJF--7||FJFJF--JL7L|7|FJF7FF-JL-7LJLJL----7|LF7||F---JF7|F-JFJF-JLJF7|F7||F----JF|JF7|
.J-.L|F7||FJJ|7-|.J|LJLJLJF-----7F-JL7||F7F7F7F-7LJLJL--JF-J||L7|7L-7F-J-FFJ|FJL7L---7|7F7F77F--JL-JLJLJF7F7||||F7L7|F7LFJL7|L7||F-----77LL|
-J.JJLJLJLJ7.|FFJ7-F------JF---7|L---JLJ|LJLJ|L7|F-----7FJF7LJLLJ-LFJL7J-FL7LJF-JF---JL-JLJ|FJF7F-7F----JLJLJLJLJ|FJLJL7L7FJ|FJ|||F-7F-J7.JJ
LFL7L||JL|.FJJ7J.7.L-------JF--JL------7L---7L7||L----7LJFJL7F7-|LFJF7L7F7FJF7|F-JF-------7|L-JLJFJ|F-----7F-7F--J|F--7L-JL-JL-JLJL7LJ|L--|.
F-L7.LJ7LJL|JL7FFJ7LLF7LF---JF7F7F----7L----JJLJL7F7F7L--JF-J||F-7L-J|FJ|||FJLJL--JF------JL----7L-JL----7LJFJL--7|L-7|F7F7F7F7F--7L7L7-LFL-
|.||.FF7.F-L-F7F7F-F-J|FJF--7|LJLJF--7L---7F-7LF7LJ||L7F--JF-J||FJF7FJL7|||L---7F7LL7F-7F7F---7FJFF-7F7F7L-7L7F-7LJF-J|||||||||L-7L-J.L7J.|7
FJF|JF|JFL-J-|||L7-L-7LJFJF7LJF7F7L-7L----J|FJFJL7F|L7|L--7|F7||L-JLJF7LJLJF7F-J||7LLJFJ|||F-7||F7L7||LJL--JFJL7L--JF7LJLJLJ||L7FJF7J7||FF.-
|L-||-J7JL7LL|LJFJF77L7FJFJL--JLJL--JF7F---JL-JF7L7|FJL7F7|LJ||L-----JL7F--JLJ|FJL7J.FJFJLJL7LJLJL-JLJF7F--7|F7L----JL7F7F7JLJFJ|F||-J|-7J-J
FFLJ77.77-JJJ|F7L7||F7||FJF7F--------JLJF------JL-JLJF7LJ|L7FJ|F7F7F7F7||F---7FJF-JF7L-JF--7L7F7F7F-7FJLJF7||||F---7F7LJ||L--7L-JFJL7.|.J|||
L-77L-7|-J..-LJL7|||||LJL-JLJF----7F7F7FJF----77F--7L|L-7|FJL7||||LJ||LJLJF7FJL7|FL|L--7L-7|FJ|||||LLJFF-JLJLJ|L7F7|||F7LJF--JF--JF-J.|..FL7
|L---|J.L.77-FF7|||LJ|FF7F-7FL7F-7LJ|||L-JF--7L7|F7|FJF-J||F7|||LJF-JL-7F-JLJF-JL7-L--7L--JLJFJLJLJF7F7L---7F7L-J||LJ|||F7L---JF-7L7F7--7.L|
F-J--JJ-L|L|-FJLJ|L-7|FJ||FJF7LJFJF7LJL-7FJF-JFJ||LJL7|F7LJ||||L7FJFF--JL-7F7L7F-JF-7-L7F---7|F7F7FJLJL77F-J|L7F-JL-7LJ||L7F7F-J|L-J||JL-7.|
J|.FJJL.LJ-J.L--7L--J|L7|||FJL77L-JL---7LJ7|F7L-JL7LFJLJL-7||||FJ|F7L-7F--J||FJL-7L7|F7LJF7FJ||LJLJF7F7L-JF7L7||F---JF7||7LJ|L------J|77L|--
LF7FF7-7FF7L-J.LL7F-7L7|||||F7L-------7L--7LJL-7F-JFJF7F--J||||L7LJ|F7|L7F7|||F--JFJLJL7FJ|L-JL7F-7|||L7F-JL-JLJL---7||LJF7|L7F------JJ-F--7
.L-7L7-L-||7|F7F-J|7L7LJLJ|LJL-7F7F7F7L7F7L77F-JL7FJFJLJF7FJ||L-JF-J|||FJ|||||L--7L---7|L7|F7F7LJFJ|LJ7LJF--7F------J||F-JL-7|L----7F|J-JFF|
FFLJJ|L|-F-7-||L7FJF7L---7L7F7LLJLJLJL7LJL7L7L-7FJL7L7F7|LJFJL-7FJ7FJLJ|||||||F-7|LF7FJL7|||||L7|L-JF----JF7|L-------JLJF-7FJ|F-7F7L-777L-FJ
F--J-L-F-JFJ-|L7|L7|L----JFJ||F7.F7F-7L--7L-JF7||F-JFJ|||F-JF-7|L-7L--7L7|LJ||L7LJFJ|L7FJ||||L7|F7F7L-----J|L7F7F-7F-7F7L7|L7|L7LJL7FJ.L-L-F
|-L|||F|F7L7.L7|L-JL-7F7F7L-JLJL-JLJL|F--JF7L||LJL7FJJ|LJ|F7|FJ|F-JF7-L7|L7FJL7L7FJFJ-||FJLJ||||||||F7FF---J-LJLJF|L7||L7||FJL7L-7L||LJ7F7J|
|.|L-7FLJ|FJF-J|F7LF7LJLJL---7F7F---7LJF7FJ|FJL7F-J|F7L-7||||L7|L-7|L-7|L7||FFJFJL7||FJLJF--JFJLJ||||L-JF--------7L-JLJ7|||L-7|F-J.LJ--F||LL
|-FJLF---JL-JF-J||FJ||F7F---7LJLJ7F-JF7||L7|L7FJL-7LJL-7|LJLJFJ|F-J|F-JL7||L7L7L7FJL7L7F-JF77L7F-J||L---JF-------JF-7F-7LJL--JLJJ.FJ-F-JLF-J
|-L.FL-7F-7F7L7L||L7|FJ|L7F7||F7F7L-7|LJL-JL7|L7F7L7F7FJ|F---JF|L7J||F7FJ||FJ-L7|L7FJFJL-7|L7FJL7FJ|F----JF7F7F7F7L7LJFJFF7F7F7|F----7JJLLJ.
|7|FF-L||JLJL7|FJ|FJ||FJFJ||L-JLJL7FJ|F-----J|FJ||FJ|LJFJL7F7F-JFJFJ||||FJ||F7FJ|FJL-JF--J|FJL7FJL7|L-----JLJ||LJL-JF7L--JLJLJL-7JJ-F|...JLF
J-7-|JFLJF7F7||L7|L7||L7L-JL-----7|L-J|F---7FJL7|LJFJF7|F-J||L-7L-JFJ|||L7||||L7||F--7L-7FJL--J|F7||F-7F7F7F-J|F----JL----7F----J-|.J-|..||.
J.L-LJ-LFJLJLJL7||FJ||FJF7F7F-7F7|L-7FJ|F--JL-7|L-7|-|||L7FJL7||F--JFJLJFJ|LJ|FJ|LJF7|F-JL--7F7|||||L7LJLJLJF7|L-77F77F7F7LJ-F7-F77FL7J-LJ--
LF.|LJ|LL-----7|||L7|||FJLJ|L7LJLJF7LJ-|L-7F--JL-7|L-JLJFJL-7L-JL7F7|F--JF|F-JL7|F7|||L--7F7|||||LJ|7L7F-77FJLJF7L-JL-JLJL---JL7||JFJ|-|-|.J
F|--.JJLLF----JLJL-JLJ|L--7|-L7F-7|L7F7L7FJL--7F7LJF----JF-7L--7FJ|||L-77FJL-77||||||L7F-J||LJ|LJF-JF7LJFJFJF7FJ|F7F----7F7F7F7||L7LF7F||F-|
LJFL-|L7.L--7F-7F7F7F7|F7FJ|F7LJ-LJFJ|L7|L7F--J|L--JF---7L7|F7FJL7|LJF-JFJF--JFJ||||L7|L7FJ|F7L-7|F7|L7FL-JFJLJLLJLJJF-7LJLJLJ|LJFJ-.J7LL7L-
|.|J-7-J-F--J|FJ|LJLJ||||L7LJL-7F7FJ7L7||FJL--7|F7F7|F--J-||||L7FJL7FJF7L7|JF7L7||||FJ|FJL7|||F7|||||FJF7F7L7F--7F7F7|FJFF---7L-7||L-FL--|7J
LFJ.||..FL---JL7|F---JLJ||L---7||LJF7FJ||L-7F7|LJ||||L7F7FJ||L7|L7FJL7|L7|L7|L7||||||FJ|F7||||||||||||FJ||L7LJF-J|||LJL--JF--J-LLJJ7FFJ-FF-7
FJFFF-F77LF---7LJL----7FJF7F--JLJF-JLJ-|L-7|||L7FJ|LJFJ|||FJL7||FJ|F-JL7|L7|L7LJ||LJ||F||||||LJ|||||||L7LJFJF7L--J||F-----J.F77F7|LF7F-7LJ||
LF|7-L|L-7L--7L7F7F---JL-JLJF-7F7L-7F--JF-J|||FJL7L7FJFJ|||F-J||L7|L7F-J|FJ|FJF7||F-JL7LJ|||L7FJ|||||L7L-7L7||S7F7LJL-------JL-J|FFF-JFJ|-7|
LJJ|J|L7FJ-F7L7||||F7F7F---7|FJ||F7|L7F7L-7|||L7||FJL-J-LJ|L-7||FJ|FJ|F-JL7|L-J|||L7F-J|FJ|L7|L7|||||.L7FJFJ||||||F7F-7F--------JF7L7FJJ||LL
F|L|LF-JL--J|7||||LJLJLJF--J||FJ|||L7||L7FJ|||FJFJL----7F-JF-JLJL7||FJL-7FJ|F7FJ|L7||JF-JFJFJL7|||||L7.|L7L7|||||LJ|L7|L---------JL-J|--.|||
-|JJFJF--7F7L-JLJL------JF7FJ||FJ||FJ||||L7|||L7L-7F7F7|L-7L--7F7LJ|L7F7LJFJ||L7L7||L7L7FJ7|F7|||||L7L7L7L7|||||L7FJFJL----------7F7FJFF7J77
LJ.LL-JF-J||F7F-7F------7|LJFJ|L7|||||L7|FJ|||FJF-J|LJ||F7|F-7LJ|F-JFJ||F7|FJ|FJFJ|L7L7|L-7LJ|||||L7L7|FJFJ|||||FJL7L-----------7LJ|L--7J.77
FF|7LF7L7FJLJ||FJ|F-----JL77L7|FJ|||FJFJ|L7||||FJF7L-7LJ|LJL7|F7||F7L-JLJ||L7|L7L-JFL7||F7L-7|||||FJFJ|L7|FJ|||LJF-JF-------7F-7L-7|F--JL|L-
FL|JFJL7LJ-F-J|L-JL7F7F7F7|F-J|L-J|||FJF|FJLJ||L7||F7|F7L-7FJLJ||LJL7F7F-JL-JL7L7FF--J|LJL7FJ||||||FL7L7||L7|||F7L-7L------7|L7L-7|LJ7-J7|.|
LFL7L-7L---JF7|F7F-J|||||LJL-7|F--J||L-7||F--J|FJ|LJLJ|L--JL--7|L7F-J|||F--7F7|FJFJF7FJLF7||FJ|||||F-JFJLJ-|||LJ|F-JF7F----JL7L7-LJJ.F-J|JF-
FJ|L|LL7F7F7||||LJF7|||||F---J|L--7|L7FJ|||F-7|L7L-7F-JF7F7F7FJ|FJL7FJ|LJF7LJ|LJ7|FJ|L-7||||L7|LJ|||F7L-7F-J||F-J|F7||L-----7L-J-JJ|-7|J|J|J
J7|LFJFJ|LJLJ||L7FJLJ||LJL-7F7L--7|L7|L7||||-|L7L7FJL-7|||||LJFJ|-FJL7L7FJ|F7L--7LJFJF7LJ||L7||F-J|LJL7FJL-7|LJF-J|||L7F7F-7L---7J.L7||7|-77
FJJF77L7|F---J|FJL7F7||F---J||F7FJ|FJ|FJLJLJFJFJFJL7FFJ||||L-7L7L7|F7|FJL7|||F--JF7|FJL7FJ|FJLJL-7L-7FJL-7FJL-7L-7|||FJ||L7L----J77-J7|L|J.7
F-FJL|-||L7F-7|L--J|LJ||F7F7|LJLJ-||JLJF7FF7|FJ||F7L7L7|||L7FJFJFJ||||L7FJLJ|L-7FJLJL-7|L7|L7F---JF-J|F7FJ|F7FJ|FJ||||FJL7L--7F77J|FFFJ7|7.|
L7JL|L-LJ7||FJ|F---JF7||||||L--7F7|L--7|L-JLJL-7LJ|FJFJ|LJL|L7L7L7||||FJL--7|F-JL-7F7FJL-J|FJL-7F7L-7LJLJFJ||L7FJFJ||LJ|-L7F7LJL7-F|--LJJLF-
-|||.LLL7F||L-JL--7FJ||LJLJL7F7LJ||F7FJL7F-7F-7L-7LJFJFJJF-JFJ|L-JLJ|||F-7FJ|L7FF-J||L---7||LF-J||F7L7F7-|FJL-JL7L7|L--7F-J|L7F-J-|LJ.LJ7.||
LL7L-J|-7-LJ|-F---J|FJL--7F-J||F7||||L7FJ|.||FJF-JF-JFJF-JF7L----7F-J||L7|L7L7L7L7FJL7F7FJLJFJF7|||L7LJL7|L--7F-JFJL-7FJL-7|FJ|JJ.L-7|J.7-F|
.|LFL7JF-JL|7FL----JL7F--JL7FJLJ||LJ|FJL7|FJ||FJF-JF7L7L-7||F7F7FJL-7|L-J|FJFJFJFJ|F-J|||F7J|FJ|||L7L7F-JL7F7|L-7|F7L||J7FLJ|FJ--|7LFJ.J|FJJ
FF77-J7FJFL7-L.F-----J|F7F-JL7F7|L7FJ|7FJ|L7||L7L7FJL7|F-J|||||||F--J|-F7LJFJFJJ|FJ|F7||LJL7LJFJ|L7|FJL-7FJ||L7FJLJL7||FL|.LLJJ-J|F7L|FJ7JL7
|JFJ-F7JFFF7.LLL--7F-7|||L7F7LJ||FJL7L7L7|FJ|L7|FJ|F-J||F7|||LJ||L7F7L7|L-7L7L-7||FJ||||F-7L-7|FJLLJ|F--JL7||FJ|F7F7|||JJL7|L-|-77L77|7-F7.|
7-L7.FFJL-|L-FLLJ|||-LJ|L-J|L7FJLJFLL7|LLJL7|FJ|L7||F7||||||L-7||FJ|L7LJF7L7|F7||||FJ||LJ7|F-JLJ-LF-JL777||||L7||||LJLJJ7-LLJF7LJL|J7LF-|7.7
|.JJF|J.L-JJF-7..FLJ77FJF7FJL|L--777.|L7JL-LJL7L7LJLJ||LJ|||F-J||L7||L7FJ|FJ||||LJ||FJL7-FJL-7.L--L7F-JJ-FJ|L7|||LJJL|.LF7.F|J|7J.J7|JL-F-JJ
|7|F7J-F--7-JL|--|JJF-JFJ||F-JF--J||-|FJ.J7J.FL-JF-7FJL-7|||L-7||FLJF-JL7|||||||F7||L7FJFJF-7L7-7LL||LF|||FJ-LJ|L7JFF7J.LJ-|7-F-.7J7..F7LF77
LJ|.LJF-7.J7.|||F|-FL-7L7||L-7L-7JFLFLJJ7F|7F|FF7L7LJF7FJLJ|F7|LJF--JF7FJLJFJ||LJ|||-||FJFJ-|FJ.|77LJ7-F-LJL-.LL-JFJ.|JL.|7LJ.JL-LJ|F.F7JL7J
L7|7.FL.F7LF-LJJJ|..L-L-J|L7FJF-JF77.L|JFJ.FF--J|FJF7||L--7LJ|L7LL-7FJ|L--7L7||F-JLJJLJL7||L||7.LF-JFLLF7.LLJ-7L7LJ-L7-7F-77|FJ.LJ7|.7||F-F.
F7J|-LLJF-7L-||7F7-7F-JFLL-JL7L--J|7|-|LFLJ-L--7LJFJ||L--7L-7|FJF--J|FJF7FJJ|||L77-LFL-LLJJ-LJJ77.FL|.F77F||LL7LJ7J|F|JL--J-F7--7FJ.L|F-7FJ7
FL7|L|.F7JF-.LFL|LJFL|-FJJ|LLL7F-7L-7|LF77||LL-|F7|FJL7F7|F-J||F|F-7||FJ||JL||L7L7J7|L.L|7.L||LFFJ7-777||LJF7|LJF--7---F|7L7LJ7|LJ-F.LL7J7L|
L.F|-L--F-|JFF7F|--7.L--..J.LFJL7L-7|7FJJL|-7J.LJ||L7FJ|LJ|F-JL7LJFJ|||FJ|JFLJJ|FJ-J7FF---|F77.FJFL.LF-LJ-LFJL-7-7FF7J7|L-.LJLF--|.-.|JL7F7L
.-J|||FFJ-JFFJ.LJLL-JFL|LFJ7J|F7L7LLJFJJJ-|.7.-7FJ|FJ|-L7FJL7F7L-7|FJ|||FJ.7||LLJJJJ|L7LLJL-JJ.JFJ7J.L|7J.FL|.7J.F7LJ.JL777.|F.LFLJJF-7F|LLJ
7F-L|-7L|JLF|7JF|.F|.L7FJJ.FFLJ|FJFJ.LJ.7|F-J-JFL7|L7L7L||F-J|L7FJ||-||LJJ..77|-J-.-FLJ7F-7F|7||7-L.FJLJF7J.J.LJ|L|7J-|F.F-FLJ||.|J.7.F-L.||
||7JL-JJL7.F.-.FLF-|-7L7J||-|J-LJ-L-F.|FJ-|-|LLJ.LJJL-J-LJ|F-JFJ|F|||LJ-LJ--JLF-FF7L|J|7|F|LFJL7|F|-|-F-JJ..|.|..FL-.L-.FF--7L|-F7.L|.-J7LL7
7.77.FL-JJFFJ7.77JLL.F7L7FF7-7.LJ.FF77F-J||.||.F|J7F||JFJLLJ-LL7L7LJ-L.FJ77.|.JLLL-JJF--|F|-L-FF7LJ.|||LLF-77-L7--7LFF-7.|L7|-----7.J-FF7|-|
.LLLF|F77F-JLF7-J-|LF.F-F|J|L7-JJ-J-J-7-7-7|JJ-|7-J-LF7L|-J|7|FL-JLJJ|7FJF7LJ.L-7.L7-L|FJJJ-|7|L|-J-J-77LL.F-7-|7LF.7JL-F7|-|LJ..F|7-F7LF7FF
FJ|L7JLJ-L...L|J..J7L7|FJL7--7|..||||FL--7L7.L-||.JJFJJ|F-LJ7|JJ||LF7L7JJ|L|.|.LFJLL7.-|JJ|FF-|||FL-JFJ|F7-|-J--|7LFJ77F|JL7L7LF-|FJ7J|.|FJ-
J.FJ|LLJLL-|-.LL-L-|LJ-LL-L-JLL-.-JJL7-7J|LJJ7.-|JJ--L-J.FLJ-|L7--.-J-L--JLLFJL-FJ.|J.LJJLLLJ-J-L7-LL7JL-|JLJ-LLLJ-LJ|JFF7J..-7J-LJ..7.FFJJJ
'''

# COMMAND ----------

import collections


m = collections.defaultdict(lambda: '.', {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)})
start_pos = next(pos for pos, c in m.items() if c == 'S')
m[start_pos] = 'F' # Hard coded based on input
q = collections.deque([(start_pos, 0)])
distances = {}

while q:
    pos, d = q.popleft()
    if pos in distances:
        continue
    distances[pos] = d

    d += 1
    if m[pos] in '|LJ': # N
        q.append(((pos[0] - 1, pos[1]), d))
    if m[pos] in '-LF': # E
        q.append(((pos[0], pos[1] + 1), d))
    if m[pos] in '|7F': # S
        q.append(((pos[0] + 1, pos[1]), d))
    if m[pos] in '-J7': # W
        q.append(((pos[0], pos[1] - 1), d))

answer = max(distances.values())
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is <em>within the area enclosed by the loop</em>?</p>
# MAGIC <p>To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:</p>
# MAGIC <pre><code>...........
# MAGIC .S-------7.
# MAGIC .|F-----7|.
# MAGIC .||.....||.
# MAGIC .||.....||.
# MAGIC .|L-7.F-J|.
# MAGIC .|..|.|..|.
# MAGIC .L--J.L--J.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>The above loop encloses merely <em>four tiles</em> - the two pairs of <code>.</code> in the southwest and southeast (marked <code>I</code> below). The middle <code>.</code> tiles (marked <code>O</code> below) are <em>not</em> in the loop. Here is the same loop again with those regions marked:</p>
# MAGIC <pre><code>...........
# MAGIC .S-------7.
# MAGIC .|F-----7|.
# MAGIC .||<em>OOOOO</em>||.
# MAGIC .||<em>OOOOO</em>||.
# MAGIC .|L-7<em>O</em>F-J|.
# MAGIC .|<em>II</em>|<em>O</em>|<em>II</em>|.
# MAGIC .L--J<em>O</em>L--J.
# MAGIC .....<em>O</em>.....
# MAGIC </code></pre>
# MAGIC <p>In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, <code>I</code> is still within the loop and <code>O</code> is still outside the loop:</p>
# MAGIC <pre><code>..........
# MAGIC .S------7.
# MAGIC .|F----7|.
# MAGIC .||<em>OOOO</em>||.
# MAGIC .||<em>OOOO</em>||.
# MAGIC .|L-7F-J|.
# MAGIC .|<em>II</em>||<em>II</em>|.
# MAGIC .L--JL--J.
# MAGIC ..........
# MAGIC </code></pre>
# MAGIC <p>In both of the above examples, <code><em>4</em></code> tiles are enclosed by the loop.</p>
# MAGIC <p>Here's a larger example:</p>
# MAGIC <pre><code>.F----7F7F7F7F-7....
# MAGIC .|F--7||||||||FJ....
# MAGIC .||.FJ||||||||L7....
# MAGIC FJL7L7LJLJ||LJ.L-7..
# MAGIC L--J.L7...LJS7F-7L7.
# MAGIC ....F-J..F7FJ|L7L7L7
# MAGIC ....L7.F7||L7|.L7L7|
# MAGIC .....|FJLJ|FJ|F7|.LJ
# MAGIC ....FJL-7.||.||||...
# MAGIC ....L---J.LJ.LJLJ...
# MAGIC </code></pre>
# MAGIC <p>The above sketch has many random bits of ground, some of which are in the loop (<code>I</code>) and some of which are outside it (<code>O</code>):</p>
# MAGIC <pre><code><em>O</em>F----7F7F7F7F-7<em>OOOO</em>
# MAGIC <em>O</em>|F--7||||||||FJ<em>OOOO</em>
# MAGIC <em>O</em>||<em>O</em>FJ||||||||L7<em>OOOO</em>
# MAGIC FJL7L7LJLJ||LJ<em>I</em>L-7<em>OO</em>
# MAGIC L--J<em>O</em>L7<em>III</em>LJS7F-7L7<em>O</em>
# MAGIC <em>OOOO</em>F-J<em>II</em>F7FJ|L7L7L7
# MAGIC <em>OOOO</em>L7<em>I</em>F7||L7|<em>I</em>L7L7|
# MAGIC <em>OOOOO</em>|FJLJ|FJ|F7|<em>O</em>LJ
# MAGIC <em>OOOO</em>FJL-7<em>O</em>||<em>O</em>||||<em>OOO</em>
# MAGIC <em>OOOO</em>L---J<em>O</em>LJ<em>O</em>LJLJ<em>OOO</em>
# MAGIC </code></pre>
# MAGIC <p>In this larger example, <code><em>8</em></code> tiles are enclosed by the loop.</p>
# MAGIC <p>Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:</p>
# MAGIC <pre><code>FF7FSF7F7F7F7F7F---7
# MAGIC L|LJ||||||||||||F--J
# MAGIC FL-7LJLJ||||||LJL-77
# MAGIC F--JF--7||LJLJ7F7FJ-
# MAGIC L---JF-JLJ.||-FJLJJ7
# MAGIC |F|F-JF---7F7-L7L|7|
# MAGIC |FFJF7L7F-JF7|JL---7
# MAGIC 7-L-JL7||F7|L7F-7F7|
# MAGIC L.L7LFJ|||||FJL7||LJ
# MAGIC L7JLJL-JLJLJL--JLJ.L
# MAGIC </code></pre>
# MAGIC <p>Here are just the tiles that are <em>enclosed by the loop</em> marked with <code>I</code>:</p>
# MAGIC <pre><code>FF7FSF7F7F7F7F7F---7
# MAGIC L|LJ||||||||||||F--J
# MAGIC FL-7LJLJ||||||LJL-77
# MAGIC F--JF--7||LJLJ<em>I</em>F7FJ-
# MAGIC L---JF-JLJ<em>IIII</em>FJLJJ7
# MAGIC |F|F-JF---7<em>III</em>L7L|7|
# MAGIC |FFJF7L7F-JF7<em>II</em>L---7
# MAGIC 7-L-JL7||F7|L7F-7F7|
# MAGIC L.L7LFJ|||||FJL7||LJ
# MAGIC L7JLJL-JLJLJL--JLJ.L
# MAGIC </code></pre>
# MAGIC <p>In this last example, <code><em>10</em></code> tiles are enclosed by the loop.</p>
# MAGIC <p>Figure out whether you have time to search for the nest by calculating the area within the loop. <em>How many tiles are enclosed by the loop?</em></p>
# MAGIC </article>

# COMMAND ----------

# Traverse the loop clockwise and mark everything on the right as "external". Right being external is hard-coded based on the specific input.
external = set()
pos = list(start_pos)
direction = 'N'
while True:
    pos2 = tuple(pos)
    if direction == 'E': # Heading east
        if m[pos2] == '-':
            external.add((pos[0] + 1, pos[1])) # S
            pos[1] += 1 # E
        elif m[pos2] == 'J':
            external.add((pos[0] + 1, pos[1])) # S, E, SE
            external.add((pos[0], pos[1] + 1))
            external.add((pos[0] + 1, pos[1] + 1))
            pos[0] -= 1 # N
            direction = 'N'
        elif m[pos2] == '7':
            external.add((pos[0] + 1, pos[1] - 1)) # SW
            pos[0] += 1 # S
            direction = 'S'
    elif direction == 'S': # Heading south
        if m[pos2] == '|':
            external.add((pos[0], pos[1] - 1)) # W
            pos[0] += 1 # S
        elif m[pos2] == 'L':
            external.add((pos[0], pos[1] - 1)) # W, SW, S
            external.add((pos[0] + 1, pos[1] - 1))
            external.add((pos[0] + 1, pos[1]))
            pos[1] += 1 # E
            direction = 'E'
        elif m[pos2] == 'J':
            external.add((pos[0] - 1, pos[1] - 1)) # NW
            pos[1] -= 1 # W
            direction = 'W'
    if direction == 'W': # Heading west
        if m[pos2] == '-':
            external.add((pos[0] - 1, pos[1])) # N
            pos[1] -= 1 # W
        elif m[pos2] == 'L':
            external.add((pos[0] - 1, pos[1] + 1)) # NE
            pos[0] -= 1# N
            direction = 'N'
        elif m[pos2] == 'F':
            external.add((pos[0] - 1, pos[1])) # N, W, NW
            external.add((pos[0], pos[1] - 1))
            external.add((pos[0] - 1, pos[1] - 1))
            pos[0] += 1 # S
            direction = 'S'
    elif direction == 'N': # Heading north
        if m[pos2] == '|':
            external.add((pos[0], pos[1] + 1)) # E
            pos[0] -= 1 # N
        elif m[pos2] == '7':
            external.add((pos[0], pos[1] + 1)) # E, N, NE
            external.add((pos[0] - 1, pos[1]))
            external.add((pos[0] - 1, pos[1] + 1))
            pos[1] -= 1 # W
            direction = 'W'
        elif m[pos2] == 'F':
            external.add((pos[0] + 1, pos[1] + 1)) # SE
            pos[1] += 1 # E
            direction = 'E'

    if tuple(pos) == start_pos:
        break

# COMMAND ----------

import re

graphic = ''
n_rows = max(row for row, _ in m)
n_cols = max(col for _, col in m)
for row in range(n_rows):
    for col in range(n_cols):
        c = '.' if (row, col) not in distances else m[(row, col)]
        if c == '.' and (row, col) in external:
            c = 'O'
        graphic += c
    graphic += '\n'

# Do some basic replacements to determine what is internal
# Any . next to a pipe MUST be internal - otherwise it would be an O
graphic = re.sub(r'([|LJ7F-])\.', r'\1#', graphic)
for _ in range(100):
    graphic = graphic.replace('#.', '##')
print(graphic)

# COMMAND ----------

answer = graphic.count('#')
print(answer)
