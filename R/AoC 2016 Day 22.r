# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/22

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 22: Grid Computing ---</h2><p>You gain access to a massive storage cluster arranged in a grid; each storage node is only connected to the four nodes directly adjacent to it (three if the node is on an edge, two if it's in a corner).</p>
# MAGIC <p>You can directly access data <em>only</em> on node <code>/dev/grid/node-x0-y0</code>, but you can perform some limited actions on the other nodes:</p>
# MAGIC <ul>
# MAGIC <li>You can get the disk usage of all nodes (via <a href="https://en.wikipedia.org/wiki/Df_(Unix)#Example"><code>df</code></a>). The result of doing this is in your puzzle input.</li>
# MAGIC <li>You can instruct a node to <span title="You suspect someone misunderstood the x86 MOV instruction."><em>move</em></span> (not copy) <em>all</em> of its data to an adjacent node (if the destination node has enough space to receive the data). The sending node is left empty after this operation.</li>
# MAGIC </ul>
# MAGIC <p>Nodes are named by their position: the node named <code>node-x10-y10</code> is adjacent to nodes <code>node-x9-y10</code>, <code>node-x11-y10</code>, <code>node-x10-y9</code>, and <code>node-x10-y11</code>.</p>
# MAGIC <p>Before you begin, you need to understand the arrangement of data on these nodes. Even though you can only move data between directly connected nodes, you're going to need to rearrange a lot of the data to get access to the data you need.  Therefore, you need to work out how you might be able to shift data around.</p>
# MAGIC <p>To do this, you'd like to count the number of <em>viable pairs</em> of nodes.  A viable pair is any two nodes (A,B), <em>regardless of whether they are directly connected</em>, such that:</p>
# MAGIC <ul>
# MAGIC <li>Node A is <em>not</em> empty (its <code>Used</code> is not zero).</li>
# MAGIC <li>Nodes A and B are <em>not the same</em> node.</li>
# MAGIC <li>The data on node A (its <code>Used</code>) <em>would fit</em> on node B (its <code>Avail</code>).</li>
# MAGIC </ul>
# MAGIC <p><em>How many viable pairs</em> of nodes are there?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     85T   68T    17T   80%
/dev/grid/node-x0-y1     89T   66T    23T   74%
/dev/grid/node-x0-y2     89T   69T    20T   77%
/dev/grid/node-x0-y3     92T   71T    21T   77%
/dev/grid/node-x0-y4     89T   69T    20T   77%
/dev/grid/node-x0-y5     88T   71T    17T   80%
/dev/grid/node-x0-y6     87T   72T    15T   82%
/dev/grid/node-x0-y7     89T   72T    17T   80%
/dev/grid/node-x0-y8     87T   67T    20T   77%
/dev/grid/node-x0-y9     88T   69T    19T   78%
/dev/grid/node-x0-y10    89T   66T    23T   74%
/dev/grid/node-x0-y11    85T   66T    19T   77%
/dev/grid/node-x0-y12    90T   67T    23T   74%
/dev/grid/node-x0-y13    89T   70T    19T   78%
/dev/grid/node-x0-y14    94T   71T    23T   75%
/dev/grid/node-x0-y15    94T   66T    28T   70%
/dev/grid/node-x0-y16    85T   71T    14T   83%
/dev/grid/node-x0-y17    85T   69T    16T   81%
/dev/grid/node-x0-y18    94T   70T    24T   74%
/dev/grid/node-x0-y19    86T   70T    16T   81%
/dev/grid/node-x0-y20    92T   65T    27T   70%
/dev/grid/node-x0-y21    92T   70T    22T   76%
/dev/grid/node-x0-y22    89T   72T    17T   80%
/dev/grid/node-x0-y23    94T   68T    26T   72%
/dev/grid/node-x0-y24    89T   66T    23T   74%
/dev/grid/node-x0-y25    92T   70T    22T   76%
/dev/grid/node-x0-y26    94T   68T    26T   72%
/dev/grid/node-x0-y27    86T   66T    20T   76%
/dev/grid/node-x0-y28    94T   69T    25T   73%
/dev/grid/node-x0-y29    88T   69T    19T   78%
/dev/grid/node-x1-y0     85T   70T    15T   82%
/dev/grid/node-x1-y1     91T   64T    27T   70%
/dev/grid/node-x1-y2     88T   66T    22T   75%
/dev/grid/node-x1-y3     85T   73T    12T   85%
/dev/grid/node-x1-y4     93T   72T    21T   77%
/dev/grid/node-x1-y5     85T   69T    16T   81%
/dev/grid/node-x1-y6     91T   65T    26T   71%
/dev/grid/node-x1-y7     93T   72T    21T   77%
/dev/grid/node-x1-y8     87T   72T    15T   82%
/dev/grid/node-x1-y9     92T   73T    19T   79%
/dev/grid/node-x1-y10    91T   67T    24T   73%
/dev/grid/node-x1-y11    87T   65T    22T   74%
/dev/grid/node-x1-y12    94T   70T    24T   74%
/dev/grid/node-x1-y13    86T   70T    16T   81%
/dev/grid/node-x1-y14    87T   64T    23T   73%
/dev/grid/node-x1-y15    86T   65T    21T   75%
/dev/grid/node-x1-y16    94T   68T    26T   72%
/dev/grid/node-x1-y17    89T   70T    19T   78%
/dev/grid/node-x1-y18    91T   64T    27T   70%
/dev/grid/node-x1-y19    89T   67T    22T   75%
/dev/grid/node-x1-y20    94T   69T    25T   73%
/dev/grid/node-x1-y21    90T   67T    23T   74%
/dev/grid/node-x1-y22    87T   72T    15T   82%
/dev/grid/node-x1-y23    93T   64T    29T   68%
/dev/grid/node-x1-y24    90T   71T    19T   78%
/dev/grid/node-x1-y25    93T   65T    28T   69%
/dev/grid/node-x1-y26    93T   72T    21T   77%
/dev/grid/node-x1-y27    86T   64T    22T   74%
/dev/grid/node-x1-y28    90T   66T    24T   73%
/dev/grid/node-x1-y29    89T   73T    16T   82%
/dev/grid/node-x2-y0     85T   71T    14T   83%
/dev/grid/node-x2-y1     90T   67T    23T   74%
/dev/grid/node-x2-y2     93T   73T    20T   78%
/dev/grid/node-x2-y3     88T   69T    19T   78%
/dev/grid/node-x2-y4     85T   64T    21T   75%
/dev/grid/node-x2-y5     88T   73T    15T   82%
/dev/grid/node-x2-y6     90T   70T    20T   77%
/dev/grid/node-x2-y7     92T   73T    19T   79%
/dev/grid/node-x2-y8     90T   71T    19T   78%
/dev/grid/node-x2-y9     86T   69T    17T   80%
/dev/grid/node-x2-y10    87T   64T    23T   73%
/dev/grid/node-x2-y11    85T   65T    20T   76%
/dev/grid/node-x2-y12    90T   70T    20T   77%
/dev/grid/node-x2-y13    90T   73T    17T   81%
/dev/grid/node-x2-y14    87T   72T    15T   82%
/dev/grid/node-x2-y15    94T   71T    23T   75%
/dev/grid/node-x2-y16    89T   64T    25T   71%
/dev/grid/node-x2-y17    93T   72T    21T   77%
/dev/grid/node-x2-y18    91T   72T    19T   79%
/dev/grid/node-x2-y19    91T   71T    20T   78%
/dev/grid/node-x2-y20    94T   65T    29T   69%
/dev/grid/node-x2-y21    86T   64T    22T   74%
/dev/grid/node-x2-y22    86T   67T    19T   77%
/dev/grid/node-x2-y23    87T   64T    23T   73%
/dev/grid/node-x2-y24    94T   70T    24T   74%
/dev/grid/node-x2-y25    85T   69T    16T   81%
/dev/grid/node-x2-y26    93T   67T    26T   72%
/dev/grid/node-x2-y27    87T   70T    17T   80%
/dev/grid/node-x2-y28    86T   71T    15T   82%
/dev/grid/node-x2-y29    85T   64T    21T   75%
/dev/grid/node-x3-y0     91T   73T    18T   80%
/dev/grid/node-x3-y1     87T   71T    16T   81%
/dev/grid/node-x3-y2     91T   70T    21T   76%
/dev/grid/node-x3-y3     86T   66T    20T   76%
/dev/grid/node-x3-y4     88T   69T    19T   78%
/dev/grid/node-x3-y5     88T   72T    16T   81%
/dev/grid/node-x3-y6     93T   66T    27T   70%
/dev/grid/node-x3-y7     91T   67T    24T   73%
/dev/grid/node-x3-y8     90T   64T    26T   71%
/dev/grid/node-x3-y9     93T   67T    26T   72%
/dev/grid/node-x3-y10    86T   73T    13T   84%
/dev/grid/node-x3-y11    85T   67T    18T   78%
/dev/grid/node-x3-y12    88T   68T    20T   77%
/dev/grid/node-x3-y13    91T   70T    21T   76%
/dev/grid/node-x3-y14    88T   66T    22T   75%
/dev/grid/node-x3-y15    90T   71T    19T   78%
/dev/grid/node-x3-y16    89T   64T    25T   71%
/dev/grid/node-x3-y17    92T   70T    22T   76%
/dev/grid/node-x3-y18    89T   71T    18T   79%
/dev/grid/node-x3-y19    89T   69T    20T   77%
/dev/grid/node-x3-y20    91T   70T    21T   76%
/dev/grid/node-x3-y21    90T   71T    19T   78%
/dev/grid/node-x3-y22    92T   66T    26T   71%
/dev/grid/node-x3-y23    90T   68T    22T   75%
/dev/grid/node-x3-y24    85T   67T    18T   78%
/dev/grid/node-x3-y25    92T   67T    25T   72%
/dev/grid/node-x3-y26    87T   65T    22T   74%
/dev/grid/node-x3-y27    87T   65T    22T   74%
/dev/grid/node-x3-y28    87T   68T    19T   78%
/dev/grid/node-x3-y29    88T   66T    22T   75%
/dev/grid/node-x4-y0     93T   67T    26T   72%
/dev/grid/node-x4-y1     92T   66T    26T   71%
/dev/grid/node-x4-y2     87T   65T    22T   74%
/dev/grid/node-x4-y3     92T   66T    26T   71%
/dev/grid/node-x4-y4     85T   71T    14T   83%
/dev/grid/node-x4-y5     90T   67T    23T   74%
/dev/grid/node-x4-y6     91T   64T    27T   70%
/dev/grid/node-x4-y7     90T   71T    19T   78%
/dev/grid/node-x4-y8     94T   69T    25T   73%
/dev/grid/node-x4-y9     85T   67T    18T   78%
/dev/grid/node-x4-y10    89T   73T    16T   82%
/dev/grid/node-x4-y11    91T   72T    19T   79%
/dev/grid/node-x4-y12    89T   64T    25T   71%
/dev/grid/node-x4-y13    87T   71T    16T   81%
/dev/grid/node-x4-y14    85T   72T    13T   84%
/dev/grid/node-x4-y15    86T   65T    21T   75%
/dev/grid/node-x4-y16    85T   65T    20T   76%
/dev/grid/node-x4-y17    90T   71T    19T   78%
/dev/grid/node-x4-y18    91T   67T    24T   73%
/dev/grid/node-x4-y19    90T   65T    25T   72%
/dev/grid/node-x4-y20    91T   69T    22T   75%
/dev/grid/node-x4-y21    91T   69T    22T   75%
/dev/grid/node-x4-y22    88T   66T    22T   75%
/dev/grid/node-x4-y23    87T   64T    23T   73%
/dev/grid/node-x4-y24    87T   69T    18T   79%
/dev/grid/node-x4-y25    90T   66T    24T   73%
/dev/grid/node-x4-y26    90T   65T    25T   72%
/dev/grid/node-x4-y27    91T   65T    26T   71%
/dev/grid/node-x4-y28    94T   64T    30T   68%
/dev/grid/node-x4-y29    89T   68T    21T   76%
/dev/grid/node-x5-y0     86T   72T    14T   83%
/dev/grid/node-x5-y1     89T   69T    20T   77%
/dev/grid/node-x5-y2     86T   66T    20T   76%
/dev/grid/node-x5-y3     90T   73T    17T   81%
/dev/grid/node-x5-y4     85T   69T    16T   81%
/dev/grid/node-x5-y5     90T   65T    25T   72%
/dev/grid/node-x5-y6     94T   72T    22T   76%
/dev/grid/node-x5-y7     92T   71T    21T   77%
/dev/grid/node-x5-y8     89T   73T    16T   82%
/dev/grid/node-x5-y9     90T   65T    25T   72%
/dev/grid/node-x5-y10    89T   67T    22T   75%
/dev/grid/node-x5-y11    89T   68T    21T   76%
/dev/grid/node-x5-y12    86T   68T    18T   79%
/dev/grid/node-x5-y13    87T   68T    19T   78%
/dev/grid/node-x5-y14    94T   66T    28T   70%
/dev/grid/node-x5-y15    86T   66T    20T   76%
/dev/grid/node-x5-y16    90T   71T    19T   78%
/dev/grid/node-x5-y17    91T   68T    23T   74%
/dev/grid/node-x5-y18    94T   66T    28T   70%
/dev/grid/node-x5-y19    85T   72T    13T   84%
/dev/grid/node-x5-y20    86T   72T    14T   83%
/dev/grid/node-x5-y21    85T   67T    18T   78%
/dev/grid/node-x5-y22    90T   67T    23T   74%
/dev/grid/node-x5-y23    94T   67T    27T   71%
/dev/grid/node-x5-y24    86T   72T    14T   83%
/dev/grid/node-x5-y25    91T   66T    25T   72%
/dev/grid/node-x5-y26    92T   70T    22T   76%
/dev/grid/node-x5-y27    85T   68T    17T   80%
/dev/grid/node-x5-y28    87T   73T    14T   83%
/dev/grid/node-x5-y29    94T   66T    28T   70%
/dev/grid/node-x6-y0     90T   70T    20T   77%
/dev/grid/node-x6-y1     88T   69T    19T   78%
/dev/grid/node-x6-y2     91T   66T    25T   72%
/dev/grid/node-x6-y3     86T   68T    18T   79%
/dev/grid/node-x6-y4     92T   67T    25T   72%
/dev/grid/node-x6-y5     88T   67T    21T   76%
/dev/grid/node-x6-y6     89T   69T    20T   77%
/dev/grid/node-x6-y7     85T   72T    13T   84%
/dev/grid/node-x6-y8     88T   72T    16T   81%
/dev/grid/node-x6-y9     94T   68T    26T   72%
/dev/grid/node-x6-y10    92T   68T    24T   73%
/dev/grid/node-x6-y11    94T   70T    24T   74%
/dev/grid/node-x6-y12    93T   65T    28T   69%
/dev/grid/node-x6-y13    89T   64T    25T   71%
/dev/grid/node-x6-y14    90T   64T    26T   71%
/dev/grid/node-x6-y15    90T   69T    21T   76%
/dev/grid/node-x6-y16    94T   67T    27T   71%
/dev/grid/node-x6-y17    94T   66T    28T   70%
/dev/grid/node-x6-y18    89T   68T    21T   76%
/dev/grid/node-x6-y19    92T   70T    22T   76%
/dev/grid/node-x6-y20    93T   73T    20T   78%
/dev/grid/node-x6-y21    85T   70T    15T   82%
/dev/grid/node-x6-y22    88T   65T    23T   73%
/dev/grid/node-x6-y23    94T   72T    22T   76%
/dev/grid/node-x6-y24    90T   66T    24T   73%
/dev/grid/node-x6-y25    93T   69T    24T   74%
/dev/grid/node-x6-y26    94T   68T    26T   72%
/dev/grid/node-x6-y27    87T   68T    19T   78%
/dev/grid/node-x6-y28    90T   71T    19T   78%
/dev/grid/node-x6-y29    89T   69T    20T   77%
/dev/grid/node-x7-y0     90T   71T    19T   78%
/dev/grid/node-x7-y1     90T   65T    25T   72%
/dev/grid/node-x7-y2     87T   64T    23T   73%
/dev/grid/node-x7-y3     88T   67T    21T   76%
/dev/grid/node-x7-y4     93T   69T    24T   74%
/dev/grid/node-x7-y5     91T   71T    20T   78%
/dev/grid/node-x7-y6     93T   68T    25T   73%
/dev/grid/node-x7-y7     88T   65T    23T   73%
/dev/grid/node-x7-y8     94T   71T    23T   75%
/dev/grid/node-x7-y9     94T   68T    26T   72%
/dev/grid/node-x7-y10    88T   64T    24T   72%
/dev/grid/node-x7-y11    92T   65T    27T   70%
/dev/grid/node-x7-y12    87T   64T    23T   73%
/dev/grid/node-x7-y13    86T   71T    15T   82%
/dev/grid/node-x7-y14    89T   71T    18T   79%
/dev/grid/node-x7-y15    89T   70T    19T   78%
/dev/grid/node-x7-y16    88T   68T    20T   77%
/dev/grid/node-x7-y17    88T   64T    24T   72%
/dev/grid/node-x7-y18    91T   69T    22T   75%
/dev/grid/node-x7-y19    88T   66T    22T   75%
/dev/grid/node-x7-y20    90T   65T    25T   72%
/dev/grid/node-x7-y21    94T   73T    21T   77%
/dev/grid/node-x7-y22    93T   69T    24T   74%
/dev/grid/node-x7-y23    89T   67T    22T   75%
/dev/grid/node-x7-y24    94T   69T    25T   73%
/dev/grid/node-x7-y25    89T   66T    23T   74%
/dev/grid/node-x7-y26    94T   64T    30T   68%
/dev/grid/node-x7-y27    89T   73T    16T   82%
/dev/grid/node-x7-y28    86T   69T    17T   80%
/dev/grid/node-x7-y29    91T   66T    25T   72%
/dev/grid/node-x8-y0     90T   70T    20T   77%
/dev/grid/node-x8-y1     85T   70T    15T   82%
/dev/grid/node-x8-y2     93T   66T    27T   70%
/dev/grid/node-x8-y3     88T   68T    20T   77%
/dev/grid/node-x8-y4     86T   70T    16T   81%
/dev/grid/node-x8-y5     85T   70T    15T   82%
/dev/grid/node-x8-y6     85T   66T    19T   77%
/dev/grid/node-x8-y7     87T   66T    21T   75%
/dev/grid/node-x8-y8     88T   66T    22T   75%
/dev/grid/node-x8-y9     85T   67T    18T   78%
/dev/grid/node-x8-y10    91T   71T    20T   78%
/dev/grid/node-x8-y11    88T   71T    17T   80%
/dev/grid/node-x8-y12    93T   67T    26T   72%
/dev/grid/node-x8-y13    91T   65T    26T   71%
/dev/grid/node-x8-y14    87T   70T    17T   80%
/dev/grid/node-x8-y15    94T   66T    28T   70%
/dev/grid/node-x8-y16    91T   70T    21T   76%
/dev/grid/node-x8-y17    87T   72T    15T   82%
/dev/grid/node-x8-y18    86T   72T    14T   83%
/dev/grid/node-x8-y19    88T   66T    22T   75%
/dev/grid/node-x8-y20    93T   69T    24T   74%
/dev/grid/node-x8-y21    89T   67T    22T   75%
/dev/grid/node-x8-y22    85T   67T    18T   78%
/dev/grid/node-x8-y23    85T   71T    14T   83%
/dev/grid/node-x8-y24    90T   69T    21T   76%
/dev/grid/node-x8-y25    92T   71T    21T   77%
/dev/grid/node-x8-y26    91T   71T    20T   78%
/dev/grid/node-x8-y27    87T   65T    22T   74%
/dev/grid/node-x8-y28    89T   64T    25T   71%
/dev/grid/node-x8-y29    85T   65T    20T   76%
/dev/grid/node-x9-y0     85T   69T    16T   81%
/dev/grid/node-x9-y1     93T   69T    24T   74%
/dev/grid/node-x9-y2     94T   69T    25T   73%
/dev/grid/node-x9-y3     94T   73T    21T   77%
/dev/grid/node-x9-y4     88T   66T    22T   75%
/dev/grid/node-x9-y5     88T   68T    20T   77%
/dev/grid/node-x9-y6     89T   70T    19T   78%
/dev/grid/node-x9-y7     93T   73T    20T   78%
/dev/grid/node-x9-y8     93T   68T    25T   73%
/dev/grid/node-x9-y9     94T   71T    23T   75%
/dev/grid/node-x9-y10    86T   67T    19T   77%
/dev/grid/node-x9-y11    85T   64T    21T   75%
/dev/grid/node-x9-y12    88T   66T    22T   75%
/dev/grid/node-x9-y13    88T   67T    21T   76%
/dev/grid/node-x9-y14    89T   64T    25T   71%
/dev/grid/node-x9-y15    86T   66T    20T   76%
/dev/grid/node-x9-y16    88T   64T    24T   72%
/dev/grid/node-x9-y17    92T   66T    26T   71%
/dev/grid/node-x9-y18    87T   72T    15T   82%
/dev/grid/node-x9-y19    90T   67T    23T   74%
/dev/grid/node-x9-y20    90T   65T    25T   72%
/dev/grid/node-x9-y21    85T   70T    15T   82%
/dev/grid/node-x9-y22    92T   69T    23T   75%
/dev/grid/node-x9-y23    89T   69T    20T   77%
/dev/grid/node-x9-y24    93T   72T    21T   77%
/dev/grid/node-x9-y25    89T   73T    16T   82%
/dev/grid/node-x9-y26    90T   69T    21T   76%
/dev/grid/node-x9-y27    88T   66T    22T   75%
/dev/grid/node-x9-y28    92T   69T    23T   75%
/dev/grid/node-x9-y29    86T   67T    19T   77%
/dev/grid/node-x10-y0    89T   66T    23T   74%
/dev/grid/node-x10-y1    88T   67T    21T   76%
/dev/grid/node-x10-y2    87T   66T    21T   75%
/dev/grid/node-x10-y3    92T   65T    27T   70%
/dev/grid/node-x10-y4    88T   68T    20T   77%
/dev/grid/node-x10-y5    90T   70T    20T   77%
/dev/grid/node-x10-y6    89T   73T    16T   82%
/dev/grid/node-x10-y7    91T   72T    19T   79%
/dev/grid/node-x10-y8    93T   70T    23T   75%
/dev/grid/node-x10-y9    88T   72T    16T   81%
/dev/grid/node-x10-y10   94T   73T    21T   77%
/dev/grid/node-x10-y11   90T   67T    23T   74%
/dev/grid/node-x10-y12   91T   66T    25T   72%
/dev/grid/node-x10-y13   89T   73T    16T   82%
/dev/grid/node-x10-y14   94T   66T    28T   70%
/dev/grid/node-x10-y15   93T   71T    22T   76%
/dev/grid/node-x10-y16   91T   71T    20T   78%
/dev/grid/node-x10-y17   91T   73T    18T   80%
/dev/grid/node-x10-y18   88T   67T    21T   76%
/dev/grid/node-x10-y19   93T   72T    21T   77%
/dev/grid/node-x10-y20   90T   64T    26T   71%
/dev/grid/node-x10-y21   86T   70T    16T   81%
/dev/grid/node-x10-y22   86T   66T    20T   76%
/dev/grid/node-x10-y23   91T   71T    20T   78%
/dev/grid/node-x10-y24   93T   71T    22T   76%
/dev/grid/node-x10-y25   86T   73T    13T   84%
/dev/grid/node-x10-y26   86T   70T    16T   81%
/dev/grid/node-x10-y27   86T   65T    21T   75%
/dev/grid/node-x10-y28   93T   71T    22T   76%
/dev/grid/node-x10-y29   90T   65T    25T   72%
/dev/grid/node-x11-y0    90T   67T    23T   74%
/dev/grid/node-x11-y1    85T   66T    19T   77%
/dev/grid/node-x11-y2    89T   73T    16T   82%
/dev/grid/node-x11-y3    91T   69T    22T   75%
/dev/grid/node-x11-y4    87T   68T    19T   78%
/dev/grid/node-x11-y5    88T   73T    15T   82%
/dev/grid/node-x11-y6    87T   66T    21T   75%
/dev/grid/node-x11-y7    90T   69T    21T   76%
/dev/grid/node-x11-y8    85T   69T    16T   81%
/dev/grid/node-x11-y9   505T  493T    12T   97%
/dev/grid/node-x11-y10   85T   65T    20T   76%
/dev/grid/node-x11-y11   94T   66T    28T   70%
/dev/grid/node-x11-y12   89T   66T    23T   74%
/dev/grid/node-x11-y13   85T   66T    19T   77%
/dev/grid/node-x11-y14   88T   66T    22T   75%
/dev/grid/node-x11-y15   90T   73T    17T   81%
/dev/grid/node-x11-y16   85T   73T    12T   85%
/dev/grid/node-x11-y17   94T   71T    23T   75%
/dev/grid/node-x11-y18   88T   68T    20T   77%
/dev/grid/node-x11-y19   94T   67T    27T   71%
/dev/grid/node-x11-y20   89T   64T    25T   71%
/dev/grid/node-x11-y21   85T   64T    21T   75%
/dev/grid/node-x11-y22   87T   72T    15T   82%
/dev/grid/node-x11-y23   92T   64T    28T   69%
/dev/grid/node-x11-y24   93T   67T    26T   72%
/dev/grid/node-x11-y25   89T   66T    23T   74%
/dev/grid/node-x11-y26   89T   68T    21T   76%
/dev/grid/node-x11-y27   88T   70T    18T   79%
/dev/grid/node-x11-y28   91T   73T    18T   80%
/dev/grid/node-x11-y29   94T   64T    30T   68%
/dev/grid/node-x12-y0    91T   70T    21T   76%
/dev/grid/node-x12-y1    93T   68T    25T   73%
/dev/grid/node-x12-y2    85T   71T    14T   83%
/dev/grid/node-x12-y3    91T   72T    19T   79%
/dev/grid/node-x12-y4    91T   73T    18T   80%
/dev/grid/node-x12-y5    86T   73T    13T   84%
/dev/grid/node-x12-y6    85T   72T    13T   84%
/dev/grid/node-x12-y7    93T   68T    25T   73%
/dev/grid/node-x12-y8    86T   65T    21T   75%
/dev/grid/node-x12-y9   510T  494T    16T   96%
/dev/grid/node-x12-y10   92T   65T    27T   70%
/dev/grid/node-x12-y11   91T   67T    24T   73%
/dev/grid/node-x12-y12   85T   73T    12T   85%
/dev/grid/node-x12-y13   92T   68T    24T   73%
/dev/grid/node-x12-y14   88T   64T    24T   72%
/dev/grid/node-x12-y15   94T   68T    26T   72%
/dev/grid/node-x12-y16   93T   64T    29T   68%
/dev/grid/node-x12-y17   90T   68T    22T   75%
/dev/grid/node-x12-y18   93T   64T    29T   68%
/dev/grid/node-x12-y19   85T   68T    17T   80%
/dev/grid/node-x12-y20   92T   73T    19T   79%
/dev/grid/node-x12-y21   85T   70T    15T   82%
/dev/grid/node-x12-y22   86T   71T    15T   82%
/dev/grid/node-x12-y23   89T   73T    16T   82%
/dev/grid/node-x12-y24   93T   72T    21T   77%
/dev/grid/node-x12-y25   94T   64T    30T   68%
/dev/grid/node-x12-y26   87T   68T    19T   78%
/dev/grid/node-x12-y27   94T   64T    30T   68%
/dev/grid/node-x12-y28   86T   66T    20T   76%
/dev/grid/node-x12-y29   91T   67T    24T   73%
/dev/grid/node-x13-y0    86T   73T    13T   84%
/dev/grid/node-x13-y1    86T   70T    16T   81%
/dev/grid/node-x13-y2    86T   73T    13T   84%
/dev/grid/node-x13-y3    90T   72T    18T   80%
/dev/grid/node-x13-y4    85T   64T    21T   75%
/dev/grid/node-x13-y5    85T   69T    16T   81%
/dev/grid/node-x13-y6    91T   69T    22T   75%
/dev/grid/node-x13-y7    93T   65T    28T   69%
/dev/grid/node-x13-y8    86T   70T    16T   81%
/dev/grid/node-x13-y9   504T  499T     5T   99%
/dev/grid/node-x13-y10   90T   64T    26T   71%
/dev/grid/node-x13-y11   90T   71T    19T   78%
/dev/grid/node-x13-y12   85T   66T    19T   77%
/dev/grid/node-x13-y13   88T   73T    15T   82%
/dev/grid/node-x13-y14   93T   73T    20T   78%
/dev/grid/node-x13-y15   89T   72T    17T   80%
/dev/grid/node-x13-y16   88T   68T    20T   77%
/dev/grid/node-x13-y17   87T   66T    21T   75%
/dev/grid/node-x13-y18   91T   72T    19T   79%
/dev/grid/node-x13-y19   85T   66T    19T   77%
/dev/grid/node-x13-y20   88T   65T    23T   73%
/dev/grid/node-x13-y21   94T   66T    28T   70%
/dev/grid/node-x13-y22   88T   71T    17T   80%
/dev/grid/node-x13-y23   89T   67T    22T   75%
/dev/grid/node-x13-y24   88T   64T    24T   72%
/dev/grid/node-x13-y25   89T   71T    18T   79%
/dev/grid/node-x13-y26   92T   69T    23T   75%
/dev/grid/node-x13-y27   87T   73T    14T   83%
/dev/grid/node-x13-y28   91T   71T    20T   78%
/dev/grid/node-x13-y29   87T   72T    15T   82%
/dev/grid/node-x14-y0    88T   73T    15T   82%
/dev/grid/node-x14-y1    90T   68T    22T   75%
/dev/grid/node-x14-y2    89T   69T    20T   77%
/dev/grid/node-x14-y3    93T   64T    29T   68%
/dev/grid/node-x14-y4    85T   71T    14T   83%
/dev/grid/node-x14-y5    90T   68T    22T   75%
/dev/grid/node-x14-y6    91T   68T    23T   74%
/dev/grid/node-x14-y7    94T   64T    30T   68%
/dev/grid/node-x14-y8    94T   64T    30T   68%
/dev/grid/node-x14-y9   506T  497T     9T   98%
/dev/grid/node-x14-y10   89T   67T    22T   75%
/dev/grid/node-x14-y11   94T   71T    23T   75%
/dev/grid/node-x14-y12   92T   64T    28T   69%
/dev/grid/node-x14-y13   89T   71T    18T   79%
/dev/grid/node-x14-y14   91T   71T    20T   78%
/dev/grid/node-x14-y15   90T   71T    19T   78%
/dev/grid/node-x14-y16   88T   65T    23T   73%
/dev/grid/node-x14-y17   93T   67T    26T   72%
/dev/grid/node-x14-y18   92T   69T    23T   75%
/dev/grid/node-x14-y19   85T   65T    20T   76%
/dev/grid/node-x14-y20   91T   71T    20T   78%
/dev/grid/node-x14-y21   90T   71T    19T   78%
/dev/grid/node-x14-y22   94T   66T    28T   70%
/dev/grid/node-x14-y23   93T   69T    24T   74%
/dev/grid/node-x14-y24   92T   69T    23T   75%
/dev/grid/node-x14-y25   85T   66T    19T   77%
/dev/grid/node-x14-y26   89T   70T    19T   78%
/dev/grid/node-x14-y27   87T   64T    23T   73%
/dev/grid/node-x14-y28   89T   72T    17T   80%
/dev/grid/node-x14-y29   91T   69T    22T   75%
/dev/grid/node-x15-y0    87T   71T    16T   81%
/dev/grid/node-x15-y1    85T   69T    16T   81%
/dev/grid/node-x15-y2    94T   65T    29T   69%
/dev/grid/node-x15-y3    92T   70T    22T   76%
/dev/grid/node-x15-y4    90T   64T    26T   71%
/dev/grid/node-x15-y5    88T   72T    16T   81%
/dev/grid/node-x15-y6    88T   73T    15T   82%
/dev/grid/node-x15-y7    90T   73T    17T   81%
/dev/grid/node-x15-y8    88T   69T    19T   78%
/dev/grid/node-x15-y9   510T  498T    12T   97%
/dev/grid/node-x15-y10   91T   69T    22T   75%
/dev/grid/node-x15-y11   86T   70T    16T   81%
/dev/grid/node-x15-y12   85T   68T    17T   80%
/dev/grid/node-x15-y13   88T   71T    17T   80%
/dev/grid/node-x15-y14   91T   72T    19T   79%
/dev/grid/node-x15-y15   88T   66T    22T   75%
/dev/grid/node-x15-y16   87T   70T    17T   80%
/dev/grid/node-x15-y17   87T   72T    15T   82%
/dev/grid/node-x15-y18   91T   73T    18T   80%
/dev/grid/node-x15-y19   93T   72T    21T   77%
/dev/grid/node-x15-y20   94T   73T    21T   77%
/dev/grid/node-x15-y21   88T   72T    16T   81%
/dev/grid/node-x15-y22   91T   64T    27T   70%
/dev/grid/node-x15-y23   94T   67T    27T   71%
/dev/grid/node-x15-y24   91T   70T    21T   76%
/dev/grid/node-x15-y25   88T   65T    23T   73%
/dev/grid/node-x15-y26   91T   71T    20T   78%
/dev/grid/node-x15-y27   93T   71T    22T   76%
/dev/grid/node-x15-y28   88T   67T    21T   76%
/dev/grid/node-x15-y29   86T   64T    22T   74%
/dev/grid/node-x16-y0    89T   69T    20T   77%
/dev/grid/node-x16-y1    91T   69T    22T   75%
/dev/grid/node-x16-y2    94T   66T    28T   70%
/dev/grid/node-x16-y3    94T   66T    28T   70%
/dev/grid/node-x16-y4    85T   73T    12T   85%
/dev/grid/node-x16-y5    87T   68T    19T   78%
/dev/grid/node-x16-y6    94T   72T    22T   76%
/dev/grid/node-x16-y7    87T   72T    15T   82%
/dev/grid/node-x16-y8    86T   72T    14T   83%
/dev/grid/node-x16-y9   505T  493T    12T   97%
/dev/grid/node-x16-y10   87T   65T    22T   74%
/dev/grid/node-x16-y11   87T   65T    22T   74%
/dev/grid/node-x16-y12   94T   71T    23T   75%
/dev/grid/node-x16-y13   94T   69T    25T   73%
/dev/grid/node-x16-y14   93T   66T    27T   70%
/dev/grid/node-x16-y15   92T   67T    25T   72%
/dev/grid/node-x16-y16   92T   69T    23T   75%
/dev/grid/node-x16-y17   86T   73T    13T   84%
/dev/grid/node-x16-y18   89T   68T    21T   76%
/dev/grid/node-x16-y19   88T   68T    20T   77%
/dev/grid/node-x16-y20   87T   69T    18T   79%
/dev/grid/node-x16-y21   88T   71T    17T   80%
/dev/grid/node-x16-y22   92T   67T    25T   72%
/dev/grid/node-x16-y23   86T   72T    14T   83%
/dev/grid/node-x16-y24   89T   67T    22T   75%
/dev/grid/node-x16-y25   90T   70T    20T   77%
/dev/grid/node-x16-y26   89T   68T    21T   76%
/dev/grid/node-x16-y27   86T   66T    20T   76%
/dev/grid/node-x16-y28   89T   72T    17T   80%
/dev/grid/node-x16-y29   94T   72T    22T   76%
/dev/grid/node-x17-y0    85T   65T    20T   76%
/dev/grid/node-x17-y1    91T   71T    20T   78%
/dev/grid/node-x17-y2    91T   67T    24T   73%
/dev/grid/node-x17-y3    88T   69T    19T   78%
/dev/grid/node-x17-y4    89T   72T    17T   80%
/dev/grid/node-x17-y5    86T   69T    17T   80%
/dev/grid/node-x17-y6    90T   65T    25T   72%
/dev/grid/node-x17-y7    90T   64T    26T   71%
/dev/grid/node-x17-y8    88T   71T    17T   80%
/dev/grid/node-x17-y9   505T  490T    15T   97%
/dev/grid/node-x17-y10   87T   66T    21T   75%
/dev/grid/node-x17-y11   89T   70T    19T   78%
/dev/grid/node-x17-y12   91T   73T    18T   80%
/dev/grid/node-x17-y13   91T   73T    18T   80%
/dev/grid/node-x17-y14   85T   66T    19T   77%
/dev/grid/node-x17-y15   91T   67T    24T   73%
/dev/grid/node-x17-y16   88T   64T    24T   72%
/dev/grid/node-x17-y17   86T   69T    17T   80%
/dev/grid/node-x17-y18   93T   69T    24T   74%
/dev/grid/node-x17-y19   94T   72T    22T   76%
/dev/grid/node-x17-y20   92T   71T    21T   77%
/dev/grid/node-x17-y21   89T   73T    16T   82%
/dev/grid/node-x17-y22   85T   65T    20T   76%
/dev/grid/node-x17-y23   85T   69T    16T   81%
/dev/grid/node-x17-y24   93T   65T    28T   69%
/dev/grid/node-x17-y25   90T   72T    18T   80%
/dev/grid/node-x17-y26   89T   67T    22T   75%
/dev/grid/node-x17-y27   91T   73T    18T   80%
/dev/grid/node-x17-y28   86T   67T    19T   77%
/dev/grid/node-x17-y29   86T   71T    15T   82%
/dev/grid/node-x18-y0    86T   72T    14T   83%
/dev/grid/node-x18-y1    87T   68T    19T   78%
/dev/grid/node-x18-y2    86T   73T    13T   84%
/dev/grid/node-x18-y3    89T   73T    16T   82%
/dev/grid/node-x18-y4    90T   73T    17T   81%
/dev/grid/node-x18-y5    88T   72T    16T   81%
/dev/grid/node-x18-y6    92T   66T    26T   71%
/dev/grid/node-x18-y7    91T   71T    20T   78%
/dev/grid/node-x18-y8    89T   73T    16T   82%
/dev/grid/node-x18-y9   510T  492T    18T   96%
/dev/grid/node-x18-y10   87T   64T    23T   73%
/dev/grid/node-x18-y11   91T   65T    26T   71%
/dev/grid/node-x18-y12   93T   67T    26T   72%
/dev/grid/node-x18-y13   92T   68T    24T   73%
/dev/grid/node-x18-y14   85T   72T    13T   84%
/dev/grid/node-x18-y15   93T   64T    29T   68%
/dev/grid/node-x18-y16   86T   64T    22T   74%
/dev/grid/node-x18-y17   86T   73T    13T   84%
/dev/grid/node-x18-y18   93T   64T    29T   68%
/dev/grid/node-x18-y19   88T   73T    15T   82%
/dev/grid/node-x18-y20   93T   72T    21T   77%
/dev/grid/node-x18-y21   85T   64T    21T   75%
/dev/grid/node-x18-y22   87T   72T    15T   82%
/dev/grid/node-x18-y23   88T   68T    20T   77%
/dev/grid/node-x18-y24   93T   64T    29T   68%
/dev/grid/node-x18-y25   94T   66T    28T   70%
/dev/grid/node-x18-y26   89T   68T    21T   76%
/dev/grid/node-x18-y27   87T   64T    23T   73%
/dev/grid/node-x18-y28   88T   67T    21T   76%
/dev/grid/node-x18-y29   87T   73T    14T   83%
/dev/grid/node-x19-y0    85T   72T    13T   84%
/dev/grid/node-x19-y1    86T   68T    18T   79%
/dev/grid/node-x19-y2    89T   68T    21T   76%
/dev/grid/node-x19-y3    92T   64T    28T   69%
/dev/grid/node-x19-y4    90T   66T    24T   73%
/dev/grid/node-x19-y5    93T   72T    21T   77%
/dev/grid/node-x19-y6    93T   66T    27T   70%
/dev/grid/node-x19-y7    87T   65T    22T   74%
/dev/grid/node-x19-y8    86T   69T    17T   80%
/dev/grid/node-x19-y9   509T  492T    17T   96%
/dev/grid/node-x19-y10   89T   64T    25T   71%
/dev/grid/node-x19-y11   92T   65T    27T   70%
/dev/grid/node-x19-y12   92T   73T    19T   79%
/dev/grid/node-x19-y13   85T   68T    17T   80%
/dev/grid/node-x19-y14   90T   68T    22T   75%
/dev/grid/node-x19-y15   92T   70T    22T   76%
/dev/grid/node-x19-y16   92T   69T    23T   75%
/dev/grid/node-x19-y17   92T   66T    26T   71%
/dev/grid/node-x19-y18   87T   65T    22T   74%
/dev/grid/node-x19-y19   92T   71T    21T   77%
/dev/grid/node-x19-y20   87T   67T    20T   77%
/dev/grid/node-x19-y21   94T   73T    21T   77%
/dev/grid/node-x19-y22   94T   69T    25T   73%
/dev/grid/node-x19-y23   90T   67T    23T   74%
/dev/grid/node-x19-y24   89T   70T    19T   78%
/dev/grid/node-x19-y25   91T   66T    25T   72%
/dev/grid/node-x19-y26   85T   65T    20T   76%
/dev/grid/node-x19-y27   91T   68T    23T   74%
/dev/grid/node-x19-y28   87T   68T    19T   78%
/dev/grid/node-x19-y29   88T   70T    18T   79%
/dev/grid/node-x20-y0    91T   69T    22T   75%
/dev/grid/node-x20-y1    90T   64T    26T   71%
/dev/grid/node-x20-y2    89T   72T    17T   80%
/dev/grid/node-x20-y3    94T   72T    22T   76%
/dev/grid/node-x20-y4    91T   64T    27T   70%
/dev/grid/node-x20-y5    91T   71T    20T   78%
/dev/grid/node-x20-y6    88T   65T    23T   73%
/dev/grid/node-x20-y7    93T   70T    23T   75%
/dev/grid/node-x20-y8    91T   73T    18T   80%
/dev/grid/node-x20-y9   509T  497T    12T   97%
/dev/grid/node-x20-y10   93T   66T    27T   70%
/dev/grid/node-x20-y11   86T   66T    20T   76%
/dev/grid/node-x20-y12   86T   73T    13T   84%
/dev/grid/node-x20-y13   94T   70T    24T   74%
/dev/grid/node-x20-y14   85T   69T    16T   81%
/dev/grid/node-x20-y15   85T   68T    17T   80%
/dev/grid/node-x20-y16   86T   70T    16T   81%
/dev/grid/node-x20-y17   85T   73T    12T   85%
/dev/grid/node-x20-y18   89T   73T    16T   82%
/dev/grid/node-x20-y19   89T   64T    25T   71%
/dev/grid/node-x20-y20   94T   69T    25T   73%
/dev/grid/node-x20-y21   85T   66T    19T   77%
/dev/grid/node-x20-y22   87T   71T    16T   81%
/dev/grid/node-x20-y23   85T   71T    14T   83%
/dev/grid/node-x20-y24   85T   70T    15T   82%
/dev/grid/node-x20-y25   93T   65T    28T   69%
/dev/grid/node-x20-y26   90T   65T    25T   72%
/dev/grid/node-x20-y27   89T   71T    18T   79%
/dev/grid/node-x20-y28   89T   66T    23T   74%
/dev/grid/node-x20-y29   89T   64T    25T   71%
/dev/grid/node-x21-y0    90T   65T    25T   72%
/dev/grid/node-x21-y1    92T   71T    21T   77%
/dev/grid/node-x21-y2    90T   64T    26T   71%
/dev/grid/node-x21-y3    90T   66T    24T   73%
/dev/grid/node-x21-y4    89T   71T    18T   79%
/dev/grid/node-x21-y5    89T   65T    24T   73%
/dev/grid/node-x21-y6    94T   73T    21T   77%
/dev/grid/node-x21-y7    88T   66T    22T   75%
/dev/grid/node-x21-y8    85T   67T    18T   78%
/dev/grid/node-x21-y9   508T  497T    11T   97%
/dev/grid/node-x21-y10   94T   71T    23T   75%
/dev/grid/node-x21-y11   87T   72T    15T   82%
/dev/grid/node-x21-y12   88T   66T    22T   75%
/dev/grid/node-x21-y13   86T   64T    22T   74%
/dev/grid/node-x21-y14   87T   73T    14T   83%
/dev/grid/node-x21-y15   89T   65T    24T   73%
/dev/grid/node-x21-y16   93T   69T    24T   74%
/dev/grid/node-x21-y17   88T   73T    15T   82%
/dev/grid/node-x21-y18   85T   67T    18T   78%
/dev/grid/node-x21-y19   90T   73T    17T   81%
/dev/grid/node-x21-y20   93T   66T    27T   70%
/dev/grid/node-x21-y21   91T   64T    27T   70%
/dev/grid/node-x21-y22   86T   68T    18T   79%
/dev/grid/node-x21-y23   86T   67T    19T   77%
/dev/grid/node-x21-y24   91T   65T    26T   71%
/dev/grid/node-x21-y25   87T   67T    20T   77%
/dev/grid/node-x21-y26   94T   71T    23T   75%
/dev/grid/node-x21-y27   89T   64T    25T   71%
/dev/grid/node-x21-y28   87T   71T    16T   81%
/dev/grid/node-x21-y29   86T   68T    18T   79%
/dev/grid/node-x22-y0    90T   71T    19T   78%
/dev/grid/node-x22-y1    88T   73T    15T   82%
/dev/grid/node-x22-y2    91T   72T    19T   79%
/dev/grid/node-x22-y3    89T   72T    17T   80%
/dev/grid/node-x22-y4    92T   72T    20T   78%
/dev/grid/node-x22-y5    86T   73T    13T   84%
/dev/grid/node-x22-y6    87T   65T    22T   74%
/dev/grid/node-x22-y7    85T   73T    12T   85%
/dev/grid/node-x22-y8    94T   71T    23T   75%
/dev/grid/node-x22-y9   508T  492T    16T   96%
/dev/grid/node-x22-y10   93T   66T    27T   70%
/dev/grid/node-x22-y11   91T   67T    24T   73%
/dev/grid/node-x22-y12   86T   64T    22T   74%
/dev/grid/node-x22-y13   91T   64T    27T   70%
/dev/grid/node-x22-y14   86T   65T    21T   75%
/dev/grid/node-x22-y15   89T   71T    18T   79%
/dev/grid/node-x22-y16   89T   69T    20T   77%
/dev/grid/node-x22-y17   91T   72T    19T   79%
/dev/grid/node-x22-y18   91T   70T    21T   76%
/dev/grid/node-x22-y19   92T   66T    26T   71%
/dev/grid/node-x22-y20   92T   72T    20T   78%
/dev/grid/node-x22-y21   94T   64T    30T   68%
/dev/grid/node-x22-y22   85T   67T    18T   78%
/dev/grid/node-x22-y23   89T   71T    18T   79%
/dev/grid/node-x22-y24   91T   71T    20T   78%
/dev/grid/node-x22-y25   94T   65T    29T   69%
/dev/grid/node-x22-y26   87T   71T    16T   81%
/dev/grid/node-x22-y27   85T   72T    13T   84%
/dev/grid/node-x22-y28   93T   69T    24T   74%
/dev/grid/node-x22-y29   91T   68T    23T   74%
/dev/grid/node-x23-y0    86T   67T    19T   77%
/dev/grid/node-x23-y1    91T   69T    22T   75%
/dev/grid/node-x23-y2    85T   64T    21T   75%
/dev/grid/node-x23-y3    86T   68T    18T   79%
/dev/grid/node-x23-y4    90T   66T    24T   73%
/dev/grid/node-x23-y5    89T   71T    18T   79%
/dev/grid/node-x23-y6    87T   66T    21T   75%
/dev/grid/node-x23-y7    93T   70T    23T   75%
/dev/grid/node-x23-y8    93T   66T    27T   70%
/dev/grid/node-x23-y9   502T  494T     8T   98%
/dev/grid/node-x23-y10   88T   70T    18T   79%
/dev/grid/node-x23-y11   87T   66T    21T   75%
/dev/grid/node-x23-y12   86T   67T    19T   77%
/dev/grid/node-x23-y13   94T   72T    22T   76%
/dev/grid/node-x23-y14   87T   70T    17T   80%
/dev/grid/node-x23-y15   91T   67T    24T   73%
/dev/grid/node-x23-y16   93T   68T    25T   73%
/dev/grid/node-x23-y17   93T   65T    28T   69%
/dev/grid/node-x23-y18   89T   64T    25T   71%
/dev/grid/node-x23-y19   93T   66T    27T   70%
/dev/grid/node-x23-y20   89T   73T    16T   82%
/dev/grid/node-x23-y21   87T   73T    14T   83%
/dev/grid/node-x23-y22   93T   71T    22T   76%
/dev/grid/node-x23-y23   93T   73T    20T   78%
/dev/grid/node-x23-y24   94T   69T    25T   73%
/dev/grid/node-x23-y25   91T   70T    21T   76%
/dev/grid/node-x23-y26   93T   69T    24T   74%
/dev/grid/node-x23-y27   90T   67T    23T   74%
/dev/grid/node-x23-y28   90T   65T    25T   72%
/dev/grid/node-x23-y29   93T   73T    20T   78%
/dev/grid/node-x24-y0    85T   66T    19T   77%
/dev/grid/node-x24-y1    85T   70T    15T   82%
/dev/grid/node-x24-y2    92T   72T    20T   78%
/dev/grid/node-x24-y3    94T   66T    28T   70%
/dev/grid/node-x24-y4    87T   68T    19T   78%
/dev/grid/node-x24-y5    87T   71T    16T   81%
/dev/grid/node-x24-y6    86T   70T    16T   81%
/dev/grid/node-x24-y7    94T   68T    26T   72%
/dev/grid/node-x24-y8    87T   65T    22T   74%
/dev/grid/node-x24-y9   505T  497T     8T   98%
/dev/grid/node-x24-y10   85T   68T    17T   80%
/dev/grid/node-x24-y11   89T   67T    22T   75%
/dev/grid/node-x24-y12   90T   66T    24T   73%
/dev/grid/node-x24-y13   94T   65T    29T   69%
/dev/grid/node-x24-y14   86T   73T    13T   84%
/dev/grid/node-x24-y15   93T   66T    27T   70%
/dev/grid/node-x24-y16   88T   64T    24T   72%
/dev/grid/node-x24-y17   93T   65T    28T   69%
/dev/grid/node-x24-y18   93T   66T    27T   70%
/dev/grid/node-x24-y19   87T   66T    21T   75%
/dev/grid/node-x24-y20   88T   70T    18T   79%
/dev/grid/node-x24-y21   93T   66T    27T   70%
/dev/grid/node-x24-y22   88T   73T    15T   82%
/dev/grid/node-x24-y23   87T   73T    14T   83%
/dev/grid/node-x24-y24   90T   66T    24T   73%
/dev/grid/node-x24-y25   87T   67T    20T   77%
/dev/grid/node-x24-y26   89T   67T    22T   75%
/dev/grid/node-x24-y27   87T   69T    18T   79%
/dev/grid/node-x24-y28   92T   69T    23T   75%
/dev/grid/node-x24-y29   88T   67T    21T   76%
/dev/grid/node-x25-y0    88T   72T    16T   81%
/dev/grid/node-x25-y1    87T   66T    21T   75%
/dev/grid/node-x25-y2    85T   68T    17T   80%
/dev/grid/node-x25-y3    88T   73T    15T   82%
/dev/grid/node-x25-y4    89T   70T    19T   78%
/dev/grid/node-x25-y5    89T   70T    19T   78%
/dev/grid/node-x25-y6    87T   69T    18T   79%
/dev/grid/node-x25-y7    88T   73T    15T   82%
/dev/grid/node-x25-y8    91T   72T    19T   79%
/dev/grid/node-x25-y9   507T  498T     9T   98%
/dev/grid/node-x25-y10   94T   73T    21T   77%
/dev/grid/node-x25-y11   93T   67T    26T   72%
/dev/grid/node-x25-y12   94T   69T    25T   73%
/dev/grid/node-x25-y13   91T   65T    26T   71%
/dev/grid/node-x25-y14   93T   73T    20T   78%
/dev/grid/node-x25-y15   91T   69T    22T   75%
/dev/grid/node-x25-y16   91T   65T    26T   71%
/dev/grid/node-x25-y17   88T   69T    19T   78%
/dev/grid/node-x25-y18   85T   69T    16T   81%
/dev/grid/node-x25-y19   92T   69T    23T   75%
/dev/grid/node-x25-y20   85T   65T    20T   76%
/dev/grid/node-x25-y21   87T   67T    20T   77%
/dev/grid/node-x25-y22   93T   65T    28T   69%
/dev/grid/node-x25-y23   91T   71T    20T   78%
/dev/grid/node-x25-y24   86T   73T    13T   84%
/dev/grid/node-x25-y25   91T   67T    24T   73%
/dev/grid/node-x25-y26   90T   69T    21T   76%
/dev/grid/node-x25-y27   93T   72T    21T   77%
/dev/grid/node-x25-y28   93T   66T    27T   70%
/dev/grid/node-x25-y29   88T   71T    17T   80%
/dev/grid/node-x26-y0    94T   71T    23T   75%
/dev/grid/node-x26-y1    94T   72T    22T   76%
/dev/grid/node-x26-y2    91T   73T    18T   80%
/dev/grid/node-x26-y3    89T   69T    20T   77%
/dev/grid/node-x26-y4    94T   71T    23T   75%
/dev/grid/node-x26-y5    93T   65T    28T   69%
/dev/grid/node-x26-y6    93T   65T    28T   69%
/dev/grid/node-x26-y7    88T   66T    22T   75%
/dev/grid/node-x26-y8    94T   71T    23T   75%
/dev/grid/node-x26-y9   507T  493T    14T   97%
/dev/grid/node-x26-y10   93T   69T    24T   74%
/dev/grid/node-x26-y11   89T   65T    24T   73%
/dev/grid/node-x26-y12   90T    0T    90T    0%
/dev/grid/node-x26-y13   92T   67T    25T   72%
/dev/grid/node-x26-y14   87T   71T    16T   81%
/dev/grid/node-x26-y15   94T   66T    28T   70%
/dev/grid/node-x26-y16   89T   71T    18T   79%
/dev/grid/node-x26-y17   87T   65T    22T   74%
/dev/grid/node-x26-y18   88T   66T    22T   75%
/dev/grid/node-x26-y19   92T   66T    26T   71%
/dev/grid/node-x26-y20   92T   70T    22T   76%
/dev/grid/node-x26-y21   86T   68T    18T   79%
/dev/grid/node-x26-y22   94T   70T    24T   74%
/dev/grid/node-x26-y23   87T   64T    23T   73%
/dev/grid/node-x26-y24   87T   73T    14T   83%
/dev/grid/node-x26-y25   85T   66T    19T   77%
/dev/grid/node-x26-y26   94T   67T    27T   71%
/dev/grid/node-x26-y27   86T   66T    20T   76%
/dev/grid/node-x26-y28   86T   69T    17T   80%
/dev/grid/node-x26-y29   91T   67T    24T   73%
/dev/grid/node-x27-y0    94T   73T    21T   77%
/dev/grid/node-x27-y1    93T   65T    28T   69%
/dev/grid/node-x27-y2    92T   66T    26T   71%
/dev/grid/node-x27-y3    87T   68T    19T   78%
/dev/grid/node-x27-y4    93T   73T    20T   78%
/dev/grid/node-x27-y5    87T   72T    15T   82%
/dev/grid/node-x27-y6    91T   69T    22T   75%
/dev/grid/node-x27-y7    89T   64T    25T   71%
/dev/grid/node-x27-y8    86T   69T    17T   80%
/dev/grid/node-x27-y9   508T  498T    10T   98%
/dev/grid/node-x27-y10   91T   72T    19T   79%
/dev/grid/node-x27-y11   87T   72T    15T   82%
/dev/grid/node-x27-y12   90T   69T    21T   76%
/dev/grid/node-x27-y13   90T   72T    18T   80%
/dev/grid/node-x27-y14   85T   69T    16T   81%
/dev/grid/node-x27-y15   90T   66T    24T   73%
/dev/grid/node-x27-y16   94T   68T    26T   72%
/dev/grid/node-x27-y17   92T   66T    26T   71%
/dev/grid/node-x27-y18   94T   73T    21T   77%
/dev/grid/node-x27-y19   93T   64T    29T   68%
/dev/grid/node-x27-y20   85T   68T    17T   80%
/dev/grid/node-x27-y21   86T   67T    19T   77%
/dev/grid/node-x27-y22   85T   66T    19T   77%
/dev/grid/node-x27-y23   87T   65T    22T   74%
/dev/grid/node-x27-y24   94T   70T    24T   74%
/dev/grid/node-x27-y25   91T   65T    26T   71%
/dev/grid/node-x27-y26   92T   69T    23T   75%
/dev/grid/node-x27-y27   88T   68T    20T   77%
/dev/grid/node-x27-y28   90T   72T    18T   80%
/dev/grid/node-x27-y29   89T   66T    23T   74%
/dev/grid/node-x28-y0    85T   66T    19T   77%
/dev/grid/node-x28-y1    85T   66T    19T   77%
/dev/grid/node-x28-y2    93T   69T    24T   74%
/dev/grid/node-x28-y3    92T   66T    26T   71%
/dev/grid/node-x28-y4    93T   69T    24T   74%
/dev/grid/node-x28-y5    90T   66T    24T   73%
/dev/grid/node-x28-y6    90T   69T    21T   76%
/dev/grid/node-x28-y7    86T   64T    22T   74%
/dev/grid/node-x28-y8    94T   70T    24T   74%
/dev/grid/node-x28-y9   505T  498T     7T   98%
/dev/grid/node-x28-y10   88T   71T    17T   80%
/dev/grid/node-x28-y11   87T   73T    14T   83%
/dev/grid/node-x28-y12   93T   72T    21T   77%
/dev/grid/node-x28-y13   86T   64T    22T   74%
/dev/grid/node-x28-y14   87T   73T    14T   83%
/dev/grid/node-x28-y15   92T   73T    19T   79%
/dev/grid/node-x28-y16   88T   68T    20T   77%
/dev/grid/node-x28-y17   89T   67T    22T   75%
/dev/grid/node-x28-y18   91T   65T    26T   71%
/dev/grid/node-x28-y19   94T   68T    26T   72%
/dev/grid/node-x28-y20   88T   64T    24T   72%
/dev/grid/node-x28-y21   86T   70T    16T   81%
/dev/grid/node-x28-y22   91T   65T    26T   71%
/dev/grid/node-x28-y23   91T   65T    26T   71%
/dev/grid/node-x28-y24   94T   70T    24T   74%
/dev/grid/node-x28-y25   92T   71T    21T   77%
/dev/grid/node-x28-y26   89T   71T    18T   79%
/dev/grid/node-x28-y27   86T   64T    22T   74%
/dev/grid/node-x28-y28   87T   67T    20T   77%
/dev/grid/node-x28-y29   94T   73T    21T   77%
/dev/grid/node-x29-y0    91T   64T    27T   70%
/dev/grid/node-x29-y1    87T   67T    20T   77%
/dev/grid/node-x29-y2    93T   68T    25T   73%
/dev/grid/node-x29-y3    86T   72T    14T   83%
/dev/grid/node-x29-y4    87T   66T    21T   75%
/dev/grid/node-x29-y5    89T   65T    24T   73%
/dev/grid/node-x29-y6    86T   67T    19T   77%
/dev/grid/node-x29-y7    86T   71T    15T   82%
/dev/grid/node-x29-y8    94T   66T    28T   70%
/dev/grid/node-x29-y9   505T  491T    14T   97%
/dev/grid/node-x29-y10   86T   70T    16T   81%
/dev/grid/node-x29-y11   94T   66T    28T   70%
/dev/grid/node-x29-y12   86T   68T    18T   79%
/dev/grid/node-x29-y13   91T   72T    19T   79%
/dev/grid/node-x29-y14   87T   67T    20T   77%
/dev/grid/node-x29-y15   90T   65T    25T   72%
/dev/grid/node-x29-y16   88T   69T    19T   78%
/dev/grid/node-x29-y17   88T   69T    19T   78%
/dev/grid/node-x29-y18   85T   69T    16T   81%
/dev/grid/node-x29-y19   88T   73T    15T   82%
/dev/grid/node-x29-y20   90T   68T    22T   75%
/dev/grid/node-x29-y21   88T   70T    18T   79%
/dev/grid/node-x29-y22   89T   72T    17T   80%
/dev/grid/node-x29-y23   93T   70T    23T   75%
/dev/grid/node-x29-y24   85T   72T    13T   84%
/dev/grid/node-x29-y25   88T   72T    16T   81%
/dev/grid/node-x29-y26   93T   73T    20T   78%
/dev/grid/node-x29-y27   90T   68T    22T   75%
/dev/grid/node-x29-y28   91T   65T    26T   71%
/dev/grid/node-x29-y29   93T   71T    22T   76%
/dev/grid/node-x30-y0    93T   64T    29T   68%
/dev/grid/node-x30-y1    94T   73T    21T   77%
/dev/grid/node-x30-y2    87T   71T    16T   81%
/dev/grid/node-x30-y3    93T   71T    22T   76%
/dev/grid/node-x30-y4    94T   72T    22T   76%
/dev/grid/node-x30-y5    89T   72T    17T   80%
/dev/grid/node-x30-y6    88T   73T    15T   82%
/dev/grid/node-x30-y7    85T   73T    12T   85%
/dev/grid/node-x30-y8    88T   64T    24T   72%
/dev/grid/node-x30-y9   503T  490T    13T   97%
/dev/grid/node-x30-y10   87T   68T    19T   78%
/dev/grid/node-x30-y11   86T   65T    21T   75%
/dev/grid/node-x30-y12   86T   65T    21T   75%
/dev/grid/node-x30-y13   85T   67T    18T   78%
/dev/grid/node-x30-y14   85T   73T    12T   85%
/dev/grid/node-x30-y15   87T   70T    17T   80%
/dev/grid/node-x30-y16   93T   68T    25T   73%
/dev/grid/node-x30-y17   88T   70T    18T   79%
/dev/grid/node-x30-y18   93T   66T    27T   70%
/dev/grid/node-x30-y19   94T   73T    21T   77%
/dev/grid/node-x30-y20   86T   64T    22T   74%
/dev/grid/node-x30-y21   93T   67T    26T   72%
/dev/grid/node-x30-y22   88T   64T    24T   72%
/dev/grid/node-x30-y23   90T   72T    18T   80%
/dev/grid/node-x30-y24   93T   65T    28T   69%
/dev/grid/node-x30-y25   89T   66T    23T   74%
/dev/grid/node-x30-y26   88T   69T    19T   78%
/dev/grid/node-x30-y27   91T   71T    20T   78%
/dev/grid/node-x30-y28   92T   68T    24T   73%
/dev/grid/node-x30-y29   85T   72T    13T   84%
/dev/grid/node-x31-y0    88T   65T    23T   73%
/dev/grid/node-x31-y1    90T   73T    17T   81%
/dev/grid/node-x31-y2    89T   66T    23T   74%
/dev/grid/node-x31-y3    89T   72T    17T   80%
/dev/grid/node-x31-y4    91T   68T    23T   74%
/dev/grid/node-x31-y5    89T   67T    22T   75%
/dev/grid/node-x31-y6    85T   67T    18T   78%
/dev/grid/node-x31-y7    90T   73T    17T   81%
/dev/grid/node-x31-y8    86T   64T    22T   74%
/dev/grid/node-x31-y9   510T  497T    13T   97%
/dev/grid/node-x31-y10   85T   64T    21T   75%
/dev/grid/node-x31-y11   87T   66T    21T   75%
/dev/grid/node-x31-y12   92T   67T    25T   72%
/dev/grid/node-x31-y13   93T   70T    23T   75%
/dev/grid/node-x31-y14   94T   65T    29T   69%
/dev/grid/node-x31-y15   89T   73T    16T   82%
/dev/grid/node-x31-y16   85T   65T    20T   76%
/dev/grid/node-x31-y17   85T   66T    19T   77%
/dev/grid/node-x31-y18   89T   73T    16T   82%
/dev/grid/node-x31-y19   89T   73T    16T   82%
/dev/grid/node-x31-y20   85T   73T    12T   85%
/dev/grid/node-x31-y21   93T   66T    27T   70%
/dev/grid/node-x31-y22   87T   65T    22T   74%
/dev/grid/node-x31-y23   90T   72T    18T   80%
/dev/grid/node-x31-y24   85T   71T    14T   83%
/dev/grid/node-x31-y25   89T   66T    23T   74%
/dev/grid/node-x31-y26   94T   72T    22T   76%
/dev/grid/node-x31-y27   91T   71T    20T   78%
/dev/grid/node-x31-y28   87T   71T    16T   81%
/dev/grid/node-x31-y29   92T   69T    23T   75%
/dev/grid/node-x32-y0    94T   67T    27T   71%
/dev/grid/node-x32-y1    92T   66T    26T   71%
/dev/grid/node-x32-y2    86T   69T    17T   80%
/dev/grid/node-x32-y3    94T   69T    25T   73%
/dev/grid/node-x32-y4    91T   68T    23T   74%
/dev/grid/node-x32-y5    92T   72T    20T   78%
/dev/grid/node-x32-y6    91T   66T    25T   72%
/dev/grid/node-x32-y7    88T   64T    24T   72%
/dev/grid/node-x32-y8    89T   65T    24T   73%
/dev/grid/node-x32-y9   506T  499T     7T   98%
/dev/grid/node-x32-y10   88T   68T    20T   77%
/dev/grid/node-x32-y11   91T   69T    22T   75%
/dev/grid/node-x32-y12   91T   65T    26T   71%
/dev/grid/node-x32-y13   90T   64T    26T   71%
/dev/grid/node-x32-y14   92T   73T    19T   79%
/dev/grid/node-x32-y15   91T   70T    21T   76%
/dev/grid/node-x32-y16   87T   64T    23T   73%
/dev/grid/node-x32-y17   92T   72T    20T   78%
/dev/grid/node-x32-y18   90T   71T    19T   78%
/dev/grid/node-x32-y19   91T   68T    23T   74%
/dev/grid/node-x32-y20   87T   70T    17T   80%
/dev/grid/node-x32-y21   93T   71T    22T   76%
/dev/grid/node-x32-y22   88T   68T    20T   77%
/dev/grid/node-x32-y23   87T   65T    22T   74%
/dev/grid/node-x32-y24   89T   65T    24T   73%
/dev/grid/node-x32-y25   93T   73T    20T   78%
/dev/grid/node-x32-y26   94T   67T    27T   71%
/dev/grid/node-x32-y27   90T   71T    19T   78%
/dev/grid/node-x32-y28   93T   73T    20T   78%
/dev/grid/node-x32-y29   91T   71T    20T   78%
"

# COMMAND ----------

# input <- "
# Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%
# "

# COMMAND ----------

df <-
  read_table(input, skip = 1) %>%
  mutate_all(~str_remove(., "T|%") %>% parse_guess()) %>%
  rename_all(~str_remove(str_to_lower(.), '[^a-z]')) %>%
  mutate(
    x = str_extract(filesystem, "(?<=x)\\d+") %>% parse_integer(),
    y = str_extract(filesystem, "(?<=y)\\d+") %>% parse_integer()
  )
df

# COMMAND ----------

answer <- sqldf::sqldf("
SELECT COUNT(DISTINCT a.filesystem || b.filesystem)
FROM
  df a
  LEFT JOIN df b ON
    b.avail >= a.used
    AND b.filesystem != a.filesystem
WHERE
  a.used > 0
") %>%
  pull(1)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now that you have a better understanding of the grid, it's time to get to work.</p>
# MAGIC <p>Your goal is to gain access to the data which begins in the node with <code>y=0</code> and the <em>highest <code>x</code></em> (that is, the node in the top-right corner).</p>
# MAGIC <p>For example, suppose you have the following grid:</p>
# MAGIC <pre><code>Filesystem            Size  Used  Avail  Use%
# MAGIC /dev/grid/node-x0-y0   10T    8T     2T   80%
# MAGIC /dev/grid/node-x0-y1   11T    6T     5T   54%
# MAGIC /dev/grid/node-x0-y2   32T   28T     4T   87%
# MAGIC /dev/grid/node-x1-y0    9T    7T     2T   77%
# MAGIC /dev/grid/node-x1-y1    8T    0T     8T    0%
# MAGIC /dev/grid/node-x1-y2   11T    7T     4T   63%
# MAGIC /dev/grid/node-x2-y0   10T    6T     4T   60%
# MAGIC /dev/grid/node-x2-y1    9T    8T     1T   88%
# MAGIC /dev/grid/node-x2-y2    9T    6T     3T   66%
# MAGIC </code></pre>
# MAGIC <p>In this example, you have a storage grid <code>3</code> nodes wide and <code>3</code> nodes tall.  The node you can access directly, <code>node-x0-y0</code>, is almost full. The node containing the data you want to access, <code>node-x2-y0</code> (because it has <code>y=0</code> and the highest <code>x</code> value), contains 6 <a href="https://en.wikipedia.org/wiki/Terabyte">terabytes</a> of data - enough to fit on your node, if only you could make enough space to move it there.</p>
# MAGIC <p>Fortunately, <code>node-x1-y1</code> looks like it has enough free space to enable you to move some of this data around.  In fact, it seems like all of the nodes have enough space to hold any node's data (except <code>node-x0-y2</code>, which is much larger, very full, and not moving any time soon). So, initially, the grid's capacities and connections look like this:</p>
# MAGIC <pre><code>( 8T/10T) --  7T/ 9T -- [ 6T/10T]
# MAGIC     |           |           |
# MAGIC   6T/11T  --  0T/ 8T --   8T/ 9T
# MAGIC     |           |           |
# MAGIC  28T/32T  --  7T/11T --   6T/ 9T
# MAGIC </code></pre>
# MAGIC <p>The node you can access directly is in parentheses; the data you want starts in the node marked by square brackets.</p>
# MAGIC <p>In this example, most of the nodes are interchangable: they're full enough that no other node's data would fit, but small enough that their data could be moved around. Let's draw these nodes as <code>.</code>. The exceptions are the empty node, which we'll draw as <code>_</code>, and the very large, very full node, which we'll draw as <code>#</code>. Let's also draw the goal data as <code>G</code>. Then, it looks like this:</p>
# MAGIC <pre><code>(.) .  G
# MAGIC  .  _  .
# MAGIC  #  .  .
# MAGIC </code></pre>
# MAGIC <p>The goal is to move the data in the top right, <code>G</code>, to the node in parentheses. To do this, we can issue some commands to the grid and rearrange the data:</p>
# MAGIC <ul>
# MAGIC <li><p>Move data from <code>node-y0-x1</code> to <code>node-y1-x1</code>, leaving node <code>node-y0-x1</code> empty:</p><pre><code>(.) _  G
# MAGIC  .  .  .
# MAGIC  #  .  .
# MAGIC </code></pre>
# MAGIC </li><li><p>Move the goal data from <code>node-y0-x2</code> to <code>node-y0-x1</code>:</p><pre><code>(.) G  _
# MAGIC  .  .  .
# MAGIC  #  .  .
# MAGIC </code></pre>
# MAGIC </li><li><p>At this point, we're quite close. However, we have no deletion command, so we have to move some more data around. So, next, we move the data from <code>node-y1-x2</code> to <code>node-y0-x2</code>:</p><pre><code>(.) G  .
# MAGIC  .  .  _
# MAGIC  #  .  .
# MAGIC </code></pre>
# MAGIC </li><li><p>Move the data from <code>node-y1-x1</code> to <code>node-y1-x2</code>:</p><pre><code>(.) G  .
# MAGIC  .  _  .
# MAGIC  #  .  .
# MAGIC </code></pre>
# MAGIC </li><li><p>Move the data from <code>node-y1-x0</code> to <code>node-y1-x1</code>:</p><pre><code>(.) G  .
# MAGIC  _  .  .
# MAGIC  #  .  .
# MAGIC </code></pre>
# MAGIC </li><li><p>Next, we can free up space on our node by moving the data from <code>node-y0-x0</code> to <code>node-y1-x0</code>:</p><pre><code>(_) G  .
# MAGIC  .  .  .
# MAGIC  #  .  .
# MAGIC </code></pre>
# MAGIC </li>
# MAGIC <li><p>Finally, we can access the goal data by moving the it from <code>node-y0-x1</code> to <code>node-y0-x0</code>:</p><pre><code>(G) _  .
# MAGIC  .  .  .
# MAGIC  #  .  .
# MAGIC </code></pre>
# MAGIC </li>
# MAGIC </ul>
# MAGIC <p>So, after <code>7</code> steps, we've accessed the data we want. Unfortunately, each of these moves takes time, and we need to be efficient:</p>
# MAGIC <p><em>What is the fewest number of steps</em> required to move your goal data to <code>node-x0-y0</code>?</p>
# MAGIC </article>

# COMMAND ----------

df %>%
  mutate(value = str_c(used, " | ", avail)) %>%
  select(x, y, value) %>%
  pivot_wider(names_from = x) %>%
  display()

# COMMAND ----------

df %>%
  mutate(
    col = case_when(
      x == min(x) & y == min(y) ~ "blue",
      x == max(x) & y == min(y) ~ "orange",
      avail == 90 ~ "green",
      used > 90 ~ "red",
      TRUE ~ "grey"
    )
  ) %>%
  ggplot(aes(x, y, fill = I(col))) +
  geom_tile(col = "black") +
  scale_x_continuous(
    breaks = seq(from = min(df$x), to = max(df$x), by = 1),
    expand = c(0, 0)
  ) +
  scale_y_reverse(
    breaks = seq(from = min(df$y), to = max(df$y), by = 1),
    expand = c(0, 0)
  ) +
  theme_void() +
  theme(axis.text = element_text(size = rel(0.7)))

# COMMAND ----------

# Clearly this is just a sliding puzzle with a wall.
answer <- 16 + 12 + 22 + 31 * 5
answer
