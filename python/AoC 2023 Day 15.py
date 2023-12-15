# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/15

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 15: Lens Library ---</h2><p>The newly-focused parabolic reflector dish is sending all of the collected light to a point on the side of yet another mountain - the largest mountain on Lava Island. As you approach the mountain, you find that the light is being collected by the wall of a large facility embedded in the mountainside.</p>
# MAGIC <p>You find a door under a large sign that says "Lava Production Facility" and next to a smaller sign that says "Danger - Personal Protective Equipment required beyond this point".</p>
# MAGIC <p>As you step inside, you are immediately greeted by a somewhat panicked <span title="do you like my hard hat">reindeer</span> wearing goggles and a loose-fitting <a href="https://en.wikipedia.org/wiki/Hard_hat" target="_blank">hard hat</a>. The reindeer leads you to a shelf of goggles and hard hats (you quickly find some that fit) and then further into the facility. At one point, you pass a button with a faint snout mark and the label "PUSH FOR HELP". No wonder you were loaded into that <a href="1">trebuchet</a> so quickly!</p>
# MAGIC <p>You pass through a final set of doors surrounded with even more warning signs and into what must be the room that collects all of the light from outside. As you admire the large assortment of lenses available to further focus the light, the reindeer brings you a book titled "Initialization Manual".</p>
# MAGIC <p>"Hello!", the book cheerfully begins, apparently unaware of the concerned reindeer reading over your shoulder. "This procedure will let you bring the Lava Production Facility online - all without burning or melting anything unintended!"</p>
# MAGIC <p>"Before you begin, please be prepared to use the Holiday ASCII String Helper algorithm (appendix 1A)." You turn to appendix 1A. The reindeer leans closer with interest.</p>
# MAGIC <p>The HASH algorithm is a way to turn any <a href="https://en.wikipedia.org/wiki/String_(computer_science)" target="_blank">string</a> of characters into a single <em>number</em> in the range 0 to 255. To run the HASH algorithm on a string, start with a <em>current value</em> of <code>0</code>. Then, for each character in the string starting from the beginning:</p>
# MAGIC <ul>
# MAGIC <li>Determine the <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">ASCII code</a> for the current character of the string.</li>
# MAGIC <li>Increase the <em>current value</em> by the ASCII code you just determined.</li>
# MAGIC <li>Set the <em>current value</em> to itself multiplied by <code>17</code>.</li>
# MAGIC <li>Set the <em>current value</em> to the <a href="https://en.wikipedia.org/wiki/Modulo" target="_blank">remainder</a> of dividing itself by <code>256</code>.</li>
# MAGIC </ul>
# MAGIC <p>After following these steps for each character in the string in order, the <em>current value</em> is the output of the HASH algorithm.</p>
# MAGIC <p>So, to find the result of running the HASH algorithm on the string <code>HASH</code>:</p>
# MAGIC <ul>
# MAGIC <li>The <em>current value</em> starts at <code>0</code>.</li>
# MAGIC <li>The first character is <code>H</code>; its ASCII code is <code>72</code>.</li>
# MAGIC <li>The <em>current value</em> increases to <code>72</code>.</li>
# MAGIC <li>The <em>current value</em> is multiplied by <code>17</code> to become <code>1224</code>.</li>
# MAGIC <li>The <em>current value</em> becomes <code><em>200</em></code> (the remainder of <code>1224</code> divided by <code>256</code>).</li>
# MAGIC <li>The next character is <code>A</code>; its ASCII code is <code>65</code>.</li>
# MAGIC <li>The <em>current value</em> increases to <code>265</code>.</li>
# MAGIC <li>The <em>current value</em> is multiplied by <code>17</code> to become <code>4505</code>.</li>
# MAGIC <li>The <em>current value</em> becomes <code><em>153</em></code> (the remainder of <code>4505</code> divided by <code>256</code>).</li>
# MAGIC <li>The next character is <code>S</code>; its ASCII code is <code>83</code>.</li>
# MAGIC <li>The <em>current value</em> increases to <code>236</code>.</li>
# MAGIC <li>The <em>current value</em> is multiplied by <code>17</code> to become <code>4012</code>.</li>
# MAGIC <li>The <em>current value</em> becomes <code><em>172</em></code> (the remainder of <code>4012</code> divided by <code>256</code>).</li>
# MAGIC <li>The next character is <code>H</code>; its ASCII code is <code>72</code>.</li>
# MAGIC <li>The <em>current value</em> increases to <code>244</code>.</li>
# MAGIC <li>The <em>current value</em> is multiplied by <code>17</code> to become <code>4148</code>.</li>
# MAGIC <li>The <em>current value</em> becomes <code><em>52</em></code> (the remainder of <code>4148</code> divided by <code>256</code>).</li>
# MAGIC </ul>
# MAGIC <p>So, the result of running the HASH algorithm on the string <code>HASH</code> is <code><em>52</em></code>.</p>
# MAGIC <p>The <em>initialization sequence</em> (your puzzle input) is a comma-separated list of steps to start the Lava Production Facility. <em>Ignore newline characters</em> when parsing the initialization sequence. To verify that your HASH algorithm is working, the book offers the sum of the result of running the HASH algorithm on each step in the initialization sequence.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7</code></pre>
# MAGIC <p>This initialization sequence specifies 11 individual steps; the result of running the HASH algorithm on each of the steps is as follows:</p>
# MAGIC <ul>
# MAGIC <li><code>rn=1</code> becomes <code><em>30</em></code>.</li>
# MAGIC <li><code>cm-</code> becomes <code><em>253</em></code>.</li>
# MAGIC <li><code>qp=3</code> becomes <code><em>97</em></code>.</li>
# MAGIC <li><code>cm=2</code> becomes <code><em>47</em></code>.</li>
# MAGIC <li><code>qp-</code> becomes <code><em>14</em></code>.</li>
# MAGIC <li><code>pc=4</code> becomes <code><em>180</em></code>.</li>
# MAGIC <li><code>ot=9</code> becomes <code><em>9</em></code>.</li>
# MAGIC <li><code>ab=5</code> becomes <code><em>197</em></code>.</li>
# MAGIC <li><code>pc-</code> becomes <code><em>48</em></code>.</li>
# MAGIC <li><code>pc=6</code> becomes <code><em>214</em></code>.</li>
# MAGIC <li><code>ot=7</code> becomes <code><em>231</em></code>.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the sum of these results is <code><em>1320</em></code>. Unfortunately, the reindeer has stolen the page containing the expected verification number and is currently running around the facility with it excitedly.</p>
# MAGIC <p>Run the HASH algorithm on each step in the initialization sequence. <em>What is the sum of the results?</em> (The initialization sequence is one long line; be careful when copy-pasting it.)</p>
# MAGIC </article>

# COMMAND ----------

inp = '''jpv-,ndd-,bqpgj-,fp=5,fl-,bfh-,qh=2,npxt-,tsjpg=3,fls-,gm-,lk-,nj-,hvv-,nl=4,kplg-,xbm-,tscn=3,lnxm-,cqx-,mr-,dmc-,bfh-,mdt=3,sq-,shs-,csqs=9,plf=2,zt-,sxl=1,lvb=6,rn-,ttzb-,qv=9,dt=1,fh=7,jb-,bxhm-,bcdb=3,bqbp=1,pvp=8,knv=2,pl=5,vb=1,tscn-,dng-,zv-,nlvdlx=1,fvdf-,kk-,lrc=3,mfxq-,sflz=8,rvsd=6,zr-,ggt-,jrd=4,tt-,htqh-,sxl=8,csj-,nc=1,dqjj=2,pk-,js=6,bcdb=6,bcjt-,mpv-,gpbkvq=1,xx-,st=4,dxdn-,tc=6,cfrc=6,hvv=3,dm=1,dr-,gxnjx=1,ls-,tcc=3,zhlm=3,hzqdd=3,thpf-,hh-,rp-,rz-,sc-,mxkrjm=7,nl-,zm=6,mdl-,lv-,pfb=3,rpf-,ns-,rkx-,vg-,nqx-,jhr=6,nlx=7,bgl=9,xtg-,hg-,qc=7,ll-,mm=5,flv-,vnh-,mh-,zff=4,mf=3,tbkkg=7,sggps=6,tsjpg-,sflz=2,tbkkg-,nhk=5,mpk-,dqh-,qfhlzp-,xgh=1,tvht=7,gtc=3,kg=4,nfk-,zmx-,kdvj=7,mdl=4,sggps-,fgm=4,nhqsh=8,xqr-,tthtm=3,svv=6,gj-,vd-,csj=8,jth=5,fgc=9,gj=3,smz-,rrs=2,npxt=6,fvdf=5,zm-,jvd=1,hrd=6,dr-,jrd=4,nj=1,hzl-,fsg-,nhqsh-,bchf=1,zk=9,pv-,kk-,qfhlzp=1,qhghd-,xqr-,lvb=6,bcjt-,cz-,gfcm-,hpv-,rm-,gckm-,bgl-,mxkrjm=5,dkzr-,ng-,bbz=6,mftk=2,gqmkxf-,vzx-,sms-,kbk-,dkzr=5,nmv-,ttvjlj=8,lvb-,st-,dsm=4,tnq=1,bgzxt-,fls=2,fjdj=6,nf=3,vms=6,xbm=7,ss=3,xrqgg-,dknbzm=8,js=8,bzsv-,lvb-,fhv=8,lrc-,bzg-,dqs-,fffn=7,hcnm-,hdjnr=5,nmb-,mj=9,nsqk=2,cb=4,cxs=8,vz-,zj-,bgzxt=1,frrxp=7,dxl-,pnv-,mdt=2,tlxx=6,kt=6,vh-,dkj-,gjsbqs-,fq-,gcr=2,kpq-,gtc=4,hrb=4,ptjxn-,rft-,sc=1,cts-,gp-,hzl-,ldvln-,tt=8,fpcl-,nkf=2,lvx-,tscn-,kps=2,qdc=8,rrs=5,xbm-,bvl-,gg-,pzgq-,htqh-,ns=9,kfj-,cfrc-,jr=9,gp-,lvb-,nchj-,kpq-,rcb=9,zrdhj-,lvx=3,cjx-,bn-,jr=1,qrd-,qpt-,mhdmdh=4,tc=7,hvv-,kdvj-,fsp=5,pjb=6,xhhc=7,hzqdd-,fq=5,ns-,mlmmlr=6,hpv-,cm=4,vfr-,rfbp-,fp-,blfx=5,kfj=7,rsf=4,nq-,hpv=4,flcjxc=3,kr-,pl=3,jkf-,ctx-,lfzv=7,frll-,xbm=6,dlfs=7,zr-,bcdb=7,zr-,fvdf=5,qd-,rq-,msjk=8,hfd-,hxmx-,zdjn=8,qj-,fsg=8,kfj-,xls-,gnn-,zg-,dt-,hvr=4,rkx-,hq-,gm=4,grq=8,ndhs-,tsjpg-,fl-,bmt=6,nvcxm=8,hvr=1,ghcr=1,skdjv-,sf=8,tfq=2,dqs=7,hdjnr-,pk-,ll-,qhghd=5,bnd-,gtc-,zd=8,zj-,gg=4,pm=8,mccz-,nmv-,fjdj-,ggt-,jhr-,dp=7,zff=3,hzc-,dm=5,rft-,nkf-,rpf=1,gpbkvq-,gm-,vqs=9,lt-,tfjpc-,qj-,cfrc-,mr-,bj=2,kzqn-,xp=6,xgh-,hnj=3,xhhc=4,qhghd=5,ldnqhq=7,xhhc=1,tmcm=3,tfjpc=5,pl=2,rq-,qj-,lt-,mhdmdh=4,fffn=8,cxs=1,lx-,tgb=7,gln-,zj=2,ndgj-,xrqgg=6,clb-,clb=8,jxbtg-,kz-,rt-,bz-,nm-,cfrc-,nchj=3,dbxv-,gnn=7,trm=7,cjs=6,hpt=6,mhdmdh=3,xz=8,rn=7,rvsd=5,gcr=1,hqkjgn=6,dqh=5,kv=5,nvcxm=3,rhz=9,th=5,fxq-,hp=3,nmb=4,kjz-,kzqn-,czv=4,kpsl=2,mhdmdh-,kpsl=1,tmcm=3,gpbkvq-,kjz-,pjkjdg=4,xmh=2,kqdh-,kk=3,th-,pjkjdg-,zd-,nc-,xqr=7,cptb=5,hg=6,pphc-,cjs=4,vjx=8,fdhzkb-,prm=8,kpr-,tfjpc=8,xxp-,svv-,xczkz=9,vbplh-,lc-,pjkjdg-,gzbd=8,tbkkg=5,gzv-,mjv-,ndhs-,rft-,dcvv=4,fls-,fxq=9,fhmb-,xtg=5,rfvh=6,xp=5,lm-,qsgtrg-,skzm-,mfxq-,mhdmdh=8,tnq-,ctx-,lfk=2,fdb-,lrc=6,xjz=7,fjf=1,tgb-,zqc=6,ss-,stg-,fl-,ndd=7,plf-,xhhc-,zt-,zg-,zsmsq=4,prm-,mr=6,mlmmlr-,sfv-,vd-,dgfg=8,kms=1,plkfl=3,dkj-,kpsl=2,bnd=3,gfcm=1,kdvj=4,ndhs=7,vq-,jpv-,dpc=3,hfctsf-,cts=1,fjf-,qj=8,pfq-,rq-,pphc=3,rn-,tvht-,fvgv=1,lt-,nkf=8,zsmsq-,zhlm=9,xkg-,kkf=7,pf=8,skzm-,lsvvbb-,bvl=9,gj-,kv-,gnn-,hg=9,hq=4,nmv=3,htqh-,plf=5,pj-,jq-,rfvh-,bblmx=7,tv=8,mftk=6,vjx=6,ctx-,kr-,plkfl=2,bz=1,tjf-,rsf-,tcsv=2,hpt=7,tt=5,zsjm-,jb=7,zqx-,qvbgg=5,kx-,psr=6,cts=9,lm-,kfj-,ttvjlj-,ldvln=9,gzbd=3,plpz-,gv-,rkx-,dsm=9,zmx-,nhk-,dlfs=2,hsqpx=6,cn-,mhzt=2,cptb=9,dmc=1,hzc=2,ktnj=4,flkxn-,gl=4,pzgq=9,rm=5,dpmm-,mm=5,sjzd=1,mpv-,jb-,dqjj=9,kz-,vbplh=6,kdvj=7,flkxn-,xnkdz=1,mm=3,fhmb=3,svvk-,xhhc-,cb-,gxd-,bn-,tbkkg-,jzcfh-,pqc=3,frll-,frrxp-,ns-,kdf=8,flv=5,cd=4,mv=1,zt=3,xkf=4,xgh=5,nhk=2,pjb=5,szrhtl=6,nvcxm=8,dht-,zg=2,shs-,kz-,fvgv-,hvr-,ng=2,dknbzm=6,jrd-,gkv=5,qpt-,ffbp=3,bnd=3,fsp-,pnv=6,dq-,cs=4,lt-,pjb=1,xls=1,hs=4,vz-,hpt-,tbc-,flkxn=5,rfvh-,rkx-,bbz=4,kfj=2,gm=8,mjv=5,xj-,ztbm=3,ng-,fp-,ldvln=4,rrs-,hs=9,jrd=8,dlfs-,pnv=1,kfj-,fffn=8,nd=1,nsqk-,npmrk=5,ll=1,bbz-,sjc=3,mjv=5,fpcl-,dt=6,js-,sjc=4,tlxx-,tb=9,mpv-,mfh-,kpq-,kplg=4,cn-,fl=1,mfxq=7,jvhb-,gtc=6,mccz=1,xr-,nlvdlx-,prm-,nd=1,bblmx=8,mbhn-,dknbzm=3,cr-,lsvvbb=9,xnkdz-,rv-,sc-,xst-,gd-,smx-,lk-,tcsv-,kvh=7,qj-,nlx=2,dbcp-,qpt=2,hs=4,zff-,npxt=5,bzd-,zps=2,mj=7,bz-,vcms=9,sggps=6,hq-,tnq=8,tbkkg-,fhmb-,vzx=5,rjg-,vmb=2,tnq-,hx-,pv-,vvn=4,gxnjx-,gb-,dsz=6,bgl=1,kqdh-,fr=3,nmhh-,mfxq=2,xv-,dfhm=2,qfd=8,cptb=7,pfb-,zzn-,kdf-,pkd=7,vq=4,flkxn-,xkf=8,qv-,dnlcv=6,cjx-,flv-,zrdhj-,fjf=5,hjx-,kdf=7,ls=8,nhk=4,rt-,km=4,zt-,kx=7,mtd-,vnghr=1,kplg=6,fdhzkb=1,prm=8,dlpc=1,svv-,fpcl=1,hq-,dvgz=8,bqzd-,clb-,nqx=6,ls-,cn=1,grq=5,qlcnt=7,zv=1,dqs=5,xrqgg=6,bbz-,dvgz-,nk-,tmnh=3,tjf-,hrb=7,hfctsf-,msf=5,xx=6,xhhc-,mdt=6,kk-,pl=6,flcjxc=3,jbs-,cb-,zzn=1,fjdj=4,qrd=6,cz=3,pvp-,dr=8,sphpg=2,cts=3,skzm-,prm=7,hg=3,gp-,fsp=6,lrc=2,gx-,mv-,svv-,gln=1,rcb-,fxq-,zr=6,fv-,prm=9,bn=8,mmj=2,mbxf-,qrd-,bxpfs=2,zj=7,dqs=8,kk=2,fp-,vnh=4,cptb-,ctx-,nlvdlx=1,mbxf-,tcc=7,xqr-,fhv-,zzn=7,fxq-,vvn=9,bvl-,smz-,tm-,frrxp=9,vb-,gcr-,hcnm-,bcjt=9,hnr-,ndhs-,xv=5,qljb=2,gj-,bz=5,cznml-,ss=8,lnxm=7,hvv-,xrqgg=4,gr=1,tcsv-,cqx-,lv-,rd-,nnsrc=7,sflz-,xkd-,dng-,lk=6,jrd-,hvv-,pfk-,ftf=5,skdjv-,frll-,ktnj=3,zhlm-,scznqk=6,nnsrc-,zmx-,ggkc=2,bfh=1,ghcr-,gx=4,tmcm=4,lvb=3,jxngl-,pm-,dt=1,npmrk-,zx-,ttvjlj=7,dpmm-,qd=4,xbm-,gg-,htqh=4,ptjxn-,gxd-,npmrk=3,thqgnq-,bn-,clh-,nf-,ttzb-,npxt=8,bn=3,qh=3,ndd=7,hfctsf-,dmc-,pr=1,zhlm=7,smz-,bqbp=8,stg-,zg=5,zps=6,jxngl-,gcr-,knv-,pvp-,jbs-,hnj=8,bgl=7,fffn-,lm=4,qlcnt-,pfb-,ls-,rcb-,mjv-,fhv=7,pzgq=4,kmfvzg=2,zpjt=5,cts=9,kfj-,hg=8,hrb-,fxl=3,tjt-,snq=6,rhz=8,lrc=1,tbkkg-,mjv-,zz-,psr=1,fgc=7,tvn=5,zx-,js-,kpr=4,prvp=8,ftf-,tfq=7,tmcm=9,lsvvbb=7,hmp=1,ggt=4,vd-,jb=6,zg-,xbm-,ggm=6,dcv-,prvp=5,sc=2,hfd=9,br=2,gg-,jzcfh=1,vm-,qhghd=6,skdjv=4,kq=1,dsm=2,thbps-,jpv=7,vg=7,rvsd-,nfk-,lfk=7,bqbp=3,rq-,nqx=1,nvcxm-,cg=3,hvv=4,gd-,kms=3,gdstln-,mhdmdh=3,bk-,dkzr=7,hfd=9,mtd-,lnxm-,nhqsh-,cb-,nmhh-,mjvdv-,vbplh-,rv-,vb-,bchf=3,bgl=1,mxl=6,qljb=2,xnkdz=7,lt-,nk=2,pfq=1,pj-,bsp-,pf=5,vmb=4,dsm=3,vb=1,fq=3,xkg-,sxl-,prvp=3,lvb-,zdl-,pnv=4,nvcxm=8,hj-,xls-,gxnjx-,jrd=9,kqdh=8,trm-,pnv=5,qh-,cs-,thbps-,bzg-,qpj-,hmp=1,js-,vb=6,prm-,xqr-,qj-,dm-,ffbp-,mhdmdh-,mgmbpl-,kms=6,jth-,jnv=9,hpv-,xp=3,hzl=9,csqs=7,rq-,pkd=9,vvn-,xqr-,lxz-,bc-,hqkjgn=1,tm=6,tbc-,hzc=8,sxl=6,cptb=2,qljb=6,ls-,gb=7,ldvln=9,dcv-,lfzv=9,dpvz=1,kv-,ngg=8,ggm-,jpv-,dbxv-,fddbgx=2,vb=1,qdc-,plf-,vsxmj=4,gxnjx-,vsxmj=5,kqdh-,tm-,xhhc-,dlfs=3,cxs=1,dpmm=2,hj=6,tb-,fgm-,mgmbpl=8,hc=8,kpr=7,cn-,msf=9,nmb=8,dxdn-,ggt=5,qc=1,kqdh-,xls-,fxq-,rv=3,mv=3,kvh-,cqx=4,nvcxm-,gg-,rd=2,thqgnq-,jzcfh=1,nlx-,hg=1,dkzr-,dm=4,xx-,gckm-,pk=9,dgk-,rvsd-,rk=1,lvx-,mbhn=7,ndd-,kg=3,xnkdz-,rhz-,gf-,jxngl-,ns-,gf=1,dnlcv=4,gln=3,xmh-,cr-,fr-,gcr=3,gv-,br-,tscn=4,fv-,mn-,stg-,dt-,pjkjdg=2,mr-,hg=1,xjz=4,sms-,hzc-,pjkjdg=8,zpjt-,qdc=7,mr=6,tbc=8,dng=7,gzbd-,bxpfs-,kplg=5,rkx-,ggm-,fhv=2,ls=9,km=2,tthtm-,dpvz-,mxl=4,kpsl-,thbps-,rv-,rp=4,zzn=5,nk=4,mccz=5,kpsl-,fdhzkb-,dqjj-,hpt-,dkzr-,bfh-,gcr-,dsz=3,zd-,rfvh=9,zj-,fsp=6,dgfg=1,zsjm-,tc-,stg=9,nhk-,mn-,kk=7,xqr=9,lc-,fp-,kdf=5,gjsbqs-,sx=7,ggt=7,fhmb=6,bcdb-,lhl=8,qmzxc-,xjz-,tf-,mxl-,cqx-,jr=3,dsm-,bzd-,prm-,mlr=5,jpv-,cznml=7,sms-,cts-,dqjj-,fp=9,xnkdz=7,qpt-,pzgq=3,bchf=3,zd-,kjz-,rsf-,sfv-,zqc-,jth-,mccz-,zqc=9,ss=1,dxl=5,mlr-,kpr-,fr-,plpz=1,fxq-,mjv=3,mf=1,tmcm-,ldvln-,bsp-,kpr-,gv-,ptjxn-,ndd=8,ngg=1,qj-,ggt-,xx-,rp=1,hj-,fjdj=8,qmzxc=9,xls-,ctx=5,tbkkg-,nmhh-,nl=6,cptb=3,zps-,vg=8,clb-,jzcfh-,qsgtrg=3,zr-,fv=8,dsz=7,hzqdd-,kg=4,nb-,svvk-,pjb=2,vsxmj-,qhghd=7,hfctsf=8,fb-,nlx=3,scznqk=7,fvgv-,rkx=2,nc=1,ktnj=4,gtc-,nnsrc=7,qvbgg=1,rm-,tlxx-,kqdh=2,xxr-,svv-,cqx=3,cts=6,fvdf-,pmbd=4,zk-,nj=7,hgxt-,nnsrc=1,bqpgj=1,sj=7,jnv-,rv-,mfh=6,ggt-,mxl-,nfk=6,fhmb-,tnq-,hq-,zqx-,vmb=3,dbxv=7,qlcnt=7,lnxm=1,gp-,mhdmdh=3,xnkdz=4,hvr=9,pjkjdg-,ttvjlj=6,cb-,svvk-,zd-,nmb-,dpvz=1,mtd-,zd-,ggm=9,bblmx=7,nr-,fxl=8,rclvz-,ffbp-,fjdj-,bchf-,gj=2,npmrk-,hcnm-,dp-,mdt=9,sq=9,tcc-,jth=4,rft-,fls=3,rkx=1,kbk=1,qmzxc-,hmp-,lk=6,scznqk=4,jth=2,qpt=4,qpt=3,bzd-,gcr-,dmc=6,hrd=9,szrhtl=2,ptjxn-,bc-,rq=8,nj=3,xkd=7,qpj-,zd=2,bchf-,gln=6,zff-,qc-,xqr-,jdfpp-,hrf-,dlfs=8,ndd=8,gj=7,dxl=9,sggps=3,zrdhj-,hvr-,vms-,gckm-,mftk-,vsxmj-,sxl-,mtd-,gnn=3,hxmx=3,xx=2,csj-,plkfl-,qv-,cznml=9,zrdhj-,ml-,nk-,hgxt-,grq-,rcb-,cs=4,nl-,lfk=8,gp=1,bcjt-,frll=1,km=2,szrhtl=7,nvcxm-,sxl-,pvp=4,fdb=8,fl-,gb=7,bc=5,qpj=8,cg-,hgxt-,zzs-,bj-,ll=8,fddbgx=4,xv=6,kv=4,vnghr-,thpf=5,xkf-,tnq-,pj-,hfctsf=2,bgl=9,jxbtg-,pv=3,bvl=6,blfx=8,msjk-,tgb-,ctl-,dcvv=2,dng=3,thqgnq=1,hh=7,plpz-,fvdf=1,hpv=2,bsp-,dr-,mh=6,pn=1,gkv=6,jbs=3,dknr-,jdfpp=8,mj-,ctx=4,vsxmj=3,sggps-,mjvdv=9,rjg-,zv-,dcvv-,zr-,km=4,sq-,dnlcv=7,kzqn=7,thpf-,pnccf=3,mcf-,flkxn-,dqjj=4,sms-,ss-,gl-,blfx-,fgm-,bqbp-,rn-,csj-,ldnqhq-,ss=8,cm-,lljp-,tvn-,vdn=7,cjx-,nxh-,plpz-,br-,ggm-,mhzt=5,fpcl=3,tmnh=6,vcms-,nxh=7,dvgz=7,xrqgg-,mxkrjm-,mlr=6,km=8,dr=7,fl-,fdhzkb-,ghcr=9,szfp=8,hs-,zqc=7,fh=1,svv-,jxngl=5,hrb=2,gpbkvq=2,csqs=4,ns=8,lnxm=3,fsg=9,vbplh=6,szrhtl-,kx-,cs=1,jvd=8,st=9,cptb=3,jr=2,cr=5,vqs=1,vmb-,dfhm=7,tf-,bgl=3,prvp=8,hqkjgn-,dcvv-,pm=3,rft=6,bd-,thpf=9,cs=2,dpmm=7,sc=8,xqr=3,cqx=1,jf=5,xxp-,sx-,qgp=2,kps-,fsp=7,clb=3,rkx-,hnr=1,hfctsf-,mxkrjm-,qmzxc=5,kms-,mpk-,ggkc-,tlxx-,cg-,zsmsq=2,dp-,hvr=1,pjb=7,bmt-,hnj-,vh=6,kg=7,bxpfs-,vnghr=2,mr-,qpj-,gln-,nk-,ggt=7,km=4,tsjpg=9,fr=9,lvb=1,dng-,bmt-,pfq=7,kz=8,zx-,kjz-,szrhtl=8,frrxp=4,jvd=1,fhv-,fdr=1,nj-,tc=9,dnlcv=1,pvp=3,xst-,pf=9,sj-,lrc-,xxr-,fq=3,rsf=8,cs=8,jgzcb-,cxs-,dcv-,clb-,tb=8,xz-,sq-,dnlcv-,hp=4,qc=9,hqkjgn=1,shs=5,thbps=6,blfx=8,tf-,cxs=1,hrd-,lrc=1,flv=1,dgk=9,cr=3,rfbp=1,gv=6,nfk=1,gn-,ldvln=6,mjv-,ftf-,rft-,dgfg=5,clh-,msjk-,xczkz=4,pv-,js=2,gj=3,fdn-,nf-,dt=2,vbplh-,clb-,gp-,kr=4,mhzt=7,qpj-,kpr=8,shs-,ml=6,shs-,pnccf-,hs-,hp-,knv-,dcvv=3,gd=5,szrhtl=2,rsf-,rv-,lk=1,hq-,ss-,nnsrc=2,zz-,kms=8,bzg-,tm=9,bqbp=7,dbxv=5,kv-,xbm-,tf-,sms-,nkf-,bnd-,grq=2,rcb-,qh-,mndt-,jnv=1,rjg-,mdl-,dpmm-,jf=5,tv=8,hjx-,fdhzkb-,qsgtrg-,xhhc=2,cjs-,kg=1,vp-,fxl=3,pjb=5,xxr-,qj-,dxl-,pk=3,fq-,mm=4,fh=5,cjs=6,smz=7,msf-,sj=7,vnghr-,bbz=4,sc=9,ldvln-,xst=6,cn=1,gj-,dfhm=3,dxl=8,svvk-,xbm-,plkfl=2,nb=8,cptb=4,nm=1,lfk=4,gkv-,nf=7,cznml=8,xls-,cjs=7,bfh=6,kg-,fdb=7,msf=9,tfjpc=2,snq-,vbplh=9,zrdhj-,fjdj-,lhl-,tc-,stg=7,bk=4,ct=9,pkd-,qsgtrg=3,nb-,pfb=4,mbhn=9,bqbp-,zsjm=7,nk=4,mj=5,lk=9,cz-,gtc-,htqh=6,gcr=3,bbz-,jr=1,cz=3,dknbzm=2,lz-,st=6,tthtm-,thpf-,mfxq-,tvn-,tmcm-,gjsbqs-,hvv-,cm-,pnv=4,bblmx-,zzn-,czv-,kx-,jgzcb=2,bzg-,bmt-,ls=9,pnv-,frll=4,fq=7,qj-,bblmx-,dknbzm-,kdf=4,fhmb-,zd=4,fhv=3,smz=4,ll=8,cqx-,pvp=8,fdn-,pr=4,nfk=1,lk-,clh=6,jvd=9,qv=2,lc-,dgk-,pqc-,dr-,bd-,dcv=8,nchj=9,cfrc=6,tnq=2,xhhc-,bxpfs-,tmcm=6,xmh-,rfbp=9,gb=6,hpt-,pjkjdg-,qpt-,rfvh-,mh-,thqgnq=8,tfq=9,nf=1,xxp=7,jvd=9,bzsv-,dt=4,tmnh-,hc-,xkg=2,rp-,fhmb=4,jdfpp-,sx=3,vfr=1,mftk=9,bchf-,hfctsf-,kv=3,xtg-,rrs-,rsf=5,nl-,qvj-,hfhr=4,dmc=4,mn-,dpvz-,tjt=3,nvcxm=1,bxhm=3,rp-,xp=7,pjkjdg-,tvht=7,flcjxc-,xxr-,csqs=4,rft-,hj-,xbm-,msf=8,lsvvbb-,nc=7,hfctsf-,sggps-,kg=8,qpt=2,hp=8,rvsd-,hzqdd-,bqbp=2,qgp-,pn=7,nqx-,lrc-,bk-,gj-,xbqr-,sfv-,skzm=2,lhl=7,hnj-,pkd-,ns=1,rft-,cptb=1,mhdmdh=3,cqx-,mcf-,bxhm=8,ch-,ch=4,nsqk-,zm-,mr=8,kdvj-,gg-,sxl=8,fvdf=2,pjkjdg=6,hc=5,tv-,pr=1,hzdgj-,mn-,gp=6,prvp-,nr-,nk-,fh-,flv-,zk-,mr-,mpv-,hj=6,shs=3,tmnh=2,gg-,hj=5,kbk-,dvgz-,gtc=4,qd=5,hp=8,hdjnr-,hh=3,mj=4,kqdh=5,svv=9,mlr-,dqs=8,qmzxc-,zsjm-,rd-,mxkrjm=6,rfbp=8,pv-,plkfl=5,nvcxm-,cs-,htqh-,cjx-,fh=5,kv-,rk=6,sj=5,tmcm-,thqgnq-,mxl=9,ktnj-,pv=1,xrqgg-,hxmx-,ndd=4,skzm=3,gb-,bxpfs-,rvsd=5,dlfs-,vms=2,nmhh-,ct-,cqf-,hzqdd-,fdb=1,rrs-,zdl=3,tjf-,vb-,kx-,npmrk=5,zd-,sxl-,zsjm=4,sms-,sj-,sggps-,fb-,fxl=9,rq-,nqx=3,fvdf=2,ftf=8,lhl=3,lgklm-,xv-,grq-,psr-,nchj=9,hgxt=7,thpf-,vjx-,sjc=6,gjsbqs-,ztbm=8,zsjm=5,shs=2,ndhs=3,rd=5,zqx=7,dsm=3,msf=4,rm-,gln-,vp=8,rz-,cqx=1,tc=5,bxpfs-,xls=5,dbcp=6,mbxf-,zm=3,xczkz-,plkfl-,mn-,blfx-,xjz-,bblmx=2,dcvv-,lhl-,fsg=6,tsjpg=9,htqh-,cjs-,gd-,xnkdz-,flcjxc=4,vn-,mr=4,frll-,kplg=5,ss-,dbcp-,sggps-,nmb=9,tbkkg-,zsmsq=9,zg-,xtg=6,hjx-,dknr-,ml=7,xr=9,kjz=9,zsjm=9,lz-,zr-,bqzd-,nhk-,ktnj=5,htqh-,hcnm=9,tcsv-,lz-,rfbp-,vnh=4,pfb-,pnv=8,xkf-,pnv-,bgl=6,mj=6,vms=1,ggkc=5,vqs=6,lsvvbb-,tcsv=5,ndd-,xrqgg-,bcjt-,bqbp-,tb=2,dbcp-,zg-,gqmkxf=7,nvcxm=3,nl-,zz=1,mh-,lv-,stg-,knv=8,dpvz=5,kpq-,nmhh=4,qlcnt=2,vqjp-,hvr=4,lljp-,clb=4,mccz=1,qvbgg-,km-,mr=4,cr-,pv-,kx-,vnh=2,tv=8,hz-,gx-,zx=3,bxpfs=3,snq-,bj-,plpz=5,cd-,psr=2,bcjt-,xbm-,jf=3,knv-,dvgz=2,qv-,bdvl=7,cd-,dqh-,grq=4,frll=8,qc-,vqs=6,vsxmj-,lt-,flcjxc-,bz=5,thbps-,dsz=7,hrb-,zk=4,jzcfh=9,mhdmdh=1,vn-,bzg-,qc=6,nmv=2,dm-,hz=9,smz=1,pzgq=3,vjx=5,zzs=6,zg=7,kps-,qfd-,gl-,tp-,rfvh=8,hz-,tcsv=3,szfp=1,kmfvzg-,bvl-,dknr=4,tgb-,rp=7,hfd=4,nj=3,bcdb=3,ztbm=3,sjzd-,zmx-,kz-,qgp=8,dpvz-,fdr=7,kq-,qh=7,lv-,hrf-,kr=1,flcjxc=2,kmfvzg=3,knv-,tfq-,lt-,st=7,jtkh=5,hvv-,fdn=6,nc=1,fr-,csqs=1,cm=9,fvgv=5,fl=1,ldvln-,xx-,pn-,pjkjdg-,svv=6,xbqr-,gckm=8,lrc-,xbm-,pr=4,vbplh-,qljb=4,cxs-,xgh-,sflz=3,jth-,hp=9,jq=3,gcr-,dcv=8,qgp-,bnd=4,dkj=4,nl=2,mccz-,zt=8,jq=9,tbc-,xnkdz-,mgmbpl-,ffbp-,mhdmdh=4,gxnjx=7,cr=2,dqh-,vdn=9,gb=5,vzx=2,xrqgg=6,bzg-,pn=7,rk=5,dmc-,bgzxt-,xjz-,fpcl-,nlx-,zzs-,cg=3,nsqk-,vb=9,lfzv-,rvsd=2,vzx=5,xxr-,qj=7,xkf=8,xqr=9,lhl=8,rm-,mh=9,kt=2,qh=3,lhl-,xnkdz=7,xkd=5,hsqpx=4,mdl-,vj-,vmb=8,bblmx-,tfjpc-,dsm-,xnkdz=9,km=3,rclvz=9,ll-,bd-,kdvj-,blfx=2,dkzr=8,rk-,dng-,thpf=8,tb=1,zd=3,hzc-,fdn=9,qc=8,lnxm=4,mndt-,gdstln-,zqc-,rd=9,ttzb-,lnxm-,bfh=6,fsg-,hnr-,gxnjx-,shs-,pfq-,vdn=2,rv-,rclvz=3,pf-,xkf=5,kps=3,dht=2,tbkkg-,fr-,fls-,bgzxt-,rn-,gpbkvq-,nc-,cqf-,tjf-,ctl-,fxl=8,xls=7,lfk=9,xnkdz=2,sj-,vqs-,jnv=5,sxl=2,smz-,dknbzm-,tjf=8,nr=7,grq-,rz-,lt=7,vsxmj-,jvhb=2,hrb-,xrqgg=5,fdhzkb-,rkx-,cd-,mj=6,qv=1,pfq-,nq=8,pjb=4,xkd-,fxq=9,jtkh-,lgklm-,mmj-,vqjp=2,pj-,rcb=9,flv-,nc=1,nd-,cqf=5,qd=5,js=8,fvgv=6,bblmx-,kk=6,kfj=7,xj-,mfxq=4,plkfl=2,vqjp=8,fpcl-,cg-,rrs=9,mccz=6,fp=8,shs=2,cr=2,bcjt-,nmb=1,gxd-,lz-,clb-,nmb-,qpj-,xr=3,nb-,mhdmdh=7,fh-,vb-,xhhc=4,xj-,hzc-,hpv-,rpf=9,blfx=5,cjx-,bqbp-,smz=4,szrhtl-,stg=4,pqc-,gnn=5,jkf=8,mf-,zz-,qsgtrg-,jb=9,kx-,lvx=3,dkzr-,lvb=3,zz=7,hzc-,fpcl=1,jr=3,rv=9,ggt=8,zrdhj-,nb-,hq=2,fdn-,tm=5,tgb=6,tm=3,tthtm-,hpt=5,rz=5,vnh-,skzm=3,qlcnt=3,br=8,kg-,qh-,kpsl=8,dng=2,sx-,snq=3,zmx-,lv-,gl-,dxdn-,tthtm-,kkf-,kkf-,pv=7,hsqpx=3,qgp=3,blfx=4,fp=8,dr=1,hnr-,vjx-,kbk=3,tjf=9,vp-,dqh=3,vjx=9,lgklm-,vh-,bzd-,ghcr=1,kvh=8,gfcm=2,ffbp=9,sxl=2,dkj-,ztbm-,xnkdz-,nkf-,mj=9,dxdn-,dmc-,vn=2,nb=3,dt-,fls=5,pnccf-,kz=8,nf-,gcr-,pqc-,ktnj-,zr-,hcnm-,kf=3,ns-,fddbgx-,rsf-,xgh-,gv-,tbkkg-,kx-,svv=2,pr-,hqkjgn=6,kf=1,lhl-,pf-,lk-,xqr-,gn-,dbcp=9,dlfs=2,bzd=1,rk=6,zr-,zqx=8,hz=9,hnj-,skdjv=6,nf-,gzv=8,mtd=2,vj-,rn=1,cznml-,hnr-,vcms=5,mhzt=7,cxs-,vq-,npmrk-,pphc-,xczkz-,zr=5,jb-,pnv=6,cts=6,vcms-,xgh=5,sxl-,dr-,zsmsq=6,jzcfh-,vnh-,ggt-,thqgnq=1,gdstln=9,lrc=8,nm=4,cn=9,rfvh=2,tb=2,nchj=4,gzv-,dxl-,bgl-,nc-,rrs-,mf-,vh-,ml-,fsp-,vz-,ztbm=6,zrdhj-,psr-,rk-,rz-,fgc-,zv-,hfd-,dmc=8,rft-,jr=4,fvdf-,hsqpx-,cqf-,mbxf-,vb=5,nqx-,sflz=8,dkj=8,dht=3,kkf=8,cg=1,cts=3,gln=8,tjt=9,nfk-,prm=9,bxpfs=3,mdt=2,bxpfs=1,nd-,jxngl=7,nq=2,mbxf=4,jdfpp=2,svvk=8,gl-,pfb=9,kzqn-,dfhm-,xz=6,ml-,zps-,qc=7,ml-,tmcm=2,clh-,kvh-,prm=2,cqx=5,sflz=3,fxq=5,lx-,csj-,mdl=9,dqh=5,thbps=4,kqdh-,svvk=6,kpsl-,thqgnq-,nmb=7,pfk=9,bgl-,nlvdlx=1,xx=2,tb-,dkzr-,jvd=3,gcr-,ggm-,ml=6,bxhm=4,gkv=6,dkzr-,jxbtg=2,fr-,tp-,kf=6,frrxp=9,dnlcv-,nj-,gzbd=9,hzdgj=4,dq=9,mlr-,qhghd=5,fxl-,hh=2,qpj-,ggm-,vz=8,nk=4,mxkrjm=4,gdstln=4,hcnm=7,fsg-,gzbd-,mpk=6,vmb=5,pn-,hnj=2,mjvdv-,fjf=6,cznml-,hc=1,xqr=9,nf=6,hzl=6,vq=9,dvc=5,mj=3,qc=3,vqs=7,kz=3,npxt=5,pnccf-,mgmbpl-,dng=2,gln=1,pzgq=1,dknr=1,tbkkg=2,mtd-,jtkh-,lnxm-,vj-,sjc=6,gp=3,ztbm-,ttzb-,cjx=7,kbk=2,rfbp=4,mlr-,gjsbqs=2,mfh-,bblmx=4,qfhlzp-,xp=7,cb-,bmt=3,hvr=4,hj-,nqx-,clh-,qvj=8,fffn=3,nkf-,gnn=3,sggps=7,pphc=8,lfzv-,pjkjdg=5,csqs=7,jr=2,nmv=4,nmv=1,hvr-,frrxp=1,xxp=7,sjzd-,vm-,qgp-,xp=3,nchj=9,tjf=8,bzsv-,js-,fhmb-,kkf=8,smz=9,mbxf-,thbps-,dp-,xz-,ttvjlj=1,mjv=8,kbk-,cqf-,vh-,ztbm=8,tjt=8,vfr=8,gxd=7,qrd-,bnd=4,sj=6,czv=1,bnd=1,qsgtrg-,vh=6,dng-,snq=5,rm=2,rhz-,zsmsq-,hcnm-,dkj-,ss-,hz=3,tjt=1,zj-,lnxm=9,msjk-,msjk-,pphc=2,szrhtl=1,sxl-,dpc-,jnv-,ldvln-,fh-,htqh-,bxpfs-,sphpg=5,bzg=9,jxbtg=1,kpq=4,tvht-,xqr-,vvn-,vzx-,fjdj=4,ftf=6,grq-,rd-,kpr-,nnsrc-,ktnj-,blfx-,dxdn=7,dm=2,dqjj-,ml-,qd=6,dt=2,hp-,dq=7,fv=1,mhdmdh-,fq=1,ffbp-,ml-,bzd=1,bgzxt-,qfd-,dknr=6,hdjnr-,hcnm=6,qfd=3,hs-,rsf=3,sq-,vqjp-,qj=7,hrf-,pr-,mdt=8,nj-,fv-,rk-,ggkc-,pr-,gqmkxf-,kzqn-,kz=5,pnccf=1,ttvjlj=2,dpvz=1,vn-,qc-,clh=1,zdjn-,skzm-,xtg=8,dkzr=5,dcvv-,xr=7,bmt-,hqkjgn-,kt=6,kg-,zzs=1,nr=4,sf=1,fvgv=1,pkd-,dxl=3,mcf-,trm-,mbxf-,kqdh=7,tbc=9,mlr-,rcb=6,gr=7,hzl=1,bn=3,hs=3,npmrk=5,kqdh-,bvl=9,cfrc=5,bxhm=8,rq-,bj=6,sj-,skdjv=5,gf-,qgp-,mdl-,mmj-,fpcl-,svvk-,blfx-,cznml-,dbcp=7,jq=1,rvsd-,fjf-,gjsbqs=9,hrb-,mjv=7,dxl-,bblmx=8,sj-,lc=4,pjkjdg=3,blfx=6,bxhm=6,dsm-,gkv=8,rfvh=9,ch=4,dqjj-,fl-,pjkjdg-,qljb-,vmb=5,lrc=2,qpt-,mpv-,ndhs=1,lrc-,vcms-,hvv=9,blfx-,fpcl-,kx=2,cjx=1,smx=9,pnccf=9,qc-,sc=4,hrf=9,stg-,xv=1,hpt-,zg-,prm=9,hpt-,pjb=8,jhr=3,bd=5,fdhzkb=4,bk-,lvx=2,gqmkxf-,gn=4,tvn=5,mlr=2,pphc-,nlvdlx-,ctl-,flkxn-,mpv-,gcr-,dkj-,vnh=3,tfjpc=1,plf-,nr=2,pf=4,cxs=4,nf-,ndgj=4,pfk=9,tc-,jth-,dpvz=4,tnq-,plkfl-,tb=5,ch=8,dr-,kqdh=6,kdvj-,qh=3,zk=7,tkqkm-,xr=6,hzc=7,dmc-,kms=4,qc=1,pnccf-,fpcl-,bnd-,hx-,mftk-,pkd-,mj=7,lgklm-,rhz=4,ndd=5,hnr=5,lc=1,jf=3,xqr-,nxh-,ls-,fddbgx-,dm-,npmrk=4,hmp-,nhqsh-,fsp-,jzcfh=5,vmb-,kf-,sggps=1,mlr-,cptb-,bblmx=3,dht=9,blfx=5,zhlm-,xhhc=5,fvdf-,gckm-,vdn-,mdt-,dknbzm=5,bxhm-,tfjpc=2,xgh-,mdt-,tmnh=6,cz=8,kkf=5,rn=4,jph-,hfctsf-,dpc-,mccz=5,fb=9,gqmkxf-,bxpfs-,rjg=2,kdf=4,ldvln-,ng=4,kms-,dxl=6,shs-,bgj-,xz-,vmb-,qfd=7,jpv=8,ttvjlj-,tv-,dp-,bzg=6,cjx=1,nq-,zpjt=7,lvb=8,flcjxc-,zsjm-,mdt-,tmcm-,scznqk-,bdvl=7,kmfvzg=8,mftk=9,gckm-,dxl=4,rv=9,sxl-,hz=9,qljb=8,lc=1,lhl-,nc-,zm=2,lv-,tmnh=3,rrs-,vjx-,gx=3,skzm=3,bnd-,mv-,bgl=5,tfjpc-,lz=8,gm=1,kz-,hp-,lvb-,cm-,sphpg=8,vb=7,nj-,lc-,sphpg=3,dknr-,hrd=8,ldvln-,htqh-,rhz-,vnh-,mj-,fls=9,szrhtl=9,xbqr=2,tthtm=1,dgk-,nb-,zff-,dgfg-,lgklm=7,tmnh=6,cjs-,jvhb=5,zsjm=6,prm=9,jr=5,dcvv=7,jtkh=3,sflz=3,xrqgg=5,mr-,kpr-,bblmx=4,rt=5,ng=9,mccz=4,bsp-,lsvvbb=2,gzv-,km=8,cptb-,pm=1,tkqkm-,hvv=7,stg=9,tgb-,bd-,pv=6,dht=3,dqjj=4,xkd-,ndhs-,mbxf-,lfk-,hgxt=7,pf-,lljp-,grq=9,bdvl-,nnsrc-,sc-,fvgv=2,fjdj=4,cb-,bxhm=7,fjdj-,dgfg=7,lz=8,cznml=4,mjvdv-,nhk=3,mhzt=1,jhr=3,xhhc-,pmbd-,nhqsh=1,hq=2,shs-,rclvz-,rt-,xkd-,zpjt=8,jgzcb-,nf-,rd=2,hg=9,dlpc=4,hvv-,cd-,dsz-,cb-,sx-,pfq-,fjf-,nhk=1,bcjt=1,xczkz-,ndgj-,pkd=2,mfh=4,pqc-,gjsbqs-,cb=5,pk=2,sjzd-,ch=7,kqdh=2,sc=3,th=3,pm=1,lk-,kpsl-,bxhm=1,nxh=8,ghcr=6,jxngl-,gv-,gj-,gg-,csj=2,ch=4,dcv-,jf-,vp-,nhk=6,gnn=1,tscn-,kdf=9,jth-,rjg-,vq=1,hmp=6,mh-,pjkjdg=7,zdl-,ftf=1,dsz-,bbz=7,xbm-,nsqk=2,grq-,hvv=2,msjk-,zzs=7,mh=6,tlxx=4,kz-,gx-,fb-,clb-,ngg-,nq-,nmv=6,sggps-,vvn-,kms=8,xxr=7,rp-,cs=1,plf=3,hgxt-,vfr-,zdl=1,lvx-,nqx=9,mn=6,xj-,rv=1,bdvl=6,mn-,dpc-,hrd-,nmhh=8,km=6,gx=9,ll-,km=1,vfr=9,gp=3,dxdn=6,dvgz-,bn-,zsmsq=9,vnh-,xqr=5,dfhm=3,xrqgg=7,mj=6,mxl=8,fjf-,dvc=6,jxngl-,fdn-,tbc-,kplg=2,rvsd-,fr-,pl-,hzdgj=1,hzqdd=3,bxhm-,jkf-,zdl-,kpsl-,lt=3,cfrc-,zd-,ldvln=6,pn=8,kdf-,br=2,pzgq-,bxhm-,gkv=9,ls=7,clb=6,kvh=1,hrd=5,tm-,gr-,fb=1,hs=3,htqh=6,br-,hjx-,dr=6,skzm=8,fdn-,tfjpc=7,qh=7,kq-,plpz=9,ttvjlj-,dfhm=5,fsg-,jvd=8,bmt-,pvp-,vfr=8,nmv-,dq=6,mbhn=6,flcjxc=7,gl=2,hzl-,jq-,rn-,bxpfs=6,nlvdlx=2,mlmmlr-,pqh=4,kr-,ss-,tnq-,kq=9,ggm=7,qsgtrg-,gcr=6,hcnm-,vd-,hzl-,qc-,js-,mmj=2,ns-,mccz=8,bzsv-,xkd=3,hrf-,mhzt=9,dp-,sfv=2,sms-,fxq-,hzqdd=4,bqpgj=8,mf-,nnsrc-,pr=6,ldvln-,xxp-,mftk-,flv=9,gcr=1,hzqdd-,dqh=5,nchj=7,dbcp-,gv=7,bgzxt=2,lx=3,tjf-,bxpfs=8,vh=1,dvgz-,zg=6,tkqkm-,qljb=2,xx=7,xr-,mbhn-,gpbkvq=1,lx=8,hzdgj=7,zx=9,jhr=9,zqx=4,sf=4,qfhlzp=8,flcjxc-,tt=9,nl-,xr=5,mccz-,sjzd-,hzqdd=8,xz=7,tthtm-,ctl=9,cn=8,jgzcb=2,pjkjdg-,zhlm=2,vzx=8,thbps-,pfq=6,xz=5,bchf-,htqh-,hzqdd=4,nq=9,rkx=3,pjb-,dnlcv-,ffbp=1,pk-,tmnh-,bgj-,gd=1,xmh=8,rm-,qrd=2,dpc=1,czv-,dpc=9,hnj-,hfctsf-,zj=3,gkv=6,jb-,fhmb=5,ctl-,plpz=6,lvx-,dvc-,rfvh=8,hdjnr=7,lz=4,lfzv=3,rcb-,bzg=5,snq=4,kx=4,vn=7,pnv=4,sc=7,gd=4,cn=8,hz=5,fdb=1,jrd=1,xbqr-,gkv-,xhhc-,nb-,npmrk-,ffbp-,gp=3,qrd-,gtc-,hp=9,cd=7,kbk-,bzd-,vnghr=9,flv=6,rclvz-,pjb-,nmhh=9,fp=5,bbz-,hxmx-,nvcxm-,ghcr=9,qfhlzp=7,dpmm=7,hh-,xkd=1,bcdb=3,cznml=3,pnv=9,gxd=3,zqc-,dqs-,fffn-,hdjnr-,fddbgx-,st=3,dsm-,prvp-,vg=5,jr-,fjf-,qc-,mftk-,pr=9,vnh=6,nmv-,qmzxc-,mxl=6,xkg-,lljp-,mm=1,ggt-,dknbzm-,ghcr=2,bk-,thqgnq-,fq=3,sphpg=3,zx-,kfj=7,hnj-,rq-,xkf-,ffbp-,clb=3,bzsv-,mpk-,zqc-,trm=9,xnkdz-,lrc=9,pk=2,cg-,ctl=4,vg=9,hzdgj-,qh-,tcsv=6,rfvh=7,hq=4,fffn=8,tscn=2,gcr-,tvn-,qhghd-,xj-,dgfg-,pm=6,ngg-,ss=6,hz-,czv-,zzn=1,dknr=5,jtkh-,zzs-,zff-,fffn-,fl=4,mfxq=2,nm=2,jvd=4,htqh=7,pf=6,hz=4,zg=7,rft=9,pj=9,gb-,hq-,vn-,bd=8,ngg=5,vms-,mpk-,hrb-,fdb-,nj-,vm=5,qpj=3,gj=6,pn=3,cjx=5,trm=5,bgj=2,bnd-,tv=2,ptjxn-,gr=8,ng=4,mxkrjm-,fhv=9,hh=3,cqx=2,kf-,fffn=1,dbxv=7,dxdn=9,vj=1,qsgtrg-,mv-,mccz=7,xbm=6,mcf=5,htqh=6,hz=6,rjg=4,mbhn-,hx=9,xrqgg-,nmhh=4,nhk-,kbk=5,qfd=5,xv=1,vp-,hp=1,hz-,bgj-,bzg-,ctl-,pv=1,jph=6,pqh=5,xxr-,cb-,rrs-,cs=7,dmc=4,lhl-,blfx-,hrb=7,ls-,jf-,dxl-,cts-,kg=9,xnkdz-,js=7,fgm-,ll-,lsvvbb=2,dqh=7,kdvj-,cn-,kpsl-,snq-,tjf=4,jdfpp=6,tmnh-,kplg=4,ns-,bchf-,csj=2,gxnjx=3,jhr-,xqr-,dbcp-,gnn-,mm=2,js-,pfq-,xst=4,gckm=3,nfk-,dkzr-,vb=3,jb=9,gn=1,rcb=6,dvgz-,xbm-,tbc=3,kdvj=3,bk=3,qvbgg-,zpjt=2,hrb-,rm-,zqx=5,dlpc-,tsjpg=9,fxq-,hfhr=1,lvx-,zt-,dlfs-,pr-,fb=6,jgzcb-,dng=6,hgxt=1,nb=5,bgzxt=9,tgb-,bbz=8,pfk-,gd-,mmj-,npxt=1,cs=4,kplg=2,bqzd-,tjf=1,thbps-,bzg-,kzqn=3,tf=3,zk-,kr=2,xxp=3,vbplh=9,dqjj=6,vcms-,nhqsh=7,gjsbqs-,gn-,dbcp=9,fjdj-,bcjt-,sj-,cxs=1,zmx=3,nchj-,bc-,pzgq-,zps-,clb-,qmzxc=7,sphpg=3,npxt-,dlfs-,hfctsf=9,zpjt=5,nchj=6,smz-,jf-,tb-,lgklm-,ggm-,ls=7,lk-,fxl=9,prvp=8,hvv=8,jxbtg-,zqc=2,vq-,tfjpc=7,mjv-,lnxm=3,lfk-,qhghd=9,bcdb=2,lvx-,cfrc=3,sc-,cxs=6,gln-,thbps-,cptb-,gln=4,sq-,xqr=4,nf-,vzx=2,gckm-,bqpgj=3,bdvl-,cfrc=3,csqs-,tb=7,cqx=6,hc-,mjvdv=7,vm-,kkf=4,kpsl=9,xxp=6,hj=7,nq-,lz=9,hg-,rt-,skdjv=4,cg=8,gcr=3,ztbm=7,xr=4,sflz=9,fv=1,frrxp=6,gl-,kx-,ct=9,xkd-,sflz-,xst-,gln-,ns-,mbhn=2,zv-,mcf=6,msjk=5,xls=7,tf=6,fpcl-,bchf-,vm=4,zsjm-,hfctsf-,tcsv=4,ngg-,bxhm=7,xczkz=2,jpv-,dgk=1,vsxmj=4,kps-,nkf-,xrqgg=8,hj-,zz=4,hrf=8,tm=4,mlr=2,xkd-,gpbkvq=8,xtg-,cjx=3,ngg=3,mlmmlr=5,mm-,pj=6,gpbkvq=9,dpvz=1,dt=4,bgl=1,frll-,fl-,rz-,bgj-,kpsl=8,bzg-,lrc=7,mf-,zff-,ch=4,qd-,tnq-,cqf=2,nxh-,gfcm-,mbxf=4,tv=8,prm=9,nk=1,vzx-,hpt=2,dmc-,lt-,bdvl=3,tmcm-,ctx-,jtkh=7,hz=2,mjv=4,fv-,hjx=2,kx=6,mj=7,hq-,vh=7,cjs-,ldvln-,mcf=6,nc=5,dxdn=4,svv=6,tcc=3,flkxn-,pk-,rcb=1,cqx=3,rz-,fxq-,dvgz=9,ztbm=2,mmj-,mfh-,lxz-,smx=6,zk-,vh=9,dq-,blfx-,bdvl=6,hvr-,svv-,fgc=3,bfh=9,rvsd=3,pfb=8,jgzcb=2,vm=9,rn=2,kjz-,nj-,tm-,jnv-,jvhb-,lrc-,hc-,dlfs-,hrb-,plpz-,rk=4,smx-,ls=9,cznml=1,vp=1,rz-,rk=3,cqf-,bdvl=2,sphpg=3,zhlm=2,lvx-,gd-,hrf=1,gxnjx=9,fxl-,cfrc-,nmhh=3,vsxmj-,nmhh-,vn=2,vvn-,gxd-,gl-,hc=8,sxl=4,pfb-,rd-,ss-,zff=8,gf=5,trm=4,lljp-,skdjv=8,fp=8,xxp-,dxdn=3,rz-,xr=8,ttvjlj=3,zqx-,skzm-,dmc=2,nlvdlx-,szfp-,zzs=3,mgmbpl=7,kvh=2,nm-,mccz=4,dlpc=3,sms=7,pfb-,mgmbpl=5,rkx-,dmc=5,kplg=8,xp=1,hzc-,dgfg-,dqjj-,ghcr-,hp-,ttzb=5,sms-,gm-,pqh-,zrdhj-,dknr-,rq-,bzd-,ls=1,cxs-,xxr-,cr=2,tcsv-,zj=7,ftf=8,sjc=3,cg=8,dng=8,xrqgg-,ndhs-,gr-,zv=6,gd-,qpt=5,sms-,nsqk-,zz-,rv-,rk-,tscn=7,prvp-,fl-,xbqr-,fxl=4,gx=5,fjf=4,vz-,jth-,sq-,tmnh=5,lvb-,tt-,tlxx-,dgfg=7,bqbp-,csqs=1,fjdj-,hfd=9,ct-,zdl=6,ldnqhq=4,flkxn-,pfq=1,pzgq-,xnkdz=2,sj-,jpv-,rft=4,vms=8,dkj=2,bgj=7,qhghd-,stg=6,hcnm=1,ch-,fq-,cb=9,tkqkm-,qc-'''

# COMMAND ----------

def get_hash(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

answer = sum(get_hash(s) for s in inp.split(','))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You convince the reindeer to bring you the page; the page confirms that your HASH algorithm is working.</p>
# MAGIC <p>The book goes on to describe a series of 256 <em>boxes</em> numbered <code>0</code> through <code>255</code>. The boxes are arranged in a line starting from the point where light enters the facility. The boxes have holes that allow light to pass from one box to the next all the way down the line.</p>
# MAGIC <pre><code>      +-----+  +-----+         +-----+
# MAGIC Light | Box |  | Box |   ...   | Box |
# MAGIC -----------------------------------------&gt;
# MAGIC       |  0  |  |  1  |   ...   | 255 |
# MAGIC       +-----+  +-----+         +-----+
# MAGIC </code></pre>
# MAGIC <p>Inside each box, there are several <em>lens slots</em> that will keep a lens correctly positioned to focus light passing through the box. The side of each box has a panel that opens to allow you to insert or remove lenses as necessary.</p>
# MAGIC <p>Along the wall running parallel to the boxes is a large library containing lenses organized by <em>focal length</em> ranging from <code>1</code> through <code>9</code>. The reindeer also brings you a small handheld <a href="https://en.wikipedia.org/wiki/Label_printer" target="_blank">label printer</a>.</p>
# MAGIC <p>The book goes on to explain how to perform each step in the initialization sequence, a process it calls the Holiday ASCII String Helper Manual Arrangement Procedure, or <em>HASHMAP</em> for short.</p>
# MAGIC <p>Each step begins with a sequence of letters that indicate the <em>label</em> of the lens on which the step operates. The result of running the HASH algorithm on the label indicates the correct box for that step.</p>
# MAGIC <p>The label will be immediately followed by a character that indicates the <em>operation</em> to perform: either an equals sign (<code>=</code>) or a dash (<code>-</code>).</p>
# MAGIC <p>If the operation character is a <em>dash</em> (<code>-</code>), go to the relevant box and remove the lens with the given label if it is present in the box. Then, move any remaining lenses as far forward in the box as they can go without changing their order, filling any space made by removing the indicated lens. (If no lens in that box has the given label, nothing happens.)</p>
# MAGIC <p>If the operation character is an <em>equals sign</em> (<code>=</code>), it will be followed by a number indicating the <em>focal length</em> of the lens that needs to go into the relevant box; be sure to use the label maker to mark the lens with the label given in the beginning of the step so you can find it later. There are two possible situations:</p>
# MAGIC <ul>
# MAGIC <li>If there is already a lens in the box with the same label, <em>replace the old lens</em> with the new lens: remove the old lens and put the new lens in its place, not moving any other lenses in the box.</li>
# MAGIC <li>If there is <em>not</em> already a lens in the box with the same label, add the lens to the box immediately behind any lenses already in the box. Don't move any of the other lenses when you do this. If there aren't any lenses in the box, the new lens goes all the way to the front of the box.</li>
# MAGIC </ul>
# MAGIC <p>Here is the contents of every box after each step in the example initialization sequence above:</p>
# MAGIC <pre><code>After "rn=1":
# MAGIC Box 0: [rn 1]
# MAGIC
# MAGIC After "cm-":
# MAGIC Box 0: [rn 1]
# MAGIC
# MAGIC After "qp=3":
# MAGIC Box 0: [rn 1]
# MAGIC Box 1: [qp 3]
# MAGIC
# MAGIC After "cm=2":
# MAGIC Box 0: [rn 1] [cm 2]
# MAGIC Box 1: [qp 3]
# MAGIC
# MAGIC After "qp-":
# MAGIC Box 0: [rn 1] [cm 2]
# MAGIC
# MAGIC After "pc=4":
# MAGIC Box 0: [rn 1] [cm 2]
# MAGIC Box 3: [pc 4]
# MAGIC
# MAGIC After "ot=9":
# MAGIC Box 0: [rn 1] [cm 2]
# MAGIC Box 3: [pc 4] [ot 9]
# MAGIC
# MAGIC After "ab=5":
# MAGIC Box 0: [rn 1] [cm 2]
# MAGIC Box 3: [pc 4] [ot 9] [ab 5]
# MAGIC
# MAGIC After "pc-":
# MAGIC Box 0: [rn 1] [cm 2]
# MAGIC Box 3: [ot 9] [ab 5]
# MAGIC
# MAGIC After "pc=6":
# MAGIC Box 0: [rn 1] [cm 2]
# MAGIC Box 3: [ot 9] [ab 5] [pc 6]
# MAGIC
# MAGIC After "ot=7":
# MAGIC Box 0: [rn 1] [cm 2]
# MAGIC Box 3: [ot 7] [ab 5] [pc 6]
# MAGIC </code></pre>
# MAGIC <p>All 256 boxes are always present; only the boxes that contain any lenses are shown here. Within each box, lenses are listed from front to back; each lens is shown as its label and focal length in square brackets.</p>
# MAGIC <p>To confirm that all of the lenses are installed correctly, add up the <em>focusing power</em> of all of the lenses. The focusing power of a single lens is the result of multiplying together:</p>
# MAGIC <ul>
# MAGIC <li>One plus the box number of the lens in question.</li>
# MAGIC <li>The slot number of the lens within the box: <code>1</code> for the first lens, <code>2</code> for the second lens, and so on.</li>
# MAGIC <li>The focal length of the lens.</li>
# MAGIC </ul>
# MAGIC <p>At the end of the above example, the focusing power of each lens is as follows:</p>
# MAGIC <ul>
# MAGIC <li><code>rn</code>: <code>1</code> (box 0) * <code>1</code> (first slot) * <code>1</code> (focal length) = <code><em>1</em></code></li>
# MAGIC <li><code>cm</code>: <code>1</code> (box 0) * <code>2</code> (second slot) * <code>2</code> (focal length) = <code><em>4</em></code></li>
# MAGIC <li><code>ot</code>: <code>4</code> (box 3) * <code>1</code> (first slot) * <code>7</code> (focal length) = <code><em>28</em></code></li>
# MAGIC <li><code>ab</code>: <code>4</code> (box 3) * <code>2</code> (second slot) * <code>5</code> (focal length) = <code><em>40</em></code></li>
# MAGIC <li><code>pc</code>: <code>4</code> (box 3) * <code>3</code> (third slot) * <code>6</code> (focal length) = <code><em>72</em></code></li>
# MAGIC </ul>
# MAGIC <p>So, the above example ends up with a total focusing power of <code><em>145</em></code>.</p>
# MAGIC <p>With the help of an over-enthusiastic reindeer in a hard hat, follow the initialization sequence. <em>What is the focusing power of the resulting lens configuration?</em></p>
# MAGIC </article>

# COMMAND ----------

boxes = [[] for _ in range(256)]

for instruction in inp.split(','):
    if '=' in instruction:
        target, num = instruction.split('=')
        box = get_hash(target)
        
        for i, (t, n) in enumerate(boxes[box]):
            if t == target:
                boxes[box][i] = (target, num)
                break
        else:
            boxes[box].append((target, num))
    else: # -
        target = instruction[:-1]
        box = get_hash(target)
        for i, (t, n) in enumerate(boxes[box]):
            if t == target:
                del boxes[box][i]
                break

answer = 0
for i_box, box in enumerate(boxes, 1):
    for i_slot, (_, num) in enumerate(box, 1):
        answer += i_box * i_slot * int(num)
print(answer)
