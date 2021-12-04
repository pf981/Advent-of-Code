# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 4: Giant Squid ---</h2><p>You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you <em>can</em> see, however, is a giant squid that has attached itself to the outside of your submarine.</p>
# MAGIC <p>Maybe it wants to play <a href="https://en.wikipedia.org/wiki/Bingo_(American_version)" target="_blank">bingo</a>?</p>
# MAGIC <p>Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is <em>marked</em> on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board <em>wins</em>. (Diagonals don't count.)</p>
# MAGIC <p>The submarine has a <em>bingo subsystem</em> to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:</p>
# MAGIC <pre><code>7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
# MAGIC 
# MAGIC 22 13 17 11  0
# MAGIC  8  2 23  4 24
# MAGIC 21  9 14 16  7
# MAGIC  6 10  3 18  5
# MAGIC  1 12 20 15 19
# MAGIC 
# MAGIC  3 15  0  2 22
# MAGIC  9 18 13 17  5
# MAGIC 19  8  7 25 23
# MAGIC 20 11 10 24  4
# MAGIC 14 21 16 12  6
# MAGIC 
# MAGIC 14 21 17 24  4
# MAGIC 10 16 15  9 19
# MAGIC 18  8 23 26 20
# MAGIC 22 11 13  6  5
# MAGIC  2  0 12  3  7
# MAGIC </code></pre>
# MAGIC <p>After the first five numbers are drawn (<code>7</code>, <code>4</code>, <code>9</code>, <code>5</code>, and <code>11</code>), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):</p>
# MAGIC <pre><code>22 13 17 <em>11</em>  0         3 15  0  2 22        14 21 17 24  <em>4</em>
# MAGIC  8  2 23  <em>4</em> 24         <em>9</em> 18 13 17  <em>5</em>        10 16 15  <em>9</em> 19
# MAGIC 21  <em>9</em> 14 16  <em>7</em>        19  8  <em>7</em> 25 23        18  8 23 26 20
# MAGIC  6 10  3 18  <em>5</em>        20 <em>11</em> 10 24  <em>4</em>        22 <em>11</em> 13  6  <em>5</em>
# MAGIC  1 12 20 15 19        14 21 16 12  6         2  0 12  3  <em>7</em>
# MAGIC </code></pre>
# MAGIC <p>After the next six numbers are drawn (<code>17</code>, <code>23</code>, <code>2</code>, <code>0</code>, <code>14</code>, and <code>21</code>), there are still no winners:</p>
# MAGIC <pre><code>22 13 <em>17</em> <em>11</em>  <em>0</em>         3 15  <em>0</em>  <em>2</em> 22        <em>14</em> <em>21</em> <em>17</em> 24  <em>4</em>
# MAGIC  8  <em>2</em> <em>23</em>  <em>4</em> 24         <em>9</em> 18 13 <em>17</em>  <em>5</em>        10 16 15  <em>9</em> 19
# MAGIC <em>21</em>  <em>9</em> <em>14</em> 16  <em>7</em>        19  8  <em>7</em> 25 <em>23</em>        18  8 <em>23</em> 26 20
# MAGIC  6 10  3 18  <em>5</em>        20 <em>11</em> 10 24  <em>4</em>        22 <em>11</em> 13  6  <em>5</em>
# MAGIC  1 12 20 15 19        <em>14</em> <em>21</em> 16 12  6         <em>2</em>  <em>0</em> 12  3  <em>7</em>
# MAGIC </code></pre>
# MAGIC <p>Finally, <code>24</code> is drawn:</p>
# MAGIC <pre><code>22 13 <em>17</em> <em>11</em>  <em>0</em>         3 15  <em>0</em>  <em>2</em> 22        <em>14</em> <em>21</em> <em>17</em> <em>24</em>  <em>4</em>
# MAGIC  8  <em>2</em> <em>23</em>  <em>4</em> <em>24</em>         <em>9</em> 18 13 <em>17</em>  <em>5</em>        10 16 15  <em>9</em> 19
# MAGIC <em>21</em>  <em>9</em> <em>14</em> 16  <em>7</em>        19  8  <em>7</em> 25 <em>23</em>        18  8 <em>23</em> 26 20
# MAGIC  6 10  3 18  <em>5</em>        20 <em>11</em> 10 <em>24</em>  <em>4</em>        22 <em>11</em> 13  6  <em>5</em>
# MAGIC  1 12 20 15 19        <em>14</em> <em>21</em> 16 12  6         <em>2</em>  <em>0</em> 12  3  <em>7</em>
# MAGIC </code></pre>
# MAGIC <p>At this point, the third board <em>wins</em> because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: <code><em>14 21 17 24  4</em></code>).</p>
# MAGIC <p>The <em>score</em> of the winning board can now be calculated. Start by finding the <em>sum of all unmarked numbers</em> on that board; in this case, the sum is <code>188</code>. Then, multiply that sum by <em>the number that was just called</em> when the board won, <code>24</code>, to get the final score, <code>188 * 24 = <em>4512</em></code>.</p>
# MAGIC <p>To guarantee victory against the giant squid, figure out which board will win first. <em>What will your final score be if you choose that board?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''91,17,64,45,8,13,47,19,52,68,63,76,82,44,28,56,37,2,78,48,32,58,72,53,9,85,77,89,36,22,49,86,51,99,6,92,80,87,7,25,31,66,84,4,98,67,46,61,59,79,0,3,38,27,23,95,20,35,14,30,26,33,42,93,12,57,11,54,50,75,90,41,88,96,40,81,24,94,18,39,70,34,21,55,5,29,71,83,1,60,74,69,10,62,43,73,97,65,15,16

83 40 67 98  4
50 74 31 30  3
75 64 79 61  5
12 59 26 25 72
36 33 18 54 10

68 56 28 57 12
78 66 20 85 51
35 23  7 99 44
86 37  8 45 49
40 77 32  6 88

75 15 20 79  8
81 69 54 33 28
 9 53 48 95 27
65 84 40 71 36
13 31  6 68 29

94  6 30 16 74
91 47 66 31 90
14 56 45 55 20
58 70 27 46 73
77 67 97 51 54

60 12 49 80 52
15 27 85 82 48
21 76 83 55 54
 8  5  4 38 47
73  2 86 44 99

64 60  6 38 37
 3 69 21 24 11
36 88 16 55 41
78  7 81 95 91
27 34 92 39 30

38 57 20 68 49
21 18 69 97 60
34 92  0 59 62
10 43 93 87 64
53 35 94 76 61

48 74 58 13 54
57 18 37 92 78
89 10 25 97 43
38 99 64  6 66
21 83 29 93 95

94 37 98 87 51
50 65 77 83 95
68  4 91 53 32
56 26 15  2 80
20 55 58 81 33

73 32 66 38 89
18 79 40 78 55
26 63 93 60 98
42 65 96 47 57
45 75 72 23 35

64 28 21 80 27
93 58 71 67 11
61 20 74 13 90
76 35 46 94 40
92  2  4 85 69

22 70 87 31 61
74 78 58  4 90
63 28 24 35 84
59  8 89 88 47
17 48 80 33 32

57  7 30 39 19
 1 13 41 15 50
44 72  2  5 70
34 93 60 80 69
49 14 25 10 33

45 41 77 89 27
68 99 11 32 95
15  4 72 98 52
53 28 14 75 44
57  9 62 92 69

 7 21  2 73 40
52 60 57 53 65
63 86 36 82 44
14 28 39 12 80
66 64 91 50 51

82  5 38 41 95
70 52 11 21 51
81 20  0 14 83
57 36 60 59 42
77 13 85 32 63

91 40 42  3 50
22 24 81 31 93
 9 79 82 43 89
 6 77 76 26 37
29  8 53 23  4

 7 78 32 44 74
29  3 84 38 79
58 41 87 88 30
68 19 72 81 47
15 63 52  6 26

20 41 92 84 25
 9  4 96 85 66
49 15 50 89 19
48 45 82 86 60
29 18 53 47 16

75 39 45 31 73
91 86 69 94 66
28 61 17 20  0
88 21 89 41 37
35  2 10 18 82

80 23  4 73 93
89  8 20 12 45
74 99 58 90 67
50 85 35 88 55
18 65 42 47 48

16 38 65 64 25
20 74 37 15 82
23 76 97 48 53
60 93 85  1 35
77 10 59  2 58

11  9 57 40 46
35 88 29 52 17
30  2  7  6  0
13 63 44 68 59
83 98  5 50 65

82 40  2 14 50
 7 31 91 19 11
51 42 56 44  6
66 74 22 95 64
63  1 17 86 24

18 19 66 63 80
65 23 74 22 85
 5  7 37 75 51
38 58 68 83 32
40 29 31 15 43

37 54 13 77 31
57 96 28 87 95
10 11 19 49 45
12 21 79 56 24
34 64 84 69 17

 6 33 48 61  0
85 34  7 84 37
25 46 59 76 82
18 62 20 44  2
12 78 60 56 99

95  6  1 39  2
46 34 28 64 22
48 23 89 56 55
44 81 82 43 74
65 31 94 49 91

69 42 27 52 54
79 60 62 83 38
 5 21 56 48 99
51 40 15  7 24
92 10 66 64 88

99 18 22 52 81
21 42 13 71 59
91 38 68 10 25
54 19 76 60 24
41 92  2  3 64

76  5 25 55 84
70 15 89 67 68
34 86 11  4  6
 9 23 43 41 52
58 10 88 38  0

83 91 85 81 86
 5 10 89  6 48
45 77  2  9 90
74  8 57 75 67
73 30 49 96 15

66 13 82 89 20
 5 67 94 64  0
58 73  4 62 49
59 28 75 79 44
54 71 57 33 36

23 36 29 80 30
51 91 77  2 84
78 90 15 21 75
28 93 22 55 16
67 50 58 60 68

82 80 37 91  7
54 81 85 25 24
33 36 89 30 56
83 95 99 48 10
 4 44  1 55 79

 9 13 53 20 26
 7 31 49 84 58
51 91 90 68 55
19 38 23 81 33
34 99 85 37 54

44 66 81 78 15
31 14 48 65  0
26 10 20  4 41
77 68 95 34 73
74 12 36  3 60

 6 24 78 58 36
30 51 75 13 40
17  1  3 42 59
64 20  4 18 79
37 61 84 63  7

41 83  1 75 18
14 56 67 32 22
69 80 46 84 49
72 21  9 10 35
 4 37 28 40 12

56 80 47 17 70
12 22 77 81 11
61 30 58 60 71
52  0 25 86 65
59 28 79 20 26

70 75 81 18 67
 2 85 73  8 17
74  3 34 92 30
51 72 84 56 45
37 90 31 97 78

 2 73 71 43 69
 6 54 89 57 93
81  0 39 25 90
79 27 92 29 15
45 76 87 11 91

98 35 51 49 34
23 12 77 27 82
 6 89  0 76 46
81 48 99 45 90
10 75 17 96 29

45 19 82 93  0
84 24 73  2 98
94 46  7 48 56
80 34  5 18 31
58 33 83 29 55

66 81 99 54 63
21 94 72 77 64
58 52 85 46 68
 5  6 78 42  4
76 38 51 24 33

93 26  5 59 67
13 84 76  4 69
 0 17 30 83 48
 8 53 32 14 92
94 18 66 46 61

28 48 38  6 25
70 39 71 77 22
66 94 18 43 36
30 67 57  9 90
15 34 50  3 86

11 90 99 92 87
78 79 56 21 50
19 18 22 20 30
95 41 59 85 26
66 58 46 38 57

49 92  2 93 77
46 89 44 57 19
53  8 32 18 88
54 95 59 70 10
72 84 86 42 81

44 78 25  4 57
72  7 42 94  8
61 79 11 29 59
22 82  6 90 12
98 77  5 68 50

48 41 64 15 57
76  7 52 53 93
70 84 94 38 35
47 18 13 51 21
77 62 63  3 65

31 33 48 79 69
30  9 83 53 50
60 94 36  2 28
59 19 10  5 40
26 41 72 14 96

 0 16 49 75 17
28 20 21 99 94
15  8  4 68 71
23 53 76 19 74
79 61 72 70 52

70 89 12 80 76
14 18 16  4 91
34 64 43 51 71
 6 78 30  5 13
57 42 15 73 24

64 99 72 41 54
21 29 25 40  9
92 48 82 70 98
65 62  8 78 27
71 86 36 34 23

23 19 72 77 63
85  0 61 40 14
69 76 18 56 95
68 66 28 79 13
83 84 45 89  2

18 40 28 70 37
80 30 67 96 34
77 25 97 32 11
48 46 89 14 29
 2  8 95  0 12

 0 26  1  9 30
17  2 78 18 65
84  7 61 93 81
80 44 82 23 99
72 95 19 60 28

37 39  0 20 21
91 36 93 16 22
53 95 26 72 25
97 33 60 55 65
79 56 73 29 75

22 58 99 57 28
 2 56 93 91 18
44 64 92 85 46
70 47 89 27 54
83  5 48 97 72

72  1 73 68 36
31  8 14 41 35
23 96  7 92 83
56 39 77 93 91
20 28 67 10 11

62 27 17 54  0
35 60 73 20  5
23 58 46 99 75
19 53 79 70 88
31 85 77  1 32

22 90 81 42 55
70 78 86 19 94
 1 43 15 33 51
84 96 87 58  6
49 64  4 59 23

82 63 58 75 89
35 37 52 80 24
93 50 76 79  1
86 59 30 92  7
42 11 55 70 22

83  3 71 28 95
70 23 68 57  1
60  6 19 63 32
64 55 97 81 49
91 80 88  5 35

23 68 51 62 20
70 52 98 34 41
12 21 85 43 84
69 49 36 28  0
76 30 58 91 60

30 72  6 41 43
67 79 46 96 99
58 71 39 87 69
17 18 11 57 25
45 75 16 33 42

22 75 24 74 90
34 70 44 86 23
29 59 68  4 48
88 45 92 27 49
47 77 26 99 82

42 29 21 74 33
64 37 38 50 84
46 44 41  1 67
53 66 96 68 59
 6 94 11 31 99

24 32 71 87 57
42 26 55 80 99
82 27 16 19 92
96 48 62 31 61
60 89 95 18  6

99 33 55 71 29
75 37 23 27 98
 2 78 90 18 35
59 10 56  0  6
12 19 76 70 96

33 37 23 61 80
 6 13 68 51 76
92 25  3 95 55
99 63 17 52 30
11 94 42  5 98

77 37 25 14 73
95 90 10 19 72
78 30 44 47 91
 3 60 32  5 66
21 55 87 98  6

 6 60 82 90 98
21 70 54 66 27
37 64 55 10 14
57 25 84 50 20
42 59 85  3 73

74 84 92 10 51
57 82 93 90 44
41 43 76 48 59
79 49 69 16 72
37 29 63 15 68

37 90 97 86 18
 2 83 30 53 92
45 35 78 47 40
67 61 17 14 84
32 33 81 10 11

46 48 39  3 50
83 29 91 73 67
25 43 89 71 36
63 62 78 95 18
82 34 23 85 11

19 68 80 50 13
 1 45 51 27 39
98 26 24 46 49
14 92 63 88 66
15 44 84 47 94

19 39 93 43 86
91 58  3 69 41
18 36 95 52 83
12  6 22 48  0
25 70 40 88 73

95 11 94 13 14
64 87 57 98 49
47 88 84 61  2
46 21 15 74 59
82 73 78  3 51

18 72 29  7 36
96 67 81 78 23
43 40 44 47 98
41 26 15 90 71
42 62 93 70  2

17  8 59 25 33
81 47 55 99 48
86 14 71 54 50
90 11 23 18  0
97 65 82 68 42

50 54 68 90 83
10 28 77 55 61
38 60 52 80 44
40 81 14 24 87
51 82 42 30  8

54  5 64 22 60
70 19 83 11 45
46 39  2 56  6
61  8 28 20 94
 0  4 81 34 84

96 21 48 89 15
91 40  9 97 65
26 58 10 18 78
98 79 29 80 28
17 59 43 84 99

67 73 21  9 31
68 37 26 65 84
63 24 42 27 40
61 25 30 34 35
53 23 48 81 29

24 34  5 67 62
89 85 68 37 78
42 87 13 49 41
74 55 70 86 76
73 94 97 63 48

88 24  6 75 30
77 64 16 34 93
36 76  0 40 81
67 14 89 84 95
32 19 18 66  9

97 71 65 30 69
41 21 40 31 33
50 55 35 52 53
 4 51 13 81 72
12 83 14 64 18

97  7  8 74 10
 3 92 31 25 41
20 32 45 72 55
 1 43 49 98 27
99 54 57 13 76

86 81 67  6 97
34 18 96 43 56
59 75 17 26  9
 0 38 60 94 14
 4 55 64 61 88

37 15 48 43 66
45 54 90 81 47
63 64 28 82 93
34 52  6 99 61
49 12 71 23 46

90 87 89 97  1
48  0 82 60 43
55 30 68 25 83
78  3 23 16 66
98  2 19 63 17

89 52 49 14 38
69 12 50 17 90
58 53 26 20 29
39 65 43  7  5
84 68 94 85 25

95 25 42 36 47
50 54 83 84 37
94 70 99 79 18
57  8 69 52 31
66 20 35 71 38

81 18 47 68 15
 3 50 16 83 37
34 31  9 57 76
74 95 40 63 48
13 28 20 43 66

52 21 62 41 67
22 56 36 18 23
59 44 27 73  3
72 50 19 33 76
45 55 70 46 92

72 96 50 83 68
31 78 59 57 93
43 58 17 52 35
87 34 91 76  0
54 75 53 25 62

21 53 68  5 80
47 67  6 81  9
64 46 35 26 39
50 24 84 45 71
66 15 83  3 97

22 97 31 90 63
21 51 38 74 78
10 64 92 82  1
70 12 75 16 14
68 50 35 73 26'''

# COMMAND ----------

draws, *boards = inp.split('\n\n')
draws = [int(draw) for draw in draws.split(',')]
boards = [[[int(x) for x in line.split(' ') if x] for line in board.splitlines()] for board in boards]

# COMMAND ----------

import copy

def has_won(board):
  for row in board:
    if all(num == -1 for num in row):
      return True

  for col in zip(*board):
    if all(num == -1 for num in col):
      return True
  
  return False

def winning_score(draws, boards, nth_winner=1):
  draws = draws.copy()
  boards = copy.deepcopy(boards)
  completed_boards = set()

  for draw in draws:
    for board_id, board in enumerate(boards):
      if board_id in completed_boards:
        continue

      for line in board:
        for i, _ in enumerate(line):
          line[i] = -1 if line[i] == draw else line[i]

      if has_won(board):
        completed_boards.add(board_id)
        if len(completed_boards) == nth_winner:
          return draw * sum(num for row in board for num in row if num != -1)

answer = winning_score(draws, boards)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>On the other hand, it might be wise to try a different strategy: <span title="That's 'cuz a submarine don't pull things' antennas out of their sockets when they lose. Giant squid are known to do that.">let the giant squid win</span>.</p>
# MAGIC <p>You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to <em>figure out which board will win last</em> and choose that one. That way, no matter which boards it picks, it will win for sure.</p>
# MAGIC <p>In the above example, the second board is the last to win, which happens after <code>13</code> is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to <code>148</code> for a final score of <code>148 * 13 = <em>1924</em></code>.</p>
# MAGIC <p>Figure out which board will win last. <em>Once it wins, what would its final score be?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = winning_score(draws, boards, len(boards))
print(answer)
