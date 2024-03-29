# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/23

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 23: A Long Walk ---</h2><p>The Elves resume water filtering operations! Clean water starts flowing over the edge of Island Island.</p>
# MAGIC <p>They offer to help <em>you</em> go over the edge of Island Island, too! Just <span title="It'll be fiiiiiiiine.">hold on tight</span> to one end of this impossibly long rope and they'll lower you down a safe distance from the massive waterfall you just created.</p>
# MAGIC <p>As you finally reach Snow Island, you see that the water isn't really reaching the ground: it's being <em>absorbed by the air</em> itself. It looks like you'll finally have a little downtime while the moisture builds up to snow-producing levels. Snow Island is pretty scenic, even without any snow; why not take a walk?</p>
# MAGIC <p>There's a map of nearby hiking trails (your puzzle input) that indicates <em>paths</em> (<code>.</code>), <em>forest</em> (<code>#</code>), and steep <em>slopes</em> (<code>^</code>, <code>&gt;</code>, <code>v</code>, and <code>&lt;</code>).</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>#.#####################
# MAGIC #.......#########...###
# MAGIC #######.#########.#.###
# MAGIC ###.....#.&gt;.&gt;.###.#.###
# MAGIC ###v#####.#v#.###.#.###
# MAGIC ###.&gt;...#.#.#.....#...#
# MAGIC ###v###.#.#.#########.#
# MAGIC ###...#.#.#.......#...#
# MAGIC #####.#.#.#######.#.###
# MAGIC #.....#.#.#.......#...#
# MAGIC #.#####.#.#.#########v#
# MAGIC #.#...#...#...###...&gt;.#
# MAGIC #.#.#v#######v###.###v#
# MAGIC #...#.&gt;.#...&gt;.&gt;.#.###.#
# MAGIC #####v#.#.###v#.#.###.#
# MAGIC #.....#...#...#.#.#...#
# MAGIC #.#########.###.#.#.###
# MAGIC #...###...#...#...#.###
# MAGIC ###.###.#.###v#####v###
# MAGIC #...#...#.#.&gt;.&gt;.#.&gt;.###
# MAGIC #.###.###.#.###.#.#v###
# MAGIC #.....###...###...#...#
# MAGIC #####################.#
# MAGIC </code></pre>
# MAGIC <p>You're currently on the single path tile in the top row; your goal is to reach the single path tile in the bottom row. Because of all the mist from the waterfall, the slopes are probably quite <em>icy</em>; if you step onto a slope tile, your next step must be <em>downhill</em> (in the direction the arrow is pointing). To make sure you have the most scenic hike possible, <em>never step onto the same tile twice</em>. What is the longest hike you can take?</p>
# MAGIC <p>In the example above, the longest hike you can take is marked with <code>O</code>, and your starting position is marked <code>S</code>:</p>
# MAGIC <pre><code>#S#####################
# MAGIC #OOOOOOO#########...###
# MAGIC #######O#########.#.###
# MAGIC ###OOOOO#OOO&gt;.###.#.###
# MAGIC ###O#####O#O#.###.#.###
# MAGIC ###OOOOO#O#O#.....#...#
# MAGIC ###v###O#O#O#########.#
# MAGIC ###...#O#O#OOOOOOO#...#
# MAGIC #####.#O#O#######O#.###
# MAGIC #.....#O#O#OOOOOOO#...#
# MAGIC #.#####O#O#O#########v#
# MAGIC #.#...#OOO#OOO###OOOOO#
# MAGIC #.#.#v#######O###O###O#
# MAGIC #...#.&gt;.#...&gt;OOO#O###O#
# MAGIC #####v#.#.###v#O#O###O#
# MAGIC #.....#...#...#O#O#OOO#
# MAGIC #.#########.###O#O#O###
# MAGIC #...###...#...#OOO#O###
# MAGIC ###.###.#.###v#####O###
# MAGIC #...#...#.#.&gt;.&gt;.#.&gt;O###
# MAGIC #.###.###.#.###.#.#O###
# MAGIC #.....###...###...#OOO#
# MAGIC #####################O#
# MAGIC </code></pre>
# MAGIC <p>This hike contains <code><em>94</em></code> steps. (The other possible hikes you could have taken were <code>90</code>, <code>86</code>, <code>82</code>, <code>82</code>, and <code>74</code> steps long.)</p>
# MAGIC <p>Find the longest hike you can take through the hiking trails listed on your map. <em>How many steps long is the longest hike?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = """#.###########################################################################################################################################
#.............#...#...###...#...#.......#...###...#...#...#.....#...#...#...###...#...#...#.....###...#.....#...#####...#...#...............#
#############.#.#.#.#.###.#.#.#.#.#####.#.#.###.#.#.#.#.#.#.###.#.#.#.#.#.#.###.#.#.#.#.#.#.###.###.#.#.###.#.#.#####.#.#.#.#.#############.#
#.............#.#...#.#...#.#.#...#.....#.#...#.#.#.#.#.#.#.#...#.#.#.#.#.#.#...#.#.#.#.#.#.#...#...#.#...#...#...#...#.#.#.#.......#.......#
#.#############.#####.#.###.#.#####.#####.###.#.#.#.#.#.#.#.#.###.#.#.#.#.#.#.###.#.#.#.#.#.#.###.###.###.#######.#.###.#.#.#######.#.#######
#.............#.....#.#...#.#.#.....#...#.#...#.#.#.#.#.#...#...#.#...#.#.#.#...#.#.#.#.#.#.#...#...#.###.....#...#...#...#...#...#.#.......#
#############.#####.#.###.#.#.#.#####.#.#.#.###.#.#.#.#.#######.#.#####.#.#.###.#.#.#.#.#.#.###.###.#.#######.#.#####.#######.#.#.#.#######.#
#.............#...#.#.#...#.#.#...>.>.#.#.#.###.#.#.#...#.......#.....#.#.#.###.#.#.#.#.#...#...#...#.#...#...#.#...#.....#...#.#.#.#.....#.#
#.#############.#.#.#.#.###.#.#####v###.#.#.###.#.#.#####.###########.#.#.#.###.#.#.#.#.#####.###.###.#.#.#.###.#.#.#####.#.###.#.#.#.###.#.#
#.........#...#.#.#.#.#...#...#...#.#...#.#.###.#.#.#.....#...#####...#.#.#...#.#.#.#.#.....#...#...#...#.#...#.#.#.#...#.#...#.#.#.#...#.#.#
#########.#.#.#.#.#.#.###.#####.#.#.#.###.#.###.#.#.#.#####.#.#####.###.#.###.#.#.#.#.#####.###.###.#####.###.#.#.#.#.#.#.###.#.#.#.###.#.#.#
#.........#.#.#.#...#...#.#...#.#.#.#.#...#.#...#.#.#.....#.#.#.>.>.#...#.#...#.#.#.#.###...#...###.....#.....#.#.#...#.#.#...#.#...#...#...#
#.#########.#.#.#######.#.#.#.#.#.#.#.#.###.#.###.#.#####.#.#.#.#v###.###.#.###.#.#.#.###.###.#########.#######.#.#####.#.#.###.#####.#######
#.#.......#.#.#...#.....#...#...#.#.#...###.#.###.#.....#...#.#.#.###.....#...#.#...#...#.#...#...#...#.......#...#...#.#.#...#.#...#...#...#
#.#.#####.#.#.###.#.#############.#.#######.#.###.#####.#####.#.#.###########.#.#######.#.#.###.#.#.#.#######.#####.#.#.#.###.#.#.#.###.#.#.#
#.#.#.....#.#.###.#...#...#.....#.#.....###.#.###.#...#.#.....#.#.#.....#.....#.....#...#.#.###.#.#.#.###...#.......#.#.#...#...#.#...#...#.#
#.#.#.#####.#.###.###.#.#.#.###.#.#####.###.#.###.#.#.#.#.#####.#.#.###.#.#########.#.###.#.###.#.#.#.###.#.#########.#.###.#####.###.#####.#
#...#.#.....#.#...#...#.#.#...#.#.#...#...#...###.#.#...#.......#...#...#.>.>...#...#.#...#...#.#...#.>.>.#.#.....#...#...#.#.....###...#...#
#####.#.#####.#.###v###.#.###.#.#.#.#.###.#######.#.#################.#####v###.#.###.#.#####.#.#######v###.#.###.#.#####.#.#.#########.#.###
###...#.....#...###.>.#.#.....#...#.#...#.......#.#.###...###.........#.....#...#.#...#.....#.#.....###...#.#...#.#.....#...#.....#...#.#...#
###.#######.#######v#.#.###########.###.#######.#.#.###.#.###.#########.#####.###.#.#######.#.#####.#####.#.###.#.#####.#########.#.#.#.###.#
#...#...#...#.......#...#...........###.........#...#...#.....#...#...#.....#.....#.....#...#...#...#.....#.#...#.......#.......#...#.#.#...#
#.###.#.#.###.###########.###########################.#########.#.#.#.#####.###########.#.#####.#.###.#####.#.###########.#####.#####.#.#.###
#.#...#.#.###...###...###.#.................#.....#...#.....#...#...#.###...###...#...#...#####.#.###.....#.#.....#...#...#...#.......#...###
#.#.###.#.#####.###.#.###.#.###############.#.###.#.###.###.#.#######.###.#####.#.#.#.#########.#.#######.#.#####.#.#.#.###.#.###############
#.#.###...#...#.....#...#...#...............#.#...#.#...#...#.#.......#...#...#.#.#.#.#...###...#.....#...#.......#.#.#.....#.......#.......#
#.#.#######.#.#########.#####.###############.#.###.#.###.###.#.#######.###.#.#.#.#.#.#.#.###.#######.#.###########.#.#############.#.#####.#
#.#...#.....#.....#...#.....#.................#...#...#...#...#.....#...#...#...#.#.#...#...#.........#.....#...#...#.#...###.......#.#.....#
#.###.#.#########.#.#.#####.#####################.#####.###.#######.#.###.#######.#.#######.###############.#.#.#.###.#.#.###.#######.#.#####
#.#...#.....#...#.#.#.......###.....#...#.......#.#...#...#.#...#...#...#.#.......#.....#...###...#...###...#.#.#...#.#.#...#.........#.....#
#.#.#######.#.#.#.#.###########.###.#.#.#.#####.#.#.#.###.#.#.#.#.#####.#.#.###########.#.#####.#.#.#.###v###.#.###.#.#.###.###############.#
#...#...###...#.#...###.....#...###...#...#####...#.#.###...#.#.#.#...#...#.......#...#.#.#...#.#.#.#.#.>.>.#.#...#.#.#...#.#...#...#...#...#
#####.#.#######v#######.###.#.#####################.#.#######.#.#.#.#.###########.#.#.#.#.#.#.#.#.#.#.#.#v#.#.###.#.#.###.#.#.#.#v#.#.#.#.###
#...#.#.#...###.>.#...#...#.#.###...#####...###...#.#.#.......#...#.#.#...#.......#.#...#...#.#.#.#.#...#.#...#...#.#...#.#...#.>.#...#...###
#.#.#.#.#.#.###v#.#.#.###.#.#v###.#.#####.#.###.#.#.#.#.###########.#.#.#.#.#######.#########.#.#.#.#####.#####.###.###.#.#######v###########
#.#...#...#...#.#.#.#.#...#.>.>.#.#...#...#...#.#.#.#.#...........#.#.#.#.#.......#.........#.#.#.#.#.....#...#...#...#.#.#.....#...#...#####
#.###########.#.#.#.#.#.#####v#.#.###.#.#####.#.#.#.#.###########.#.#.#.#.#######v#########.#.#.#.#.#.#####.#.###.###.#.#.#.###.###.#.#.#####
#.......#...#.#.#...#.#.#.....#.#.#...#.....#.#.#.#.#.#...###...#.#.#.#.#.#.....>.>.#...#...#...#.#.#.......#...#.#...#.#.#...#.###...#.....#
#######.#.#.#.#.#####.#.#.#####.#.#.#######.#.#.#.#.#.#.#.###.#.#.#.#.#.#.#.#####v#.#.#.#.#######.#.###########.#.#.###.#.###.#.###########.#
#.....#...#.#.#...###.#.#.....#...#...#...#.#.#.#.#.#.#.#.###.#.#.#.#.#.#...#.....#.#.#.#.......#...#...........#...#...#...#.#.............#
#.###.#####.#.###.###.#.#####.#######.#.#.#.#.#.#.#.#.#.#.###.#.#v#.#.#.#####.#####.#.#.#######.#####.###############.#####.#.###############
#...#.....#.#.#...#...#.#.....#...###.#.#.#.#...#.#.#.#.#.#...#.>.>.#...#...#.....#...#...#...#.#.....#.........#...#...#...#...#...........#
###.#####.#.#.#.###.###.#.#####.#.###.#.#.#.#####.#.#.#.#.#.#####v#######.#.#####.#######.#.#.#.#.#####.#######.#.#.###.#.#####.#.#########.#
#...#...#.#.#...###.....#.#.....#...#.#.#.#.#.....#.#...#.#.#.....#.....#.#.....#.......#...#...#.......#####...#.#.###.#.#.....#.#.........#
#.###.#.#.#.#############.#.#######.#.#.#.#.#.#####.#####.#.#.#####.###.#.#####.#######.#####################.###.#.###.#.#.#####.#.#########
#.....#.#.#.###.......###...#...#...#.#.#...#.....#.....#...#.......#...#.....#...#...#.#...#...#...#...#.....#...#...#...#.......#.........#
#######.#.#.###.#####.#######.#.#.###.#.#########.#####.#############.#######.###.#.#.#.#.#.#.#.#.#.#.#.#.#####.#####.#####################.#
#.......#.#.....#.....#.......#...###...###...#...#.....###...#...#...#...#...###.#.#...#.#...#.#.#...#.#...#...#...#.....#...###...........#
#.#######.#######.#####.###################.#.#.###.#######.#.#.#.#.###.#.#.#####.#.#####.#####.#.#####.###.#.###.#.#####.#.#.###.###########
#.......#.......#.....#...............#...#.#.#.....#...#...#...#...###.#.#.....#.#...###.#.....#...#...###...#...#.......#.#.#...#.........#
#######.#######.#####.###############.#.#.#.#.#######.#.#.#############.#.#####.#.###.###.#.#######.#.#########.###########.#.#.###.#######.#
#.......#.....#.#...#.#...#...#.......#.#.#.#...#.....#.#...........#...#.......#.#...#...#...#...#.#...#.....#.............#.#...#.#.......#
#.#######.###.#.#.#.#.#.#.#.#.#.#######.#.#.###.#.#####.###########.#.###########.#.###.#####.#.#.#.###.#.###.###############.###.#.#.#######
#.......#.#...#...#...#.#...#.#...#####.#.#.#...#.....#.......#.....#...#.......#.#...#.....#.#.#...#...#...#...#.............###...#...#...#
#######.#.#.###########.#####.###.#####.#.#.#.#######v#######.#.#######.#.#####.#.###.#####.#.#.#####.#####.###.#.#####################.#.#.#
#.......#.#.###.........#...#.....#.....#.#.#.#.....>.>.#...#.#...#.....#.#.....#.....#...#.#.#.....#.#...#.#...#.#...#.......#.....###...#.#
#.#######.#v###.#########.#.#######.#####.#.#.#.#####v#.#.#.#.###.#.#####.#.###########.#.#.#.#####.#.#.#.#.#.###v#.#.#.#####.#.###.#######.#
#.#.......#.>.#...........#.......#.....#.#.#.#.#...#.#.#.#.#.....#.......#...#...###...#.#.#.#.....#...#...#...>.>.#.#.#.....#...#.........#
#.#.#######v#.###################.#####.#.#.#.#.#.#.#.#.#.#.#################.#.#.###.###.#.#.#.#################v###.#.#.#######.###########
#...#...#...#...###.....#.........#.....#.#.#...#.#.#.#...#...#...#...........#.#.#...###.#.#.#.#...............#.#...#.#.#.....#...........#
#####.#.#.#####.###.###.#.#########.#####.#.#####.#.#.#######.#.#.#.###########.#.#.#####.#.#.#.#.#############.#.#.###.#.#.###.###########.#
#...#.#.#...#...#...#...#.........#.....#.#...#...#...#.....#...#.#.........#...#.#.....#.#.#.#.#...#.........#...#.....#.#.#...###...#...#.#
#.#.#.#.###.#.###.###.###########.#####.#.###.#.#######.###.#####.#########.#.###.#####.#.#.#.#.###.#.#######.###########.#.#.#####.#.#.#.#.#
#.#...#.....#...#...#.#...###...#.#...#.#.....#.........#...#.....#...#####.#...#.......#...#...###...#.......#...#.......#.#.#...#.#.#.#.#.#
#.#############.###.#.#.#.###.#.#v#.#.#.#################.###.#####.#.#####v###.#######################.#######.#.#.#######.#.#.#.#.#.#v#.#.#
#.............#...#.#.#.#...#.#.>.>.#...###...............###...#...#...#.>.>.#.#...###...###...###...#.....###.#.#.....#...#.#.#.#.#.>.#...#
#############.###.#.#.#.###.#.###v#########.###################.#.#####.#.#v#.#.#.#.###.#.###.#.###.#.#####.###.#.#####.#.###.#.#.#.###v#####
#.............###.#.#.#...#.#...#...###...#...#...#.......###...#.#.....#.#.#...#.#...#.#.#...#.#...#.......#...#...###...#...#.#.#.#...#...#
#.###############.#.#.###.#.###.###.###.#.###.#.#.#.#####.###.###.#.#####.#.#####.###.#.#.#.###.#.###########.#####.#######.###.#.#.#.###.#.#
#...............#.#.#.#...#.#...###...#.#.###...#...#...#...#.#...#.#...#.#...###.#...#.#.#...#.#.......###...#.....#...###.....#...#.....#.#
###############.#.#.#.#.###.#.#######.#.#.###########.#.###.#.#.###.#.#.#.###.###.#.###.#.###.#.#######.###.###.#####.#.###################.#
###.............#...#...###.#.#.......#.#.....#.......#.....#...###...#...###.#...#.....#...#.#.#.....#...#...#...#...#.#...#...#...###...#.#
###.#######################.#.#.#######.#####.#.#############################.#.###########.#.#.#.###.###.###.###.#.###.#.#.#.#.#.#.###.#.#.#
#...#...#.....#.......#...#...#.......#.#.....#.........###...#...###...#...#...###...#.....#.#.#...#.#...###.#...#.#...#.#.#.#.#.#.#...#.#.#
#.###.#.#.###.#.#####.#.#.###########.#.#.#############.###.#.#.#.###.#.#.#.#######.#.#v#####.#.###.#.#v#####.#.###.#.###.#.#.#.#.#.#v###.#.#
#...#.#.#.#...#.#.....#.#.....#.......#.#...#...........#...#.#.#.#...#.#.#...#...#.#.>.>.#...#.#...#.>.>.....#.....#.#...#.#.#...#.>.###...#
###.#.#.#.#.###.#v#####.#####.#.#######.###.#.###########.###.#.#.#.###.#.###.#.#.#.###v#.#.###.#.#####v#############.#.###.#.#######v#######
###...#...#.....#.>.#...#.....#.......#.#...#...........#.#...#.#.#...#.#.###.#.#.#.#...#...###...#.....#.....#...###.#...#...#.......###...#
#################v#.#.###.###########.#.#.#############.#.#.###.#.###.#.#.###.#.#.#.#.#############.#####.###.#.#.###.###.#####.#########.#.#
#.................#.#.#...###.......#...#.....#...###...#.#.###.#.#...#...###.#.#...#.....#.........#...#.###...#...#.#...#...#.......#...#.#
#.#################.#.#.#####.#####.#########.#.#.###.###.#.###.#.#.#########.#.#########.#.#########.#.#.#########.#.#.###.#.#######.#.###.#
#.#.........#.....#...#.#...#.#.....#...#.....#.#.#...#...#.#...#.#.....###...#...#.......#...#...#...#.#.#.........#...###.#.........#.#...#
#.#.#######.#.###.#####.#.#.#.#.#####.#.#.#####.#.#.###.###.#.###.#####.###.#####.#.#########.#.#.#.###.#.#.###############.###########.#.###
#.#.#.......#.#...###...#.#...#...#...#...###...#.#...#.#...#.#...#...#...#...#...#.........#.#.#.#.#...#.#...............#.........#...#...#
#.#.#.#######.#.#####.###.#######.#.#########.###.###.#.#.###.#.###.#.###.###.#.###########.#.#.#.#.#.###.###############.#########.#.#####.#
#...#.........#.....#.#...#.......#.........#...#.###.#.#.#...#...#.#...#...#.#.#...........#...#.#.#...#.#...............#.........#.#.....#
###################.#.#.###.###############.###.#.###v#.#.#.#####.#.###.###.#.#.#.###############.#.###.#.#.###############.#########.#.#####
#...#...#...........#...#...#...#...#...#...###.#...>.>.#...#...#.#...#.#...#...#.........###...#...#...#.#...............#.....#.....#.....#
#.#.#.#.#.###############.###.#.#.#.#.#.#v#####.#####v#######.#.#.###.#.#.###############.###.#.#####.###.###############.#####.#.#########.#
#.#...#.#...#...........#...#.#.#.#.#.#.>.>...#.#...#.........#.#.....#.#.#...#.........#.....#.....#.#...#.....#...#.....#####...#.........#
#.#####.###.#.#########.###.#.#.#.#.#.###v###.#.#.#.###########.#######.#.#.#.#.#######.###########.#.#.###.###.#.#.#.#############.#########
#.....#...#...#.....#...###...#.#.#.#.#...###...#.#.#.......#...###...#...#.#.#.......#.............#.#...#...#...#...#####.........#...#...#
#####.###.#####.###.#.#########.#.#.#.#.#########.#.#.#####.#.#####.#.#####.#.#######.###############.###.###.#############.#########.#.#.#.#
#####...#.#...#.###...###...###...#...#.......#...#...#...#...#...#.#.#...#.#.#.....#...........#...#.....###.............#...........#...#.#
#######.#.#.#.#.#########.#.#################.#.#######.#.#####.#.#.#.#.#.#.#.#.###.###########.#.#.#####################.#################.#
###...#.#.#.#.#.....#...#.#.#...###...###.....#.......#.#.#...#.#.#.#.#.#.#.#.#.#...#.......#...#.#.#.....#...............#.................#
###.#.#.#.#.#.#####.#.#.#.#.#.#.###.#.###.###########.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###.#####.#.###.#.#.###.#.###############.#################
#...#...#...#.......#.#.#.#.#.#...#.#.#...#.......###...#.#.#.#.#.#.#.#.#...#.#.#...#.....#.#.#...#.#.#...#...............#.#...............#
#.###################.#.#.#.#.###.#.#.#.###.#####.#######.#.#.#.#.#.#.#.#####.#.###.#####.#.#.#.###.#.#.#################.#.#.#############.#
#.......#...#.....###.#.#.#.#.#...#.#.#...#.....#...#.....#.#.#.#.#.#.#...#...#.#...#...#.#...#.#...#.#.#...#...........#.#...#.......#.....#
#######.#.#.#.###.###.#.#.#.#.#.###.#.###v#####.###.#.#####.#.#.#.#.#.###.#.###.#.###.#.#v#####.#.###.#.#.#.#.#########.#.#####.#####.#.#####
#.......#.#...#...#...#...#...#.#...#...>.>.#...#...#...###.#.#.#.#.#.#...#.#...#.#...#.>.>.###.#.#...#...#.#.........#.#.#...#.....#.#.....#
#.#######.#####v###.###########.#.#######v#.#.###.#####v###.#.#.#.#.#.#.###.#.###.#.#####v#.###.#.#.#######.#########.#.#.#.#.#####v#.#####.#
#.........#...#.>...#...#...###...#...#...#...#...#...>.>...#...#...#.#...#.#.###.#...#...#...#.#.#.......#.#...#.....#...#.#.#...>.#.#.....#
###########.#.#v#####.#.#.#.#######.#.#.#######.###.###v#############.###.#.#.###.###.#.#####.#.#.#######.#.#.#.#.#########.#.#.###v#.#.#####
#...........#.#.......#...#.....#...#.#.......#...#.#...###...#...###...#.#.#.#...#...#.....#.#.#.#...###.#.#.#.#.###.....#.#.#.#...#...#...#
#.###########.#################.#.###.#######.###.#.#.#####.#.#.#.#####.#.#.#.#.###.#######.#.#.#.#.#.###.#.#.#.#v###.###.#.#.#.#.#######.#.#
#.#.........#.#.....#.....#.....#...#...#.....###...#.....#.#.#.#.#####.#.#.#.#...#.#.......#.#.#.#.#...#.#.#.#.>.>.#...#.#.#.#.#.#...###.#.#
#.#.#######.#.#.###.#.###.#.#######.###.#.###############.#.#.#.#.#####.#.#.#.###.#.#.#######.#.#.#.###.#.#.#.###v#.###.#.#.#.#.#.#.#.###.#.#
#.#.#.....#.#...###.#.#...#.#...###.#...#.........#...###...#...#.....#.#.#...#...#.#.......#...#.#.#...#.#.#.###.#.#...#.#.#.#.#.#.#.....#.#
#.#.#.###.#.#######.#.#.###.#.#.###.#.###########.#.#.###############.#.#.#####.###.#######.#####.#.#.###.#.#.###.#.#.###.#.#.#.#.#.#######.#
#...#...#.#.#...###...#...#.#.#.....#...#...#...#.#.#.................#.#...###...#.#.......#...#.#.#...#.#.#.#...#...#...#.#.#.#.#.#.......#
#######.#.#.#.#.#########.#.#.#########.#.#.#.#.#.#.###################.###.#####.#.#.#######.#.#.#.###.#.#.#.#.#######.###.#.#.#.#.#.#######
###...#.#.#...#.........#...#...#.....#.#.#.#.#...#...................#...#.....#...#.........#.#...###...#...#.......#...#.#...#...#...#...#
###.#.#.#.#############.#######.#.###.#.#.#.#.#######################.###.#####.###############.#####################.###.#.###########.#.#.#
#...#...#...#...#.....#.###...#...###.#.#.#.#.#.....#.................###...#...#.............#.#...#...#####...#...#...#.#...#...#...#...#.#
#.#########.#.#.#.###.#.###.#.#######.#.#.#.#.#.###.#.#####################.#.###.###########.#.#.#.#.#.#####.#.#.#.###.#.###.#.#.#.#.#####.#
#.........#.#.#.#.###...#...#...###...#...#...#.#...#.........###...#...###...###.........###...#.#...#...#...#.#.#.#...#.#...#.#...#.......#
#########.#.#.#.#.#######.#####.###.###########.#.###########.###.#.#.#.#################.#######.#######.#.###.#.#.#.###.#.###.#############
#.........#...#.#.....#...#...#.....#...#...#...#...#...#...#.....#...#.......#.....#...#.......#.......#.#.###...#...###.#.###.............#
#.#############.#####.#.###.#.#######.#.#.#.#.#####.#.#.#.#.#################.#.###.#.#.#######.#######.#.#.#############.#.###############.#
#.............#.......#.....#.......#.#.#.#.#...#...#.#.#.#.#.................#...#...#.#.......###.....#.#.......#...###...#...#...........#
#############.#####################.#.#.#.#.###.#.###.#.#.#.#v###################.#####.#.#########v#####.#######.#.#.#######.#.#.###########
#.......#.....#...#...#...###.......#.#.#.#.#...#...#.#.#.#.>.>.....#...###...###.....#...###...#.>.>...#.........#.#.#...###.#.#...........#
#.#####.#.#####.#.#.#.#.#.###.#######.#.#.#.#.#####.#.#.#.#########.#.#.###.#.#######.#######.#.#.#####.###########.#.#.#.###.#.###########.#
#.....#.#...###.#.#.#...#...#.....#...#...#.#.....#.#.#.#.#...#.....#.#.#...#.#.....#.......#.#...#.....#...#.....#.#...#.#...#...#...#.....#
#####.#.###.###.#.#.#######.#####.#.#######.#####.#.#.#.#.#.#.#.#####.#.#.###.#.###.#######.#.#####.#####.#.#.###.#.#####.#.#####.#.#.#.#####
#.....#.....#...#.#.#.......#...#.#.......#.#...#.#.#.#.#.#.#.#.....#.#.#...#.#...#...#.....#.#.....#...#.#.#.#...#.#.....#.....#...#.#.....#
#.###########.###.#.#.#######.#.#v#######.#.#.#.#.#.#.#.#.#.#.#####.#.#.###.#.###.###.#.#####.#.#####.#.#.#.#.#.###.#.#########.#####.#####.#
#.#...#.....#...#.#.#.#.....#.#.>.>...#...#.#.#.#.#...#...#.#.......#.#.###.#.###...#.#...#...#.#...#.#...#.#.#.###.#.#.......#.....#.###...#
#.#.#.#.###.###.#.#.#.#.###.#.#######.#.###.#.#.#.#########.#########.#.###.#.#####.#.###v#.###.#.#.#.#####.#.#.###.#.#.#####.#####.#.###.###
#...#...#...###.#...#...###.#.#.......#.###...#.#.#.........#...#...#.#.#...#...#...#.#.>.>.#...#.#.#.#...#...#...#.#.#.#.....#...#.#.#...###
#########.#####.###########.#.#.#######.#######.#.#.#########.#.#.#.#.#.#.#####.#.###.#.#####.###.#.#.#.#.#######.#.#.#.#.#####.#.#.#.#.#####
#.........#.....#...###...#.#.#...#...#.......#.#.#...#.....#.#.#.#.#.#.#...###.#.###...#.....#...#.#.#.#.........#.#.#.#.#...#.#.#.#.#...###
#.#########.#####.#.###.#.#.#.###.#.#.#######.#.#.###.#.###.#.#.#.#.#.#.###.###.#.#######.#####.###.#.#.###########.#.#.#.#.#.#.#.#.#.###v###
#.........#.......#.....#.#.#.#...#.#.....#...#.#.###...###...#.#.#.#.#.#...#...#.......#.....#...#...#.#...#.....#.#.#.#.#.#.#.#.#.#.#.>.###
#########.###############.#.#.#.###.#####.#.###.#.#############.#.#.#.#.#.###.#########.#####.###.#####.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.#v###
#.........#...#...#...#...#.#.#...#.....#.#...#.#.#.............#.#.#.#.#.###...#.....#.....#.#...#.....#.#.#.#...#.#.#.#.#.#.#.#.#.#.#.#.###
#.#########.#.#.#.#.#.#.###.#.###.#####.#.###.#.#.#.#############.#.#.#.#.#####.#.###.#####.#.#.###.#####.#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.###
#...........#...#...#...###...###.......#.....#...#...............#...#...#####...###.......#...###.......#...#.....#...#...#...#...#...#...#
###########################################################################################################################################.#
"""

# COMMAND ----------

def get_longest_hike(m, target):
    stack = [((0, 1), 0)]
    longest_hike = 0
    seen = set()

    while stack:
        pos, d = stack.pop()
        
        if pos not in m or m[pos] == '#':
            continue

        if pos == target:
            longest_hike = max(longest_hike, d)

        if (pos) in seen:
            continue
        seen.add((pos))

        for direction in '<>^v':
            if m[pos] in '<>^v' and direction != m[pos]:
                continue

            new_pos = (
                pos[0] + (direction == 'v') - (direction == '^'),
                pos[1] + (direction == '>') - (direction == '<')
            )

            if new_pos not in m:
                continue
            if m[new_pos] == dict(zip('^>v<', 'v<^>'))[direction]:
                continue

            stack.append((new_pos, d + 1))
    return longest_hike


lines = inp.splitlines()
m = {(row, col): c for row, line in enumerate(lines) for col, c in enumerate(line)}
target = (len(lines) - 1, len(lines[0]) - 2)

answer = get_longest_hike(m, target)
print(answer) # 1 minute

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you reach the trailhead, you realize that the ground isn't as slippery as you expected; you'll have <em>no problem</em> climbing up the steep slopes.</p>
# MAGIC <p>Now, treat all <em>slopes</em> as if they were normal <em>paths</em> (<code>.</code>). You still want to make sure you have the most scenic hike possible, so continue to ensure that you <em>never step onto the same tile twice</em>. What is the longest hike you can take?</p>
# MAGIC <p>In the example above, this increases the longest hike to <code><em>154</em></code> steps:</p>
# MAGIC <pre><code>#S#####################
# MAGIC #OOOOOOO#########OOO###
# MAGIC #######O#########O#O###
# MAGIC ###OOOOO#.&gt;OOO###O#O###
# MAGIC ###O#####.#O#O###O#O###
# MAGIC ###O&gt;...#.#O#OOOOO#OOO#
# MAGIC ###O###.#.#O#########O#
# MAGIC ###OOO#.#.#OOOOOOO#OOO#
# MAGIC #####O#.#.#######O#O###
# MAGIC #OOOOO#.#.#OOOOOOO#OOO#
# MAGIC #O#####.#.#O#########O#
# MAGIC #O#OOO#...#OOO###...&gt;O#
# MAGIC #O#O#O#######O###.###O#
# MAGIC #OOO#O&gt;.#...&gt;O&gt;.#.###O#
# MAGIC #####O#.#.###O#.#.###O#
# MAGIC #OOOOO#...#OOO#.#.#OOO#
# MAGIC #O#########O###.#.#O###
# MAGIC #OOO###OOO#OOO#...#O###
# MAGIC ###O###O#O###O#####O###
# MAGIC #OOO#OOO#O#OOO&gt;.#.&gt;O###
# MAGIC #O###O###O#O###.#.#O###
# MAGIC #OOOOO###OOO###...#OOO#
# MAGIC #####################O#
# MAGIC </code></pre>
# MAGIC <p>Find the longest hike you can take through the surprisingly dry hiking trails listed on your map. <em>How many steps long is the longest hike?</em></p>
# MAGIC </article>

# COMMAND ----------

import collections


def get_adjacencies(m, pos):
    adjacencies = []

    for direction in '^>v<':
        new_pos = (
            pos[0] + (direction == 'v') - (direction == '^'),
            pos[1] + (direction == '>') - (direction == '<')
        )

        if new_pos in m and m[new_pos] != '#':
            adjacencies.append(new_pos)
    
    return adjacencies


def get_edges(m, target):
    edges = collections.defaultdict(list) # pos -> [(pos, d), ...]

    stack = [((0, 1), (1, 1), 1)] # prev_node, pos, d
    visited = set()
    while stack:
        prev_node, pos, d = stack.pop()

        if (prev_node, pos) in visited:
            continue
        visited.add((prev_node, pos))

        adjacencies = get_adjacencies(m, pos)
        new_d = d + 1

        if pos == target:
            edges[prev_node].append((pos, d))
            continue

        if len(adjacencies) > 2:
            edges[prev_node].append((pos, d))
            prev_node = pos
            new_d = 1

        for new_pos in adjacencies:
            stack.append((prev_node, new_pos, new_d))
    
    return edges


def get_longest_hike2(m, target):
    edges = get_edges(m, target) # pos -> pos, d

    start_pos = (0, 1)
    stack = [(start_pos, 0, frozenset())]
    longest_hike = 0
    while stack:
        pos, d, visited = stack.pop()

        if pos == target:
            longest_hike = max(longest_hike, d)
            continue

        if (pos) in visited:
            continue
        visited = visited.union(set([pos]))

        for new_pos, d2 in edges[pos]:
            stack.append((new_pos, d + d2, visited))

    return longest_hike


lines = inp.splitlines()
m = {(row, col): c for row, line in enumerate(lines) for col, c in enumerate(line)}
target = (len(lines) - 1, len(lines[0]) - 2)

answer = get_longest_hike2(m, target)
print(answer) # 1 minute
