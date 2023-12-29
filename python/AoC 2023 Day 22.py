# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/22

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 22: Sand Slabs ---</h2><p>Enough sand has fallen; it can finally filter water for Snow Island.</p>
# MAGIC <p>Well, <em>almost</em>.</p>
# MAGIC <p>The sand has been falling as large compacted <em>bricks</em> of sand, piling up to form an impressive stack here near the edge of Island Island. In order to make use of the sand to filter water, some of the bricks will need to be broken apart - nay, <em><span title="Disintegrate - X,R
# MAGIC Sorcery
# MAGIC Destroy X target bricks of sand. They cannot be regenerated. Create 32768 0/1 colorless Sand artifact creature tokens for each brick of sand destroyed in this way.">disintegrated</span></em> - back into freely flowing sand.</p>
# MAGIC <p>The stack is tall enough that you'll have to be careful about choosing which bricks to disintegrate; if you disintegrate the wrong brick, large portions of the stack could topple, which sounds pretty dangerous.</p>
# MAGIC <p>The Elves responsible for water filtering operations took a <em>snapshot of the bricks while they were still falling</em> (your puzzle input) which should let you work out which bricks are safe to disintegrate. For example:</p>
# MAGIC <pre><code>1,0,1~1,2,1
# MAGIC 0,0,2~2,0,2
# MAGIC 0,2,3~2,2,3
# MAGIC 0,0,4~0,2,4
# MAGIC 2,0,5~2,2,5
# MAGIC 0,1,6~2,1,6
# MAGIC 1,1,8~1,1,9
# MAGIC </code></pre>
# MAGIC <p>Each line of text in the snapshot represents the position of a single brick at the time the snapshot was taken. The position is given as two <code>x,y,z</code> coordinates - one for each end of the brick - separated by a tilde (<code>~</code>). Each brick is made up of a single straight line of cubes, and the Elves were even careful to choose a time for the snapshot that had all of the free-falling bricks at <em>integer positions above the ground</em>, so the whole snapshot is aligned to a three-dimensional cube grid.</p>
# MAGIC <p>A line like <code>2,2,2~2,2,2</code> means that both ends of the brick are at the same coordinate - in other words, that the brick is a single cube.</p>
# MAGIC <p>Lines like <code>0,0,10~1,0,10</code> or <code>0,0,10~0,1,10</code> both represent bricks that are <em>two cubes</em> in volume, both oriented horizontally. The first brick extends in the <code>x</code> direction, while the second brick extends in the <code>y</code> direction.</p>
# MAGIC <p>A line like <code>0,0,1~0,0,10</code> represents a <em>ten-cube brick</em> which is oriented <em>vertically</em>. One end of the brick is the cube located at <code>0,0,1</code>, while the other end of the brick is located directly above it at <code>0,0,10</code>.</p>
# MAGIC <p>The ground is at <code>z=0</code> and is perfectly flat; the lowest <code>z</code> value a brick can have is therefore <code>1</code>. So, <code>5,5,1~5,6,1</code> and <code>0,2,1~0,2,5</code> are both resting on the ground, but <code>3,3,2~3,3,3</code> was above the ground at the time of the snapshot.</p>
# MAGIC <p>Because the snapshot was taken while the bricks were still falling, some bricks will <em>still be in the air</em>; you'll need to start by figuring out where they will end up. Bricks are magically stabilized, so they <em>never rotate</em>, even in weird situations like where a long horizontal brick is only supported on one end. Two bricks cannot occupy the same position, so a falling brick will come to rest upon the first other brick it encounters.</p>
# MAGIC <p>Here is the same example again, this time with each brick given a letter so it can be marked in diagrams:</p>
# MAGIC <pre><code>1,0,1~1,2,1   &lt;- A
# MAGIC 0,0,2~2,0,2   &lt;- B
# MAGIC 0,2,3~2,2,3   &lt;- C
# MAGIC 0,0,4~0,2,4   &lt;- D
# MAGIC 2,0,5~2,2,5   &lt;- E
# MAGIC 0,1,6~2,1,6   &lt;- F
# MAGIC 1,1,8~1,1,9   &lt;- G
# MAGIC </code></pre>
# MAGIC <p>At the time of the snapshot, from the side so the <code>x</code> axis goes left to right, these bricks are arranged like this:</p>
# MAGIC <pre><code> x
# MAGIC 012
# MAGIC .G. 9
# MAGIC .G. 8
# MAGIC ... 7
# MAGIC FFF 6
# MAGIC ..E 5 z
# MAGIC D.. 4
# MAGIC CCC 3
# MAGIC BBB 2
# MAGIC .A. 1
# MAGIC --- 0
# MAGIC </code></pre>
# MAGIC <p>Rotating the perspective 90 degrees so the <code>y</code> axis now goes left to right, the same bricks are arranged like this:</p>
# MAGIC <pre><code> y
# MAGIC 012
# MAGIC .G. 9
# MAGIC .G. 8
# MAGIC ... 7
# MAGIC .F. 6
# MAGIC EEE 5 z
# MAGIC DDD 4
# MAGIC ..C 3
# MAGIC B.. 2
# MAGIC AAA 1
# MAGIC --- 0
# MAGIC </code></pre>
# MAGIC <p>Once all of the bricks fall downward as far as they can go, the stack looks like this, where <code>?</code> means bricks are hidden behind other bricks at that location:</p>
# MAGIC <pre><code> x
# MAGIC 012
# MAGIC .G. 6
# MAGIC .G. 5
# MAGIC FFF 4
# MAGIC D.E 3 z
# MAGIC ??? 2
# MAGIC .A. 1
# MAGIC --- 0
# MAGIC </code></pre>
# MAGIC <p>Again from the side:</p>
# MAGIC <pre><code> y
# MAGIC 012
# MAGIC .G. 6
# MAGIC .G. 5
# MAGIC .F. 4
# MAGIC ??? 3 z
# MAGIC B.C 2
# MAGIC AAA 1
# MAGIC --- 0
# MAGIC </code></pre>
# MAGIC <p>Now that all of the bricks have settled, it becomes easier to tell which bricks are supporting which other bricks:</p>
# MAGIC <ul>
# MAGIC <li>Brick <code>A</code> is the only brick supporting bricks <code>B</code> and <code>C</code>.</li>
# MAGIC <li>Brick <code>B</code> is one of two bricks supporting brick <code>D</code> and brick <code>E</code>.</li>
# MAGIC <li>Brick <code>C</code> is the other brick supporting brick <code>D</code> and brick <code>E</code>.</li>
# MAGIC <li>Brick <code>D</code> supports brick <code>F</code>.</li>
# MAGIC <li>Brick <code>E</code> also supports brick <code>F</code>.</li>
# MAGIC <li>Brick <code>F</code> supports brick <code>G</code>.</li>
# MAGIC <li>Brick <code>G</code> isn't supporting any bricks.</li>
# MAGIC </ul>
# MAGIC <p>Your first task is to figure out <em>which bricks are safe to disintegrate</em>. A brick can be safely disintegrated if, after removing it, <em>no other bricks</em> would fall further directly downward. Don't actually disintegrate any bricks - just determine what would happen if, for each brick, only that brick were disintegrated. Bricks can be disintegrated even if they're completely surrounded by other bricks; you can squeeze between bricks if you need to.</p>
# MAGIC <p>In this example, the bricks can be disintegrated as follows:</p>
# MAGIC <ul>
# MAGIC <li>Brick <code>A</code> cannot be disintegrated safely; if it were disintegrated, bricks <code>B</code> and <code>C</code> would both fall.</li>
# MAGIC <li>Brick <code>B</code> <em>can</em> be disintegrated; the bricks above it (<code>D</code> and <code>E</code>) would still be supported by brick <code>C</code>.</li>
# MAGIC <li>Brick <code>C</code> <em>can</em> be disintegrated; the bricks above it (<code>D</code> and <code>E</code>) would still be supported by brick <code>B</code>.</li>
# MAGIC <li>Brick <code>D</code> <em>can</em> be disintegrated; the brick above it (<code>F</code>) would still be supported by brick <code>E</code>.</li>
# MAGIC <li>Brick <code>E</code> <em>can</em> be disintegrated; the brick above it (<code>F</code>) would still be supported by brick <code>D</code>.</li>
# MAGIC <li>Brick <code>F</code> cannot be disintegrated; the brick above it (<code>G</code>) would fall.</li>
# MAGIC <li>Brick <code>G</code> <em>can</em> be disintegrated; it does not support any other bricks.</li>
# MAGIC </ul>
# MAGIC <p>So, in this example, <code><em>5</em></code> bricks can be safely disintegrated.</p>
# MAGIC <p>Figure how the blocks will settle based on the snapshot. Once they've settled, consider disintegrating a single brick; <em>how many bricks could be safely chosen as the one to get disintegrated?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''7,0,231~7,2,231
3,8,44~4,8,44
4,2,331~4,4,331
4,3,236~4,4,236
4,6,155~4,8,155
7,5,141~7,7,141
7,7,72~7,9,72
4,8,190~6,8,190
6,2,107~8,2,107
0,4,122~0,5,122
6,1,177~6,3,177
5,5,247~5,8,247
0,1,184~3,1,184
5,3,306~5,4,306
1,2,13~3,2,13
0,7,198~2,7,198
5,7,333~8,7,333
5,6,281~5,6,282
3,6,8~5,6,8
2,2,277~2,3,277
2,4,229~3,4,229
1,3,121~2,3,121
5,4,317~7,4,317
4,4,103~5,4,103
3,6,200~3,8,200
3,2,248~3,2,250
3,4,162~3,7,162
6,7,169~6,9,169
0,9,148~1,9,148
6,0,190~7,0,190
6,3,247~6,5,247
0,0,289~0,1,289
0,2,228~3,2,228
8,8,230~8,8,233
2,4,221~2,6,221
4,0,215~4,0,217
3,4,250~6,4,250
9,3,205~9,3,205
1,2,227~1,4,227
1,5,322~4,5,322
7,4,18~7,5,18
7,9,220~8,9,220
0,9,326~1,9,326
9,6,90~9,8,90
0,1,62~0,3,62
4,6,264~6,6,264
5,0,100~7,0,100
4,0,212~7,0,212
2,5,289~2,7,289
8,6,67~9,6,67
7,5,20~7,5,22
6,4,27~7,4,27
0,3,225~0,4,225
3,2,161~5,2,161
4,8,269~5,8,269
3,9,115~4,9,115
6,7,222~6,7,224
8,1,78~8,1,80
9,3,301~9,5,301
4,6,35~6,6,35
0,6,14~0,8,14
3,6,9~3,7,9
6,6,99~8,6,99
2,1,150~2,4,150
5,5,248~5,7,248
3,4,110~6,4,110
5,6,65~5,8,65
8,6,46~8,8,46
6,7,168~8,7,168
0,4,23~1,4,23
9,3,14~9,5,14
4,2,30~4,2,32
7,1,244~7,2,244
2,5,179~2,8,179
0,2,44~0,3,44
6,2,7~6,5,7
3,8,39~5,8,39
3,7,117~5,7,117
2,7,196~5,7,196
2,4,84~2,7,84
4,2,150~4,5,150
1,3,8~2,3,8
7,7,136~7,8,136
3,3,238~6,3,238
3,1,25~5,1,25
6,5,9~6,5,11
0,9,109~2,9,109
3,7,44~3,7,46
5,7,37~5,9,37
5,1,132~5,4,132
6,8,100~7,8,100
3,0,186~5,0,186
2,3,305~2,5,305
1,6,81~1,8,81
1,0,325~3,0,325
0,7,145~0,9,145
3,5,135~4,5,135
4,0,24~4,2,24
0,0,188~0,0,190
7,6,170~7,8,170
5,1,186~7,1,186
1,2,11~4,2,11
5,1,271~8,1,271
1,3,171~3,3,171
2,0,187~2,3,187
1,0,71~4,0,71
1,7,295~1,8,295
9,2,74~9,3,74
3,7,233~3,9,233
4,8,118~7,8,118
2,7,24~2,9,24
9,1,68~9,2,68
2,9,144~3,9,144
6,7,284~8,7,284
6,9,95~6,9,96
1,6,54~4,6,54
8,2,204~8,3,204
2,4,30~4,4,30
2,2,42~3,2,42
5,4,209~7,4,209
8,6,24~8,8,24
6,7,106~8,7,106
6,7,181~6,9,181
6,5,213~6,6,213
5,1,75~5,2,75
6,8,95~8,8,95
6,4,230~7,4,230
2,7,207~4,7,207
2,0,100~3,0,100
0,5,234~0,7,234
0,7,226~0,7,228
1,5,154~1,7,154
1,3,297~1,5,297
5,0,263~5,2,263
9,7,288~9,8,288
0,8,276~2,8,276
1,3,47~3,3,47
5,0,53~8,0,53
5,4,264~7,4,264
4,2,75~4,4,75
3,0,312~3,3,312
8,7,34~8,9,34
7,0,101~9,0,101
1,6,55~1,8,55
0,7,205~1,7,205
6,6,210~8,6,210
1,9,272~3,9,272
3,8,74~6,8,74
4,8,286~6,8,286
2,6,144~5,6,144
7,5,23~7,5,24
9,0,42~9,2,42
3,5,131~5,5,131
5,9,311~6,9,311
0,7,207~0,7,207
4,5,51~4,7,51
9,6,40~9,8,40
6,2,133~8,2,133
9,4,233~9,4,233
6,5,92~6,7,92
0,4,326~3,4,326
6,7,207~6,9,207
6,4,166~6,7,166
4,0,38~5,0,38
5,3,252~7,3,252
0,1,69~3,1,69
5,1,69~7,1,69
6,5,83~6,6,83
8,8,218~8,9,218
4,2,129~6,2,129
7,0,233~7,2,233
9,5,28~9,8,28
1,7,232~4,7,232
1,9,270~3,9,270
6,7,220~6,7,221
3,1,33~6,1,33
5,6,102~7,6,102
5,2,164~6,2,164
9,4,110~9,6,110
1,9,317~4,9,317
8,0,109~8,3,109
0,5,61~0,7,61
1,4,225~1,6,225
4,3,328~4,3,330
1,8,280~3,8,280
0,3,321~0,7,321
2,8,72~3,8,72
4,5,60~5,5,60
4,3,195~4,5,195
8,5,319~8,7,319
4,4,149~5,4,149
3,7,52~3,7,53
7,5,67~9,5,67
4,0,282~6,0,282
6,6,192~6,7,192
6,4,151~6,7,151
3,2,106~6,2,106
7,7,56~7,9,56
7,2,1~7,4,1
4,2,325~4,5,325
0,3,51~2,3,51
6,1,131~6,3,131
8,0,241~8,3,241
3,4,245~6,4,245
6,7,286~9,7,286
4,2,159~4,4,159
3,5,299~3,7,299
6,4,171~6,6,171
7,0,238~9,0,238
3,5,254~3,7,254
6,3,86~6,5,86
2,5,201~2,8,201
1,8,274~2,8,274
7,3,100~7,4,100
4,8,192~5,8,192
5,3,207~7,3,207
7,4,316~8,4,316
0,6,52~0,7,52
7,7,101~9,7,101
6,0,254~8,0,254
2,6,245~6,6,245
1,4,139~3,4,139
9,3,305~9,4,305
3,6,108~5,6,108
1,6,249~1,6,250
1,9,275~2,9,275
0,4,292~0,6,292
5,2,109~6,2,109
3,7,256~3,7,259
4,5,59~4,7,59
1,5,27~1,8,27
3,2,53~5,2,53
5,9,26~7,9,26
3,3,180~3,5,180
6,3,24~6,5,24
6,6,283~6,8,283
9,1,289~9,3,289
2,4,56~2,4,58
6,4,97~9,4,97
2,4,206~2,6,206
4,9,277~5,9,277
1,0,227~2,0,227
6,6,121~6,8,121
4,6,136~5,6,136
3,1,55~6,1,55
7,3,295~9,3,295
5,6,122~5,9,122
3,7,239~3,8,239
1,5,235~1,7,235
7,4,214~7,6,214
5,6,21~7,6,21
6,1,99~6,1,102
7,2,323~8,2,323
5,4,252~7,4,252
0,7,25~2,7,25
3,0,278~4,0,278
2,6,91~2,9,91
5,2,133~5,3,133
4,3,152~6,3,152
2,5,232~4,5,232
3,1,181~3,4,181
1,1,152~1,2,152
4,4,251~6,4,251
3,4,324~4,4,324
5,3,60~5,3,60
4,7,189~5,7,189
5,2,36~7,2,36
3,6,315~3,9,315
6,8,104~6,8,106
8,1,110~9,1,110
2,8,42~2,9,42
5,9,34~7,9,34
7,0,288~7,3,288
8,8,37~9,8,37
5,7,90~5,9,90
6,4,307~6,7,307
9,5,233~9,8,233
0,2,293~0,2,294
9,2,45~9,2,45
5,5,15~7,5,15
1,2,41~3,2,41
5,0,166~5,3,166
6,5,105~6,7,105
5,3,173~8,3,173
4,6,115~4,8,115
1,1,237~1,4,237
6,5,194~9,5,194
0,7,107~0,8,107
5,1,142~6,1,142
4,4,254~4,6,254
4,6,134~6,6,134
5,4,259~5,4,261
4,3,297~4,4,297
9,3,65~9,5,65
1,3,52~2,3,52
3,5,2~3,7,2
7,2,270~7,4,270
5,4,323~5,7,323
3,1,150~3,2,150
7,0,56~7,2,56
9,0,35~9,3,35
2,3,181~2,3,184
2,7,185~5,7,185
7,7,123~8,7,123
8,4,294~8,7,294
0,0,222~2,0,222
4,0,254~5,0,254
7,2,228~7,4,228
5,1,260~5,2,260
1,3,329~3,3,329
9,5,153~9,7,153
6,7,194~8,7,194
4,4,32~4,6,32
6,9,42~8,9,42
1,7,294~1,8,294
0,7,210~0,7,211
8,8,49~8,9,49
6,0,97~6,1,97
0,6,140~1,6,140
0,7,204~3,7,204
7,9,227~9,9,227
3,2,242~3,2,243
5,0,193~7,0,193
0,5,47~0,5,50
7,9,136~9,9,136
0,4,293~0,4,297
9,5,303~9,6,303
7,4,146~7,5,146
5,2,335~7,2,335
1,9,322~4,9,322
7,7,75~7,9,75
9,9,140~9,9,141
1,3,120~3,3,120
4,1,324~4,2,324
8,7,297~8,9,297
2,6,279~4,6,279
1,4,312~1,6,312
5,1,52~5,3,52
6,5,62~9,5,62
3,6,271~3,8,271
1,2,184~4,2,184
2,7,62~5,7,62
2,2,130~3,2,130
3,0,98~6,0,98
3,7,236~4,7,236
6,3,15~9,3,15
6,1,268~7,1,268
9,3,298~9,5,298
3,4,230~3,6,230
7,3,182~7,7,182
9,3,308~9,6,308
7,9,37~7,9,39
4,5,193~4,7,193
2,3,327~2,4,327
2,8,94~4,8,94
7,1,269~9,1,269
4,5,246~4,5,250
1,5,208~1,6,208
4,1,74~6,1,74
0,2,9~3,2,9
0,4,56~0,6,56
3,9,294~5,9,294
7,0,52~9,0,52
5,6,289~5,6,290
0,3,13~0,4,13
5,1,169~7,1,169
3,5,59~3,8,59
1,4,248~1,7,248
0,4,88~2,4,88
3,1,235~3,4,235
0,3,28~0,6,28
2,9,7~3,9,7
1,8,211~1,9,211
1,5,296~3,5,296
1,8,221~2,8,221
0,8,49~0,8,52
7,0,6~7,3,6
2,5,31~4,5,31
6,5,260~6,6,260
4,4,285~7,4,285
6,4,313~8,4,313
3,3,149~3,6,149
2,6,272~4,6,272
7,1,182~9,1,182
6,4,215~9,4,215
7,1,181~7,1,181
3,6,92~3,6,92
3,7,263~6,7,263
0,0,38~1,0,38
0,4,226~0,4,228
7,1,234~7,1,234
5,8,18~8,8,18
9,4,232~9,5,232
6,3,288~6,6,288
6,3,325~7,3,325
4,2,122~4,3,122
4,1,102~4,4,102
4,1,105~5,1,105
6,8,3~6,9,3
3,1,155~6,1,155
2,3,118~2,5,118
5,5,209~8,5,209
6,1,229~6,3,229
2,4,122~4,4,122
2,8,111~2,9,111
3,5,126~3,7,126
7,9,36~9,9,36
7,0,210~9,0,210
3,2,241~5,2,241
1,7,56~1,9,56
1,7,60~1,9,60
4,2,120~4,4,120
2,7,177~4,7,177
1,2,232~2,2,232
2,0,38~2,2,38
5,9,4~7,9,4
6,5,265~6,7,265
2,8,5~4,8,5
0,0,9~2,0,9
3,7,42~3,9,42
7,1,241~7,2,241
4,7,216~7,7,216
2,8,311~5,8,311
2,1,9~3,1,9
8,4,15~9,4,15
5,3,94~5,3,97
1,0,77~3,0,77
1,9,202~5,9,202
3,6,313~3,9,313
2,8,45~4,8,45
3,4,322~5,4,322
1,3,182~1,5,182
6,3,201~9,3,201
2,5,291~2,5,292
5,7,91~5,8,91
3,0,318~5,0,318
3,1,245~3,3,245
3,7,30~3,9,30
3,4,65~3,4,67
3,8,20~6,8,20
6,3,226~9,3,226
4,0,276~4,2,276
7,9,205~9,9,205
7,8,43~9,8,43
3,8,157~3,8,160
6,6,320~9,6,320
0,7,82~0,7,82
3,6,57~5,6,57
1,7,79~4,7,79
6,2,206~6,4,206
2,0,14~2,0,17
5,1,26~7,1,26
8,4,318~8,5,318
8,5,176~8,6,176
5,5,328~7,5,328
0,0,315~3,0,315
6,7,23~6,9,23
7,1,294~7,3,294
6,1,92~6,3,92
9,1,213~9,4,213
1,0,150~1,2,150
3,2,68~6,2,68
6,5,205~6,8,205
0,6,241~2,6,241
2,5,211~4,5,211
2,7,27~2,8,27
4,9,94~7,9,94
2,6,290~4,6,290
4,3,206~4,3,208
5,2,67~8,2,67
3,7,159~5,7,159
4,6,295~6,6,295
0,8,22~0,8,24
4,1,307~6,1,307
7,8,89~9,8,89
1,7,182~2,7,182
2,9,43~3,9,43
2,1,280~2,4,280
3,8,148~5,8,148
0,6,9~2,6,9
9,4,211~9,4,211
0,7,237~0,9,237
3,5,106~3,6,106
3,1,129~5,1,129
6,1,323~6,3,323
1,4,17~1,7,17
5,5,329~5,6,329
2,7,147~2,9,147
9,7,105~9,8,105
5,7,328~5,7,329
6,2,54~7,2,54
4,6,275~7,6,275
8,3,286~9,3,286
5,0,304~5,3,304
4,2,186~6,2,186
0,7,44~0,8,44
9,4,16~9,7,16
0,2,148~3,2,148
8,3,20~8,5,20
2,0,221~2,3,221
0,0,297~0,2,297
0,5,119~2,5,119
1,3,228~1,5,228
2,5,105~2,7,105
6,6,106~8,6,106
3,2,45~3,3,45
5,6,84~5,8,84
6,4,319~8,4,319
6,0,147~8,0,147
1,0,41~1,1,41
7,7,289~7,9,289
3,7,219~5,7,219
7,7,173~9,7,173
7,5,205~9,5,205
3,5,10~3,7,10
5,4,326~5,7,326
5,2,58~5,4,58
7,5,199~7,8,199
3,0,27~5,0,27
1,3,142~1,6,142
1,2,299~1,3,299
5,6,88~5,8,88
5,2,332~5,5,332
7,9,215~8,9,215
2,0,224~5,0,224
2,3,74~2,5,74
0,2,108~2,2,108
1,8,271~2,8,271
4,1,71~4,3,71
7,3,151~8,3,151
2,5,57~2,6,57
5,5,145~5,8,145
7,6,209~8,6,209
4,3,49~7,3,49
0,1,174~2,1,174
1,2,320~3,2,320
0,4,287~2,4,287
1,2,46~4,2,46
1,7,289~1,9,289
8,6,228~8,8,228
1,3,239~1,4,239
6,6,137~6,8,137
4,0,105~6,0,105
7,0,36~7,0,39
4,5,321~4,7,321
0,9,141~2,9,141
2,4,147~5,4,147
2,2,3~2,4,3
5,2,29~5,2,30
0,5,223~0,7,223
6,6,93~6,8,93
0,4,54~3,4,54
8,3,143~8,3,143
7,5,84~8,5,84
7,7,3~7,9,3
3,5,174~3,5,177
3,8,21~5,8,21
1,6,15~1,8,15
2,3,82~2,6,82
8,6,288~8,8,288
2,2,289~2,2,289
9,0,209~9,2,209
3,0,324~6,0,324
8,0,58~9,0,58
9,1,16~9,3,16
7,3,197~7,6,197
6,9,82~8,9,82
2,3,185~3,3,185
6,1,153~6,3,153
8,2,229~8,4,229
0,2,327~2,2,327
5,3,91~8,3,91
3,4,74~5,4,74
4,8,259~7,8,259
4,0,168~7,0,168
4,4,117~4,6,117
2,3,169~5,3,169
3,0,314~5,0,314
9,7,156~9,8,156
9,6,92~9,6,93
0,2,224~0,4,224
6,3,102~7,3,102
4,8,147~6,8,147
8,4,125~8,7,125
4,0,21~4,2,21
9,1,302~9,3,302
3,2,282~4,2,282
7,3,59~7,5,59
5,6,19~5,8,19
7,7,137~8,7,137
1,0,45~2,0,45
5,7,104~9,7,104
2,5,235~2,7,235
2,0,6~2,2,6
6,4,185~7,4,185
4,2,60~6,2,60
2,8,212~5,8,212
1,9,203~2,9,203
7,4,283~9,4,283
6,4,126~8,4,126
5,7,22~7,7,22
3,3,204~6,3,204
6,5,291~9,5,291
0,7,143~0,9,143
4,6,234~4,6,236
6,6,190~8,6,190
1,0,21~2,0,21
1,0,74~3,0,74
3,1,151~3,1,154
2,2,105~4,2,105
6,6,48~8,6,48
8,4,141~8,4,143
2,6,10~2,8,10
0,9,31~3,9,31
3,7,73~5,7,73
0,3,31~0,6,31
4,5,270~6,5,270
1,7,266~3,7,266
6,1,31~8,1,31
7,8,84~7,8,87
7,1,104~7,3,104
0,8,142~0,9,142
6,4,310~8,4,310
4,0,285~7,0,285
7,7,129~7,7,132
0,9,284~1,9,284
7,4,322~8,4,322
2,4,12~2,7,12
3,5,3~5,5,3
4,2,127~4,4,127
7,9,216~9,9,216
7,6,201~9,6,201
5,5,179~8,5,179
6,0,338~6,2,338
2,6,7~5,6,7
2,2,29~2,3,29
5,1,36~7,1,36
3,2,113~3,4,113
0,4,229~0,4,232
4,1,187~4,1,189
9,0,75~9,2,75
4,6,276~6,6,276
7,4,150~7,5,150
6,6,270~8,6,270
5,5,121~6,5,121
7,7,28~7,7,28
5,0,60~8,0,60
5,4,263~5,6,263
2,8,234~4,8,234
6,3,89~6,5,89
8,6,222~9,6,222
5,5,95~8,5,95
9,0,243~9,0,244
5,4,203~7,4,203
2,7,267~2,9,267
8,3,285~8,5,285
0,7,273~0,9,273
5,5,154~5,8,154
4,9,280~6,9,280
9,1,38~9,1,41
6,0,180~6,1,180
1,8,322~3,8,322
2,2,152~2,3,152
9,2,218~9,6,218
1,9,5~1,9,6
4,8,162~6,8,162
0,5,271~0,8,271
0,2,101~0,4,101
6,7,97~6,8,97
1,2,66~1,5,66
3,7,49~6,7,49
5,7,308~5,8,308
7,3,37~9,3,37
5,3,4~5,3,5
1,3,180~1,5,180
0,0,42~2,0,42
3,1,309~3,4,309
4,5,13~6,5,13
7,6,77~7,6,79
9,1,153~9,3,153
2,2,162~4,2,162
7,2,295~9,2,295
6,6,261~6,7,261
2,5,116~5,5,116
7,1,28~7,2,28
8,1,70~8,2,70
4,4,125~4,5,125
0,7,231~1,7,231
5,6,269~8,6,269
4,2,25~4,5,25
2,9,234~4,9,234
5,8,268~7,8,268
3,4,323~3,7,323
4,1,277~4,1,279
1,3,310~1,5,310
3,8,146~4,8,146
8,7,212~8,9,212
3,3,108~3,5,108
3,7,249~6,7,249
6,0,96~6,2,96
8,6,55~8,8,55
4,2,319~4,4,319
8,4,64~8,6,64
3,0,339~6,0,339
2,5,14~2,8,14
3,4,55~3,5,55
8,1,231~8,3,231
5,4,21~6,4,21
0,0,40~0,3,40
4,7,238~5,7,238
9,0,241~9,1,241
4,9,38~5,9,38
5,7,252~5,7,256
2,6,95~2,9,95
2,6,187~2,8,187
2,0,80~5,0,80
5,1,135~7,1,135
0,1,220~0,4,220
3,0,104~5,0,104
5,9,74~7,9,74
8,7,227~8,8,227
5,1,340~7,1,340
6,7,52~6,8,52
0,4,213~2,4,213
2,1,310~2,4,310
5,4,288~5,7,288
8,1,177~8,2,177
1,0,35~5,0,35
9,5,63~9,8,63
1,2,234~2,2,234
0,9,204~1,9,204
7,1,10~7,2,10
3,5,91~3,8,91
8,4,85~8,5,85
0,3,83~0,6,83
7,1,148~7,4,148
3,8,96~3,8,98
2,7,218~4,7,218
1,4,135~1,6,135
7,4,280~7,6,280
2,6,223~3,6,223
6,0,171~9,0,171
3,1,325~3,4,325
6,7,100~8,7,100
6,1,56~6,3,56
3,4,68~3,4,69
8,1,257~8,4,257
7,5,260~7,5,260
7,0,51~7,3,51
6,5,316~8,5,316
4,4,296~6,4,296
5,1,243~5,2,243
1,2,230~3,2,230
0,3,314~2,3,314
9,2,79~9,4,79
9,2,202~9,3,202
0,4,298~0,6,298
0,5,92~3,5,92
7,6,172~7,8,172
0,1,193~0,4,193
9,4,302~9,7,302
3,1,247~3,1,249
6,3,11~7,3,11
4,6,250~6,6,250
3,5,222~6,5,222
4,2,231~6,2,231
4,4,114~4,7,114
0,6,11~1,6,11
1,7,90~1,8,90
1,3,155~1,4,155
1,4,89~3,4,89
1,1,27~3,1,27
3,1,58~5,1,58
6,3,8~6,4,8
6,5,255~6,8,255
3,6,292~3,9,292
1,5,294~2,5,294
0,2,48~2,2,48
3,9,204~5,9,204
1,9,283~4,9,283
0,9,33~0,9,35
8,3,218~8,6,218
1,2,186~1,4,186
5,0,65~7,0,65
2,5,142~2,6,142
7,9,137~9,9,137
5,6,175~8,6,175
6,7,258~6,9,258
4,0,146~6,0,146
7,6,236~8,6,236
8,0,11~8,0,13
5,7,258~5,8,258
0,4,277~3,4,277
2,7,222~4,7,222
1,3,317~3,3,317
0,8,41~3,8,41
5,4,254~7,4,254
9,1,216~9,1,218
2,3,5~2,6,5
7,9,290~7,9,292
7,6,291~9,6,291
6,7,219~6,9,219
4,4,162~4,6,162
4,6,161~4,9,161
0,8,21~2,8,21
5,3,223~6,3,223
2,3,38~2,5,38
3,3,220~6,3,220
1,5,19~1,8,19
0,3,176~1,3,176
2,1,159~4,1,159
6,2,238~9,2,238
3,5,153~5,5,153
0,4,20~2,4,20
5,6,279~7,6,279
3,6,69~3,8,69
0,7,320~4,7,320
9,0,240~9,2,240
2,9,27~5,9,27
4,7,70~8,7,70
0,0,113~0,2,113
1,5,132~1,7,132
6,5,18~6,6,18
4,3,33~4,5,33
6,7,310~6,9,310
7,4,206~7,7,206
2,9,5~4,9,5
4,4,317~4,6,317
0,8,296~1,8,296
0,0,114~0,2,114
4,1,47~4,3,47
0,1,292~0,2,292
1,7,221~4,7,221
1,5,129~3,5,129
1,8,93~3,8,93
2,4,212~6,4,212
4,4,194~4,5,194
2,3,249~2,5,249
4,3,250~6,3,250
1,7,200~1,9,200
9,2,76~9,4,76
4,0,30~4,1,30
6,9,83~6,9,85
6,7,266~6,7,269
2,5,209~3,5,209
5,6,166~5,8,166
2,8,189~4,8,189
7,6,294~7,7,294
0,3,179~3,3,179
7,0,102~9,0,102
7,1,76~9,1,76
5,7,221~5,7,223
2,5,304~2,8,304
7,4,202~9,4,202
7,1,138~7,3,138
6,7,83~9,7,83
3,7,250~4,7,250
6,9,261~7,9,261
1,2,153~1,5,153
3,2,62~3,5,62
0,4,215~0,4,217
2,7,107~2,9,107
8,3,256~8,4,256
3,6,155~3,8,155
2,2,237~5,2,237
3,7,72~6,7,72
0,9,287~2,9,287
6,9,103~8,9,103
4,2,273~4,5,273
3,1,28~3,2,28
0,4,290~0,5,290
4,3,3~7,3,3
2,1,224~3,1,224
0,1,324~0,4,324
6,5,252~6,7,252
7,8,306~9,8,306
8,5,86~8,7,86
1,5,205~4,5,205
1,3,63~3,3,63
4,9,295~6,9,295
6,1,34~6,3,34
9,0,307~9,2,307
7,3,269~7,5,269
7,1,170~7,1,172
6,4,299~7,4,299
7,9,30~9,9,30
3,4,171~3,6,171
9,5,108~9,8,108
0,2,314~2,2,314
5,5,22~6,5,22
9,2,229~9,4,229
6,3,315~8,3,315
7,2,174~7,4,174
4,5,220~4,8,220
0,2,46~0,5,46
0,7,106~2,7,106
4,2,279~7,2,279
6,9,171~7,9,171
0,5,78~3,5,78
2,7,302~4,7,302
3,6,152~5,6,152
7,4,221~9,4,221
8,3,234~8,6,234
0,1,190~2,1,190
3,7,67~5,7,67
4,2,2~4,3,2
2,8,144~4,8,144
0,6,204~3,6,204
9,5,70~9,5,74
8,4,230~8,4,230
5,1,138~5,1,140
9,2,66~9,4,66
4,4,198~4,4,201
4,2,181~6,2,181
9,2,13~9,5,13
2,3,274~2,5,274
3,6,175~3,8,175
6,2,93~8,2,93
4,7,280~6,7,280
3,5,316~3,6,316
9,2,221~9,2,223
7,1,305~9,1,305
3,6,95~4,6,95
3,6,231~4,6,231
6,4,186~8,4,186
0,1,42~0,3,42
2,6,139~2,9,139
0,4,51~2,4,51
9,2,242~9,2,243
6,5,31~9,5,31
3,9,92~7,9,92
1,3,141~3,3,141
8,6,220~8,7,220
6,2,175~8,2,175
4,7,186~5,7,186
6,7,193~9,7,193
2,1,313~2,4,313
7,9,95~9,9,95
7,5,213~7,7,213
3,5,301~4,5,301
7,7,133~7,9,133
6,4,258~6,4,261
0,7,110~0,9,110
9,5,152~9,7,152
7,5,103~9,5,103
3,3,98~5,3,98
6,6,223~8,6,223
2,0,37~2,3,37
5,2,324~6,2,324
5,9,32~8,9,32
9,1,71~9,3,71
4,5,27~4,6,27
5,0,183~5,2,183
6,6,96~7,6,96
0,6,138~2,6,138
3,6,178~5,6,178
6,8,48~8,8,48
7,2,100~9,2,100
2,7,220~2,8,220
3,1,37~6,1,37
2,6,128~4,6,128
0,2,30~0,4,30
6,7,128~8,7,128
8,4,2~8,6,2
3,0,323~3,2,323
0,2,59~0,4,59
0,3,49~0,4,49
3,4,151~4,4,151
3,1,186~4,1,186
3,1,158~5,1,158
4,4,16~4,6,16
5,6,148~7,6,148
2,3,247~2,5,247
2,7,210~2,9,210
0,1,110~0,3,110
0,2,1~0,4,1
5,5,16~5,8,16
2,2,286~2,5,286
5,6,267~5,8,267
4,2,239~4,4,239
5,0,286~5,0,288
5,5,93~8,5,93
5,2,235~5,4,235
1,9,207~1,9,208
3,0,60~3,1,60
7,1,49~9,1,49
4,5,192~7,5,192
3,4,314~6,4,314
0,8,17~2,8,17
8,6,239~8,7,239
6,4,255~8,4,255
0,9,2~2,9,2
4,1,274~4,3,274
3,7,4~3,9,4
2,1,217~2,3,217
3,7,165~6,7,165
4,5,267~6,5,267
6,2,179~6,3,179
2,0,167~2,2,167
5,0,341~7,0,341
5,1,66~7,1,66
3,6,194~4,6,194
1,0,302~1,2,302
3,7,319~3,9,319
5,3,134~7,3,134
2,8,142~3,8,142
6,0,38~6,1,38
3,7,197~5,7,197
4,2,243~4,5,243
8,0,56~8,2,56
1,7,92~3,7,92
3,3,51~5,3,51
6,3,290~6,3,291
2,4,72~4,4,72
1,6,222~3,6,222
5,9,28~7,9,28
7,0,177~7,2,177
4,6,188~7,6,188
6,9,79~8,9,79
2,5,55~2,6,55
7,6,151~9,6,151
5,2,37~5,2,40
2,3,86~2,6,86
3,6,22~5,6,22
0,0,11~2,0,11
0,1,43~0,2,43
0,1,223~0,1,223
7,8,21~8,8,21
9,6,5~9,8,5
2,5,103~5,5,103
6,0,62~8,0,62
5,2,62~5,3,62
7,9,207~9,9,207
3,4,169~6,4,169
0,4,26~0,6,26
1,7,326~3,7,326
4,1,185~6,1,185
7,0,34~7,2,34
1,8,324~1,8,326
6,4,19~8,4,19
5,6,119~5,8,119
0,1,188~0,4,188
6,7,54~8,7,54
6,7,101~6,9,101
6,2,291~8,2,291
3,7,275~3,9,275
4,5,120~6,5,120
3,2,206~3,4,206
2,4,243~2,7,243
4,2,100~4,5,100
5,5,225~7,5,225
2,9,274~5,9,274
8,1,272~8,1,273
4,8,48~4,9,48
2,7,318~3,7,318
8,1,81~9,1,81
3,7,210~6,7,210
2,0,170~2,0,170
0,0,285~0,2,285
4,8,260~6,8,260
1,2,165~3,2,165
3,4,233~5,4,233
2,4,226~2,6,226
5,0,187~8,0,187
6,2,134~9,2,134
0,3,81~0,5,81
3,7,116~4,7,116
5,5,220~5,7,220
6,6,120~6,9,120
2,7,186~2,9,186
8,7,71~8,9,71
9,0,32~9,3,32
1,1,195~1,1,197
3,5,76~3,8,76
0,0,287~0,2,287
8,4,138~8,7,138
4,7,120~4,8,120
7,2,236~9,2,236
7,1,39~7,3,39
7,0,8~8,0,8
4,3,217~4,7,217
5,9,78~7,9,78
7,6,219~7,8,219
8,6,89~8,6,92
1,0,68~1,3,68
8,2,111~9,2,111
1,9,324~3,9,324
6,6,183~6,6,185
7,6,140~7,8,140
8,7,242~9,7,242
3,5,202~7,5,202
0,0,187~0,3,187
4,6,29~4,7,29
6,0,189~7,0,189
7,2,29~9,2,29
2,0,19~4,0,19
2,7,23~5,7,23
5,8,40~7,8,40
2,5,299~2,7,299
2,4,214~2,6,214
0,4,58~0,6,58
2,0,177~2,1,177
5,5,17~5,5,20
6,3,317~6,3,320
5,2,258~8,2,258
4,7,331~5,7,331
3,2,124~3,5,124
4,9,276~5,9,276
4,2,322~7,2,322
7,0,57~7,0,59
2,0,33~4,0,33
1,1,123~1,3,123
1,3,308~3,3,308
5,5,104~8,5,104
2,1,14~2,2,14
0,5,106~2,5,106
4,4,190~4,6,190
1,2,27~5,2,27
1,2,147~4,2,147
5,3,246~5,4,246
6,4,181~6,6,181
0,0,230~3,0,230
4,0,36~6,0,36
4,1,32~5,1,32
1,5,41~3,5,41
0,2,150~0,3,150
3,9,97~5,9,97
8,3,312~8,5,312
9,8,225~9,9,225
5,4,324~5,5,324
3,7,277~6,7,277
3,5,291~5,5,291
0,1,70~3,1,70
2,7,306~6,7,306
2,9,114~3,9,114
5,3,182~5,5,182
6,5,174~7,5,174
1,0,173~1,3,173
6,6,149~7,6,149
0,0,283~0,2,283
7,3,286~7,6,286
1,1,239~1,2,239
0,6,46~0,8,46
6,6,225~7,6,225
0,6,49~0,6,49
0,8,291~1,8,291
6,8,4~9,8,4
6,5,315~8,5,315
7,5,82~7,8,82
4,0,101~6,0,101
5,4,301~7,4,301
2,4,174~4,4,174
5,0,176~7,0,176
0,7,294~0,9,294
1,2,138~1,4,138
0,5,80~0,7,80
1,2,311~3,2,311
0,4,98~0,7,98
0,0,44~2,0,44
2,1,283~2,2,283
2,8,66~5,8,66
5,0,3~5,2,3
7,5,121~7,8,121
9,3,100~9,5,100
7,0,68~8,0,68
3,6,251~4,6,251
1,3,143~1,6,143
6,5,258~7,5,258
4,0,236~7,0,236
4,6,81~7,6,81
1,4,201~1,8,201
4,7,179~6,7,179
1,5,271~4,5,271
9,1,44~9,1,46
2,1,239~5,1,239
3,6,111~5,6,111
7,6,74~7,8,74
0,2,181~0,3,181
7,3,152~9,3,152
6,0,143~6,2,143
2,2,91~2,4,91
8,5,30~9,5,30
1,1,191~1,3,191
2,5,28~5,5,28
5,3,302~5,6,302
9,1,245~9,3,245
8,2,98~8,4,98
7,3,227~7,4,227
2,6,114~3,6,114
4,0,173~7,0,173
4,8,87~6,8,87
0,5,94~0,5,96
3,4,97~3,6,97
6,5,2~6,5,5
0,8,268~3,8,268
1,0,304~1,1,304
5,7,157~8,7,157
2,3,186~5,3,186
4,0,40~4,0,40
0,5,270~0,8,270
1,2,56~5,2,56
1,5,59~1,7,59
6,4,216~6,4,218
4,0,251~7,0,251
2,3,81~2,5,81
1,1,193~1,1,193
3,5,208~5,5,208
3,3,210~4,3,210
6,0,145~7,0,145
6,4,68~9,4,68
8,7,102~8,9,102
7,4,267~8,4,267
2,2,144~2,4,144
3,1,127~3,3,127
5,4,256~5,5,256
8,8,210~8,9,210
3,6,172~3,9,172
1,6,239~4,6,239
4,5,168~4,8,168
0,0,280~4,0,280
3,9,293~5,9,293
3,0,81~5,0,81
7,8,220~7,8,222
4,3,132~4,6,132
8,0,172~8,1,172
5,9,203~8,9,203
1,5,246~3,5,246
0,8,88~4,8,88
8,3,140~8,6,140
2,1,219~2,4,219
2,7,195~4,7,195
6,3,273~8,3,273
2,1,236~4,1,236
6,5,289~6,7,289
0,3,222~0,5,222
5,3,170~5,3,170
4,5,235~7,5,235
1,8,3~1,8,5
3,4,184~3,4,186
3,4,278~3,6,278
9,2,47~9,2,49
2,3,215~2,5,215
5,2,8~8,2,8
2,4,22~2,4,25
9,1,208~9,4,208
0,3,11~2,3,11
3,1,313~3,1,315
6,0,58~6,1,58
6,3,12~9,3,12
6,8,224~9,8,224
5,6,101~7,6,101
0,2,317~1,2,317
9,7,303~9,9,303
1,1,109~1,2,109
4,0,179~6,0,179
7,5,57~7,8,57
4,4,293~4,6,293
1,8,12~3,8,12
3,7,278~3,9,278
0,1,231~0,3,231
7,0,308~7,1,308
6,1,267~6,4,267
4,3,156~4,6,156
7,1,179~9,1,179
4,1,154~6,1,154
1,8,18~2,8,18
9,2,17~9,4,17
8,3,94~8,5,94
7,7,27~9,7,27
2,3,27~2,6,27
0,2,139~1,2,139
0,3,323~2,3,323
0,7,140~2,7,140
7,0,27~7,2,27
7,0,146~9,0,146
5,1,65~5,4,65
5,0,249~5,3,249
9,5,109~9,7,109
7,5,144~7,8,144
7,3,199~7,4,199
'''

# COMMAND ----------

import re


def get_points(x1, y1, x2, y2):
  s = set()
  for x in range(x1, x2 + 1):
    for y in range(y1, y2 + 1):
      s.add((x, y))
  return s


def get_supports(i, bricks):
  x1, y1, z1, x2, y2, z2 = bricks[i]
  z1 -= 1
  z2 -= 1
  ps = get_points(x1, y1, x2, y2)

  sups = set()
  for i2 in range(i):
    bx1, by1, bz1, bx2, by2, bz2 = bricks[i2]
    if bz2 != z1: # The bottom of the ith brick needs to have the same z as the top of the lower brick
      continue
    if get_points(bx1, by1, bx2, by2).intersection(ps):
      sups.add(i2)
  
  return sups


X1, Y1, Z1, X2, Y2, Z2 = range(6)
bricks = [[int(num) for num in re.findall(r'-?[0-9]+', line)] for line in inp.splitlines()]
bricks.sort(key=lambda brick: brick[2])
supports = {}

for i, _ in enumerate(bricks):
  sups = []
  while bricks[i][Z1] > 1 and not (sups := get_supports(i, bricks)):
    bricks[i][Z1] -= 1
    bricks[i][Z2] -= 1
  supports[i] = sups

brick_ids = set(range(len(bricks)))
cannot_remove = {next(iter(s)) for s in supports.values() if len(s) == 1}
can_remove = brick_ids.difference(cannot_remove)
answer = len(can_remove)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Disintegrating bricks one at a time isn't going to be fast enough. While it might sound dangerous, what you really need is a <em>chain reaction</em>.</p>
# MAGIC <p>You'll need to figure out the best brick to disintegrate. For each brick, determine how many <em>other bricks would fall</em> if that brick were disintegrated.</p>
# MAGIC <p>Using the same example as above:</p>
# MAGIC <ul>
# MAGIC <li>Disintegrating brick <code>A</code> would cause all <code><em>6</em></code> other bricks to fall.</li>
# MAGIC <li>Disintegrating brick <code>F</code> would cause only <code><em>1</em></code> other brick, <code>G</code>, to fall.</li>
# MAGIC </ul>
# MAGIC <p>Disintegrating any other brick would cause <em>no other bricks</em> to fall. So, in this example, the sum of <em>the number of other bricks that would fall</em> as a result of disintegrating each brick is <code><em>7</em></code>.</p>
# MAGIC <p>For each brick, determine how many <em>other bricks</em> would fall if that brick were disintegrated. <em>What is the sum of the number of other bricks that would fall?</em></p>
# MAGIC </article>

# COMMAND ----------

fall_counts = []
for candidate in cannot_remove:
  fallen = set([candidate])
  for _ in range(10):
    for i, s in supports.items():
      if bricks[i][Z1] == 1:
        continue
      if not s.difference(fallen):
        fallen.add(i)
  
  fall_counts.append(len(fallen) - 1)

answer = sum(fall_counts)
print(answer)