# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/16

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 16: The Floor Will Be Lava ---</h2><p>With the beam of light completely focused <em>somewhere</em>, the reindeer leads you deeper still into the Lava Production Facility. At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.</p>
# MAGIC <p>Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the <span title="Not anymore, there's a blanket!">beam</span> of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.</p>
# MAGIC <p>Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing <em>empty space</em> (<code>.</code>), <em>mirrors</em> (<code>/</code> and <code>\</code>), and <em>splitters</em> (<code>|</code> and <code>-</code>).</p>
# MAGIC <p>The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into <em>heat</em> to melt the rock in the cavern.</p>
# MAGIC <p>You note the layout of the contraption (your puzzle input). For example:</p>
# MAGIC <pre><code>.|...\....
# MAGIC |.-.\.....
# MAGIC .....|-...
# MAGIC ........|.
# MAGIC ..........
# MAGIC .........\
# MAGIC ..../.\\..
# MAGIC .-.-/..|..
# MAGIC .|....-|.\
# MAGIC ..//.|....
# MAGIC </code></pre>
# MAGIC <p>The beam enters in the top-left corner from the left and heading to the <em>right</em>. Then, its behavior depends on what it encounters as it moves:</p>
# MAGIC <ul>
# MAGIC <li>If the beam encounters <em>empty space</em> (<code>.</code>), it continues in the same direction.</li>
# MAGIC <li>If the beam encounters a <em>mirror</em> (<code>/</code> or <code>\</code>), the beam is <em>reflected</em> 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a <code>/</code> mirror would continue <em>upward</em> in the mirror's column, while a rightward-moving beam that encounters a <code>\</code> mirror would continue <em>downward</em> from the mirror's column.</li>
# MAGIC <li>If the beam encounters the <em>pointy end of a splitter</em> (<code>|</code> or <code>-</code>), the beam passes through the splitter as if the splitter were <em>empty space</em>. For instance, a rightward-moving beam that encounters a <code>-</code> splitter would continue in the same direction.</li>
# MAGIC <li>If the beam encounters the <em>flat side of a splitter</em> (<code>|</code> or <code>-</code>), the beam is <em>split into two beams</em> going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a <code>|</code> splitter would split into two beams: one that continues <em>upward</em> from the splitter's column and one that continues <em>downward</em> from the splitter's column.</li>
# MAGIC </ul>
# MAGIC <p>Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is <em>energized</em> if that tile has at least one beam pass through it, reflect in it, or split in it.</p>
# MAGIC <p>In the above example, here is how the beam of light bounces around the contraption:</p>
# MAGIC <pre><code>&gt;|&lt;&lt;&lt;\....
# MAGIC |v-.\^....
# MAGIC .v...|-&gt;&gt;&gt;
# MAGIC .v...v^.|.
# MAGIC .v...v^...
# MAGIC .v...v^..\
# MAGIC .v../2\\..
# MAGIC &lt;-&gt;-/vv|..
# MAGIC .|&lt;&lt;&lt;2-|.\
# MAGIC .v//.|.v..
# MAGIC </code></pre>
# MAGIC <p>Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is <em>energized</em> (<code>#</code>) or not (<code>.</code>):</p>
# MAGIC <pre><code>######....
# MAGIC .#...#....
# MAGIC .#...#####
# MAGIC .#...##...
# MAGIC .#...##...
# MAGIC .#...##...
# MAGIC .#..####..
# MAGIC ########..
# MAGIC .#######..
# MAGIC .#...#.#..
# MAGIC </code></pre>
# MAGIC <p>Ultimately, in this example, <code><em>46</em></code> tiles become <em>energized</em>.</p>
# MAGIC <p>The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, <em>how many tiles end up being energized?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = r'''\....\..-...........|..\........|.........|./.\..............\................/.....-............./...........
......-........../.........--........................|..-../.............................-\.....|.............
....-.-........................................................../..........................|...|......\|.....
....\.-......\|...............................-|........\.............................../......\..............
..|.|.|...-..-...-..................--........../.......................|.\-.../....................-....\....
....\...................|..............|..../../.......................\......................................
...............\.|..............\........\.\.-...--..-...\........................|.|.........................
..........-........\............-....|...|.............\.\...............\./............./....................
...\.....\.\...............||...........................................-...............-...../...|...........
......./......./....-..../...-........./././\..||.......-.|.......\.........\|................./........-.....
......................|./...|......................./...|....\................-....|....|.\...|.../......../..
.\...........\-......\.\|..\\..-|//../............/...............................-........|..|............-..
..|.............../.............|..-./..\....-|...........................-.|......|....\\......-..../...\....
............\......\|.../...............-......./.........\.\.\.../.|.........................................
....\-......./-........../....................|.........-......../........-.............\..|...../...-........
|.................|....................-.............|...........-.-....-...-......-................./|.\.....
|................/......./.........|.........................-/...........|.................\-/|.........\../.
...................-..............\................|..../.||.-....\...............-......................\..\.
.......|......\..-....-...............\.....|../..\..-...........|......../....\.././..........\.|........-..\
..\..|............|....\......../............-.\.................................-............-............\..
.........|.....\...........................................|....|............../..-.............../...........
...........-................................\...../....|.....|..............|.................................
./........................\..\...........................|.|................................-.................
......|\./....................|..../.........\......|.\..-.|.....|........./........|.........-.-.............
.........\.....................-.................\.....|...................../........./..............|.......
.................-.........\........\.....-...................\.....-..\........../........................./|
............|...........-....\..\............-....-........................|...|........../.............\.....
........................................../............/..................\............\..../......\../.......
......../..........-.....-...................../......................-......\..../..\.-...../....|.|....-....
\.........\.......-.................\.......\-......|.......\......................\......................-...
.........../.................|....................................|...\..../.../|.............................
..\.......................\...........-..\...../.................\.\..-................-...........|..........
...../.../............................\............................../.-../........\.-...|....................
...|....\.\...\...........-............\.............|............\.........................../........./.....
........../......../................/.../........................|............-......................\......./
.../............................-.....-...|.......\....................|...............\......................
......|..-|\..\............../.\.............-....-.......\................./.././/......../.....|....../|....
.............\.........\.......\........-...........||.......|...-.............\........./................/.|.
...\...../.-.....................-..........................-..-............../...../......|..|......|......\.
...|................|.............................|........./....\.....\...................................\..
..............-......................../........\.......................|.\/................-.........\.......
.\........\..\.....-.......\.-.-......................\..-........../................../..................--..
........|.....-.......|.../../..........|........\..|...../..\....../..|...............\|.....................
..........|...../........|....../..........-..-................../....-..........|............................
|...............-......../......./..................\.............\..........|.......\............||..........
........|.........|...............|.........../|..-\..........|....|...\..|\.\...............|-..-............
/......./.............-.....-.......\......-./.......\..\............|...\..\...../...............-.\.........
.-.........|....../.............|........|.......|.....-..............-....../............|............-/\....
..-...|........-...............-........\......../.-........................-................../-.......|.....
...\.-.....................-............................\...................||.....-..........\......\..../...
..........\./........\.||\...|..........-...../.......\.///......../...|...................../....--..........
.....\........./../.............-|...-..---.................../....|...\.../.....|./..........|...../.........
/..........-...../........-.................../..................\./.|..............-...-...............|.....
............\.............\..................................\|....|.../.....|..........\..................|..
...........\........./......\.................................../...-.....\.............\..|...........-......
.............\..-......................\.......|.../...............\.....-...|...|............................
................|-...................../|...|......................................\.............|.......|....
..|........./.................../...................../.....|.-...\............-.............................\
|.\........\.-..........|..|.........|\.-|\\.-....-...............................|....|...........-..|.....-.
./................|.|..|......\.....................-..........\........-...................../......|........
........../.........../............../...||..-.........|....\.\.......|..../.......|............./.-......./..
.........\.\.......-................/.../....|...................\.\|./...../........\.....................|..
..............|........-................|..............|.....-.-................\.........|......./......-....
.........................../.-.-...........................-................-.....-.............|.........\.\.
....|....|.../..........................|............................-...........--....../..|.............\\|.
......./...../..............-...............\|............/-..............................-/.....-.\..........
....-........-....\\.....|../.....-......../.............|.............|...../.......\\....../.........|......
......................-.../.................................................................-..../........|.-/
.................|...........-..|.-.......|............/................./......-.....................-.|.....
|...|.........\.|\..\....../..........-......\\......\.....................\/../.........../..../..-...|.|....
.|.|....|.....|\............./.|......-......-............/....-...-......../-|...............................
....../..............\............../....\..............\............|..\.........|....................|......
.........................\|.......-..........................................................\|...............
...............\.........|../.....-......\..................-.........................-..............-......|.
.....|...|.-...........................\..........\......\../.................-...............-........\......
.|........../........../..............|..../...../...|........-......../.\..........\......................-..
.............-|..................../.......-.../......-.../......./......|..........-./.......................
...\.........|.|...................|../.|...........|....................///....-.........-......./.......|...
.\........-.\..................................-\../...../..\......\...................../|.......-...........
........\..................\.......|...|................../\............|........-............\||.../..-../...
.............\..|/...................../....|.|...//....../|............\..\..|.......-..............-........
.........|/..................-............/....../............/....||.........................................
.|............-........|.........-//..........-................../........../..-...............|..|.......\...
........|.../......-..|.\..|..................|./....|.....-................................/.........../.....
..............-..........|......../.................................../.....\.............../.../..\..|/......
--................\...............|.........-.....|...../.........................-.....-.\\..........\.......
.......\.........\.................-..................../......\.....................\.................-......
....|....|......|...\.........\......../............/..../....\.......\...\....\.........|...................|
..........|....\\.............|........./.....|............../...-/...-.||......./......\.....................
..-./..-./.|...............-/.-.............|...............................\.....-...........................
/......|..|\........\........../...................-.\.......-...............-..\.......|.......|..-..........
./..\................................/.-..................-................-......../.......-.....|...........
............|..|.....\............\.\............\......|.-....../........\..|............../...........|.....
...|....|............|......../....|.|............./......................................|....../.|..-.......
............\......\........-.../....................-./....-.../.\....|........|......-...\........../.......
...........................-................./.......\...........................-.......\....................
.-.-.......|.......|.......-..................................../......-\......./..\.-.............-..........
.............../............-...................|..........................\.-..............\.................
..................................../|..............................|.../....\............/|.........\......./
.\...../\.-.........../....-.-|................./.../..../..........|..................................|.....-
..|......................\..................-...........\....-........\......-...-..-........................|
..-.......-......................\....-...........................|.......-../-...-......................|....
.............-..........................|..................................\./.........................-...../
....\......|........................|..................../........................|.|\.......\......../......\
.../........./..................\..../.../\............|.......|...\.\...../...\.....-...........|..|.\.......
....\../..................\...|.........|../..../.......................|..........-...|....\../............./
../......-......\.......\...........\|.......|...-./..........|................|../|......./..................
........../\/............................-.....|...-..|...............|.........................-.\...........
......................|..........\..................../..-........-...../.........-........./.........../.....
/.........-...................\.-\..............\...\....\.......\...|....................../.........|.......
'''

# COMMAND ----------

def count_energized(start_pos, start_dir, m):
    movements = {
        '.^': '^',
        '.>': '>',
        '.v': 'v',
        '.<': '<',
        '|^': '^',
        '|>': 'v^',
        '|v': 'v',
        '|<': 'v^',
        '-^': '<>',
        '->': '>',
        '-v': '<>',
        '-<': '<',
        '/^': '>',
        '/>': '^',
        '/v': '<',
        '/<': 'v',
        '\\^': '<',
        '\\>': 'v',
        '\\v': '>',
        '\\<': '^'
    }

    seen = set() # pos, direction
    stack = [(start_pos, start_dir)]
    while stack:
        pos, direction = stack.pop()

        if pos not in m:
            continue

        if (pos, direction) in seen:
            continue
        seen.add((pos, direction))

        for new_direction in movements[m[pos] + direction]:
            stack.append(((pos[0] + (new_direction == 'v') - (new_direction == '^'), pos[1] + (new_direction == '>') - (new_direction == '<')), new_direction))

    return len({pos for pos, _ in seen}) 


lines = inp.splitlines()
m = {(row, col): c for row, line in enumerate(lines) for col, c in enumerate(line)}
answer = count_energized((0, 0), '>', m)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 16: The Floor Will Be Lava ---</h2><p>With the beam of light completely focused <em>somewhere</em>, the reindeer leads you deeper still into the Lava Production Facility. At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.</p>
# MAGIC <p>Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the <span title="Not anymore, there's a blanket!">beam</span> of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.</p>
# MAGIC <p>Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing <em>empty space</em> (<code>.</code>), <em>mirrors</em> (<code>/</code> and <code>\</code>), and <em>splitters</em> (<code>|</code> and <code>-</code>).</p>
# MAGIC <p>The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into <em>heat</em> to melt the rock in the cavern.</p>
# MAGIC <p>You note the layout of the contraption (your puzzle input). For example:</p>
# MAGIC <pre><code>.|...\....
# MAGIC |.-.\.....
# MAGIC .....|-...
# MAGIC ........|.
# MAGIC ..........
# MAGIC .........\
# MAGIC ..../.\\..
# MAGIC .-.-/..|..
# MAGIC .|....-|.\
# MAGIC ..//.|....
# MAGIC </code></pre>
# MAGIC <p>The beam enters in the top-left corner from the left and heading to the <em>right</em>. Then, its behavior depends on what it encounters as it moves:</p>
# MAGIC <ul>
# MAGIC <li>If the beam encounters <em>empty space</em> (<code>.</code>), it continues in the same direction.</li>
# MAGIC <li>If the beam encounters a <em>mirror</em> (<code>/</code> or <code>\</code>), the beam is <em>reflected</em> 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a <code>/</code> mirror would continue <em>upward</em> in the mirror's column, while a rightward-moving beam that encounters a <code>\</code> mirror would continue <em>downward</em> from the mirror's column.</li>
# MAGIC <li>If the beam encounters the <em>pointy end of a splitter</em> (<code>|</code> or <code>-</code>), the beam passes through the splitter as if the splitter were <em>empty space</em>. For instance, a rightward-moving beam that encounters a <code>-</code> splitter would continue in the same direction.</li>
# MAGIC <li>If the beam encounters the <em>flat side of a splitter</em> (<code>|</code> or <code>-</code>), the beam is <em>split into two beams</em> going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a <code>|</code> splitter would split into two beams: one that continues <em>upward</em> from the splitter's column and one that continues <em>downward</em> from the splitter's column.</li>
# MAGIC </ul>
# MAGIC <p>Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is <em>energized</em> if that tile has at least one beam pass through it, reflect in it, or split in it.</p>
# MAGIC <p>In the above example, here is how the beam of light bounces around the contraption:</p>
# MAGIC <pre><code>&gt;|&lt;&lt;&lt;\....
# MAGIC |v-.\^....
# MAGIC .v...|-&gt;&gt;&gt;
# MAGIC .v...v^.|.
# MAGIC .v...v^...
# MAGIC .v...v^..\
# MAGIC .v../2\\..
# MAGIC &lt;-&gt;-/vv|..
# MAGIC .|&lt;&lt;&lt;2-|.\
# MAGIC .v//.|.v..
# MAGIC </code></pre>
# MAGIC <p>Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is <em>energized</em> (<code>#</code>) or not (<code>.</code>):</p>
# MAGIC <pre><code>######....
# MAGIC .#...#....
# MAGIC .#...#####
# MAGIC .#...##...
# MAGIC .#...##...
# MAGIC .#...##...
# MAGIC .#..####..
# MAGIC ########..
# MAGIC .#######..
# MAGIC .#...#.#..
# MAGIC </code></pre>
# MAGIC <p>Ultimately, in this example, <code><em>46</em></code> tiles become <em>energized</em>.</p>
# MAGIC <p>The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, <em>how many tiles end up being energized?</em></p>
# MAGIC </article>

# COMMAND ----------

best = 0
n_rows = len(lines)
n_cols = len(lines[0])

for col in range(n_cols):
    best = max(count_energized((0, col), 'v', m), best)
    best = max(count_energized((n_rows-1, col), '^', m), best)
    
for row in range(n_rows):
    best = max(count_energized((row, 0), '>', m), best)
    best = max(count_energized((row, n_cols - 1), '^', m), best)

answer = best
print(answer)