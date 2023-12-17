# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/17

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 17: Clumsy Crucible ---</h2><p>The lava starts flowing rapidly once the Lava Production Facility is operational. As you <span title="see you soon?">leave</span>, the reindeer offers you a parachute, allowing you to quickly reach Gear Island.</p>
# MAGIC <p>As you descend, your bird's-eye view of Gear Island reveals why you had trouble finding anyone on your way up: half of Gear Island is empty, but the half below you is a giant factory city!</p>
# MAGIC <p>You land near the gradually-filling pool of lava at the base of your new <em>lavafall</em>. Lavaducts will eventually carry the lava throughout the city, but to make use of it immediately, Elves are loading it into large <a href="https://en.wikipedia.org/wiki/Crucible" target="_blank">crucibles</a> on wheels.</p>
# MAGIC <p>The crucibles are top-heavy and pushed by hand. Unfortunately, the crucibles become very difficult to steer at high speeds, and so it can be hard to go in a straight line for very long.</p>
# MAGIC <p>To get Desert Island the machine parts it needs as soon as possible, you'll need to find the best way to get the crucible <em>from the lava pool to the machine parts factory</em>. To do this, you need to minimize <em>heat loss</em> while choosing a route that doesn't require the crucible to go in a <em>straight line</em> for too long.</p>
# MAGIC <p>Fortunately, the Elves here have a map (your puzzle input) that uses traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>2413432311323
# MAGIC 3215453535623
# MAGIC 3255245654254
# MAGIC 3446585845452
# MAGIC 4546657867536
# MAGIC 1438598798454
# MAGIC 4457876987766
# MAGIC 3637877979653
# MAGIC 4654967986887
# MAGIC 4564679986453
# MAGIC 1224686865563
# MAGIC 2546548887735
# MAGIC 4322674655533
# MAGIC </code></pre>
# MAGIC <p>Each city block is marked by a single digit that represents the <em>amount of heat loss if the crucible enters that block</em>. The starting point, the lava pool, is the top-left city block; the destination, the machine parts factory, is the bottom-right city block. (Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)</p>
# MAGIC <p>Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move <em>at most three blocks</em> in a single direction before it must turn 90 degrees left or right. The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.</p>
# MAGIC <p>One way to <em>minimize heat loss</em> is this path:</p>
# MAGIC <pre><code>2<em>&gt;</em><em>&gt;</em>34<em>^</em><em>&gt;</em><em>&gt;</em><em>&gt;</em>1323
# MAGIC 32<em>v</em><em>&gt;</em><em>&gt;</em><em>&gt;</em>35<em>v</em>5623
# MAGIC 32552456<em>v</em><em>&gt;</em><em>&gt;</em>54
# MAGIC 3446585845<em>v</em>52
# MAGIC 4546657867<em>v</em><em>&gt;</em>6
# MAGIC 14385987984<em>v</em>4
# MAGIC 44578769877<em>v</em>6
# MAGIC 36378779796<em>v</em><em>&gt;</em>
# MAGIC 465496798688<em>v</em>
# MAGIC 456467998645<em>v</em>
# MAGIC 12246868655<em>&lt;</em><em>v</em>
# MAGIC 25465488877<em>v</em>5
# MAGIC 43226746555<em>v</em><em>&gt;</em>
# MAGIC </code></pre>
# MAGIC <p>This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only <code><em>102</em></code>.</p>
# MAGIC <p>Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, <em>what is the least heat loss it can incur?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''233244231122553122525413454522354135462222326535344662264544223642652255336664663346353252645466356456462435622214553413332454432211214411143
223141234553125225554452413445222253233246635553325226333542552424263422323666243555565625352563233242463262245343212134422111434232123132432
222211241414332422353143154123232224435622425635432542244626326352546424262544336555243322432452265334323634435625353134233211423335325223333
322232223424242153454434322156223244543255665445556362542353232362553242363465623353356322354425466433346323664633124432225444231511234544333
332334545315334114453243332464466364433664255323465255433565444463354334373422362334624463322442462434232264664443442124112355243442414251234
133242121141341224224443146434432622365634323533462456343364634763756335446443456442433652326466222624526234652633644454443153343412234115322
242111232112124242412443465234554263455236425536235434654756753344376453734466455435654443663636234535423533255364633332435354221345432131332
334124233122435421244334545423235454235234226263534536466575566753354475654773667473734745556556553464464266456224322665345422331434452231141
243223315411111451244356366462432364552556662462264547566444575463455364744746675765673333337763436424643625333252343225253232544524352423331
144524212211331535513566546435422255553524423345447556774457553555563373554557766774556766545447333542362354662325562465252451325524314232511
435521114224413334453546253526535655234455245563465555546537665674435746456456573644466575353564753546632222233354542466433421132325235415124
443122134353315433453536336522526545262256444775735576745345475457663763633476754434565463374734556476656335526423425662456622151554525514153
254344545432133514243555454223344344344235434463453346553366743433475674736654344567353475374734636335563522344434534622445663435524554314435
555543211152424432235242543642646452246566537346745634647653544445537433437536757644565337343433776537374346323654224635525253242541414151234
224532344111341335623565634332235565476535353637575633544547664764464765554546746644433363336643654577433753635452525665463423355325244315534
332423132323256224435255244455363437475376445775644433674675674777636333563774756654674346447646477765355663252522553244336246432453321343113
523325351342563622233264426223646764743735776737446465346653637633366367763454537463637556665377354755465754564353426542533534645655455424124
543515321451323355352442453662524443777435667774765547544657675477646344663644473465676775755755376664436467345233664335654456566364114314515
524544331415433342453636265422447355454554354733444735373767667665576644845687853773673574376363543547347656437465554666252332235222341243542
334422354525542664452562352245656563756355654454535464446654754477586464875666884786776674577537465676556774676365446263346423446443414312332
554115234546226433636644546564664575467746674764646336547486746446564645874746758585786836444746767667435546456336636253643265363445353134113
555523412332545442255666524563773567545656376433463368678578788677866678474578567567884668475434446453564663553575554532364422655643542535445
535551115322532533552622566677754647676633654656374566574746868448854776774467746575584574578653455667646536345365765623463333656546554115332
352152455642246446646554247744444775673445334645447867886678584565565588657564888557565786655586555475555364566346573722442243256646262452354
124252324554445242456263746376346333645753364455887777578566877656677688584768887558456756575868453446576473476456737734222236666646452341431
512231664666236556243446476376373674657757746775856577584764846486568657556654658575446575847767778754344655567763665364353524653552246535431
141414665522563445263633446674334444564555755766586587786665754455878676484877464657874677555877875467674435735334577534622554545224354462441
132324222343522456562343453577374775354564465457777785545778544578654574584575857747567585884655674847335373435547644654445662232623246622554
522265652626344325253776367756754663666587474588584658475868668556767575686678464545576745757774448676583357676773755545366232226524625554345
324323545534644533343735675645335737334685766445646847477757547865768658874544678566746764755487844767685474365653734357344444626356532322433
336362333335424256636565753367333746577754747878857655665487587675854554858548878577845655654685444575858563457474334364734636626363544565225
355465564454644255645647344534766566654764877455464758467877686756668888687745656774846844866467545755657677334346774664566575536426644456536
562463246423335335433367544334554465646447468678745864868877469558576678686778788755487486665475547486665857653655534576363756255363444456255
155534533263244555364443447434535384658774544587686674465859676696797898776557585886854645744556777784746577473346773367645456534526222555456
522356656362455266437377543646643758658674686864848648545957997965688678567789755596889587765764557857765778767555454677473335666633634332444
353325243246563634755335565545465477774544676566864448978557878899765757776686979869667588745785548846587575686567735656553547344454425535453
624564362362653565676763375453557558685678864656744468557989587765565785696886866865577599757654655457877688757835634666577633775466635523364
463435224535356633366653546754776874456644758844559795566658785899598958555996778866776989966874484577587486865767754444665475546536562264253
654235264466237454764535674444657766554545567487455679577779896599896757689779675879965957687545574645656458646467433646567575643343465645243
332646435224664677736735755568876766686786666855878886567756558668765798698599986875598767756796445665574747646886437536766546665332353235663
363532462553673354636454373784758555687774544767587656988899796789566889579998888588598595757966787856746485586844873743474776477545426654352
523635534555654553444656646577555575584657484696855796655895679888575776856955575675585785555595775668586857786576686654677665737575565465322
442423626457546563744563348858767687588668748686696567698785999789956579855977978866967688565899978568448476748868546747367676647333453553626
533352235554675757776645455544686478678565476977996878975675899685588666679557787898689876675557597856865865658484756535665674734364533623453
243236562463544673343634464875645567848776895855987676576788987577668676597578789656855576685978587787654844848585485855755733446747443535326
445565443643447366465665654886677688847458578688769588796865968997989689966888687887865865597876586855866455747544674663473545665636543462633
533652333476663774676654467786465675685779896768765587796869688767666998999896999967867699699569989957657546784647676566546646454676575225346
652463352537635754437374577686556744676675879757889979887588669679679687998989679766578858568575589797956744458888646747656463747346436435333
422524545467636665367747678585558665667556579796875677789786879999979777767767768678659659797798769769774567677577564645477647756354433566544
332426246655565773743358884866557746575695966778865776897897977678889997866999678788687868587698697979875567564885558477454636437667544566355
532566655373654435446384668444766686765789659557585768596689798697986668696866978696989676755556879889588756785448668546863367566755453353543
426353343336546436434367687655858578679677558867655965788688999769888786969897678879997777858769799858769755846565747577543537664537444555533
423522454355533556374676766475687754689596985676888996688669976778868666878878869678699676698899696969965866646878445885566454337634664552263
246445275363774466756457647877555674798667585997799586788767986676996868688966768986889669688567768785865966757668476864784734636553444463264
336342244766676374676448546885546849587957776666589878779667889968786866779666776979896767885687697896997787854845644864875373777747734646646
324565637735475333675446445566547686755958858896989968667769868996976668986666776768967887699957767986967858755868745685757473364543437676565
555642464565454445738556748775656855998567897888769788698769876667799778998886899786769878896765758976585586747858784877554345746545334365556
245464677666533773357754864754576785787958887677787986976999996776799897699789776879678989868699857677669898667748578584767433577364567352525
336533455537573573587685867566874889686855567676767679876769767899997889779767869877689766869799679775879998997744475685468566555577455773265
552324436734643575585568686464754599685769867777779988669979787788777799999877898887786779666798868596878985898684756475858677666476444762554
256567444356573636547555877447584797567875567879786969879878989899877779789989887889669677696666755755875698695867464647685567476464574445256
562627355445536353454886776556574978868585757858867987988766666879797999777878789868878687798689859858688975657674746447855675633543436637346
654235643563767655755657788885479886677878888587689888768698987787887879897979898867777787996997699586769986797568648587756536575366346677265
423565333576464557446654567674456786956775969798779679689889987997889799977978987896998798888969998557979879557676888584758487476755577554222
643443654564345344456886776868859888766656896889867968689797799788789887889988987799888986686866667869689775998848754558584766675447355767265
546563336765745576548878584668887687759688967676876867666788979798889879989889887898766699877668699959999975797774454648686656666374333634542
362236453757453735546844785885486577668858896777897996986788898887798888797899797878677699676978877587996556898485577657848746345653376556226
362453555643444676446458775684468785888986965967669886788988788777787889878977778789786678798887988569955665796976854544665866466646437734224
443336733375574377585758788857865865868698978776778986769779889797978899789877999877967886789867765897867699577758845755854577347633654343345
664544643737563457768877885575457696879858698996799789777987778987999898898778787987998978969986887797676775858886646465474574543466374373444
322674763355576357858848786755867567679798865988797996697689987798787977898799897889798988679688988955998555598958874576767856336447735343444
546375645565745343775444876784685657775976875979768797876997799898898979977879787778886668697666888595657968856967675688448563777375337363455
255563346355544345867447764857467889777976757888678979766887989889978977787889897888779689667776677765658687887586748757845876373353536437366
453353357776454433577456876457687998575779565997877997897888897977999877998797899997889677766877785575677658797874658478886483654667537444642
356655577537737377445466557576488968776855595987696797976998878889998899879787877797899966999966977586696777675847645884865656756446346747656
524534555574373364754887876885555766965885679898886686799899897778878877987977877888679988797776997788979778668785565846465854763563436437246
344646767673534643888464658686556565655695586696878889976998888898977879887999978778877998786989766998878557759788744478488586755466366745364
336323763477443556568644456688456559756585666899696878698677879899788777777989898979888786898697675875765557868746667575486873645455364755544
635334435545764765657575686857548765659978655679689969877866988898989987887977798876797699897787955765859798576554484487654664755537445647334
564653454546743543875788878658455969798866656786968666987666698799778778887987979769966977989699857569998858577685874484665674636755645676654
364345743473536754364778684784489755655595599599686679988697977787978999977887778999866677878988675796778655559557575778777733567355455434425
634344456665754455587565544866546976987798869996966989776897677898877899889889977768797797878868665576658857988554448585866756554645357754233
353456437744775464786874466474454786587788787687887897996789879689899779897987979976796968797887677789795776586658575866688643444634667756344
323366574647354337644448856574455788597575867698777988789788678878789778779788986997778766766775565669889956995457744484548545457453757672255
344555337773573345747467778578568689869999569699686999787898687988877888888779997966898799668786655856598978565657485666754733636547445364322
342222745755445475734556447568866867766858769976987687998976999997997766978967689698686978878855958689658557545654475888457665355667557773535
456223366773556353357775767688646865757655887958687699689978799676898666787779998979679668699978689556999555585756474877664645667353545535362
263433573774374365775775668778465647899879769875976966866666976777768899877696777768869989988997577975675758655686658777548335667477775576523
234242336463653736375554687485675675698776575678595877867788796888897798677779967999668876987959796686859657777646764568473773664767346343653
646333437373545765653867865487487457698666859579555787677886697967696697696669978897898786859669677665965786885757666654855636557435533436642
355464337347755574675455754774676768879857768567678569689688776688796767997898699897667668966685757668556758554775868586685465657363635733663
354263456366347346673456766584475685469589976659558959889979677996976797699969977977799765787887688899757854775877678756533636574677564536265
645556264756377567473475784877574648586976575676896876597968886667689768899796768766786789569969975687678654546458764448465456545534564442555
226332653667747346767766746858588457466756996776766598878987996899996698698788898787997858798666869669967587858545575674376766453675674253254
622642444353453336653668878865845754687668877778568758885599967999689768667786899686765769687658955657855657876544765686474437367444355563522
442422645435647555537633857584764786476778797588989857957856898998789898769696677969957665978868778688956747745575657546447367445555553563454
523665222346343364337367448557648577656667978575878978586798989699777688867987997575988855878576956599786885566467644777676643337776744265254
254424553536435674456744475875477486767678865675698658895879655896898678876698577665798568675788568566564675447584888834755764534754552545643
423245565674466533444547677478885575776744558765559887757868868799698975557987988577859796695587785574884864584654586564536737645763662322433
522464556623753345635475678788547556487464779998975759675566575995599596987796959995995896987958976867786456765575644363675435673477465566554
343224342623346676347666774466475764754478879559666586688898677569778786795858898775898666658779897845574574687865774445573567737365424554362
653424534335366566536777653556755488548576556596976678967956858898898576565988679996565559857778598768578445747878455737364576336453264342266
355643623335347453646734344388647586675744675676669875756889566996657678797757979666669957587869864848886785685855875776476565536446222225632
332256566242277337556667367445456874858587755865765797976599876855687798895878785658777656658598656875745684586758476757654474333555536645524
224236446456564673373544356777446664746564458748576699798667657758977667878968897597865665765546584487455464544477446433465454336562463333223
552244625663234545374337453454755755687468855578645957689656985798856987977789657965795578678654878784548748785555365667657476335544424325356
625644536362326656357476733333645848474766566447658788979876777656659995779797596698755967545746475678878786586765644737556537443263533252323
432225456523545344637356534653557877748854788464547467857969579665686579876685598677999768458646646844775685675734654737553553564622245423662
252246246543543577655356633556465668648546776768566857558885959976765779776989868797769667744665458754546657764553446763654336364646635325443
464636324632334476334363666643556655465466475776644788778555596775556696697786887697558488487846775454856787646556457347544366655536342526355
435225434624262645454347633573767654566645868658666874586888465798877579985876657868545567886444577747558447647337366363774773452424422353655
145665643453433422673657635364356353857545848485847474677577664554498766787845476664575585657767478455457475434733766377437476536343442634323
326654322552243545737443563355546463548468788555567666467587866664648448668768656648477764867854564786544745773544556563755445554244454664633
221336555523446346664343537574773477374688545666647544654757656755678654877475755884655784454746867548785477374364554644374333666255432333453
433265226565426534647343547347557353346585465776768864646474455758476776676677447847648868757464565466743454437564543645773454546326423432443
345242444352536536463546654464563634743545455586655567558657758665554555684678644858786768556845868587336763557363647453746244632356334326321
545124365224466425666447566353646545657647745846446466866856665448864546557758454758545488447758645685675456537775556363525262556665665343253
355412224454626533666347764764473345566553576766777875858875565488768546677578854884658474456874454375477455475557536653256563222426256662421
133454664232335356553665463637453766773566556357755766744448857754688578755775658584457654488774775477757337547376647364365533435544454623315
431153452543255245665222565653375634743554345775788685654778655888586848455454655664587787886567376445433474644774473765262653644545223644242
344452152533523344443235337357457345336643777676755876888464657676886864486877854466758445665376344554536433473654434442344356444244336542532
344325413246453523634435653435444335475444536753453767568554478548785885586466567458588578643445343576637744447463756224255355545564334511545
552551234533266236325466663365544636377634477354747366465655548858685668666484644644545644557635375353333357545634566243325562546465522524413
311524545153355426432635246437643633574376346433544633573677578547444568756545786875446775437337644446465333563536643523263542554665631344433
441132241416225343455543632356573375735746763464665747436576373857788654684755655374545536356337344566757547766673632525334546456356144135425
342421352351353662465323542522466675567747736354644343655563444576765575334543743354735555464555645455675537547655633625232635262351454423351
222321545413324652452225363546533457776544766556676477567553447676567446737453337737437545653446434736657535454465232652546642626443142243225
132541345543222362365626525344333366376535367536753533463637366545474546765665477553466764336363756767777334354453565566366562325422212423355
413455441112122663536626426454365543373734365466453664353445575355477755653334366464656454745466333456474435242445225456642252422522113411222
312215215343523224366343223324324452343467357764366465434574643747544673763763465366733535677653674754535224343623445544632322345355345145443
411555225233233422464456562346424352656565344575773637577634674737745563757544737674356657376735743457455334463445435345425462113443443544523
355453454151144115636656342566224435343536547475547443444537653454353553556347775356354367554333666646363355335622555433565521125331432242232
321112131513534552564436464562456433354544445334444634677756747736573434445555656653455355336475465235624366645224455454643224231131121314241
241431232521135412542353326662624634546536254276337634366455456756337366745364376457777463777447544355366445554535424266224455315542112242455
134425334145355324453556364535345355266554242656443566635664656664434466347666374673545535777453562466546552543454445365232551351123555251544
224535223424112431121542325265666226562664653632523266665566465553553375765544734644766544336436525434666433243455532545555223533344314521111
442243414125141241222511444444453552553465365465556256257547575374766444344436533446667326345454452324335244656553634365414214323335444555443
341411112214154352211125143324235352246665542525246566665565575536477474635576746654523223454623646642534652264363656215114551411354515255314
412344423255121144234125355432455346256622325444636254466252645663265745736464623544624333542566355333543662646354464322333224243332511231231
114411234233322532214322523225432665556655435652626366666632543466426534633623653335423342454335366335236653452623431132313343323215552121214
423123144522333242511211213533642662322324624323353366446543654442343652453363536622442526523326626535524343233442135152325133334252223142132
'''

# COMMAND ----------

import heapq


def get_min_heat_loss(m, target, min_streak, max_streak):
  reverse_direction = {
    '<': '>',
    '>': '<',
    '^': 'v',
    'v': '^',
    'x': 'x'
  }
  seen = set()
  h = [(0, (0, 0), 'x')]
  while True:
    heat, pos, streak = heapq.heappop(h)

    if pos == target:
      return heat
    
    if (streak, pos) in seen:
      continue
    seen.add((streak, pos))
    
    for direction in '<>^v':
      if reverse_direction[streak[-1]] == direction:
        continue

      new_pos = pos
      new_heat = heat
      new_streak = streak
      n_moves = 1

      if streak[-1] != direction:
        new_streak = ''
        n_moves = min_streak
      elif len(streak) == max_streak:
        continue
    
      for _ in range(n_moves):
        new_streak += direction
        new_pos = (
          new_pos[0] + (direction == 'v') - (direction == '^'),
          new_pos[1] + (direction == '>') - (direction == '<')
        )
        if new_pos not in m:
          break
        new_heat += m[new_pos]
      else:
        heapq.heappush(h, (new_heat, new_pos, new_streak))


lines = inp.splitlines()
m = {(row, col): int(c) for row, line in enumerate(lines) for col, c in enumerate(line)}
target = (len(lines) - 1, len(lines[0]) - 1)

answer = get_min_heat_loss(m, target, 1, 3)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The crucibles of lava simply aren't large enough to provide an adequate supply of lava to the machine parts factory. Instead, the Elves are going to upgrade to <em>ultra crucibles</em>.</p>
# MAGIC <p>Ultra crucibles are even more difficult to steer than normal crucibles. Not only do they have trouble going in a straight line, but they also have trouble turning!</p>
# MAGIC <p>Once an ultra crucible starts moving in a direction, it needs to move <em>a minimum of four blocks</em> in that direction before it can turn (or even before it can stop at the end). However, it will eventually start to get wobbly: an ultra crucible can move a maximum of <em>ten consecutive blocks</em> without turning.</p>
# MAGIC <p>In the above example, an ultra crucible could follow this path to minimize heat loss:</p>
# MAGIC <pre><code>2<em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em>1323
# MAGIC 32154535<em>v</em>5623
# MAGIC 32552456<em>v</em>4254
# MAGIC 34465858<em>v</em>5452
# MAGIC 45466578<em>v</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em>
# MAGIC 143859879845<em>v</em>
# MAGIC 445787698776<em>v</em>
# MAGIC 363787797965<em>v</em>
# MAGIC 465496798688<em>v</em>
# MAGIC 456467998645<em>v</em>
# MAGIC 122468686556<em>v</em>
# MAGIC 254654888773<em>v</em>
# MAGIC 432267465553<em>v</em>
# MAGIC </code></pre>
# MAGIC <p>In the above example, an ultra crucible would incur the minimum possible heat loss of <code><em>94</em></code>.</p>
# MAGIC <p>Here's another example:</p>
# MAGIC <pre><code>111111111111
# MAGIC 999999999991
# MAGIC 999999999991
# MAGIC 999999999991
# MAGIC 999999999991
# MAGIC </code></pre>
# MAGIC <p>Sadly, an ultra crucible would need to take an unfortunate path like this one:</p>
# MAGIC <pre><code>1<em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em>1111
# MAGIC 9999999<em>v</em>9991
# MAGIC 9999999<em>v</em>9991
# MAGIC 9999999<em>v</em>9991
# MAGIC 9999999<em>v</em><em>&gt;</em><em>&gt;</em><em>&gt;</em><em>&gt;</em>
# MAGIC </code></pre>
# MAGIC <p>This route causes the ultra crucible to incur the minimum possible heat loss of <code><em>71</em></code>.</p>
# MAGIC <p>Directing the <em>ultra crucible</em> from the lava pool to the machine parts factory, <em>what is the least heat loss it can incur?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = get_min_heat_loss(m, target, 4, 10)
print(answer)
