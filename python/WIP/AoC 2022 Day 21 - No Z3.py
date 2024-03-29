# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/21

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 21: Monkey Math ---</h2><p>The <a href="11">monkeys</a> are back! You're worried they're going to try to steal your stuff again, but it seems like they're just holding their ground and making various monkey noises at you.</p>
# MAGIC <p>Eventually, one of the elephants realizes you don't speak monkey and comes over to interpret. As it turns out, they overheard you talking about trying to find the grove; they can show you a shortcut if you answer their <em>riddle</em>.</p>
# MAGIC <p>Each monkey is given a <em>job</em>: either to <em>yell a specific number</em> or to <em>yell the result of a math operation</em>. All of the number-yelling monkeys know their number from the start; however, the math operation monkeys need to wait for two other monkeys to yell a number, and those two other monkeys might <em>also</em> be waiting on other monkeys.</p>
# MAGIC <p>Your job is to <em>work out the number the monkey named <code>root</code> will yell</em> before the monkeys figure it out themselves.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>root: pppw + sjmn
# MAGIC dbpl: 5
# MAGIC cczh: sllz + lgvd
# MAGIC zczc: 2
# MAGIC ptdq: humn - dvpt
# MAGIC dvpt: 3
# MAGIC lfqf: 4
# MAGIC humn: 5
# MAGIC ljgn: 2
# MAGIC sjmn: drzm * dbpl
# MAGIC sllz: 4
# MAGIC pppw: cczh / lfqf
# MAGIC lgvd: ljgn * ptdq
# MAGIC drzm: hmdt - zczc
# MAGIC hmdt: 32
# MAGIC </code></pre>
# MAGIC <p>Each line contains the name of a monkey, a colon, and then the job of that monkey:</p>
# MAGIC <ul>
# MAGIC <li>A lone number means the monkey's job is simply to yell that number.</li>
# MAGIC <li>A job like <code>aaaa + bbbb</code> means the monkey waits for monkeys <code>aaaa</code> and <code>bbbb</code> to yell each of their numbers; the monkey then yells the sum of those two numbers.</li>
# MAGIC <li><code>aaaa - bbbb</code> means the monkey yells <code>aaaa</code>'s number minus <code>bbbb</code>'s number.</li>
# MAGIC <li>Job <code>aaaa * bbbb</code> will yell <code>aaaa</code>'s number multiplied by <code>bbbb</code>'s number.</li>
# MAGIC <li>Job <code>aaaa / bbbb</code> will yell <code>aaaa</code>'s number divided by <code>bbbb</code>'s number.</li>
# MAGIC </ul>
# MAGIC <p>So, in the above example, monkey <code>drzm</code> has to wait for monkeys <code>hmdt</code> and <code>zczc</code> to yell their numbers. Fortunately, both <code>hmdt</code> and <code>zczc</code> have jobs that involve simply yelling a single number, so they do this immediately: <code>32</code> and <code>2</code>. Monkey <code>drzm</code> can then yell its number by finding <code>32</code> minus <code>2</code>: <code><em>30</em></code>.</p>
# MAGIC <p>Then, monkey <code>sjmn</code> has one of its numbers (<code>30</code>, from monkey <code>drzm</code>), and already has its other number, <code>5</code>, from <code>dbpl</code>. This allows it to yell its own number by finding <code>30</code> multiplied by <code>5</code>: <code><em>150</em></code>.</p>
# MAGIC <p>This process continues until <code>root</code> yells a number: <code><em>152</em></code>.</p>
# MAGIC <p>However, your actual situation involves <span title="Advent of Code 2022: Now With Considerably More Monkeys">considerably more monkeys</span>. <em>What number will the monkey named <code>root</code> yell?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''qlgz: 2
zstt: 2
rjtn: 7
bzbn: bgsl * nzjp
hwpf: 2
wvql: brhr + hffp
tbsp: 2
ztst: tngr * dcmn
pngb: 4
rwqh: 3
tqlt: 17
bzzg: pshd * srfl
zgwf: 13
bwzq: nhln * njww
ntds: ngtn - rlfh
npgl: wflw + vqrq
wzwc: vfsc + gqgh
llrp: 3
bwzg: zbpz + zbfc
bnbm: cpms + wqvg
lczp: vpsd - pqcp
shwt: brns * phzt
dqsd: tbrh + htzc
wbzl: nffc + clhn
vwzn: psqf / tmds
jfls: tbwd - gtbs
jdpp: crft - dwvs
dmdl: zzhz * jgch
zrbl: pltw * hhbh
pnlg: 1
hzqg: vdgh + rvts
dngq: jfpq * gtdh
rdlq: hvmt * wmqz
qldh: 4
zwsm: nhwh - rncq
qntt: spbj * vhhv
mnsl: hlrv - djqw
nbpl: dppc / pjgw
bspt: 3
bwtc: 4
vmdp: 5
lbpb: hbnc * gblh
dfzn: jrjp + hdsd
wftf: shsn * ljfs
vpbr: shzb + rdzf
pccz: 10
rvcc: 9
brgn: 7
cgbb: mzst + ltww
qwfm: 3
cpwm: fjlm * pmqs
vmgv: lczp - lmlj
cgtq: 2
qvdg: rlrq * znsc
nzjp: 4
hthd: 12
fjjb: 2
grhv: shmv + cdpq
zhll: 2
bnrm: wlfc + ptgc
zbnm: 5
qqrp: 15
bgth: 3
dgsg: 2
jsmm: szvf * pwcl
crsv: qrqc + qvdg
qnfh: vfbj * lmrp
tqrs: qqzt - hjqh
gcrr: vzhs - dvtf
pdwv: swjn + gdqv
zzrz: 5
gcmz: qrwb / gssp
hdsd: 6
cnjz: 2
wlhq: 18
btsw: wzgg * hwdc
lbzp: 5
qzgm: ztnj * btvr
hqdn: 2
bmfv: 2
jmbz: 9
tvnb: vjws * ghlt
qpgm: vqht * ppbn
jhrc: 2
cvnh: 3
zcwr: zlwd + mjqc
fwzd: pmjv + zmcn
dlqq: 6
wgbg: swwm + zphl
crfc: 3
nnnq: 3
fprl: 3
jfhp: 1
gthn: 2
trnn: 3
fjlr: mfgc + rcph
sptg: 2
slhr: 6
nrph: ttzt + dmsl
qmfj: mvtd + ccfv
bqcf: tfhg + hvcq
jzzz: 3
mbtg: ctdh + msgz
dpjj: jdhs + mfwj
btvr: 2
vmzn: 2
hwdc: 12
mfnr: 2
jdqp: 14
sbgd: dgdg * fcwq
vjbf: fpfn + rdlq
gbgm: 5
twft: 3
mhtg: 2
tsrb: 11
rrnj: 4
prdb: 3
plzs: 4
ftqr: 16
zdsw: 4
fdmm: 6
mjnl: 2
hfvg: 2
rgvc: hhsf / lhjd
bchg: 8
gjcj: bqcf - czhp
wztr: vfmp / nbtt
zjqf: fsfc / zvtj
zzjd: jdvs + pccz
dnsv: hvcl / zqrh
crwf: 3
qhpp: lddz + zchd
lhsn: qtcj - tplp
zhfb: 4
rcvw: 2
lnmc: 3
mdhq: tncm * mjwl
fcwq: vflg / vmll
tltt: ppdf + vcjn
psds: qbbc + zdnr
dmsl: ffbl / tnsc
cfsr: 11
brrc: 3
nfwl: 7
hljv: 4
qbhv: 9
tvrr: 11
ppbq: 11
vsrw: 9
gcgp: dztp + fbmz
tmpj: wrfl + bqvm
dtgf: sldj / spqv
wfhq: 2
bjlf: 14
vzqq: 7
prtt: 2
fsdz: 6
dnnl: wbzl + bnzf
nshn: 4
mgzh: 4
nbdh: 6
zpnv: 3
swwm: 3
jfpq: nvrl + hnql
gtbs: 1
jjqb: 6
zvvl: 4
mgrg: mrfd + nqfn
pjsc: fbnn + drzz
bvcs: 14
fmgh: jvsf + drgq
mmhw: 3
vrhp: 14
fcwm: 2
pgdh: 3
snbc: cflt + gsvz
mpqw: 2
jvnq: cftv / gqfz
rznt: mpwl * tssj
llzj: mzdr * qflq
ccdh: hcpv * bcpl
lwrl: 4
mvdj: lmwn * wmtf
tszg: 2
bvsj: 4
scmt: 15
plng: pftq * shcv
hnrg: 3
wtgw: 2
lmnw: 4
rsgn: 2
cltp: sgch * szcc
cjdw: ntrp * phmp
qbnb: lbzp * ltbv
qzww: 2
psqf: wwzr * zswr
hjqh: 5
sfwq: 4
dbfl: psjv * nbpl
qvbd: 2
rqwr: clwm / hhrd
dfsl: 4
fzpm: 3
frmh: wpfh * jptq
ltww: bgbh * bjrm
whrt: 5
tfgg: 6
stcb: 4
mflj: ncfr * lhsn
fdjq: szdr * btcb
zqpc: 2
swtj: ppbq + vfwb
mvnv: 2
rsbg: bnzj * pnmt
nlsf: 2
spfl: ntlt * ghtm
vfbj: 13
vjgb: 15
mvqw: 1
mcdr: hqfq + dttv
znsc: jfhp + gmqs
jzvs: 3
ngll: brrc * tchm
gcjj: 5
lzwn: hqdn * wfjb
tzhv: nppz + wvnt
tbrh: 6
gpwq: qptb + wwhl
cpwg: bzzg - smfj
ttjs: 3
zqrh: 2
sdcr: flpw * cffg
hrrq: 3
rwtn: wfhq * zrfl
drbh: qnzm * jljl
pwsh: dpvd * lwtm
wtwf: gmdg * jgrv
gslv: hcbr + mgst
hsch: phsv * rtrz
fpmv: lsgz + bbrd
hcpv: 5
rdzf: 4
drjt: 5
tbth: gpzg + bsmg
wjng: 2
fnrt: 2
rwmg: 13
mmwv: vvqq + rtmm
qstv: 2
qntb: sglz - dqjm
swdn: fchv + lvbm
wswr: cdwn / rsgn
mhjl: 3
mqfv: 2
dlqs: jwgn + cnjz
rptt: 3
bshd: nljl * rwmg
jzjv: zqgv * tmvf
vfhb: hfrw * hhqt
spqv: 2
vfwb: rrgf * nmrt
vjtc: qvzc + bshd
pprp: 3
zbpz: mnjh + cgpw
wvps: 11
jzsc: 2
hldj: splv * lrbs
zdwr: hfft * qlgr
brhr: 5
hccd: gwqr + qwhp
gtdh: 2
gpfs: vhjt + jvsr
nmdd: 3
vqrq: mwgp * hgdm
mfwj: lwln + jmhf
gpwf: cmrj + pndc
srwg: cgzq + zrbl
zpbm: 8
jmww: rhrv * trgg
njvs: crcc + mgjm
rlvh: 1
dsmj: zhbf * rtlt
tfgn: ptpr - mlvj
ldvw: lwrl + bmgm
fqff: 2
gvmb: 5
vlmw: 8
sdvt: rvdl * nqdl
prrm: tqzh * zzbp
rtqj: 2
ljvc: mflj - dnnl
znvw: vwzn - tvnb
hzlt: 5
zwnc: zzrz * zbqw
lbbs: vdhv + lmfg
mdfc: wczw * glfc
mphm: 2
ncmd: dzvf + mftp
lcdt: ndvg * scfd
zssb: 4
dwcc: 11
fdbd: zpld * mpqw
rszp: bpqp + fvtc
ntlj: 3
zchd: wrmt * jznb
fcdj: pjmn - vdwb
mdqq: 4
dmjv: 1
ftnf: 20
bppd: 2
nvdm: dmcf + mthv
gnfc: zhdz + zlcr
ccnw: 2
lfnn: cnhr * cnjt
bjdt: 14
glfc: 2
dfjh: 3
ngnh: bbhp * lcrc
rmsj: 4
ppdq: fjsb * rmbv
rvpd: shtc * nqwt
svpv: 6
lwbr: hsch + pbdf
fdhq: hghc - bzcr
sptn: hpmt * pqrl
frsf: gqqc / rvst
wcrt: 3
stgr: dzpc + rplj
gtsf: 3
pjhq: rsrz / bdlt
ctjp: 2
pbbr: 4
hlwl: bddc - wdsw
lflg: wqcw * qlgz
sqtd: wtwr + fzds
sblw: 17
cwlj: 4
dsmf: 12
wzpd: sblw + jlpj
qrfh: 2
bsbh: 10
rhbh: qqrp + zhmn
drwl: mnlz * ntbh
mswz: pglf * fcwm
clhn: lfrb * gqmp
dsjm: vhws * vjqf
qvzc: 8
jggw: 3
nwdc: mnzn + jsnj
dwsz: tccc * wlqf
tzlj: 4
jndp: fcdj + qmrl
gsvz: 4
tljr: zpnv + jmmh
lfjv: lmnh / ddrp
zlsg: shvq * wvjv
lctc: 1
ncwg: 3
qbnp: 1
mcsc: 3
pjtn: 2
wrbr: 11
rbgv: jlgc + wqbg
bjjb: 5
snhj: bhhr - vmvj
nsnb: lslc * rvsp
ntqm: lznt * hmjj
ljmh: wjjz + vlsf
rlwt: hzgp * tdqp
rmqv: 3
wzhm: wphg + dshv
hlqj: 5
plhc: 3
svzs: 7
smtc: lbsm / dfjs
ftwq: 2
mtgw: lzvf * vzsb
lrwg: 1
vwrr: 3
hqtm: cqqs * rqlg
nqfn: tfnb * snhj
vjmz: 2
qnzm: 3
dsbv: jzvs * mbtg
vdhv: wmmg * hfzc
bsbr: ffbf + rmjh
bqfn: 5
ptrp: lscj + hgvp
hbnc: 4
dwlz: mmbd * pzvz
dlps: fcjl + hbbg
qwss: crzw + dzzr
vvvg: qttw + jdww
hmjj: 11
ltbv: 5
rbhh: tbnm * dfjh
pwrv: gdlh * hmvs
zzgj: ztlc - dlgb
vjqt: 3
ljsm: vvhz * jlhc
cmhw: 3
lccr: hljw + gtws
wvbw: rwqh * rchc
mhrf: bsbr * mlfh
gqzw: rrnt + schm
zdrh: rgvc + svpv
hvmt: 3
ntsd: jjdq + qvzl
vftv: vwrs * dsrf
vpfj: ftfq * tljv
dtjj: 2
pltw: vpjz / hmsr
ncjt: dhhv - zdrh
nfmm: mrqw / qttt
pclj: 5
rsrh: 2
scch: 2
mzdr: jsbd * gzqj
szvg: 2
pljm: jwmq / cgtq
wwhl: pwnq * sqzr
whzj: 3
dfmw: bchg * cltp
fzvc: scch + rlbl
jvqz: 12
gdlh: jvnq - zhrr
jhzc: bgcs + gnnt
ntlt: 2
jdhs: gtht + gwnf
cjdl: fprl + qnwd
pfnp: 3
jhgq: tcsf - wpht
pjsj: lsnb / mlfp
tdbc: 2
mlvj: srzp * lltr
vqzg: fwcf + bnsh
rqgs: 2
bmqw: mdhq + hzhv
jsnj: vtjn + fmgh
ngdv: drcf * zjnr
rchc: mjht + hpmr
qrrf: rbhh * cnbn
qflq: 2
wtvz: 14
dbsn: 2
fvtz: gnfc * srcf
wpht: fjsd * rjsd
pftq: 14
dttv: 1
ptzb: lmhj + pnfv
swcl: cslh * htqw
ttvf: qtpn + qcwq
lbnn: 3
lnlj: 2
glhf: zbnm * gslv
bddc: snbc * ntsd
svzg: 7
rmlz: 2
jnqb: pggt + rvcc
mlfh: gvgd * hqhz
hvtp: 3
wpfh: vqsm + jvhv
jrjp: 1
tbgt: bqdm + nbsb
plcm: fgww * jvlq
jsmz: crwj - bwzq
tqgg: qzgm / dbsn
przn: 4
mgst: zhhw * zcfs
rmbv: djpq + wbps
zbgw: 3
nszm: jpjn + mhzl
wbfm: rbgv + jcmn
vwrs: 2
lvbj: rjgp + lbsj
nfjl: jcqw * tzhs
mjqq: 6
dzsc: 3
hpzj: 19
jtbp: sbwh + zcjh
wgmp: 1
cpjd: 5
lrmr: 4
stvq: 16
brns: 4
hzms: mmhw * wsvq
tdfq: dsmf * tdvn
mnlr: 3
hwsd: tsnj + ssbl
hwzf: bspt * ftqr
qlbf: 4
gdqp: cmvh + jdzs
tccc: mdgw * rfpf
cjzz: qbhv - vvtj
bnps: 3
ncqw: lvbj + gcgp
hfhd: jzzz * ntlg
jljl: 5
lqvp: sbsp + splj
tdbf: ssgs + lsbv
jznb: wcrt * mdcz
fsqj: wvlr * whww
czwc: fszh * bwcl
gdbj: 1
tzdq: gpdg * jzrq
lmhj: 16
cfgj: 3
zqgv: hbhv * smgn
rshw: pjbf * flsl
gnnt: lzwn * nsjc
wlzz: 2
bfsw: 2
lzmm: 12
pfzp: ljsm - cftn
bwbc: 1
rnfw: 7
hbdf: 13
dclt: ttjs + rvvm
pwzg: mgvf + hqtm
pcpg: 2
grvv: 2
ftsj: cgcg + ctgl
zrfl: 5
mvsr: 11
bjbg: pvng / ccnw
dsrf: 5
vdhz: phjj / gtgq
mjqd: 2
bnsh: fjpl / fhvl
znvn: 2
cmvh: hbts * gbpz
nstn: mgrg + bvcs
dvdj: pczr * mhmr
vmll: 2
trgg: 7
vbfp: wzqh + vnft
cllb: djsj + hvlq
ttlw: 3
fpfn: bwbc + vsrw
gqmp: 2
fbfr: 5
zrwv: 3
zptt: gcgw + hvhb
gvsl: 7
vrtb: 15
wqbg: 1
pjjh: 2
wldc: 13
sbsp: cwst * qlpt
djpq: 7
llvd: tjhl * zgmj
hddl: gvsl * ndcr
jjhp: 4
lhzr: zphj / jwhl
jvlq: scmm + fwgh
rlvz: fcfc - vlmw
sjdg: dvdr * smtc
hwsg: gbcf / mvnv
prdn: ppgm * lqhq
zmjp: 5
tqld: 3
crbr: qgms * lmvf
drcf: 7
vbth: 2
flhw: 2
dwrg: 2
mgjm: 5
tljh: 9
ndpn: 4
zsbv: 4
ztfp: 2
lmml: jqmn + tsjr
lwtm: mwcd * ljns
nppz: 9
lqfz: rljz + sfzn
dzst: cvnh * hfvg
mjht: mnsl / vmzn
clrf: 3
swbj: tqhz + wcvw
ztnj: 13
gcgw: fdqz - vgjl
fsfc: znvw * pjtn
hscw: wsmc * jzsc
fvpb: dsmj + gnrr
zcjh: 7
wwwp: pltr * qstv
hqfq: ntjr * dqsd
dzhc: sbpw * gzzp
vpjz: hjhq * rjlc
mmrh: 3
tzmc: jdtn + cfpd
nhwh: 10
mzgw: frmh / gqjn
pncs: mwww * dnsv
cqfn: 3
pnzz: vjqt * nbdd
dzsf: nqld - dlsf
vjws: 2
lsfs: shgw * zfpf
szvf: svwv - lhpw
nbdd: 3
brqm: 4
fnph: nzsm * flvm
sclw: 3
bpbs: zssb * szvl
ldjn: 4
vhjt: 4
wjpq: 16
hmsr: 2
mbdp: jjqb + sdvl
rvcm: rzpc + ntqc
jlqb: 7
hprf: 2
nctg: wblg * gwrf
tjfb: wjpj * zfzn
trvs: 2
lbsj: gqzw * vfqd
nnvt: 11
wnss: lbpb - ccnl
scmm: ftwq * wjmf
bpqp: vchv + cpgr
pfmv: gdqp / lnwj
zfpf: 3
zvdw: dpvb + rlvh
tfnb: 2
zdsf: rvcm / wzwc
mpds: ntbp * bvlg
rbzm: ddnw + grcn
bjmz: 5
pqss: dwtq * qjcs
cnqr: fjjq / bvpc
lzcm: 5
trmq: 10
zvtj: 2
hwdl: njvs * rvjp
shgw: 2
rhrs: 4
dwzz: mcpw + rhbh
zhwq: 7
bnbs: hzlt * frgm
wfnz: 10
fpbm: 4
scfd: 2
jcqw: rfvb * pdwv
nqjp: 17
vctw: 7
hvcq: 2
rsrz: mcdr * ctjp
mlbp: hdnt * rsjv
jmmh: 11
dwtq: bnql * mnlr
nbzm: 8
zwzf: 3
rmhp: 3
pjbf: pfcj * rwrp
gtgq: 2
vzfn: zlsg + qrrf
nqvj: zfcf - njwd
mbgt: 3
tbwd: 7
mpwl: 2
lsnb: prrm + pwrv
pmnl: tfgg + pjhq
rfvb: 2
djqw: mmsl * qwfh
gqqr: jqfq * ndcs
ssgh: 3
pvbd: wdmd * sjvh
rlfh: 2
cthc: wtcv - ghms
vvgm: vmdp * qmrw
nlwf: 9
jctw: 2
rqlg: tzps * lvtm
nvrl: hghb * bgwq
vfqd: 3
lfmh: 4
mcrw: 3
gcvq: 3
dtwj: 1
wjpj: 5
fdqz: hzzm - zzqt
lqzm: 4
srfl: 2
cfsw: cllb + btlz
qmrw: pjsj - rwjc
lrbs: 3
cpms: 2
rpzj: 4
tzbj: 15
vlvb: sjjs + sqtd
pwcl: 3
hffc: nhsh * jtrm
tdzj: pgmm * wvgt
zcns: 7
wdmd: 3
lffs: jrnw + dwsz
tmds: 5
hrrc: vwfg + lzzb
ppbl: 20
cmrs: twtz + nhmt
jtrm: 5
ghtm: 19
hfqb: 5
jcmn: fttc + rvpd
rhrm: 8
hvcl: plzs * drvf
mpnz: 4
wwmb: zwlw * sclw
mdcz: ntds + hlnm
dcmn: bbgj + rzld
pmqs: jmlm * cjvd
djcd: rlmf * fflg
pqrl: 2
vlpp: tfhh * zvvl
gtht: 1
ljzw: 3
tjzl: 2
mnfl: 2
qjlz: 14
gblh: qwlc - ndrp
pndn: dzrg * tncf
jmrz: 4
bjfp: bjmz * rlws
mvql: 2
fjhh: 3
vsgp: 4
bgqq: qzbf * hfld
nvlt: sllb + ntsp
sdvl: 1
vhws: hmrq + bnbs
hcrf: 9
hblv: 2
wjjb: 18
dwrq: fsbg * cjvj
glnv: pnnz * jgwm
dbrg: zzgj / ngtc
mvtd: fpmv * qwtz
qtcj: 8
zjnr: 3
jvsf: 3
rbjv: crbr + pwmz
mwbd: gthn * ccbc
wwzr: 5
ggsm: 3
vftc: 2
pcdz: rwjr * qlnr
bngl: rpbr * trhc
rhrv: 3
mczf: 1
zhbf: 2
lznr: zcqm + zmjp
tjwh: 4
hpvf: gwtn * pfgd
lbsm: trsh * nrnj
hbwf: cfqb + lhfw
qfdp: nvjs * qrmt
rwjr: 5
rtrz: clrf * rlcd
ntbh: 12
htqw: 9
zphl: 4
wngb: vhsg * wbfm
mcpw: dsnn + dhgd
cjvj: 7
lfdp: 2
sqzr: 14
pzng: 4
shzb: hwzf - gdft
mgvf: tqzs + lqvp
dzrg: jtnq * lzcm
dbsv: 17
mstl: zstt * stgr
ppjh: 19
cgcg: dzsf * ztdl
rpbs: qzrh + nrph
dlsf: 5
gqgh: bmfv + lrmr
cmsn: bwtc * lnlj
hqhz: 2
sjjs: mqjr + nshn
tcsf: qfdp * sflc
vpnn: hcnh + dwzz
cdwn: qbrs * hsdj
schm: 9
qnwz: 6
rpjw: jbwj / sptn
hjgb: 2
pbvv: pnzz * tdfc
fvdj: 4
vflg: jtbp * vfnw
gtsg: wlzz * rhrm
jwrf: 7
rmjh: vhnw / rcvw
cftj: nrpt / jzhp
pqmc: 2
tpqp: 5
hcnh: mpns * hlqj
zrcc: ptzb * nzzf
wzcj: scbl + chdc
slrz: 2
jqfq: dzsh * clpq
prtl: 7
qttt: 4
bmhl: 2
vhbd: 3
wsmc: vjgb - wgww
rvdl: 3
pfcj: 3
wdtp: nshs + cjdl
vchv: 12
wflw: qfgh * mmsc
hzgp: lfjq + lnmc
btft: 2
fjpl: vzqq + glhf
jqlc: 13
ccfv: rhvt / mhqv
zjwv: vgwb + tdfq
rzhh: vlpt * dqhm
vngl: qhtf + lgfw
dvdr: 5
vcml: qgqh * hbwf
fgjn: lntz * wwgs
cmlr: mfms + cmsn
tnnq: dtlj * swdn
tdqp: 2
wvcl: 4
llsr: crtr * dfzn
ctzw: lbbs * vctw
twnc: wjng * glpl
rnvc: qftr - gvsm
ftfq: scqr + zqrz
hhsf: rqgs * stjw
fttc: 12
cdpn: 15
lvrw: 2
fpsg: 3
dqhb: 4
zzlp: wpbw + zwsm
zftc: rswf + zjwv
bvpc: 3
tqzs: 14
zbtv: 5
vqsm: jmrz * zfgd
cncb: 3
jnpt: 13
cdpq: gjcj * znvn
fpnh: 2
gtsh: 5
bcbq: 2
hvgh: 4
mcjp: bwzg - vcjs
cgnr: hfnq * mnsr
lzhr: pclj * sdpm
zdnr: jdjt * vqzg
wvff: qlww - blcf
tdbp: 6
mbbb: 9
splj: 1
djsj: 7
wrzs: 2
qbvj: fcjg * dhmt
rwvs: 4
fwgh: lbdq + dwrg
wvgt: gctm / bqbv
gshw: 4
clbh: 4
zfcf: dtjj * fbvw
zfzn: zhwq + bcpw
zjhz: 16
hhrd: 2
cfmc: wftf * scmt
zbwd: 2
cbbq: bgqq + jzjv
zcfs: 6
ctdh: 10
hsdj: 2
humn: 743
cfpd: wnss / mvql
qjcs: 2
gvdh: smwr + pfnp
lmnh: ncjt * plcb
fbnn: 3
zhhw: tljr / tbtv
bnfl: fjjb * gfds
tssj: tjfn + vbfp
fpbf: swbj * pqss
sghd: lflg * frww
qlww: ptjv * npgl
npwd: tpph + dmdl
rjgp: 5
nnzf: czdb * fwtl
ptjv: 5
pggt: 7
ntbp: 2
fcjl: zrlp + gbrl
gdft: 5
wcch: 2
jwmq: zrcc - sghd
prdh: wqwf * ncwg
gqld: 3
sqpt: 3
tncm: 17
qvzz: 2
mlfp: 2
phjj: npcl / lfmh
wdzb: dwfs / hjzt
msmf: sdnb * vngl
tngr: 4
pwtw: hpqs + rgcf
pdrn: pgwc * ftqm
gfhq: clnj - hsdw
lsmt: hccd * vnnb
clld: jjhp + fvgz
hpmt: 4
qlwn: 2
vsrl: 5
tqhz: blrq * zchh
sqwg: 2
ghms: 2
hffp: 4
lhpw: fqff * fvpb
dcpp: 11
mjhh: hwld / gpnb
czhp: 3
ngjr: rvtw / fsfb
qzrh: npwd * przn
lfrb: 5
fsfb: 4
lsgz: wtvz / vbth
dsqz: wbvb * lrhj
ntrp: 16
hhbh: 14
wfsl: gczm * njdz
bggr: llvd + gbtc
mpns: 4
fjsd: 2
schr: fbjg + snrp
tjrz: mbbb + nphq
jrmj: pngb + ttlw
mtcb: zdwr - thvw
cnhr: 2
zswr: cnrj + bnpz
tfhh: tjrz + dpjj
cnrj: dgsg * mdsv
rrbp: 10
qvdq: dfmw - rbjh
mnlz: 5
spcl: 3
dlgb: tjfb + jvnr
ssqm: 16
vtqp: hcsg + fgjn
plfs: sjjd * cnqr
nqdl: 3
rlws: 5
sdpm: 2
pwbf: wvps * hmht
pjmn: rvhq + psds
wggn: 9
trhc: mgzh * flzh
hnql: jbfw + zght
ncfr: tqlt * chjr
fspp: bwbt + vdbw
htjt: 1
dvtf: 4
srcf: 5
cfzp: wvql * dlmd
bnpz: hzms + gntc
jtrj: vpbr + bmqw
fpwl: 3
vnnb: 6
tvll: nlsf * lhzr
njrm: 6
vjss: zwnc - nmdd
qttw: wtwf + qmwd
qhtf: vpfj + fvtz
zntl: 4
lqhq: 2
zqrz: 3
mmfl: tdbp + gttd
jwgv: wgbg - mczf
fwwg: btsw + fztj
ffhp: 2
czdb: pprp * fllf
hbbg: 16
crwj: mjqd * srwg
hsbn: 18
rvjp: pzng * fmqv
jdqc: 3
wvlr: 11
bnzj: 2
zbqw: frlg * jhrc
ssgs: dzht * qvzz
lrcd: hztq + pslh
vwfg: cbwh * dvmq
glpl: gwwr + fpnh
cffg: 3
gntc: wrbr * nczg
hdmj: dcpp + pwtw
mhmr: 15
qlwr: 4
tcwc: zhdj * qtgc
pnlh: jvqz + gvmb
vzsb: 2
pqlh: rjtn + fpwl
cqqs: 2
bvlg: chqq + nctg
dmwb: 14
hmcl: 16
zzqt: 1
gqjn: 2
sfgt: 2
nmqn: 9
nqwt: 2
zzgq: 7
vwjl: rzhh * fvnz
qptb: 19
vlgs: jmbz * gtsg
mbbh: 2
bbfc: zjqf - gcrr
hpmw: 3
jvnr: fwwg * phvv
pdrb: lqtv + wjlz
rlpw: 2
vcjs: 2
wmzp: fcnm + dlfw
mqjr: 4
smzd: 2
rwrp: 9
hjbn: 6
swws: rlzs + prbf
vmvj: 1
ngtc: 2
wvjv: gpcp * grvv
gbtc: 1
zhrr: cccw * pnlh
nqld: mfhd * tdmr
tbjr: 11
nczg: 2
vgdn: hcdp * rbzm
jtnq: tbsp + wdgd
gmhw: trmq + dtwj
wczw: bjdt * zbwd
tchm: hwbs * bqlm
vnlb: 4
tmmc: 9
cmrj: gcjj * spwq
tmwc: 5
srps: qldh * llrp
dzpc: rsrh * mpbs
tsjr: qnpv * zcwr
blrq: 2
lszj: nwdc / zrwv
zzdf: cfmd * cfgj
rhvt: gcqq + fdhq
jchq: zwgj * qbnb
pbbh: gcvq * spfm
wsrg: 3
dfbt: 3
qnwd: 15
trsh: jcnn + wggn
cttj: 3
llrd: 2
bzcr: rshw + vfhb
sdnb: 2
wrjm: 6
qwtz: njrm * nnnq
sncz: cthc * ffdw
bqdn: 1
vjhv: pcdz - hscw
wvdj: wclw * wsbt
zblz: rlpw * fvdj
bjrm: 4
qtcq: 5
slms: 4
vgcz: pftw + wjpq
sllb: 1
qwlc: nhdr / vwzf
fjjq: vbrs + lvcm
bswp: lfjv + gqbj
gddh: pfzp * jggw
whww: bgth * tdbj
lcrc: 2
wwvp: wvcl * zbwc
tdrf: 3
mjwl: 7
gbcf: zblz * mzgw
pzds: swfs * fzpm
glzq: 9
nffc: pvlj * qrfh
ncbl: 9
fzds: 2
ssbl: ftnf * nrms
qrwb: lsrl * nqjp
jqjs: 4
szvl: dzhc / jwgv
ttwt: wdtp + lfft
vvpg: pbvv - nsnb
pqhz: mdnd + vdpp
jzgb: fsqj + jchq
wqwf: 7
zcqm: 1
rchv: jmcc + cfhw
hhqt: 4
mbht: ghrt + lctc
ffbl: vjtc * bjsf
ptpr: mstm + hswv
wdgd: qffg + wglq
hfft: mgnz * svfj
gmcl: zptt - dmjt
frdt: rqfl + pgpr
jgcg: rmlz * gwmh
svfj: rszj + hhfm
vzhs: ccjv * crwf
qwgf: plfs * fdzl
bqbv: 3
chwv: plhc * gpwq
dsnn: pvnl * rrnj
jptq: 2
wgjq: 3
hnbq: vgmb * zzhm
spwq: 2
smwr: stcb * lbbn
swqs: ntpt + ntqm
lsrl: 4
lfcc: dsbv - cpvp
lvcm: cqfn * prdh
nwdj: 5
bdvh: 2
mjqc: ttwt + rsbg
tjnw: zggf * qbnd
zmcn: 7
vfnw: 2
zbfc: cprr * fjrg
djdg: 4
lhfw: pndn / nptr
ltgn: jmww + jztb
mhlm: 2
rgcf: jmnc * lpmj
dsft: 3
hcbr: tzbj + jvcb
lbdq: 5
qflr: psrm - chwv
vdbw: gcmz * cfzp
fhvl: 2
vcjn: 4
fnnc: 4
jhjj: 5
gqfz: stcv * jstr
gndt: gnzv / slhr
jjtn: bggr * hwsd
bnzf: hwct * zbgw
nshs: 5
vqht: 3
dshv: tmnr * zbtv
gccp: vdjf / tjzl
ghlt: 9
qzbf: 3
gttd: 7
hfld: bbfc + stqq
mpbs: jsmz + jtrj
ndvg: jhgq / dbmw
frlg: 11
tfgc: 4
dwbv: 14
vwzf: 2
ctgl: 4
cfhw: 5
gmcc: 3
nphq: lzmm + pwbf
nrfj: 3
zhdj: 2
swfs: 2
zhnj: 10
wzqh: bbjb + vfvs
vdjf: cfsr * rrpj
lbbn: 2
hzfm: tvrr * pfjt
vscb: 4
fwcf: bpmn * pvbd
vdjb: 5
sjjd: 5
fmqv: 3
lqdl: ldjn + rgvb
shsn: 2
rlrq: 7
fllf: 2
fzqf: zmmh * bjlf
jdjt: 2
tntm: bdhr * ntbb
wfdg: 16
zfgd: nmtb / bpmc
ndnl: lmnw * qbvj
vjqf: 3
shmv: 9
pzzq: 12
psjv: 3
rscr: 5
cwtc: svzg + msrg
lmrb: htsb * ztst
bpld: hmcj + lsfs
gtwz: 2
gvgd: 5
jdww: 2
dztp: wcsd + lzpp
vwjj: 1
wfqv: 3
fbmz: wgjq * pjsc
fqzz: 2
lgsj: 1
stqq: wzcj - gfpv
tplp: 1
dqhl: 19
vgwb: ldvw * wdzb
vgmb: 2
rldp: vprc * gfhq
cdsz: vbfh * wshv
dzvf: vnlb * mrvh
bgmf: lcdt + fdbd
btcb: 2
mfhd: 4
gvrq: 3
hwbs: 11
dbfv: mvqw + wwvp
rvvm: 8
clfh: 6
ngww: jrmj * dwcc
svwv: hnbq / nnww
ccbc: qqvg * tpqp
crzw: vgcz * njfl
lfft: qzww * fnph
mstm: clfh + cmnv
wgjc: srrc + mdqq
tthb: 4
mmsc: 2
gwtn: fpmb + wlhq
nrpt: 16
mgnz: 5
gzfd: 2
hsdw: 4
mwcd: 2
gpjz: tgmb * tnnq
hjzt: 2
nmtb: ppdr + ddjc
tzhs: 2
stcv: 3
pzvz: 2
ghrt: 6
rpqs: 6
rtqh: pbbh / ggsm
rmbl: pmvd * mmtj
gpdg: zqpf + vzdl
rvbg: shfm + fnrt
vhhv: jwsd + jfrt
tcbz: gmcl + lfnn
jncr: rpgv + lznr
dbtz: 12
hgvp: 3
qtgc: hddl - fhsn
tpmt: 2
gtws: 1
wdsw: vtqp * slms
snrp: 5
pvng: hfbq + cpwm
rlzs: 6
hjhq: qjlz + wnzf
jwhl: 2
jqmn: jsmm * cdmt
bpmp: 3
tpwg: 5
lpdj: 10
phzt: 2
tdfc: tntm / jzfn
sgfw: ltmg * pqlh
ndcr: 9
gwwr: 5
lnbl: 4
rrgf: 2
clwm: dnwl + lsmt
rvsp: hpgd + bgmf
cbwh: 2
zhdz: 8
ntbb: 5
wclw: 3
wrvc: 4
cpvp: 4
cjvd: 2
wcvw: hblv + hpzj
srrc: hjgb * gmhw
lgdv: qlln * pbff
wmmg: 2
mnld: 2
czlt: lszj - wfsl
tcwh: gddh - hlbl
lnwj: 2
dmjt: tqld * bmhl
wglq: 3
jmlm: 3
vrpd: 4
ccnl: ftsj * swws
pvlj: 11
bnql: 3
njwd: hhqm + dsjm
pjgw: 2
swcc: 5
hzzm: mdfc / mbbh
mthv: gqqr * jblq
pfrc: 2
jqrh: 3
lttj: qnvw / dzdb
gfds: gdbj + vlzh
tmnr: nzcw - rmsj
lfjq: lzhr * wsqb
pwmz: 1
jzjj: tbmz + mdjm
mnsr: 5
twtz: 2
htzc: 1
dbnz: bjbg - jzch
vgjl: 4
hcdp: 2
bpvn: hzqg + pzzq
hztq: wjjb + dtgf
tqzh: 2
bgbh: 2
zgmj: zbpm * dwbv
wrmt: 5
bdlt: 4
lwln: mphm * tdbf
pspm: wwmb + hsdq
ptgc: srps * fjlr
qqzt: lqnm * zhnj
fjrg: 11
tgjl: 1
gmdg: 5
hljw: pqds - zqzr
dhgd: 8
lqtv: mtrh * nrfj
qffg: wfdg * mqsz
tzps: 2
wzld: llsr + nldv
tmvf: 5
vlzh: scjh * blgm
smfj: sjdg + gfsp
lzpp: hvlr * sfgt
cgtm: 5
zzbp: clld * vmfl
szdr: 3
clpq: dmwb * tpmt
jmcc: 2
pwnq: 2
lssd: bsbh - bpmp
flmh: cppr + pwsh
tncf: dbdh * ttvf
bmgm: 3
bpmn: 5
pvnl: 4
vfmp: jhzc * bglq
bbgj: fsdz + vwjj
jwjc: pwzb + dzzp
vdgh: vndv * mhlm
zfbf: vvvg + jdqp
hgpd: 3
lgfw: cdsz - ngww
jsbd: vpnn + lrnz
zrqw: 3
jzzm: 7
ldnw: 4
rsgb: hdmj * mlsf
pftw: 9
lsbj: hvgh + mbpp
wblg: rvbg + cgmn
tbrf: 3
pbdf: mlbq + gpjz
rbjh: lwbr - qvwg
wwtb: 2
tdvn: zbvj * cncb
mnzn: pdrn / zbgt
vqsn: cftj * dzst
zsjt: 2
zlwd: hwsg * vcqf
jvsr: rvnt + vqsn
gfns: zgql + llzj
swjn: 1
vdwb: lvrw * ncjp
sbwh: tjwh * nbdh
bpmc: 2
zmzg: zdgq * mffq
hpjz: 5
dwvs: hjdw * lsfg
spfm: 10
gfpv: 14
ntlg: 9
wsbt: 2
jzch: vzfn + jzgb
nfnw: bzbn / sfwq
wgww: 4
frgm: jwrf + pnsq
rszj: 2
dzdb: 4
vvtj: 2
fzlb: 5
pltr: 3
hwld: bvjp * qtcn
wvnt: gjfv * vhbd
lzvf: vwjl + rslf
hjht: 6
vfgn: jwjc * ltgn
srzp: 2
tfhg: dqhb * pjjh
wshv: rpzt + dbws
thvw: rcvb + rmhp
nptr: 2
rfpf: 7
nzzf: wswr + dtsh
gqbj: tjbw * qjsd
vcqf: 4
sgch: lnbl + nstn
qgqh: 2
qtpn: 1
rlmf: wscl + ssqm
jlpj: rqwr - pwhv
bmjb: 4
wzhb: tgpt + blfd
zlrg: 13
rrpj: pzds + npwv
qlzn: 2
lmvf: 2
mdgw: 4
mdnd: vfps + pnlg
smbb: pncs + lmml
dppc: vjmz * zgwf
nljl: 2
lbrn: 5
rcph: 4
jwsd: 8
tbtv: 2
zchh: qnfh / pjcw
qfgh: cbbq + cfmc
vfrw: 3
mfgc: 2
pmjv: rhhg * tdbc
sgsz: fspp / nblb
hmcj: 1
drgq: ggrv * rmbl
hbpr: 6
qbvd: ljzw * ftzc
jzrq: 2
hlcv: 3
nnww: 2
dzzr: trvs * zmzg
bsmg: zqnp * glzq
zpld: vlvb + tjhv
hmht: 3
qbrs: dngq / zqpc
wgcw: 5
zhvb: zdrz - lmrb
ntwz: 3
drvf: jndp + mswz
sbsm: sfgb * dfmc
vtzj: 4
hswv: 12
clnj: 18
wfjb: 5
mhzl: vgdn + pdrb
sbpw: 6
rfvc: zmqp * btft
jpjn: 10
pqds: wldc * hhfp
gwnf: rwtn * rtqh
sgld: 7
wjns: gvlv * gmcc
gvsm: 17
jjdq: fzhz - ldnw
nhsh: grhv * wcch
zqnp: 10
fbvw: mthl - dsqz
mbpp: 19
drzz: 4
njfl: vlgs + nfmm
mlsf: 5
pndc: hfqb * gtsh
rpgv: 1
mftp: 2
root: wvbw + czwc
vbfh: 2
fdzl: 3
zqpf: 19
dlmd: 3
shvq: 2
mlbq: tcwc / bppd
fflg: 4
fzhz: czjl * dlqs
rswf: sshl + sgld
zjrq: 5
mnjh: pgdh * wsrg
zflq: 2
wnzf: 8
pgpr: sbgd + wjvg
nblb: 4
mffq: fcws + lsbj
sqqr: 13
nldv: rzzp * hfhd
wmtf: 3
qtcn: gtsf * hprf
bvjp: 17
gzqj: 2
pnsq: 9
fcfc: ngjr + wtws
wzgg: 2
flzh: 2
bjsf: pswc * hhzz
vhnw: vrtb + bjfp
dzzp: 1
dmcf: smbb * nlwf
phsv: hmcl * ztfp
rzld: 10
blgm: 2
mwww: hcrf * ssgh
cftv: lffs + grff
qbnd: jqlc * sqqr
gsnz: zcns * hwpf
dwfs: tqcp * tfgn
hhfm: 5
hmrq: wzhb + bngl
qftj: cgnr + wgmp
rfnp: 9
ndrp: cpjd * bhcr
lntg: 4
fvnz: dbtz * tszg
cpmq: 2
bwzd: rldp / hchd
bbrd: rbjv * bcbq
mrfd: ngnh + nfrr
bhcr: rpzj + lbnn
gnrr: rnfw * fdms
szqv: btlq * dlqq
gwrf: wngb / mnfl
sldj: 14
nhdr: dbrg + jzbs
wscl: zjrq * lbrn
gctm: zlrg * mbgt
gpcp: 13
jwrr: 3
flsl: bnbm + qvdh
zwlw: qlzn * dqhl
mhqv: 7
hlnm: 3
bcpw: 12
lltr: 5
rlnp: humn - qflr
rvtw: sncz * rbms
nmrt: 5
bgsl: 17
tjhv: 14
gpnb: jqrh * qwns
rvnt: nwdj * cdpn
pjvm: rtqj * sgfw
lmfg: wgcw + wtgw
sglz: cnwq * rchv
ftqm: rlwt + tbth
rpzt: rznt * mljj
mtzb: 4
qvdh: 1
lvtm: hlhz + hlcv
pgwc: 10
dhmt: 2
ppdr: ppdq + ljmh
trwd: ljbj + jnqb
rplj: zzgq * tcbz
jgwm: 5
wtwr: wtdw + hthd
vprc: qntb / prdb
qdtm: qtcq + rnnj
rjlc: 2
fbjg: swtj + frsf
vpwl: 3
vhsg: 2
pgmm: 3
zggf: 3
hcqw: 4
fwtl: 5
cfmd: 3
gjfv: 13
tbmz: pfmv + vcml
njww: 10
fcjg: 4
bcpl: bfsw * qtsd
vtjn: sqwg * tzmc
pscc: rmvf * slrz
hgvn: lqdl * qvbd
wvnj: mbdp * zzlp
swgs: 19
wzps: 2
lqvf: rlnp + bhzv
crtr: vcdb + wdcs
mthl: hrrc / mtzb
gcvc: 2
rcvb: pgzl * mmrh
hbfl: rwvs + psnz
shtc: vsgp + fmbt
bgcs: 3
ztlc: qmfj * drbh
ncjp: vjhv * cfsc
ccjv: 5
chqq: rpbs * cjdw
fpmb: 7
pnfv: 12
cnbn: 17
vnft: 20
qmrl: wfpc + swqs
hbrm: tgjl + ftbc
njdz: gbgm + mlbp
qlpt: 4
tmwl: hjht + lqlc
jvcm: 6
qvqf: 12
hhqm: fzlb * gccp
lmwn: 5
zbgt: 5
qlgr: 2
tjhl: 4
chdc: 4
cvdp: 2
qdjp: 2
bzpg: 2
fmbt: 4
qbbc: cfsw + vfgn
qgms: 5
mqsz: 2
ddjc: wgjc + nfnw
chjr: 2
hcsg: 1
tgpt: 15
rbnp: 11
wwgs: 5
jfrt: 3
cdmt: spfl / gzfd
dqjm: dbfv + cwlj
qtsd: 3
vmfl: 3
cfsc: 2
dbmw: 2
ztdl: 2
mmbd: nvdm * fcvl
snts: ndpn * ppbl
ppdf: 4
cftn: 4
rzpc: 19
pshd: pljm + rpjw
sfgb: 3
btwq: 3
wlfc: glnv + fnnc
pslh: gtpr * jlrw
rvts: 1
grcn: 3
plcb: 3
rgvb: 6
hfhw: 9
fjlm: nszm * zrqw
gwmh: 3
hsdq: zdsf + ccdh
ntjr: 3
crcc: 2
jgrv: 2
zbpm: 2
wlqf: 2
pfjt: 2
rqfl: nmqn * zpbm
bqlm: 3
mmsl: sgsz - vlpp
wsvq: wrjm + ntlj
sfzn: 7
tjbw: 5
rlbl: 5
wjvg: dbsv + tzhv
qcwq: hwdl / vscb
zzhm: prdn + zftc
smpv: rnvc * jjtn
jvhv: ljvc - pjvm
blfd: 8
fvgz: tqrs + lrcd
hghc: rsgb + qvdq
cpgr: 1
hvlq: lttj * prtl
mzst: 5
ppbn: 3
qpzd: hbrm + lccr
wjmf: dfsl + cjzz
lfzp: flmh * tfgc
bwbt: pqmc * gfns
zmmh: 6
rbms: rfnp + pqcz
msgz: 1
ddrp: 3
ljfs: 4
jdvs: 1
mfms: wnlm - tltt
phmp: 2
nhmt: 5
bgwq: lfcc + hpvf
zzhz: 4
fgqw: tdzj - hfhw
vndv: mfnr * jqjs
tbnm: 12
qvzl: 6
lscj: vftv + sqpt
rvst: 2
jcnn: lrwg + zgjf
prbf: 1
nzsm: 17
zhmn: mbht * pftd
lddz: 16
qhmh: 2
jmnc: 4
jlgc: cpmq * fpbm
tdmr: gshw + hvtp
hfnq: 5
jvcb: mhtg * zgrr
mljj: 2
tclq: 4
dfmc: pwzg + bswp
pwvr: pcpg * vjbf
jdtn: wztr + rlvz
rvhq: fpbf + plcm
bwcl: vvpg * ctzw
qnvw: hzfm * bdvh
gbrl: qvqf - zwzf
zbwc: 2
rpbr: 3
jmjc: sdcr + lpdj
bpzr: fqzz * vfrw
cccw: tbjr + zpmh
hfbq: sptg * czlt
vvqq: 4
fcvl: 2
ngtn: 10
qjsd: 5
ltmg: 2
jdzs: dbfl * mstl
szcc: 4
nzcw: 13
jlrw: wqzq + mvsr
flpw: gpwf + vgrf
pgzl: mnld * hrrq
vfsc: 1
ntpt: bnps + qlwr
dvmq: hgpd * rmqz
qvwg: wmzp * tmmc
spbj: 3
gdqv: mjnl * twnc
zgjf: ncbl * dsft
dzdl: 2
vzbc: 2
tdwn: 1
rsjv: 3
qwfh: tdrf + bdbl
qrmt: 2
jzhp: 2
lzzb: dbnz * prtt
lmlj: 2
rjjg: 6
gnzv: rvsh * llrd
cdzr: 17
tqgr: 2
pswc: 3
tsrz: 16
jnnz: bnrm * rwnn
gczm: 12
fchv: 5
wrfl: hsbn - lgsj
fsbg: 5
wtcv: bjjb + nbzm
bqdm: tzdq * mpds
lzqf: 3
hchd: 2
vfgz: 2
dzht: 4
bbhp: 3
cmnv: pmnl + hbpr
nqhr: qntt - zsjt
ntsp: gqld * vzbc
wjlz: 5
stjw: hbdf + jfls
nvjs: 3
mrqw: plng * swgs
dbdh: rmqv * gcvc
qmwd: 3
gcqq: mqfv * fhrt
wtdw: 5
fhrt: vvgm - jnnz
fvtc: 3
jbfw: vmgv * dfbt
cprr: 2
wcsd: qnwz * hmnj
gfsp: ptrp * vsrl
jstr: 4
pphb: 5
mwgp: lfzp + ffhr
pwhv: 4
hfrw: 8
ftzc: 3
shcv: 2
pmvd: 2
zbmr: 2
dlfw: 1
bbjb: 6
sjvh: 7
pwzb: 9
lrhj: qdtm * bpld
wtws: hldj - zsbv
wpbw: 4
wphg: tsrb * dzdl
ghqq: btwq * whzj
psrm: bpvn + tvll
nbtt: 2
zlcr: 3
hgdm: pfrc * ngdv
ffdw: 4
psnz: wfnz + brgn
jbwj: wjns * qdwv
gtpr: 5
qlln: wfqv + hcqw
dqhm: zfbf + pwvr
rmvf: 13
ffbf: 6
scqr: 4
zdgq: trwd + vrhp
zbvj: ntwz * wwtb
jzbs: fzvc * cgtm
cflt: fjhh + rhrs
btlz: qhpp * tqgr
wfpc: tmpj * ngll
lslc: 2
crft: fzqf + wzhm
ppgm: gpfs * zflq
vvhz: gvrq + pbbr
ntqc: whrt * bpzr
scbl: cgbb * vwrr
ljfq: 3
gvlv: 4
tgmb: 2
rtmm: 2
grff: wvff / clbh
wjjz: qlwn * pqhz
gssp: 2
hlrv: smpv * dwlz
hzhv: tthb * zzjd
tljv: 7
lhjd: 2
sflc: 14
rtlt: nnvt + hgvn
fjsb: qbvd + drjt
mrvh: 2
rlcd: 3
jgch: 5
vgrf: tzlj * zhfb
rhhg: 7
hpmr: pspm * vftc
fcbf: 6
zwgj: 2
tqcp: 2
ffhr: lqvf / nvlt
gzzp: qwss / jzzm
lznt: 2
vlpt: 2
zbcn: 3
rpbc: gtwz + hbfl
zwtb: jzjj * zvdw
btlq: ljfq + mjqq
hmnj: vfgz + fbfr
msrg: 4
fztj: qlbf + jwrr
hpqs: wzps * spcl
rwnn: 8
rzzp: 2
rjsd: zzdf + vrpd
fgww: bqdn + stvq
ddnw: 4
hvlr: 3
wqvg: 5
nrms: mtcb / jncr
cgpw: 8
fhsn: 2
rvsh: tbgt * fpsg
ttzt: mpnz * djcd
bqvm: 2
dhhv: znmr * zjhz
pbff: jlqb + jgcg
zzvr: 5
hbhv: 2
gqqc: tclq * zzvr
zpmh: bwzd / wrzs
vcdb: 2
bdqj: 3
tnsc: 2
cgzq: 3
mdsv: dlps - ncmd
zphj: zhvb * ffhp
cnwq: dmjv + jvcm
nfrr: 3
hbts: 4
pglf: tcwh + hjbn
rnnj: 2
rrnt: 5
dpvb: 10
wdcs: 5
tdbj: 7
phvv: 2
pfgd: 2
fcws: ghqq * qhmh
jmhf: frdt / bqfn
bhhr: 8
lvbm: gvdh * mcsc
fszh: mcrw * gndt
wbvb: tdwn + mmwv
jblq: zbmr * hlwl
hjdw: 2
gmqs: 7
ljbj: mjhh - djdg
splv: dzsc * crfc
qwhp: 5
rslf: mhrf + jdpp
hlbl: 20
dtsh: nqvj / rrbp
zmqp: lssd + hljv
sjcs: wvdj + jhjj
bhzv: qwgf / bdqj
jwgn: 5
qnpv: 2
vdpp: 4
hghb: 3
nrnj: 2
flvm: 5
cslh: 9
lpmj: wwwp + vtzj
wmqz: cmlr - shwt
hllh: pscc * bmjb
gfsw: 3
rwjc: rscr * mvdj
lsbv: 3
zgql: cpwg / rptt
wsqb: 3
fdms: 5
zrlp: 14
zdrz: twft * jmjc
dbws: cbgj + nqrc
cgmn: mmfl * rpqs
cbgj: 2
ctqr: wrvc + qwfm
lsfg: rjjg + htjt
tsnj: ppjh * cmhw
cfqb: wzpd * dlvd
ftmn: 2
dffc: gfsw * vdhz
ftbc: 6
zght: sbsm / mhjl
zqzr: 11
nbsb: svzs * zwtb
qftr: tjnw + nrqf
gbpz: mtgw / bzpg
smgn: 5
rljz: cvdp * cdbq
czjl: 3
nsjc: jnpt * lfdp
wqcw: rszp + ntsw
htsb: 2
gpzg: ndnl - tmwl
dpvd: lqzm * ftmn
hwct: 3
dzsh: 2
jlhc: 5
wqzq: 2
hpgd: wvnj - fdmm
bglq: 2
wbps: 3
lmrp: 4
vfvs: 1
rncq: 3
dlvd: hffc + vjss
hdnt: 14
vlsf: vpwl * dwrq
ljns: 4
pftd: 2
lqlc: 1
pqcp: bvsj * jdqc
wnlm: tqgg + bnfl
mmtj: 19
ntsw: cttj * qpgm
lntz: 2
nhln: schr / jctw
qqvg: gsnz / zhll
dgdg: 3
vbrs: lzqf * rfvc
fbmv: qbnp + fdjq
ggrv: 5
tpph: lqfz + mwbd
hlhz: fcbf + szvg
cwst: 2
gwqr: 1
npcl: snts + hllh
sshl: 19
hvhb: brqm * hpjz
qlnr: 19
vzdl: tsrz + qftj
pnnz: 5
hmvs: 4
dnwl: dclt * lntg
pqcz: tbrf * mbwm
jzfn: 5
mdjm: cdzr * bpbs
scjh: 3
pjcw: 4
qwns: 2
qdwv: crsv * flhw
fcnm: tmwc + hnrg
jztb: 2
dfjs: 2
mwbz: pphb * tpwg
vfps: cmrs + mwbz
nrqf: szqv + wzld
mtrh: 4
jrnw: qpzd * swcc
mbwm: 2
lrnz: nqhr * zntl
tjfn: 4
bdbl: 4
hhzz: 3
cdbq: trnn * zdsw
vpsd: cwtc * vdjb
hfzc: qdjp * hpmw
zgrr: lgdv / ctqr
rmqz: rpbc + drwl
znmr: sdvt - zbcn
nqrc: fbmv * rbnp
qrqc: dvdj - dffc
hhfp: 4
bdhr: msmf + swcl
lqnm: 2
cppr: mcjp + nnzf
ndcs: 11
npwv: 4
frww: smzd + tljh
blcf: nfwl * fgqw
pczr: 14
shfm: ncqw - sjcs
dtlj: 2
cnjt: 14
pnmt: fwzd + nfjl'''

# COMMAND ----------

import re


def resolve(name):
  if name not in monkeys:
    return int(name)
  
  args = monkeys[name]
  if len(args) == 1:
    return resolve(args[0])
  
  lhs, op, rhs = args
  lhs = resolve(lhs)
  rhs = resolve(rhs)

  if op == '+':
    return lhs + rhs
  elif op == '-':
    return lhs - rhs
  elif op == '*':
    return lhs * rhs
  elif op == '/':
    return lhs / rhs


monkeys = {name: args for name, *args in [re.findall(r'[\w+\-*/]+', line) for line in inp.splitlines()]}

answer = int(resolve('root'))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Due to some kind of monkey-elephant-human mistranslation, you seem to have misunderstood a few key details about the riddle.</p>
# MAGIC <p>First, you got the wrong job for the monkey named <code>root</code>; specifically, you got the wrong math operation. The correct operation for monkey <code>root</code> should be <code>=</code>, which means that it still listens for two numbers (from the same two monkeys as before), but now checks that the two numbers <em>match</em>.</p>
# MAGIC <p>Second, you got the wrong monkey for the job starting with <code>humn:</code>. It isn't a monkey - it's <em>you</em>. Actually, you got the job wrong, too: you need to figure out <em>what number you need to yell</em> so that <code>root</code>'s equality check passes. (The number that appears after <code>humn:</code> in your input is now irrelevant.)</p>
# MAGIC <p>In the above example, the number you need to yell to pass <code>root</code>'s equality test is <code><em>301</em></code>. (This causes <code>root</code> to get the same number, <code>150</code>, from both of its monkeys.)</p>
# MAGIC <p><em>What number do you yell to pass <code>root</code>'s equality test?</em></p>
# MAGIC </article>

# COMMAND ----------

from scipy.optimize import root

def resolve(name):
  if name == 'humn':
    return 'x'

  if name not in monkeys:
    return name
  
  args = monkeys[name]
  if len(args) == 1:
    return resolve(args[0])
  
  lhs, op, rhs = args
  lhs = resolve(lhs)
  rhs = resolve(rhs)

  return f'(({lhs}) {op} ({rhs}))'


monkeys['root'][1] = '-'
exec(f"f = lambda x: {resolve('root')}")

answer = int(root(f, x0=0, method='broyden1')['x'])
print(answer)
