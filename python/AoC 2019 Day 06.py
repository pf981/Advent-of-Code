# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/6

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 6: Universal Orbit Map ---</h2><p>You've landed at the Universal Orbit Map facility on Mercury.  Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input).</p>
# MAGIC <p>Except for the universal Center of Mass (<code>COM</code>), every object in space is in orbit around <span title="What do you mean, Kerbal Space Program doesn't have accurate orbital physics?">exactly one other object</span>.  An <a href="https://en.wikipedia.org/wiki/Orbit">orbit</a> looks roughly like this:</p>
# MAGIC <pre><code>                  \
# MAGIC                    \
# MAGIC                     |
# MAGIC                     |
# MAGIC AAA--&gt; o            o &lt;--BBB
# MAGIC                     |
# MAGIC                     |
# MAGIC                    /
# MAGIC                   /
# MAGIC </code></pre>
# MAGIC <p>In this diagram, the object <code>BBB</code> is in orbit around <code>AAA</code>. The path that <code>BBB</code> takes around <code>AAA</code> (drawn with lines) is only partly shown. In the map data, this orbital relationship is written <code>AAA)BBB</code>, which means "<code>BBB</code> is in orbit around <code>AAA</code>".</p>
# MAGIC <p>Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download.  To verify maps, the Universal Orbit Map facility uses <em>orbit count checksums</em> - the total number of <em>direct orbits</em> (like the one shown above) and <em>indirect orbits</em>.</p>
# MAGIC 	<p>Whenever <code>A</code> orbits <code>B</code> and <code>B</code> orbits <code>C</code>, then <code>A</code> <em>indirectly orbits</em> <code>C</code>.  This chain can be any number of objects long: if <code>A</code> orbits <code>B</code>, <code>B</code> orbits <code>C</code>, and <code>C</code> orbits <code>D</code>, then <code>A</code> indirectly orbits <code>D</code>.
# MAGIC </p><p>For example, suppose you have the following map:</p>
# MAGIC <pre><code>COM)B
# MAGIC B)C
# MAGIC C)D
# MAGIC D)E
# MAGIC E)F
# MAGIC B)G
# MAGIC G)H
# MAGIC D)I
# MAGIC E)J
# MAGIC J)K
# MAGIC K)L
# MAGIC </code></pre>
# MAGIC <p>Visually, the above map of orbits looks like this:</p>
# MAGIC <pre><code>        G - H       J - K - L
# MAGIC        /           /
# MAGIC COM - B - C - D - E - F
# MAGIC                \
# MAGIC                 I
# MAGIC </code></pre>
# MAGIC <p>In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.</p>
# MAGIC <p>Here, we can count the total number of orbits as follows:</p>
# MAGIC <ul>
# MAGIC <li><code>D</code> directly orbits <code>C</code> and indirectly orbits <code>B</code> and <code>COM</code>, a total of <code>3</code> orbits.</li>
# MAGIC <li><code>L</code> directly orbits <code>K</code> and indirectly orbits <code>J</code>, <code>E</code>, <code>D</code>, <code>C</code>, <code>B</code>, and <code>COM</code>, a total of <code>7</code> orbits.</li>
# MAGIC <li><code>COM</code> orbits nothing.</li>
# MAGIC </ul>
# MAGIC <p>The total number of direct and indirect orbits in this example is <code><em>42</em></code>.</p>
# MAGIC <p><em>What is the total number of direct and indirect orbits</em> in your map data?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''R45)497
TYR)159
RJC)Z1B
ZQB)99Z
W6M)G8S
KPZ)4J3
GZ1)88C
7DK)FWL
1HX)LQV
8Y6)JRY
JBH)RLS
TNC)SDS
9SC)KXD
XXN)XQC
W3P)HHY
L4P)3VZ
L65)SXG
LD4)J5Z
8MK)88X
1QP)TLB
GFZ)SW1
LQV)8Q8
K8Q)XHQ
6H8)JFZ
3T3)T2L
RGL)R81
3HK)XWS
GXN)KWT
V4C)86B
GR8)8QG
KQ2)V4C
JHQ)KLX
XS5)RLY
QZZ)RBP
Q13)QST
1KG)TKJ
7DT)82Y
3X8)WHG
QFS)7TP
5VW)8MK
GMN)CD9
T2L)YF5
8NN)DHP
VB7)SZL
MJP)MZV
18C)WS4
SW1)3HK
TPK)P6Z
VG4)64H
SVC)GXG
9DN)RXQ
M41)L1W
GHN)K53
BWG)R9H
VHC)ZYJ
XHF)JKB
JN4)HTQ
NY9)5GB
R5Z)X5Y
M23)2LV
G9M)N1R
DL5)2XD
66B)BRZ
DHY)FC1
XNG)NYW
2RV)MCV
TH4)CZB
27D)PQH
6DV)TWP
7TP)WM2
DVZ)VVT
C97)1PW
JFQ)NG7
VX4)H83
1LP)BW4
BRZ)HQ9
SKX)NY9
PSL)3P8
41N)SVX
G63)85M
ZR5)W6M
BJY)NWT
5W3)K2T
BS4)RQR
3RD)KHX
V6F)199
MP3)QHY
RJ8)8NN
8XH)SCQ
GLZ)YKY
9JD)MB1
SK9)ZWR
R8S)JYR
F31)WMG
RXQ)5N8
BHM)FK8
NNQ)PBH
G86)K8Q
2DB)BPW
5QX)3RD
P6P)GXR
JWK)L65
TQZ)9NX
XHQ)KGX
X1S)QCT
WXH)NPT
1WM)6JV
FK4)535
L82)ZSR
MC1)XW4
WWN)YKC
CTV)CX1
JV5)P37
Q93)6YW
5TP)7MS
YW7)GTH
JDZ)PY3
BSD)M39
7BP)RYC
CQD)9FC
NPT)MJH
M5C)V61
TXL)YR8
YF3)VW9
6ZT)XTM
NVF)BPK
VZ2)WXH
82Y)KPZ
ZKC)DTZ
QH2)DJ2
TKK)729
881)GKD
P95)42J
6WD)VXK
8RY)2P6
WXX)8J9
LP9)7B7
CNJ)VBY
Z7K)VRC
M5W)JQ7
WK4)4V2
ZVF)QLP
99Z)Z7R
9W5)6TM
PS2)Z81
QDD)3C7
MF9)5CC
6JV)DJS
FP7)1H7
VDH)M85
3GF)BNF
GT8)HPT
K43)DSP
8K6)QRM
5GC)Z5Z
6YW)H6M
YQC)5W3
1VG)63H
LXH)58R
BR6)2RB
2S4)CKV
SDN)ZRB
HHY)WKD
7QW)V52
PC5)LYP
9LV)P95
LVD)Q8M
CT8)4PS
B8L)PND
C32)8FS
ZTM)V8W
1TZ)YWS
N1R)G2G
729)153
ZDJ)1PK
LXM)TC7
9SF)94L
7VN)2VC
DQS)6YD
FCZ)DGP
FN3)5WD
RBP)Z86
7VD)C97
KBN)JWK
L68)8ZM
GVS)JDQ
9G7)DCD
QSZ)RGW
5SY)LDK
NKL)MHN
ZHB)66B
TS4)R8S
J9R)RR7
N67)1TZ
HX8)XXY
4JY)9SC
LMP)YBH
XS9)XXN
RZD)WWF
JP9)KSD
YF5)139
6YD)P27
Z75)NMM
HCC)NVC
VVS)PHW
8Q8)VF2
WGX)V95
WMC)V6F
2TB)SDN
P49)4VS
K35)CF1
4LD)YDW
G96)M5C
CJF)DW5
ZRB)QMK
QSH)P3Z
KRV)BCJ
DH7)3RP
NWT)LZ5
PND)QYX
5QB)YBG
ZHM)ZFT
CJJ)BLY
YBH)9JL
D14)W7S
JG9)B41
913)CG4
LKR)Q8W
FNB)1DB
BB4)RPY
P6Z)FMX
HPT)YV6
DPD)G1M
YV6)JMQ
WW9)PVD
349)1LJ
BH1)LQQ
XSM)FX9
ZZ7)FTF
B41)C8Z
7XL)K2Q
9L9)NW3
YW1)VPF
CYK)43W
6NX)LP5
H1X)Q8J
YNQ)3CJ
QYX)718
VPF)DF7
H83)PHV
4FP)2L2
GRD)YRN
918)FTD
FF4)LHM
HQ9)HFZ
DGP)VVS
ZP2)9Q1
WJC)295
2KL)S12
PGP)VX4
G1M)W4F
9WC)GMN
YSW)G2Y
3Y6)W2J
BZX)Y7S
K4W)M5W
YJX)7DK
2LV)N42
GXG)DXD
5N8)58B
8L3)XSM
M39)512
QFD)5ZH
J2S)JNX
KBN)XCQ
WGN)TD3
D2H)SHC
QZF)897
GTJ)FTC
3ZN)99C
3T9)GJV
497)FRF
S8V)MF9
HVY)2XK
T31)42Y
295)3FB
NGP)3GF
3HJ)MG2
9TC)M6M
W7S)M1L
G1F)414
M3K)7J5
M9M)P3J
93H)K1Q
YRN)D53
BPW)TSP
1HX)BZW
G3G)9ZM
LVJ)D14
BQJ)DPD
C81)NPP
WC4)3T9
CX1)D9K
DTZ)1SQ
CN3)HKD
YX5)4NQ
DZY)RPR
897)NKG
FQG)BJM
KWT)PYH
MZV)17Y
DSL)ZGT
T2Q)727
TDR)V33
WBP)FPB
2Y3)1KG
12V)X1X
9ZR)NFW
PMN)QFD
11H)2S4
PHV)2WM
JTJ)CK7
92T)6QK
LNG)XJM
K8B)LVD
9H5)94G
1K4)X5G
9XC)BS4
2RB)KQ2
MP3)SM2
JZQ)SW2
542)PZB
HCR)FRW
NDY)QFS
DXZ)D86
5WD)XGT
PRB)VB4
5DL)9H5
XGG)LNG
43W)5CJ
681)RM3
5CJ)RJ8
DGP)QPF
7GH)96T
BPP)PYY
GJ8)LVX
2P6)4KS
WSP)8XH
YMN)8QQ
9NC)Y1S
ZCT)3FM
8J9)K1V
Q16)JBH
FPB)K8B
7PF)ZR5
RFV)84Q
YKQ)TPK
M31)RXR
Q4L)NHQ
KSV)FPS
JBR)TYR
4B9)FHK
S9X)M9M
4HT)783
J5D)9WC
ZCB)6HJ
SBH)QQ6
VF2)PVS
JRY)5DL
ZY6)PNV
ZRH)P4P
2BQ)XTT
CKV)SCR
MQ7)VGW
6SM)BZX
MVN)1NL
FWL)LMP
DV9)3N2
NG7)VG4
7QK)8XR
8QG)G63
DW5)ZKC
G8S)7GH
DSP)T43
X8T)FP7
DDQ)3RN
Q6K)CN3
64H)X6N
DTZ)XH2
Z81)HTX
YMN)SCZ
FCL)PCC
V6L)LQX
KSD)RTH
WXV)YKT
RTH)52B
N5B)MP1
RRJ)8G9
7B7)VXT
9WW)DZY
Y55)ZY8
Z1B)TM8
82Y)N8G
C97)29K
JXK)4N1
WRP)BP9
6H9)VDH
SZP)84F
414)NNQ
Z6X)P3N
P3J)9XZ
2QB)8SJ
VSC)8CS
XBT)92T
X27)6H9
GLZ)B5L
L13)DHJ
J5Q)432
69N)L2Q
VGZ)PMN
MCV)P9P
34F)12V
RX9)MJP
QJN)BB4
4KS)T28
9ZB)8GT
99C)LST
P4P)YMG
C9X)9XC
M9B)KG8
V1B)DL5
1H7)7X8
RK2)KPF
KWN)M31
718)JK9
ZR4)7BP
W3J)YNQ
38B)X8T
YBG)HF2
NPP)GZ1
81K)X1S
RGW)G1F
Y1S)5QB
36R)BWG
38W)131
YTR)LJC
71P)NR1
H94)Z1N
3N2)27J
4LD)ZHM
81K)4RT
NPQ)RYY
727)H4Q
YTR)H94
RM3)N7S
HQ9)BZG
3P8)GZQ
JHP)D2V
FXW)Q13
7F9)56W
7S8)NJT
1M5)4LD
5ZH)3YB
KWR)RX4
X6N)4RR
G8S)ZR4
RXR)6Q2
5CC)GMC
S9X)QSZ
TC7)57R
JGZ)2KL
YR8)FQG
QCT)BYH
DCD)MX7
ZD9)1TP
LQX)JNR
PYY)YW1
YQ3)H7C
R6X)XG1
TXG)TMQ
TWR)YF3
MMN)M23
5YF)9SF
V61)PWP
PZ6)QZF
KG8)PRB
L94)N7V
XCQ)5JX
L1C)PS2
R81)P57
SCZ)GMM
TD3)3T3
HZ4)TDR
RR7)V6L
4VS)R92
Z5Z)73W
HPR)ZVF
G6S)5TC
XPZ)RQZ
42J)TWR
X6N)XWW
127)JN4
BHX)9H6
LP5)QSH
7BT)JRR
XTM)R9W
JQ7)7X5
YKY)4P5
YMG)SQQ
VW9)1HX
XWW)GR8
QGM)K55
GHQ)XPZ
799)21X
NW3)6WD
YNQ)MVX
Q8W)YL3
HKD)DXF
NL6)TNC
WKD)RP2
FX9)6ZT
733)41N
SHC)FXR
C9R)5GJ
9TS)DCP
4N1)W3P
LJC)WJC
PYH)J5Q
8SJ)4JY
25P)GXN
94G)C81
HTQ)862
CT4)KRV
W4F)2BQ
HF2)V48
458)K4W
FYP)GLZ
1BF)MZB
MJK)68F
1SQ)JV5
BMN)JP9
NPP)XHF
C8Z)1LP
LXF)HVY
BKC)RNR
F3H)Z6F
PZB)38W
NHQ)XKZ
32T)ZP2
MB1)D2H
B63)MYQ
Y31)KBN
FC1)D43
SCR)9TS
6QK)DSL
X5Y)P65
GRG)M1M
PBH)1K4
HNR)ZCT
SPP)CSB
GXF)NM8
J5Z)TTK
94L)WW6
COM)7VN
3RN)TCS
YQC)T16
ZG1)VD1
GZQ)BKC
PYP)GJR
KRX)WDT
XJM)DHY
PVS)BJY
927)LD4
DJH)NYX
1DB)QLX
3CC)4J4
3FB)PTC
NVC)18C
2ZR)WGX
29K)ZZ7
GJV)SBH
FTD)9ZR
MT2)PR3
LSS)RYT
7FG)SL4
9QT)27D
FTF)G96
DHP)DV7
PY3)881
KX1)L82
KPF)V72
D9K)LKS
L99)NV9
DF7)J3D
BZG)R45
KTR)L99
B1X)G4G
V77)32T
ZP1)V5G
V3G)7ZH
7J6)6RB
DXF)R8G
8FS)GRV
WWF)JDZ
17Y)BMG
DFQ)Y7W
8VB)Y1Z
GKD)CJJ
88X)HNR
Z1N)L94
681)QJN
4RV)HMD
SCQ)Z75
HH3)6TJ
LX1)2RV
7TX)XNG
RQR)2Y3
TS4)NGL
F8L)TXG
NM8)4HT
PVD)5WC
PG1)WW9
QJY)4B9
88C)RGL
L1Q)1XB
DR4)MVN
3X2)8TP
CG4)RVJ
PF7)BR6
YLJ)KX1
KS8)SKX
1PW)DJH
DV9)J5D
5JX)4LL
H27)JW5
PHW)127
BYH)27N
71V)WSP
VL2)J64
TC7)5TP
JNR)DJF
SQQ)R6X
RMD)458
T2Q)LSS
9XZ)1QP
S1H)QDP
SST)3N8
XKZ)FN3
QQ6)VZ2
DH7)DCH
112)ZCN
B3G)HX8
LCZ)3WP
4RR)3ZN
PCC)BPP
QST)NKL
NYX)F3N
84F)HKL
CZB)2V6
YWS)V17
65J)FNB
Q8W)6MP
5TC)HCR
8G2)NGP
D23)4ZZ
5WX)71P
KHX)93H
XH2)KS8
Z54)112
1LJ)GHN
X5G)5NK
X5Y)9LV
JYR)253
5GJ)HPR
QRM)XFR
4NQ)913
6HJ)B63
SFK)6SM
7FG)RMD
TKJ)JWT
1XB)LXM
WST)1VG
NFW)HZC
JWK)LC7
YS8)PC5
WXV)F8K
27J)J7M
KKX)HH3
7ZH)XYD
K53)TDK
MX7)8NR
RPY)PSL
4ZZ)S61
YYQ)519
7VG)91Y
918)JT8
42Y)MRN
8MK)WK4
5ZY)F3H
JNX)MP3
RQZ)YOU
Z7R)JG9
FXR)5QX
PZ4)22G
JFZ)9JD
QHY)9QD
ZDJ)Q93
2XD)RJC
1PK)GFZ
WKX)LXH
G4G)6LV
SDS)X21
RYC)3Z8
G2D)5ZJ
F8K)PZ6
96T)5YF
3C7)VX7
N7S)LKR
P65)N5Q
RLS)7F9
1CJ)X27
3VK)J26
VRF)8G2
TMQ)FK4
LVX)Y31
139)9QT
7MS)PG1
1T2)ZNN
38W)S9X
ZF8)681
SZL)ZHB
4S2)CY4
STM)T31
XHF)TS4
HTX)S8V
D43)QPN
RYT)WKX
BMG)MRV
Z6F)VRF
V72)YYQ
G8H)Z7K
51F)3HJ
3CJ)TH9
GXR)TFR
ZFT)FXW
S61)YKQ
MRV)7J6
GJR)SZP
ZPG)JBR
NKG)NKY
VBD)7TX
TZP)YS8
LF1)8LD
GXF)M3K
NGL)YLJ
512)DQS
3HT)KWN
KMR)CM5
18C)SVC
LST)7VD
YX5)JGZ
4P5)9DN
KLX)JPJ
BCJ)JG1
LNG)RKH
7VD)GXK
GT1)BSD
LHM)5LG
H7C)5GC
HZC)5WW
QCF)JTJ
V95)ZY6
GT1)GH9
B5L)KWR
H6M)6DV
NCH)PYP
R92)LXF
S3D)V1B
WDT)MMN
GXK)RXL
QMK)8PM
8LL)T2Q
L2Q)W25
V48)KZP
LZ5)4S2
SM2)P49
ZNN)HCC
63H)B3G
9FC)7PQ
LFY)YM8
DCP)GVS
JFQ)FCZ
NVC)CT8
K8Q)1M5
N5Q)8K6
MK5)5SY
6Q2)BWQ
17W)SK9
K2T)MK5
WDT)M41
DJF)RZD
RJ8)VSC
GJV)NVF
8QQ)N5B
P37)ZTM
FQG)CYK
VPF)8L3
JG1)1X2
3VK)3X8
199)DDQ
2DH)HG7
K1Q)L68
9PK)F3T
1VG)2ZR
DXD)799
FC6)2W2
CY4)7DT
3FM)B71
153)YMN
137)ZQB
QDP)9WW
1SW)GXF
QHY)4M3
2XK)HDM
B78)XK8
HMD)RX9
TDX)51M
NR4)31N
QCT)YSW
RLY)LNP
R9H)BLN
XXY)TXL
9H6)XBT
CD9)H1X
GTH)K43
NLK)7BT
KZP)CTV
PTC)DVZ
TH9)9L9
5WC)3CC
MC1)YTR
TLB)SDK
FL2)SHF
WHG)X7P
57R)PKT
RX4)2QB
542)JZQ
Y7W)918
9QD)87J
3LN)MT2
TFR)FMS
LDK)VBD
P57)JHP
1NL)9ZB
G9T)YGH
YBG)CJF
PKT)GRG
8LD)YX5
XFR)MC1
B71)3X2
RNR)81K
ZSR)3LN
XGT)G8H
YPT)KSV
BJY)BHM
QPN)G9T
CH3)5G6
YW1)DXZ
NR1)TDX
41Z)SST
4RX)LF1
58B)CNL
CNL)7QK
PCC)LFY
PL8)4RX
WS4)MJK
XFR)7S8
VB4)QC2
SDK)HZ4
N42)FCL
TNC)QH2
LQT)VGZ
HG7)FC6
7X8)YQC
G1F)PL8
7VD)YJX
J7H)9TC
X1X)WST
5G6)69N
4RT)V3G
L2T)F8L
G2Y)LCZ
XYD)SBN
R8G)LP9
6RB)LDP
H6J)NLK
F84)WGN
L1W)XGG
8J9)ZPG
FRW)PZ4
WWX)F84
Z86)3VK
LYP)8LL
GMM)BHX
N7V)GT8
5LH)7D3
QLX)ZF8
H4Q)DV9
BW4)JXK
SXG)H14
MKP)927
T28)MQ7
YL3)K35
253)28S
JW5)KSR
2RY)DR4
MJH)NPQ
7GH)QDD
VBY)D6C
783)5WX
MRN)44R
9ZM)D9Z
Y1Z)WC4
7PQ)NST
24S)KMR
K1V)ZP1
J7M)SPP
T43)JFQ
3GF)24S
JRR)NR4
HN5)VL2
JMQ)RRJ
Z6B)9W5
T16)5ZY
Y7W)D7D
519)YPT
5WD)W3J
Q8J)5S9
V8W)XS9
2WM)FYP
NWT)VB7
TDK)Y55
44R)B1X
F3N)Q6K
ZP1)BH1
FC6)2D9
R9W)G2D
NMM)RK2
VX7)TH4
3VZ)2DB
BWQ)2C1
WW6)HV4
CX1)3HT
M23)WVY
PWP)4Z1
D86)LQT
2VC)L4P
KGX)1SW
5W3)NL6
TTK)WXX
FTC)TKK
KPF)11H
YKT)HN5
TSP)H7L
4M3)NCH
QPF)9NC
318)4DN
DF7)349
F3T)B78
RKH)VHC
V52)42Z
ZGT)B7T
MVX)QJY
RPR)L2T
H14)1CJ
MP1)CQD
D4W)KGT
8FS)J7H
VGW)25P
CM5)M1V
5WW)TQZ
N1R)KRX
32T)DH7
BZW)STM
N8G)ZD9
51M)L1C
2D9)9G7
J3D)V77
Q89)7PF
2L2)ZCB
RR7)Q89
3RP)232
Z1N)C9R
H7L)6NX
DJS)PGP
VXT)65J
7D3)1BF
DJ2)17W
FK4)38B
D9Z)WMC
4J3)PF7
TWP)L13
BPK)WRP
232)318
58R)H27
DW5)H6J
J26)L1Q
WST)137
5J9)LVJ
C81)W1L
CF1)5VW
X21)5J9
535)733
HDM)4RV
GR8)3Y6
D53)TZP
RP2)4FP
Q4L)J2S
27N)WWX
B7T)YW7
BNF)51F
1TP)Q7L
JK9)GTJ
WM2)S1H
RXL)2RY
JWT)G86
JT8)5LH
XW4)G9M
JKB)ZDJ
7VN)1T2
JPJ)J9R
PR3)FF4
D7D)SFK
519)Q4L
NYW)GHQ
2G1)QGM
Y7S)SAN
VGZ)WWN
NKY)G55
LC7)BQJ
DV7)27F
P27)36R
8CS)CT4
3WP)KKX
LNP)MKP
V5G)WXV
TCS)GT1
5S9)V5N
YKC)G3G
FK8)GJ8
ZNN)FL2
68F)P6P
M39)2DH
MZB)LBQ
HFZ)GRD
PQH)8Y6
KGT)8VB
FPS)ZRH
MG2)6H8
2KL)D23
MYQ)NDY
159)B8L
NJT)7VG
87J)41Z
V17)34F
8GT)C9X
ZF9)RFV
G55)YQ3
6JV)M9B
4DN)CWR
DCH)CH3
Q89)WBP
P3Z)XS5
GRV)9PK
4V2)GC4
LBQ)7FG
ZWR)ZG1
RZD)N67
7J5)542
SHF)CNJ
LQQ)2TB
YDW)BMN
8NR)8RY
28S)QCF
QC2)KTR
31N)1L2
FRF)C32
X7P)LX1
YGH)7QW
XK8)7XL
SW2)ZF9
M6M)S3D
8XR)DFQ
V5N)JHQ
MHN)Z6X
J64)D4W
LDP)R5Z
W2J)G6S
SVX)Z6B
W1L)71V
ZYJ)2G1
5ZJ)D8G
9Q1)Z54
51M)QZZ
Y1S)F31
S12)Q16
L1Q)1WM
'''

# COMMAND ----------

import collections

def count_orbits(node, orbits):
  if node not in orbits:
    return 1
  return 1 + sum(count_orbits(child, orbits) for child in orbits[node])

orbits = collections.defaultdict(list)
transfers = collections.defaultdict(list)
nodes = set()

for line in inp.splitlines():
  from_node, to_node = line.split(')')
  orbits[from_node].append(to_node)
  transfers[from_node].append(to_node)
  transfers[to_node].append(from_node)
  nodes.add(from_node)
  nodes.add(to_node)

answer = sum(count_orbits(node, orbits) for node in nodes) - len(nodes)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now, you just need to figure out how many <em>orbital transfers</em> you (<code>YOU</code>) need to take to get to Santa (<code>SAN</code>).</p>
# MAGIC <p>You start at the object <code>YOU</code> are orbiting; your destination is the object <code>SAN</code> is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.</p>
# MAGIC <p>For example, suppose you have the following map:</p>
# MAGIC <pre><code>COM)B
# MAGIC B)C
# MAGIC C)D
# MAGIC D)E
# MAGIC E)F
# MAGIC B)G
# MAGIC G)H
# MAGIC D)I
# MAGIC E)J
# MAGIC J)K
# MAGIC K)L
# MAGIC K)YOU
# MAGIC I)SAN
# MAGIC </code></pre>
# MAGIC <p>Visually, the above map of orbits looks like this:</p>
# MAGIC <pre><code>                          <em>YOU</em>
# MAGIC                          <em>/</em>
# MAGIC         G - H       <em>J - K</em> - L
# MAGIC        /           <em>/</em>
# MAGIC COM - B - C - <em>D - E</em> - F
# MAGIC                <em>\</em>
# MAGIC                 <em>I - SAN</em>
# MAGIC </code></pre>
# MAGIC <p>In this example, <code>YOU</code> are in orbit around <code>K</code>, and <code>SAN</code> is in orbit around <code>I</code>. To move from <code>K</code> to <code>I</code>, a minimum of <code>4</code> orbital transfers are required:</p>
# MAGIC <ul>
# MAGIC <li><code>K</code> to <code>J</code></li>
# MAGIC <li><code>J</code> to <code>E</code></li>
# MAGIC <li><code>E</code> to <code>D</code></li>
# MAGIC <li><code>D</code> to <code>I</code></li>
# MAGIC </ul>
# MAGIC <p>Afterward, the map of orbits looks like this:</p>
# MAGIC <pre><code>        G - H       J - K - L
# MAGIC        /           /
# MAGIC COM - B - C - D - E - F
# MAGIC                \
# MAGIC                 I - SAN
# MAGIC                  <em>\</em>
# MAGIC                   <em>YOU</em>
# MAGIC </code></pre>
# MAGIC <p><em>What is the minimum number of orbital transfers required</em> to move from the object <code>YOU</code> are orbiting to the object <code>SAN</code> is orbiting? (Between the objects they are orbiting - <em>not</em> between <code>YOU</code> and <code>SAN</code>.)</p>
# MAGIC </article>

# COMMAND ----------

import heapq

def solve(transfers):
  visited = set()
  states = [(0, 'YOU')]
  
  while True:
    d, node = heapq.heappop(states)
    
    if node in visited:
      continue
    visited.add(node)

    if node == 'SAN':
      return d - 2
    
    for new_node in transfers[node]:
      heapq.heappush(states, (d + 1, new_node))

answer = solve(transfers)
answer
