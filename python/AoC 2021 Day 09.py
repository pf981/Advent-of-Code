# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 9: Smoke Basin ---</h2><p>These caves seem to be <a href="https://en.wikipedia.org/wiki/Lava_tube" target="_blank">lava tubes</a>. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly <span title="This was originally going to be a puzzle about watersheds, but we're already under water.">settles like rain</span>.</p>
# MAGIC <p>If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).</p>
# MAGIC <p>Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:</p>
# MAGIC <pre><code>2<em>1</em>9994321<em>0</em>
# MAGIC 3987894921
# MAGIC 98<em>5</em>6789892
# MAGIC 8767896789
# MAGIC 989996<em>5</em>678
# MAGIC </code></pre>
# MAGIC <p>Each number corresponds to the height of a particular location, where <code>9</code> is the highest and <code>0</code> is the lowest a location can be.</p>
# MAGIC <p>Your first goal is to find the <em>low points</em> - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)</p>
# MAGIC <p>In the above example, there are <em>four</em> low points, all highlighted: two are in the first row (a <code>1</code> and a <code>0</code>), one is in the third row (a <code>5</code>), and one is in the bottom row (also a <code>5</code>). All other locations on the heightmap have some lower adjacent location, and so are not low points.</p>
# MAGIC <p>The <em>risk level</em> of a low point is <em>1 plus its height</em>. In the above example, the risk levels of the low points are <code>2</code>, <code>1</code>, <code>6</code>, and <code>6</code>. The sum of the risk levels of all low points in the heightmap is therefore <code><em>15</em></code>.</p>
# MAGIC <p>Find all of the low points on your heightmap. <em>What is the sum of the risk levels of all low points on your heightmap?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''5796798621237995498765434567987542999765679987545679109878999877899789876532123456998999876887899921
4645976434456789349654321298997679898654698987635678998767897656789698765432012347897899865676798799
3234987545978993298795410989998989789543256897646789498756789546896579877842123456976789954345985678
4356798679989999019987329878999798679765345689856991296545890134789467998956899967895698643239874579
6467999789999898934976598967987676568996457999967999987636789345691346789769987898934987651098763456
7598997999987796899989987959876543456789569898998998765125678956910298899898776799123998862987652345
8789876789865685578999876645987665567998689656789876554034899999891989998987564679099789879876543456
9898765498974324456799865534598786788998798645889985432126954987789878987654323567988698989987664678
9989997987543212367987654323459897899549895434569876556437899876599967996543212459876587898998798789
9877989997662101456798765434567998967932987624778989787548999989679459987687301349875456967899899893
8765678998983232367899896765788939346891295434999999899659879699894349899796532656954344756910923964
9874789019894343456789949878999321235799987545678945998778964578942139769898543769843212345891949765
7965678998765764567893433989876542346987898656789236799889653989943298652999678989754523456789898976
6598789109976975698921012398999763457896559867997647989998799899874569541098799798765676579896687897
5439898929989989789962123457899894568989435998998799878999989798765798432149898649987787899965456989
5212987898999999899854336568999989879979326569109989567898879689878987544234995434599898999874345679
4309875987999876998765687679989878998765412458929875467987854599989698955679989323459979899993214589
5996954676799984329877788989878969899874324567899765359876743489996549877789878912398767789984323456
9875432545789743212989899998967659789985595678998868249965312679865435998898767899598954698765467567
2994321036897654101996936987654543679999989789997854198764301569979423459999954678997643789978578978
0987432128998763219875424698763212478998978999876543298773212458998901267898767889598732345988789989
9876544346789979329876512349998401569897569234987994987654343457897892478999878993349891234899998695
9989875679899898939984701459886212398786456946799889998795464567896789989896999321234989345678987544
9997987889998797998743212598765323987654397899989778999989978679945698999765678930349878956999898433
8986798999987676789655329679876439876541289998878656899867898791239956799954345959499867897899765321
7845679219878565678976598999987556998732378997667545798656789892398745999765237898987656789998654310
6434798998765454567897987898798677899543467896553234987545878989499636878992156987975345899219964324
0123987999874343456789876799549789987654598998421056989434767879976521767989249876543234998909878434
4339876798955102367898985678939891099967899876542159875323854568965410156978956997684456797899989545
5498765986543234488987894799012999129878999987653249986210123467894321249769767898795867956789199656
6599754397654545589996789899993998949999998799767998975351237998995432398758998989986788946999098789
7988732198765657678975698999879876898946999544979877989876456789987643459647899876097899534878999899
9876546019878767889984567899968765667939896532989966592987887893298754598756789965198997323456799989
0998757898989899992099789988754543457898789540199854301298998984129866789998999954249986412345899878
1299898987699954954299999876543212348987698921598763212349999873234977995679439765356897601234988767
2989999876569999895989986987654103467896567892349854334568989964345698934678921976897996532349875756
9879899988698988789878995498976215989995456789498999965689879899456789323567890197998987656756994345
8765677899987677697667896329865423499989997995987878897798768778968895438678991298969398967899873201
8654546789766563459548994219876534578977789104986567789949654567899976657899789349543219988932965412
8643437899854312998435689101987645689665679323975345678959868778957987798934679959654301299549876723
6532126778969409876424578912498756796553568939863203456899979989646799899012567898976432358956987894
8544434567998912998535689843569867989432459949954212568999989594535798989123467987976563567969799985
9655566789897893479697897654567979879421267898767343467898795443123497679935679876899674789997659876
9776789998656799567989998765678998967992349929876556578987654321012989567896798765678985999876642989
9988899875434678979878999879889987657889458919997967689798865452199867456987987654567896798765431096
8799943989545789999868799989999876545678967898789898797659979874987654347899999753459987979876532145
7679969998656789987657678994323965432789979987679789896535989995998321234568939894567899764987687236
7567898959767893976543467995909876645678989996545678965423599989899754359679421986789968973199875345
3467987644978912987784989879899987856789999987434569653213679876789866468789439898993459792012989466
6569999533989999798896797867789898987897999876424678962102398765898977578996598769322375679933496578
8678998921296789679987896545698769399986789764312398993923499654567897689398999954201234567894987689
9799867890145679542998987896789954234995698765101256789894987543458999791249899895312347899995798789
2988656891237789869879998998996895999876789864212345996789987652377899910299756789436556799989999890
3977545789347899998767899989434999879989898987423467895678993210466789321987645679987867989767899921
9865437896556789999946799876545998767999987976534789954589997621245679459876437898798979876545978943
9976545789697899987834689989699767656899876989675678932679876432556789598943218997659989765434567894
9989867899989999986545678995987654545998965498797889321996997543457898797654323789943596986546789965
8896978999879878997668789213986543234987894349898996549875698665678909998965534567892345697656798987
7645989898765655689779898901987662129876789234989998698954539987899919879877645689931257898767967899
9869998789964334578995937892397654398945689345678979987643012398967898767998776798890234999898957898
6998789679892123457894325943498765987834568956889467898952134579656899656549887897789656799999546457
5987654597651012349975434799579989865423567897992378999763245678947999743435998996549767987989432347
4398753299843123457896545678992099654512455789209989398754356789439879842124999987638989876678954456
1239854987653238768998956999989298743101234678998994298765768899598765431029892196547898965466795567
0123995799768545678969869878979349543213455789997899109976779998789987532139789987656987654345789979
3235986999879656789756999867668956975434696899986987912987899999894697643298678999987898543234567898
9945799876998798897645987654456899876595989989765976899998999886989987659987567998998999864365788977
8799895995439899986534598732367968988989878979954695678919998785468998798766456997899898765479899766
5678923994323999876545987543478957999976556767893254589101987674378789899854349876799649876678987645
4567919876214899987689998954989546898765432356789123678919986543245679998765467965678999987789298756
3467898765436789998998999879995434999896521237895019789998997532135998899977569876789988798992109867
2369929876545699999987899999876545689943210235994298999997989949239876789989778989899976569993298989
3458910997676789899876989212987676899656432346789987889886979898949965679999899998998665478989987897
4567899998787895798765678923598789998789545497899996779765765787898764567878921987999543289567976546
6878978999898934989894569654589890249899876569999884568954654656989843458967899876998992123458997997
7989569899919129878989678979678931239964998978998763477943212349879932123458998765876789012567919989
8991356779909019767678989989899842498643239989987542356799302345965431014568919954345692139898929879
9410124567898998654567891294998753679654134699876521245678913459876432323589109765457789256799598767
4321267898987549876899910123987654598763245698776410234569865567997943434578999988767899767895349654
6532356789876434987898943235698765679854659987654321345678976778999894565689989999878949878943298765
7656467893987545998967896545699887998767998998765432456889988999998789689789878989999432989752129976
8767589954899756899459987756989998919879897899876548668994599989987678999898769878997643496543234988
9879678975798967987598999899878959102998766999988767899123678978986567894987653967898765789759449999
2989789996987898998987899954969643213459945789799878943239989865454478923986542656949896899898998931
1299899989776999129976899769878965425678996999656989965398798754342349435965421248956997899987687899
0467999876545789098865689879989876566789987898768997897987659983210456949878543367899898999876546797
2378988965434678987674778998999998987893598999879876798965434975672569898987665456789789998695435896
4499877994323569876523467897988999999912459999989965689896323497883479767999787578995679876564326345
9987656789212489986313568966767897899106598989999984878789212598965998956799898989664868975432101234
8798878994323478965423459954456986798919987678999873165678943679879876545689939996543459876875212345
9659989765434568976796567893299765987898765569898762054567894578998765434696549987654667998994323476
8934599879876899997898879954987654496987654346789943123489965679539854323589998998767898989889456567
7895678998987899998999998769876543345798765767898894344567896789329875434567897689998999878778967678
6796989987698969799998789878998632134899878998946799465679987898919987645679976578999098767669898799
5789995799549347689987678999986721023999999769434878987989998967898998767989787459989298653456789910
4567894698432134567988566789875432335698798653212967999997859456987679878998643212578987832345679891
3779992976553235679977455698998765487987689864343458999876543237897569989797652101459876543456789789
9889689987664346798765323456789887569876598765454569986987652145789698795698768892368987956567895678
4994567899865457999974313345699998798765439879875678955698767234999987654229878765456799767878934589
2123456999876567899875101256789109999984321989989899543249878945678996542101989877667899878989123699'''

# COMMAND ----------

import collections

heatmap = collections.defaultdict(
  lambda: 9,
  {
    (row, col): int(value)
    for row, line in enumerate(inp.splitlines())
    for col, value in enumerate(line)
  }
)

low_points = {
  (row, col): value
  for (row, col), value in heatmap.copy().items()
  if all(heatmap[(row + dr, col + dc)] > value for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)])
}

answer = sum(value + 1 for value in low_points.values())
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Next, you need to find the largest basins so you know what areas are most important to avoid.</p>
# MAGIC <p>A <em>basin</em> is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height <code>9</code> do not count as being in any basin, and all other locations will always be part of exactly one basin.</p>
# MAGIC <p>The <em>size</em> of a basin is the number of locations within the basin, including the low point. The example above has four basins.</p>
# MAGIC <p>The top-left basin, size <code>3</code>:</p>
# MAGIC <pre><code><em>21</em>99943210
# MAGIC <em>3</em>987894921
# MAGIC 9856789892
# MAGIC 8767896789
# MAGIC 9899965678
# MAGIC </code></pre>
# MAGIC <p>The top-right basin, size <code>9</code>:</p>
# MAGIC <pre><code>21999<em>43210</em>
# MAGIC 398789<em>4</em>9<em>21</em>
# MAGIC 985678989<em>2</em>
# MAGIC 8767896789
# MAGIC 9899965678
# MAGIC </code></pre>
# MAGIC <p>The middle basin, size <code>14</code>:</p>
# MAGIC <pre><code>2199943210
# MAGIC 39<em>878</em>94921
# MAGIC 9<em>85678</em>9892
# MAGIC <em>87678</em>96789
# MAGIC 9<em>8</em>99965678
# MAGIC </code></pre>
# MAGIC <p>The bottom-right basin, size <code>9</code>:</p>
# MAGIC <pre><code>2199943210
# MAGIC 3987894921
# MAGIC 9856789<em>8</em>92
# MAGIC 876789<em>678</em>9
# MAGIC 98999<em>65678</em>
# MAGIC </code></pre>
# MAGIC <p>Find the three largest basins and multiply their sizes together. In the above example, this is <code>9 * 14 * 9 = <em>1134</em></code>.</p>
# MAGIC <p><em>What do you get if you multiply together the sizes of the three largest basins?</em></p>
# MAGIC </article>

# COMMAND ----------

def get_basin_size(row, col, heatmap, visited):
  if (row, col) in visited or heatmap[(row, col)] == 9:
    return 0
  
  visited.add((row, col))
  return 1 + sum(get_basin_size(row + dr, col + dc, heatmap, visited) for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)])

basin_sizes = [get_basin_size(row, col, heatmap, set()) for row, col in low_points]
largest_basin_sizes = sorted(basin_sizes)[-3:]

answer = largest_basin_sizes[0] * largest_basin_sizes[1] * largest_basin_sizes[2]
print(answer)
