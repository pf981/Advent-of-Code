# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 13: Mine Cart Madness ---</h2><p>A crop of this size requires significant logistics to transport produce, soil, fertilizer, and so on. The Elves are very busy pushing things around in <em>carts</em> on some kind of rudimentary system of tracks they've come up with.</p>
# MAGIC <p>Seeing as how cart-and-track systems don't appear in recorded history for <span title="Time anomalies! How do they work?!">another 1000 years</span>, the Elves seem to be making this up as they go along. They haven't even figured out how to avoid collisions yet.</p>
# MAGIC <p>You map out the tracks (your puzzle input) and see where you can help.</p>
# MAGIC <p>Tracks consist of straight paths (<code>|</code> and <code>-</code>), curves (<code>/</code> and <code>\</code>), and intersections (<code>+</code>). Curves connect exactly two perpendicular pieces of track; for example, this is a closed loop:</p>
# MAGIC <pre><code>/----\
# MAGIC |    |
# MAGIC |    |
# MAGIC \----/
# MAGIC </code></pre>
# MAGIC <p>Intersections occur when two perpendicular paths cross. At an intersection, a cart is capable of turning left, turning right, or continuing straight.  Here are two loops connected by two intersections:</p>
# MAGIC <pre><code>/-----\
# MAGIC |     |
# MAGIC |  /--+--\
# MAGIC |  |  |  |
# MAGIC \--+--/  |
# MAGIC    |     |
# MAGIC    \-----/
# MAGIC </code></pre>
# MAGIC <p>Several <em>carts</em> are also on the tracks. Carts always face either up (<code>^</code>), down (<code>v</code>), left (<code>&lt;</code>), or right (<code>&gt;</code>). (On your initial map, the track under each cart is a straight path matching the direction the cart is facing.)</p>
# MAGIC <p>Each time a cart has the option to turn (by arriving at any intersection), it turns <em>left</em> the first time, goes <em>straight</em> the second time, turns <em>right</em> the third time, and then repeats those directions starting again with <em>left</em> the fourth time, <em>straight</em> the fifth time, and so on. This process is independent of the particular intersection at which the cart has arrived - that is, the cart has no per-intersection memory.</p>
# MAGIC <p>Carts all move at the same speed; they take turns moving a single step at a time. They do this based on their <em>current location</em>: carts on the top row move first (acting from left to right), then carts on the second row move (again from left to right), then carts on the third row, and so on.  Once each cart has moved one step, the process repeats; each of these loops is called a <em>tick</em>.</p>
# MAGIC <p>For example, suppose there are two carts on a straight track:</p>
# MAGIC <pre><code>|  |  |  |  |
# MAGIC v  |  |  |  |
# MAGIC |  v  v  |  |
# MAGIC |  |  |  v  X
# MAGIC |  |  ^  ^  |
# MAGIC ^  ^  |  |  |
# MAGIC |  |  |  |  |
# MAGIC </code></pre>
# MAGIC <p>First, the top cart moves. It is facing down (<code>v</code>), so it moves down one square.  Second, the bottom cart moves.  It is facing up (<code>^</code>), so it moves up one square. Because all carts have moved, the first tick ends.  Then, the process repeats, starting with the first cart.  The first cart moves down, then the second cart moves up - right into the first cart, colliding with it! (The location of the crash is marked with an <code>X</code>.) This ends the second and last tick.</p><p>
# MAGIC </p><p>Here is a longer example:</p>
# MAGIC <pre><code>/-&gt;-\        
# MAGIC |   |  /----\
# MAGIC | /-+--+-\  |
# MAGIC | | |  | v  |
# MAGIC \-+-/  \-+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /--&gt;\        
# MAGIC |   |  /----\
# MAGIC | /-+--+-\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-&gt;--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---v        
# MAGIC |   |  /----\
# MAGIC | /-+--+-\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-+&gt;-/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   v  /----\
# MAGIC | /-+--+-\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-+-&gt;/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /----\
# MAGIC | /-&gt;--+-\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-+--^
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /----\
# MAGIC | /-+&gt;-+-\  |
# MAGIC | | |  | |  ^
# MAGIC \-+-/  \-+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /----\
# MAGIC | /-+-&gt;+-\  ^
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /----&lt;
# MAGIC | /-+--&gt;-\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /---&lt;\
# MAGIC | /-+--+&gt;\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /--&lt;-\
# MAGIC | /-+--+-v  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /-&lt;--\
# MAGIC | /-+--+-\  |
# MAGIC | | |  | v  |
# MAGIC \-+-/  \-+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /&lt;---\
# MAGIC | /-+--+-\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \-&lt;--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  v----\
# MAGIC | /-+--+-\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  \&lt;+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /----\
# MAGIC | /-+--v-\  |
# MAGIC | | |  | |  |
# MAGIC \-+-/  ^-+--/
# MAGIC   \------/   
# MAGIC 
# MAGIC /---\        
# MAGIC |   |  /----\
# MAGIC | /-+--+-\  |
# MAGIC | | |  X |  |
# MAGIC \-+-/  \-+--/
# MAGIC   \------/   
# MAGIC </code></pre>
# MAGIC <p>After following their respective paths for a while, the carts eventually crash.  To help prevent crashes, you'd like to know <em>the location of the first crash</em>. Locations are given in <code>X,Y</code> coordinates, where the furthest left column is <code>X=0</code> and the furthest top row is <code>Y=0</code>:</p>
# MAGIC <pre><code>           111
# MAGIC  0123456789012
# MAGIC 0/---\        
# MAGIC 1|   |  /----\
# MAGIC 2| /-+--+-\  |
# MAGIC 3| | |  X |  |
# MAGIC 4\-+-/  \-+--/
# MAGIC 5  \------/   
# MAGIC </code></pre>
# MAGIC <p>In this example, the location of the first crash is <code><em>7,3</em></code>.</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "                                             /---------------------------------------------------------------------------------------------\\          
 /----------------------<--------------------+----------------------------\\                                                                |          
 |                                           |                            |                                                                |          
 |  /------------------\\                     |                            |                              /--------------\\                  |          
 |  |                  |                     |                            |                              |              |                  |          
 |  |                  |                     |       /--------------------+------------------------------+--------------+-------\\          |          
 |  |                  |                     |       |      /-------------+------------------------------+--------------+-------+----------+-----\\    
 |  |                  |                     |       |     /+-------------+-----------------\\            | /------------+-------+--------\\ |     |    
 |  |                  |                     |       |     ||             |                 |            | |            |       |        | |     |    
 |  |         /--------+---------------------+-------+-----++-------------+-------<---------+------------+-+--------\\   |       |        | |     |    
 |  |         |   /----+---------------------+-------+-----++-------------+-----------------+------------+-+-----\\  |   |       |        | |     |    
 |  |         |   |    |            /--------+-------+-----++-------------+------------\\    |     /------+-+-\\   |  |   |       |        | |     |    
 |  |         | /-+----+------------+--------+-------+-----++-------------+------------+----+-----+-\\    | | |   |  |   |       |     /--+-+-----+---\\
 |  |    /----+-+-+----+------------+--------+-------+-----++---\\         |            |    | /---+-+----+-+-+---+--+---+-------+-----+--+\\|     |   |
 |  |    |    | |/+----+------------+--------+-------+-----++---+---------+------------+----+-+---+\\|    | | |   |  |   |       |  /--+--+++--\\  |   |
 |  |   /+----+-+++----+------------+--------+-------+-----++---+---\\     |            |    | |   |||    | | |   |  |   |       |  |  |  |||  |  |   |
 |  |   ||    | |||    |         /--+--------+\\      |     ||   |  /+-----+------------+---\\| |   |||    | | |   |  |   |       |  |  |  |||  |  |   |
 |  |   ||    | |||    |         |  |        ||   /--+-----++---+--++-----+------------+---++-+---+++----+-+-+---+--+---+-------+--+--+--+++--+--+\\  |
 |  |   ||    | ||| /--+---------+--+-\\/-----++-\\ | /+-----++---+\\ ||     |            |   || |   |||    | | |   |  |   | /-----+--+--+--+++\\ |  ||  |
 |  |   ||    | ||| |  |         |  | ||     || | | ||     ||   || ||     |            |   || |   |||    | | |   |  |   | ^     |  |  |  |||| |  ||  |
 |  |   ||    | ||| |  |    /----+--+-++-----++-+-+-++-----++---++-++-\\   |            |   || |   |||    | | |   |  |   | |     |  |  |  |||| |  ||  |
 |  |   ||    | ||\\-+--+----+----+--+-++-----++-+-+-++-----++---++-++-+---+------------+---++-+---+++----+-+-+---/  |   | |     |  |  |  |||| |  ||  |
 |  | /-++----+-++--+--+----+-->-+--+-++-----++-+-+-++-----++>--++-++-+---+------------+---++\\|   |||    | | |      |   | |     |  |  |  |||| |  ||  |
 |  | | ||    | ||  |  |    |    |  | ||     || | | ||     ||   || || |   |            |   ||||   |||    | | |      |   | |     |  |  |  |||| |  ||  |
 |  | | ||    | ||  |  |    |    |  \\-++-----++-+-+-++-----++---++-++-+---+------------/   ||||   |||   /+-+-+------+---+-+-----+-\\|  |  |||| |  ||  |
/+--+-+-++----+-++--+--+----+----+----++-----++\\| | ||     ||   || || |   |                ||||   |||/--++-+-+--\\   |   | |     | ||  |  |||| |  ||  |
||  | | ||    | ||  |  |    | /--+----++-----++++-+-++-----++---++-++-+---+----------------++++\\  ||||  || | |  |   |   | |     | ||  |  |||| |  ||  |
||  | | \\+----+-++--+--+----+-+--+----++-----++++-+-++-----++---++-+/ |   |                |||\\+--++++--++-+-+--+---+---+-+-----+-++--+--+/|| |  ||  |
||  | |  \\----+-++--+--+----+-+--+----++-----++++-+-++-----++---/| |  |   |                ||| |  ||||  || | |  |   |  /+-+-----+-++--+--+-++-+-\\||  |
||  | |       | ||  |  |   /+-+--+---\\||     |||| \\-++-----++----+-+--+---+----------------+++-+--++++--++-+-+--+---+--++-+-----+-++--+--+-++-+-++/  |
||  | |       | ||  |  |   || |  |   |||     ||||   ||    /++----+-+\\ |   |                ||| |  ||||  || | |  |   |  || |     | ||  |  | || | ||   |
||  | |       | ||  |  |/--++-+--+---+++-----++++---++----+++----+-++-+---+-------\\        ||| |  ||||  || | |  |   |  || \\-----+-++--+--+-+/ | ||   |
||  | |       | ||  |  ||  || |  |   |||     ||||   ||  /-+++----+-++-+---+-------+--------+++\\|  ||||  || | |  |   |  ||       | ||  |  | |  | ||   |
||  | |       | ||  |  ||  || |  |   |||     ||||   ||  | |||    | || |   |       |        ||||| /++++--++-+-+--+---+--++------\\| ||  |  | |  | ||   |
||  | |       | ||  |  ||  || |  |   |||     ||||   ||/-+-+++----+-++-+---+-------+--------+++++\\|||||  || | |  |   |  ||      || ||  |  | |  | ||   |
||  | |       | ||  | /++--++-+--+---+++-----++++---+++-+-+++----+-++-+-\\ |       |   /----+++++++++++--++-+-+--+---+--++------++-++--+--+-+--+-++\\  |
||  | |       | ||  | |||  || |  |   |||     ||||   ||| | |||    | || | | |       |/--+----+++++++++++--++-+-+--+-\\ |  ||      || ||  |  | |  | |||  |
|\\--+-+-------+-++--+-+++>-++-+--+---+++-----++++---+++-+-+++----+-++-+-+-/ /-----++--+----+++++++++++--++-+-+--+-+-+--++------++-++--+--+-+--+\\|||  |
|   | |       | ||  | |||  || | /+---+++-----++++---+++\\|/+++----+-++-+-+---+-----++--+----+++++++++++--++-+-+--+-+-+--++-\\    || ||  |  | |  |||||  |
|  /+-+-------+-++--+\\|||  |v | ||   |||     ||||   ||||||\\++----+-+/ | |   |     ||  |    |||||||||||  || | |  | | |  || |    || ||  |  | |  |||||  |
|  || |       | ||  |||||  || | ||   |||/----++++---++++++-++----+-+--+-+---+-----++--+----+++++++++++--++-+-+\\ | | |  || |    || ||  |  | |  |||||  |
|  || |       | ||  |||||  || | ||   ||||    ||||   |||||| ||    | |  | |   |  /--++--+----+++++++++++--++-+-++-+-+-+--++-+----++-++--+--+-+\\ |||||  |
| /++-+-------+-++--+++++--++-+-++---++++----++++---++++++-++----+-+--+-+---+--+--++--+----+++++++++++--++-+\\|| | | |  || |    || ||  |  | || |||||  |
|/+++-+-------+-++--+++++--++-+-++---++++----++++---++++++-++\\   | |  | |   |  |  ||  |    |||||||||||  || |||| | | |  || |    || ||/-+--+-++-+++++-\\|
||||| |       | ||  |||||  || | ||   ||||    ||||   |||||| |||   | |  | |   |  |  ||  |    |||||||||||  || |||| | | |  ||/+----++-+++-+--+\\|| ||||| ||
||||| |       | ||  |||||  || | ||   ||||/---++++---++++++-+++\\  | |  | |   |  |  ||  |    |||||||||||  || |||| | | |  ||||    || ||| |  |||| ||||| ||
||||| |       | ||  |||||  || | ||   |||||   ||||   |||||| ||||  | |  | | /-+--+-<++--+----+++++++++++--++-++++-+-+-+--++++----++-+++-+--++++-+++++\\||
||||| |       | ||  |||||  || | |\\---+++++---+/||   |||||| ||||  | |  | |/+-+--+--++--+----+++++++++++--++-++++\\| | |  ||||    || ||| |  |||| ||||||||
||||| |     /-+-++--+++++--++-+-+----+++++---+-++-\\ |||||| ||||/-+-+--+-+++-+--+--++--+----+++++++++++\\ || |||||| | |  ||||    || ||| |  |||| ||||||||
||||| |     | |/++--+++++--++-+-+----+++++---+-++-+-++++++-+++++-+-+--+-+++-+--+--++-\\|    |||||||||||| || |||||| | |  ||||    || ||| |  |||| ||||||||
||||| |     | ||||  |||||  || | |    |||||   | || | |||||\\-+++++-+-+--+-+++-+--+--++-++----++++++++++++-++-++++++-+-+--+++/    || ||| |  |||| ||||||||
||||| |     | ||||  |||||  || | |    ||||| /-+-++-+-+++++--+++++-+-+--+-+++-+--+--++-++----++++++++++++-++-++++++\\| |  |||     || |\\+-+--++++-/|||||||
||||| |     | ||||  |||||  || | |    ||||| | | || | ||||| /+++++-+-+--+-+++-+--+--++-++----++++++++++++\\|| |||||||| |  |||     || | | |  ||||  |||||||
||||| |     | ||||  ||||| /++-+-+----+++++-+-+-++-+-+++++-++++++-+-+--+-+++-+--+--++-++----+++++++++++++++-++++++++-+\\ |||     || | | |  ||||  |||||||
||||| |     | ||||  ||||| ||| | |  /-+++++-+-+-++-+-+++++-++++++-+-+--+-+++-+--+--++\\||    |||||||\\+++++++-++/||||| || |||  /--++-+-+-+--++++\\ |||||||
||||| |     | ||||  \\++++-+++-+-+--+-+/||| | | || | ||||| |||||| | |  | ||\\-+--+--+++++----+++++++-+++++++-++-+++++-++-+++--+--++-+-+-+--+++++-++++/||
||||| |     | ||||   |||| ||| | |  | | ||| | | || | \\++++-++++++-/ |  | ||  |  |  ||||\\----+++++++-+++++++-++-+++++-++-+++--+--++-+-+-+--+++++-+++/ ||
||||| |     | ||||   |||| ||| | |  | | ||| | | || |  |||| ||||||   |  | ||  |  |  ||||     ||||||| ||||||| || ||||| || |||  |  || | | |  ||||| |||  ||
||||| |     | ||||   |||| ||| | |  | | ||| | | || |  |||| ||||||   |  | ||  |  |  ||||     ||||||\\-+++++++-++-+++++-++-+++--+--/| | | v  ||||| |||  ||
||||| |     | ||||   |||| ||| |/+--+-+-+++-+-+-++-+--++++-++++++---+-\\| ||  |  |  ||||     ||||||  ||||||| || ||||| || |||  |   | | | |  ||||| |||  ||
||||| |     | ||||   |||| ||| |||  | | ||| | | || |  \\+++-++++++---+-++-++--+--+--++++-----++++++--+++++++-++-+++++-++-+++--+---/ | | |  ||||| |||  ||
||||| |     | ||||   |||| ||| |||  | | ||| | | || |   ||| ||||||   | || ||  |  |  ||||     ||||||  ||||||| || ||||| || |||  |     | | |  ||||| |||  ||
\\++++-+-----+-++++---++++-+++-+++--+-+-+++-+-+-/|/+---+++-++++++---+-++-++--+--+\\ ||||     ||||||  ||||||| \\+-+++++-++-+++--+-----+-+-+--/|||| |||  ||
 |||| |     | |||| /-++++-+++-+++--+-+-+++-+-+--+++---+++-++++++---+-++-++\\ |  || ||||     ||||||  |||||||  | ||||| || |||  |     | | |   |||| |||  ||
 |||| |   /-+-++++-+-++++-+++-+++--+-+-+++-+-+--+++---+++-++++++---+-++-+++-+--++-++++-----++++++--+++++++--+-+++++\\|| |||  |     | | |   |||| |||  ||
 |||| |   | | |||| | |||| ||| |||  | | ||| | |  |||   ||| ||||||   | ||/+++-+--++-++++-----++++++--+++++++--+-++++++++-+++--+-----+-+-+---++++-+++\\ ||
 |||| |   | | |||| | |||| ||| |||  | | ||| | |  |||   ||| ||||||   \\-++++++-+--++-++++-----/|||||  |||||||  | |||||||| |||  |     | | |   |||| |||| ||
 \\+++-+---+-+-++++-+-++++-+++-+++--+-+-+++-+-+--+++---+++-+++/|\\-----++++++-+--++-++++------+++++--+++/|||  | |||||||| |||  |     | | |   |||| |||| ||
  ||| |   | | |||| |/++++-+++-+++-\\| | ||| | |  |||   ||| ||| |      |||||| |  || ||||     /+++++--+++-+++--+-++++++++-+++--+-----+-+-+--\\|||| |||| ||
  ||| |   | | |||| |||||| ||| ||| || | ||| | |  |||   ||| ||| |      |||||| | /++-++++-----++++++--+++-+++--+-++++++++-+++-\\|     | | \\--+++++-++++-+/
  ||| |   | | |||| |||||| ||| ||| || | ||| | |  |||   ||| ||| |      |||||| | ||| ||||     ||||||  ||| |||  | |||||||| ||| ||     | |    ||||| |||| | 
  ||| |   | | |||| |||||| |||/+++-++-+-+++-+-+--+++---+++-+++-+------++++++-+-+++-++++-----++++++--+++-+++--+-++++++++-+++\\||     | |    ||||| |||| | 
 /+++-+---+-+-++++-++++++-+++++++-++-+-+++-+-+--+++---+++-+++-+------++++++-+-+++\\||||     ||||||  ||| |||  | |||||||| ||||||     | \\----+++++-++++-/ 
 |||| |   | | |||| |||||| ||||||| || | ||| | |  |||   ||| ||| |      |||||| | ||||||||     ||||||  ||| |\\+--+-++++++++-++++++-----/      ||||| ||||   
 |||| |   | | |||| |||||| ||||||| || | ||| | |  |||   ||| ||| |      ||\\+++-+-++++++++-----++++++--+++-+-+--+-++++++++-++++++------------+++++-+++/   
 |||\\-+---+-+-++++-++++/| ||||||| || | ||| | |  |||   ||| ||| |      || ||| | ||||||||   /-++++++-\\||| | |  | |||||||| ||||||            ||||| |||    
 |||  |   | | |||| ||||/+-+++++++-++-+-+++-+-+--+++---+++-+++-+------++-+++-+-++++++++---+-++++++-++++-+-+--+-++++++++-++++++-----\\      ||||| |||    
 |||  |   | | |||| |||||| ||||||| || | ||| | |  |||   ||| ||| |      || ||| | ||||||||   | |||||| |||| | |  | |||||||| ||||||     |  /---+++++-+++-\\  
 |||  |   | | |||| |\\++++-+++++++-/| |/+++-+-+--+++---+++-+++-+------++-+++-+-++++++++---+-++++++-++++-+-+--+-++++++++-++++++-\\   |  |   ||||| ||| |  
 |||  |   | | |||| | |||| |||||||  | |||||/+-+--+++---+++-+++-+----\\ || |\\+-+-++++++++---+-++++++-++++-+-+--+-+/|||||| |||||| |   |  |   ||||| ||| |  
 |||  |   | | |||| | |||| ||||\\++--+-+++++++-+--+++---+++-+++-+----+-++-+-+-+-++++++++---+-++++/| |||| | |  | | |||||| |||||| |   |  |   ||||| ||| |  
 |||  |   | | |||| | |||| |||| ||  | ||||||| |  |||   ||| ||| |    | || | | | ||||||||   | |||| | |||| | |  | | |||||| |||||| |   |  |   ||||| ||| |  
 |||  |   | | |||| | |||| |||| ||  | ||||||| |  |||   ||| ||| |    | || | | | ||||||||   | |||| | |||| | |  | | |||||| |||||| |   |  |   ||||| ||| |  
 |||  |   | | |||| | ||||/++++-++--+-+++++++-+--+++---+++-+++-+----+-++-+-+-+-++++++++---+>++++-+-++++-+-+--+-+\\|||||| |||||| |   |  |   ||||| ||| |  
 |||  |   | | |||| | ||||||||| ||  | ||||||\\-+--+++---+++-+++-+----+-++-+-+-+-++++++++---+-++++-+-++++-+-+--+-+++/|||| |||||| |   |  |   ||||| ||| |  
 |||  |/--+-+-++++-+-+++++++++-++--+-++++++--+--+++---+++-+++-+----+-++-+-+-+-++++++++---+-++++-+-++++-+-+\\ | ||| |||| |||||| |   |  |   ||||| ||| |  
 |||  ||  | | |||| | ||||||||| ||  | ||\\+++--+--/||   ||| ||| |    | || | | | ||||||||   | |||| | |||| | || | ||| |||| |||||| |   |  |   ||||| ||| |  
 |||  ||  | | |||| | ||||||||| ||  | || |||  |   ||   ||| ||| |    | || | | | ||||||||   | |||| | |||| | || | ||| |||| |||||| |   |  |   ||||| ||| |  
 \\++--++--+-+-++++-+-+++++++++-++--+-++-+++--+---++---+++-+++-+----+-++-+-+-+-+++/||||   | |||| | |||| | || | ||| |||| |||||| |   |  |   ||||| ||| |  
  ||  ||  | | |||| | ||||||||| ||  | || |||  | /-++---+++-+++-+----+-++-+-+-+-+++-++++---+-++++-+\\|||| | || | ||| |||| |||||| |   |  |   ||||| ||| |  
  ||  ||  |/+-++++-+-+++++++++-++--+-++\\|||  | | ||   ||| ||| |    | || | | | ||| ||||   | |||| |||||| |/++-+-+++-++++-++++++\\|   |  |   ||||| ||| |  
  ||  ||  |||/++++-+-+++++++++\\||  | ||||||  | | ||   ||| ||| |    | || | | | |\\+-++++---+-++++-++++++-++++-+-+++-++++-++++++++---+--+---+++/| ||| ^  
  |\\--++--++++++++-+-/|||||||||||  | ||||||  | | ||   ||| ||| |    | || | | | \\-+-++++---+-++++-++++++-++++-+-+++-++++-++++/|||   |  |   ||| | ||| |  
  |   ||  |||||||| |  |||||||||||  | ||||||  | | ||   ||| |\\+-+----+-++-+-+-+---+-++++---+-+/|| |||||| |||| | ||| |||| |||| |||   |  \\---+++-+-+++-/  
  |   ||  |||||||| |  |||||||||||/-+-++++++--+-+-++---+++-+-+-+----+-++-+-+-+---+-++++---+-+-++-++++++-++++-+-+++-++++-++++-+++--\\|      ||| | |||    
  |   \\+--++++++++-+--++++++++++++-+-++++++--+-+-++---+++-+-+-+----+-++-+-+-+---+-++++---+-+-/| |||||| |||| | ||| |||| |||| |||  ||      ||| | |||    
  |    |  |||||\\++-+--++++++++++++-+-++++++--+-+-++---+++-+-+-+----+-++-+-+-+---+-+++/   | |  | |||||| |||| | ||| |||| |||| |||  ||      ||| | |||    
  |    \\--+++++-++-+--++++++++++++-+-++++++--+-+-++---+++-+-+-+----+-++-+-+-+---+-+++----+-+--+-++++++-+++/ | ||| |||| |||| |||  ||      ||| | |||    
/-+-------+++++\\|| |  |||||||||||| | ||||||  \\-+-++---+++-+-+-+----+-++-+-+-+---+-+++----+-+--+-++++++-+++--+-+++-++++-++++-+++--++------++/ | |||    
| |       ||||\\+++-+--++++++++++++-+-++++++----+-++---+++-+-+-+----+-++-+-+-+---+-+++----+-+--+-++++++-+++--+-+++-++/| |||| |||  ||      ||  | |||    
| |       |||| ||| |  |||||||||||| | ||||||    | ||   ||| | \\-+----+-++-+-+-+---+-+++----+-+--+-++++++-+++--+-+++-++-+-++++-+++--++------++--+-++/    
| |       |||| ||| |  |||||||||||| | ||||||    | ||   ||| |   |    | || | | \\---+-+++----+-+--+-++++++-+++--+-+++-++-+-++++-+++--++------++--+-/|     
| |       |||| ||| |  ||||||||||\\+-+-++++++----+-++---+/|/+---+----+\\|| | |     | |||    | |  | |||||| ||\\--+-+++-++-+-+/|| |||  ||      ||  |  |     
| |       |||| ||| |  |||||||^|\\-+-+-++++++----+-++---+-+++---+----++/| | |     | |||    | |  | |||||| ||  /+-+++-++-+-+-++-+++--++----\\ ||  |  |     
| |       |||| ||| |  ||||||\\++--+-+-++++++----+-++---+-+++---+----++-/ | |     | |||    | |  | |||||| ||  || ||| || | | || |||  ||    | ||  |  |     
| |       |||| ||| |  |||||| ||  | | ||||||    | ||   | |||   |    ||   | |     | |||    | |  | |||||\\-++--++-++/ || | \\-++-+++--++----+-++--+--/     
| |       |||| ||| |  ||\\+++-++--+-+-++++++----+-++---+-+++---+----++---+-+-----+-/|| /--+-+--+-+++++--++--++-++--++-+---++-+++--++---\\| ||  |        
| |       ||\\+-+++-+--++-+++-++--+-+-++++++----+-+/   | |||   |    ||   | |     |  || |  | |  | |||||  ||  || ||  || |   || |||  ||   || ||  |        
| |       || | ||| |  || ||| ||  \\-+-++++++----+-+----+-+++---+----++---+-+-----+--++-+--+-+--+-+++++--++--++-++--++-+---++-+++--/|   || ||  |        
| |       || | ||| |  || ||| ||    | ||||||    | |    |/+++---+----++---+-+-----+--++-+--+-+--+-+++++--++--++-++--++-+---++-+++---+---++-++--+-----\\  
| |       || | ||| |  || ||| ||    | |||\\++----+-+----+++++---+----++---+-+-----+--++-+--+-+--+-+++++--++--++-/|  || |   || |||   |   || ||  |     |  
| |       || | |||/+--++-+++-++----+-+++-++----+-+----+++++---+----++---+-+-----+--++-+--+-+--+-+++++--++--++\\ |  || |   || |||   |   || ||  |     |  
| |       || | |||||  || \\++-++----+-+++-++----+-+----+++++---+----++---+-+-----+--++-+--+-+--+-+++++--++--+++-/  || |   || |||   |   || ||  |     |  
| |       || | ||||\\--++--++-++----+-+++-++----+-+----+++++---+----++---+-/     |  || |  | |  | |||||  ||  |||    || |   || |||   |   || ||  |     |  
| |       |\\-+-++++---++--++-++----+-++/ ||    | \\----+++++---+----++---+-------/  || |  | |  | |||||  ||  |||    || |   || \\++---+---++-++--/     |  
|/+-------+--+-++++---++--++-++----+-++--++\\   |      |||||   |    ||   |          || |  | \\--+-+++++--++--+++----++-+---++--++---+---++-/|        |  
|||       |  | ||||   ||  || ||    | ||  |||   |      ||\\++---+----++---+--->------++-+--+----/ |||||  ||  |||    || |   \\+--++---+---++--/        |  
|||       |  | |\\++---++--++-++----+-++--+++---+------++-++---+----++---+----------++-+--+------++++/  ||  |||    || |    |  ||   |   ||           |  
|||       |  | | ||   ||  || ||/---+-++--+++---+---\\  || \\+---+----+/   |  /-------++\\|  |      ||||   ||  \\++----++-+----+--++---+---+/           |  
|||       |  | | \\+---++--++-+++---+-++--+++---+---+--++--+---+----+----+--+-------++++--+------+++/   ||   ||    || |    |  ||   |   |            |  
|||/------+--+-+--+---++--++-+++---+-++--+++---+---+--++--+---+--\\ |    |  |       |||\\--+------+++----++---++----++-+----+--++---+---/            |  
||||      |/-+-+--+---++--++-+++---+-++--+++---+---+--++--+---+--+-+----+--+\\      \\++---+------+++----++---++----/| |    |  ||   |                |  
||||      || | |  |   ||  || |||   | ||  |||   |   |  ||  |   |  | |    |  ||/------++---+------+++----++---++-----+-+----+--++---+-----\\          |  
||||      || | |  |  /++--++-+++---+-++--+++---+---+--++--+---+--+-+----+--+++------++---+------+++<---++---++-----+-+----+--++-\\ |     |          |  
||||      ||/+-+--+--+++--++-+++\\  | ||  |||   |   |  ||  |   |  | |    |  |||      ||   |      |||/---++---++-----+-+---\\|  || | |     |          |  
||||      |||| |  |  |||  \\+-++++--+-++--+++---+---+--++--+---+--+-+----+--+++------++---+------++++---++---++-----+-/   ||  || | |     |          |  
||||      |||| |  |  |||   | ||||  | ||  |||   |   |  ||  |   |  | |    |  |||      ||   |      ||||   ||   ||     |     ||  || | |     |          |  
||||      |||| |  |  |||   | ||||  | ||  |||   |   |  ||  |   |  | |    |  \\++------+/   |      ||||   ||   ||     |     ||  || | |     |          |  
\\+++------++++-/  |  |||   | ||||  | ||  |\\+---+---+--++--+---+--+-/    |   ||      |    |      ||||   ||   ||     |     ||  || | |     |          |  
 |||      ||||    |  |\\+---+-++++--+-++--+-+---+---+--++--+---+--+------/   ||      |   /+------++++---++---++-----+-----++--++-+-+-----+------\\   |  
 |||      ||||    |  | |   | ||||  | |\\--+-+---+---+--++--+---+--+----------++------+---++------++++---++---++-----+-----++--+/ | |     |      |   |  
 |\\+------++++----+--+-+---+-++++--+-+---+-+---+---+--++--+---+--+----------++------+---++------++++---++---/|     |     ||  |  | |     |      |   |  
 | |      ||||    |  | |   \\-++++--+-/   | |   |   |  ||  \\---+--+----------++------+---++------++++---/|    |     |     ||  |  | |     |      |   |  
 | |      ||||    |  | |     ||||  |     | |   |   |  ||      |  |          ||      |   ||      ||||    |    |     |     ||  |  | |     |      |   |  
 | |      ||||    |  \\-+-----++++--+-----+-+---+---+--++------+--+----------++------+---++------++++----+----+-----+-----++--+--/ |     |      |   |  
 | |      ||||    |    |     ||||  |     | |   \\---+--++------+--+----------++->----+---++------+/||    |    |     |     ||  |    |     |      |   |  
 | |      ||||    |    \\-----++++--+-----+-+-------+--++------+--+----------++------+---++------+-++----+----+-----+-----++--+----/     |      |   |  
 | |      ||||    \\----------++++--+-----+-+-------+--++------+--+----------++------+---++------+-++----+----/     |     ||  |          |      |   |  
 | |      ||||               ||||  |     \\-+-------+--++------/  |          |\\------+---++------+-++----+----------+-----++--+----------/      |   |  
 | |      ||||               ||\\+--+-------+-------/  \\+---------+----------+-------+---++->----/ ||    |          |     ||  |                 |   |  
 | |      |||\\---------------+/ |  |       |           |         |          |       |   ||        ||    |          |     ||  |                 |   |  
 | |      ||\\----------------+--/  \\-------+-----------+---------+----------+-------/   ||        ||    |          |     ||  |                 |   |  
 | \\------++-----------------+-------------+-----------+---------/          |           ||        ||    |          |     ||  |                 |   |  
 |        ||                 |             |           |                    |           |\\--------/\\----+----------+-----/|  |                 |   |  
 |        \\+-----------------+-------------+-----------+--------------------+-----------+---------------+----------/      |  |                 |   |  
 \\-<-------+-----------------+-------------/           |                    |           \\---------------+-----------------+--+-----------------/   |  
           \\-----------------+-------------------------+--------------------/                           |                 |  |                     |  
                             \\-------------------------+------------------------------------------------+-----------------/  |                     |  
                                                       |                                                \\--------------------/                     |  
                                                       \\-------------------------------------------------------------------------------------------/  
"

# COMMAND ----------

m <-
  input %>%
  read_lines() %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

# COMMAND ----------

carts <-
  map_dfr(
    str_split("^v<>", "")[[1]],
    function(dir) {
      which(m == dir, arr.ind = TRUE) %>%
        as_tibble() %>%
        mutate(direction = dir, intersections = 0)
    }
  ) %>%
  arrange(row, col)
carts

# COMMAND ----------

step <- function(carts) {
  for (i in seq_len(nrow(carts))) {
    dir <- carts$direction[i]
    row <- carts$row[i]
    col <- carts$col[i]
    intersections <- carts$intersections[i]
    track <- m[row, col]
    dir <- case_when(
      dir == "^" && track == "\\" ~ "<",
      dir == "^" && track ==  "/" ~ ">",
      dir == "v" && track == "\\" ~ ">",
      dir == "v" && track ==  "/" ~ "<",
      dir == "<" && track == "\\" ~ "^",
      dir == "<" && track ==  "/" ~ "v",
      dir == ">" && track == "\\" ~ "v",
      dir == ">" && track ==  "/" ~ "^",
      TRUE ~ dir
    )
    if (track == "+") {
      dir <- case_when(
        # Left
        dir == "^" && intersections == 0 ~ "<",
        dir == "v" && intersections == 0 ~ ">",
        dir == "<" && intersections == 0 ~ "v",
        dir == ">" && intersections == 0 ~ "^",
        # Straight (no change)
        # Right
        dir == "^" && intersections == 2 ~ ">",
        dir == "v" && intersections == 2 ~ "<",
        dir == "<" && intersections == 2 ~ "^",
        dir == ">" && intersections == 2 ~ "v",
        TRUE ~ dir
      )
      intersections <- (intersections + 1) %% 3
    }

    if (dir == "^") {
      row <- row - 1
    } else if (dir == "v") {
      row <- row + 1
    } else if (dir == "<") {
      col <- col - 1
    } else if (dir == ">") {
      col <- col + 1
    }
    
    if (any(carts$row == row & carts$col == col)) {
      # Just return the answer rather than carts
      return(str_c(col - 1, row - 1, sep = ","))
    }
    
    carts$direction[i] <- dir
    carts$row[i] <- row
    carts$col[i] <- col
    carts$intersections[i] <- intersections
  }
  
  carts %>% arrange(row, col)
}

print_cart <- function(carts) {
  m2 <- mt
  m2[str_detect(m2, "[v^<>]")] <- "?"
  for (i in seq_len(nrow(carts))) {
    m2[carts$row[i], carts$col[i]] <- carts$direction[i]
  }
  cat(str_c(apply(m2, 1, str_c, collapse = ""), collapse = "\n"))
  cat("\n\n")
}

first_crash <- function(carts) {
  repeat {
    carts <- step(carts)
    if (is.character(carts)) {
      return(carts)
    }
  }
}

# COMMAND ----------

answer <- first_crash(carts)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>There isn't much you can do to prevent crashes in this ridiculous system. However, by predicting the crashes, the Elves know where to be in advance and <em>instantly remove the two crashing carts</em> the moment any crash occurs.</p>
# MAGIC <p>They can proceed like this for a while, but eventually, they're going to run out of carts. It could be useful to figure out where the last cart that <em>hasn't</em> crashed will end up.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>/&gt;-&lt;\  
# MAGIC |   |  
# MAGIC | /&lt;+-\
# MAGIC | | | v
# MAGIC \&gt;+&lt;/ |
# MAGIC   |   ^
# MAGIC   \&lt;-&gt;/
# MAGIC 
# MAGIC /---\  
# MAGIC |   |  
# MAGIC | v-+-\
# MAGIC | | | |
# MAGIC \-+-/ |
# MAGIC   |   |
# MAGIC   ^---^
# MAGIC 
# MAGIC /---\  
# MAGIC |   |  
# MAGIC | /-+-\
# MAGIC | v | |
# MAGIC \-+-/ |
# MAGIC   ^   ^
# MAGIC   \---/
# MAGIC 
# MAGIC /---\  
# MAGIC |   |  
# MAGIC | /-+-\
# MAGIC | | | |
# MAGIC \-+-/ <em>^</em>
# MAGIC   |   |
# MAGIC   \---/
# MAGIC </code></pre>
# MAGIC <p>After four very expensive crashes, a tick ends with only one cart remaining; its final location is <code><em>6,4</em></code>.</p>
# MAGIC <p><em>What is the location of the last cart</em> at the end of the first tick where it is the only cart left?</p>
# MAGIC </article>

# COMMAND ----------

step <- function(carts) {
  carts$delete <- FALSE
  for (i in seq_len(nrow(carts))) {
    if (carts$delete[i]) next
    dir <- carts$direction[i]
    row <- carts$row[i]
    col <- carts$col[i]
    intersections <- carts$intersections[i]
    track <- m[row, col]
    dir <- case_when(
      dir == "^" && track == "\\" ~ "<",
      dir == "^" && track ==  "/" ~ ">",
      dir == "v" && track == "\\" ~ ">",
      dir == "v" && track ==  "/" ~ "<",
      dir == "<" && track == "\\" ~ "^",
      dir == "<" && track ==  "/" ~ "v",
      dir == ">" && track == "\\" ~ "v",
      dir == ">" && track ==  "/" ~ "^",
      TRUE ~ dir
    )
    if (track == "+") {
      dir <- case_when(
        # Left
        dir == "^" && intersections == 0 ~ "<",
        dir == "v" && intersections == 0 ~ ">",
        dir == "<" && intersections == 0 ~ "v",
        dir == ">" && intersections == 0 ~ "^",
        # Straight (no change)
        # Right
        dir == "^" && intersections == 2 ~ ">",
        dir == "v" && intersections == 2 ~ "<",
        dir == "<" && intersections == 2 ~ "^",
        dir == ">" && intersections == 2 ~ "v",
        TRUE ~ dir
      )
      intersections <- (intersections + 1) %% 3
    }

    if (dir == "^") {
      row <- row - 1
    } else if (dir == "v") {
      row <- row + 1
    } else if (dir == "<") {
      col <- col - 1
    } else if (dir == ">") {
      col <- col + 1
    }
    
    if (any(carts$row == row & carts$col == col & !carts$delete)) {
      carts$delete[i] <- TRUE
      carts$delete[carts$row == row & carts$col == col] <- TRUE
      next
    }
    
    carts$direction[i] <- dir
    carts$row[i] <- row
    carts$col[i] <- col
    carts$intersections[i] <- intersections
  }
  
  carts %>%
    filter(!delete) %>%
    select(-delete) %>%
    arrange(row, col)
}

last_cart <- function(carts) {
  repeat {
    carts <- step(carts)
    if (nrow(carts) <= 1) {
      return(carts)
    }
  }
}

# COMMAND ----------

result <- last_cart(carts)
answer <- str_c(result$col - 1, result$row - 1, sep = ",")
answer
