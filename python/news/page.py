#!/usr/local/bin/python

import urllib, re, codecs
from bs4 import BeautifulSoup

def getArticles(exchange, symbol):
    fh = urllib.urlopen("http://www.google.com/finance/company_news?q=" \
                            + exchange +":" + symbol +"&start=0&num=100")
    return fh.read()

# returns link, date, src
# def parseURLs(lines):
#     links = []
#     dates = []
#     source = []
#     for i in range(len(lines)):
#         if lines[i]
#         if not lines[i].find("<span class=name>") == -1:
#             links.append(lines[i+1])
#     return links

def parseSources(d):
    sources = []
    spans=d.findAll("span", {"class" : "src"})
    for s in spans:
        sources.append(s.string)
    return sources

def parseDate(d):
    spans=d.findAll("span", {"class" : "date"})
    return spans[0].string

def standardizeDate(aDate):
    if(re.search("hour ago", aDate)):
        return u'Jun 9, 2012'
    else:
        return aDate


def parseTitles(d):
    titles = []
    links = d.findAll('a')
    articleLinks = links[:-1] #last element is "Related Stories"
    for l in articleLinks: 
        titles.append(l.contents[0].replace('\n', '')) # 0th element is the title
    return titles

def parseLinks(d):
    actualLinks = []
    links = d.findAll('a')
    articleLinks = links[:-1] #last element is "Related Stories"
    for l in articleLinks: 
        actualLinks.append(l["href"]) # 0th element is the title
    return actualLinks


def parseDiv(d):
    dstl = []
    sources = parseSources(d)
    links = parseLinks(d)
    titles = parseTitles(d)
    tuples = zip(sources, titles, links)
    date = standardizeDate(parseDate(d))
    for t in tuples:
        dstl.append((date, t[0], t[1], t[2]))
    return dstl;

def parsePage(page):
    dstl = []
    soup = BeautifulSoup(page)
    articleDivs = soup.findAll("div", {"class" : "g-section news sfe-break-bottom-16"})
    for d in articleDivs:
        dstl += parseDiv(d)
    return dstl

def dumpPSV(fh, market, symbol, vals):    
    for v in vals:
        fh.write(market + u"|" + symbol + u"|" + v[0] + u"|" + v[1] + u"|" + v[2] + u"|" + v[3] + u"\n")

        

def PSVForTicker(market, symbol, fh):
    page = getArticles(market, symbol)
    things = parsePage(page)    
    dumpPSV(fh, market, symbol, things)

def tickers():
    return [\
     #    (u"NASDAQ", u"FLWS"),\
     # (u"NASDAQ", u"FCTY"),\
     # (u"NASDAQ", u"FCCY"),
     # (u"NASDAQ", u"SRCE"),\
     # (u"NASDAQ", u"TCHC"),\
     # (u"NASDAQ", u"VNET"),\
     # (u"NASDAQ", u"SSRX"),\
     # (u"NASDAQ", u"JOBS"),\
     # (u"NASDAQ", u"EGHT"),\
     # (u"NASDAQ", u"AVHI"),\
     # (u"NASDAQ", u"SHLM"),\
     # (u"NASDAQ", u"AONE"),\
     # (u"NASDAQ", u"AAON"),\
     # (u"NASDAQ", u"ASTM"),\
     # (u"NASDAQ", u"ABAX"),\
     # (u"NASDAQ", u"ABMD"),\
     # (u"NASDAQ", u"AXAS"),\
     # (u"NASDAQ", u"ACTG"),\
     # (u"NASDAQ", u"ACHC"),\
     # (u"NASDAQ", u"ACAD"),\
     # (u"NASDAQ", u"ACCL"),\
     # (u"NASDAQ", u"ANCX"),\
     # (u"NASDAQ", u"ARAY"),\
     # (u"NASDAQ", u"ACRX"),\
     # (u"NASDAQ", u"ACET"),\
     # (u"NASDAQ", u"ACHN"),\
     # (u"NASDAQ", u"ACIW"),\
     # (u"NASDAQ", u"APKT"),\
     # (u"NASDAQ", u"ACNB"),\
     # (u"NASDAQ", u"ACOR"),\
     # (u"NASDAQ", u"ACFN"),\
     # (u"NASDAQ", u"ACTS"),\
     # (u"NASDAQ", u"ACPW"),\
     # (u"NASDAQ", u"ATVI"),\
     # (u"NASDAQ", u"BIRT"),\
     # (u"NASDAQ", u"ACUR"),\
     # (u"NASDAQ", u"ACXM"),\
     # (u"NASDAQ", u"ADES"),\
     # (u"NASDAQ", u"ADUS"),\
     # (u"NASDAQ", u"AEY"),\
     # (u"NASDAQ", u"ADEP"),\
     # (u"NASDAQ", u"ADBE"),\
     # (u"NASDAQ", u"ADTN"),\
     # (u"NASDAQ", u"AEIS"),\
     # (u"NASDAQ", u"ADVS"),\
     # (u"NASDAQ", u"AVCA"),\
     # (u"NASDAQ", u"AEGR"),\
     # (u"NASDAQ", u"AEGN"),\
     # (u"NASDAQ", u"AEHR"),\
     # (u"NASDAQ", u"AEPI"),\
     # (u"NASDAQ", u"AVAV"),\
     # (u"NASDAQ", u"AEZS"),\
     # (u"NASDAQ", u"ATRM"),\
     # (u"NASDAQ", u"AFCE"),\
     # (u"NASDAQ", u"AFFY"),\
     # (u"NASDAQ", u"AFFX"),\
     # (u"NASDAQ", u"AGEN"),\
     # (u"NASDAQ", u"AGYS"),\
     # (u"NASDAQ", u"AIRM"),\
     # (u"NASDAQ", u"AIRT"),\
     # (u"NASDAQ", u"ATSG"),\
     # (u"NASDAQ", u"AMCN"),\
     # (u"NASDAQ", u"AIXG"),\
     # (u"NASDAQ", u"AKAM"),\
     # (u"NASDAQ", u"AKRX"),\
     # (u"NASDAQ", u"ALSK"),\
     # (u"NASDAQ", u"AMRI"),\
     # (u"NASDAQ", u"ALXN"),\
     # (u"NASDAQ", u"ALXA"),\
     # (u"NASDAQ", u"ALCO"),\
     # (u"NASDAQ", u"ALGN"),\
     # (u"NASDAQ", u"ALIM"),\
     # (u"NASDAQ", u"ALKS"),\
     # (u"NASDAQ", u"ALGT"),\
     # (u"NASDAQ", u"ALLB"),\
     # (u"NASDAQ", u"ABVA"),\
     # (u"NASDAQ", u"AFOP"),\
     # (u"NASDAQ", u"ALNC"),\
     # (u"NASDAQ", u"AHGP"),\
     # (u"NASDAQ", u"ARLP"),\
     # (u"NASDAQ", u"AHPI"),\
     # (u"NASDAQ", u"AMOT"),\
     # (u"NASDAQ", u"ALTH"),\
     # (u"NASDAQ", u"ALLT"),\
     # (u"NASDAQ", u"MDRX"),\
     # (u"NASDAQ", u"AFAM"),\
     # (u"NASDAQ", u"ALNY"),\
     # (u"NASDAQ", u"AOSL"),\
     # (u"NASDAQ", u"ATEC"),\
     # (u"NASDAQ", u"ALTI"),\
     # (u"NASDAQ", u"ALTR"),\
     # (u"NASDAQ", u"ALTE"),\
     # (u"NASDAQ", u"ASPS"),\
     # (u"NASDAQ", u"APSA"),\
     # (u"NASDAQ", u"AIMC"),\
     # (u"NASDAQ", u"ALVR"),\
     # (u"NASDAQ", u"AMAG"),\
     # (u"NASDAQ", u"AMRN"),\
     # (u"NASDAQ", u"AMZN"),\
     # (u"NASDAQ", u"EPAX"),\
     # (u"NASDAQ", u"AMBT"),\
     # (u"NASDAQ", u"AMCX"),\
     # (u"NASDAQ", u"AMED"),\
     # (u"NASDAQ", u"UHAL"),\
     # (u"NASDAQ", u"ASBI"),\
     # (u"NASDAQ", u"ATAX"),\
     # (u"NASDAQ", u"AMOV"),\
     # (u"NASDAQ", u"AGNC"),\
     # (u"NASDAQ", u"AGNCP"),\
     # (u"NASDAQ", u"MTGE"),\
     # (u"NASDAQ", u"ACAS"),\
     # (u"NASDAQ", u"ANCI"),\
     # (u"NASDAQ", u"AETI"),\
     # (u"NASDAQ", u"AMIC"),\
     # (u"NASDAQ", u"ALRN"),\
     # (u"NASDAQ", u"AMNB"),\
     # (u"NASDAQ", u"ANAT"),\
     # (u"NASDAQ", u"APFC"),\
     # (u"NASDAQ", u"APEI"),\
     # (u"NASDAQ", u"ARII"),\
     # (u"NASDAQ", u"ARCP"),\
     # (u"NASDAQ", u"ARCT"),\
     # (u"NASDAQ", u"AMRB"),\
     # (u"NASDAQ", u"ASEI"),\
     # (u"NASDAQ", u"AMSWA"),\
     # (u"NASDAQ", u"AMSC"),\
     # (u"NASDAQ", u"AMWD"),\
     # (u"NASDAQ", u"CRMT"),\
     # (u"NASDAQ", u"ARGN"),\
     # (u"NASDAQ", u"ABCB"),\
     # (u"NASDAQ", u"AMSF"),\
     # (u"NASDAQ", u"ASRV"),\
     # (u"NASDAQ", u"ASRVP"),\
     # (u"NASDAQ", u"ASCA"),\
     # (u"NASDAQ", u"ATLO"),\
     # (u"NASDAQ", u"AMGN"),\
     # (u"NASDAQ", u"FOLD"),\
     # (u"NASDAQ", u"AMKR"),\
     # (u"NASDAQ", u"AMPL"),\
     # (u"NASDAQ", u"AMPE"),\
     # (u"NASDAQ", u"AMSG"),\
     # (u"NASDAQ", u"ASYS"),\
     # (u"NASDAQ", u"AFSI"),\
     # (u"NASDAQ", u"AMLN"),\
     # (u"NASDAQ", u"AMRS"),\
     # (u"NASDAQ", u"ANAC"),\
     # (u"NASDAQ", u"ANAD"),\
     # (u"NASDAQ", u"ADI"),\
     # (u"NASDAQ", u"ALOG"),\
     # (u"NASDAQ", u"ANLY"),\
     # (u"NASDAQ", u"ANEN"),\
     # (u"NASDAQ", u"ACOM"),\
     # (u"NASDAQ", u"ANCB"),\
     # (u"NASDAQ", u"AMCF"),\
     # (u"NASDAQ", u"ANDA"),\
     # (u"NASDAQ", u"ANDAU"),\
     # (u"NASDAQ", u"ANDAW"),\
     # (u"NASDAQ", u"ANGN"),\
     # (u"NASDAQ", u"ANGI"),\
     # (u"NASDAQ", u"ANGO"),\
     # (u"NASDAQ", u"ANIK"),\
     # (u"NASDAQ", u"ANNB"),\
     # (u"NASDAQ", u"ANSS"),\
     # (u"NASDAQ", u"ANTH"),\
     # (u"NASDAQ", u"APAGF"),\
     # (u"NASDAQ", u"ATNY"),\
     # (u"NASDAQ", u"APOG"),\
     # (u"NASDAQ", u"APOL"),\
     # (u"NASDAQ", u"AINV"),\
     # (u"NASDAQ", u"AAPL"),\
     # (u"NASDAQ", u"ARCI"),\
     # (u"NASDAQ", u"AMAT"),\
     # (u"NASDAQ", u"AMCC"),\
     # (u"NASDAQ", u"AREX"),\
     # (u"NASDAQ", u"APRI"),\
     # (u"NASDAQ", u"ARCW"),\
     # (u"NASDAQ", u"ABIO"),\
     # (u"NASDAQ", u"ACGL"),\
     # (u"NASDAQ", u"ACAT"),\
     # (u"NASDAQ", u"RDEA"),\
     # (u"NASDAQ", u"ARDNA"),\
     # (u"NASDAQ", u"ARNA"),\
     # (u"NASDAQ", u"ARCC"),\
     # (u"NASDAQ", u"AGII"),\
     # (u"NASDAQ", u"ARIA"),\
     # (u"NASDAQ", u"ARBA"),\
     # (u"NASDAQ", u"ARKR"),\
     # (u"NASDAQ", u"ABFS"),\
     # (u"NASDAQ", u"ARMH"),\
     # (u"NASDAQ", u"ARTX"),\
     # (u"NASDAQ", u"ARQL"),\
     # (u"NASDAQ", u"ARRY"),\
     # (u"NASDAQ", u"ARRS"),\
     # (u"NASDAQ", u"AROW"),\
     # (u"NASDAQ", u"ARWR"),\
     # (u"NASDAQ", u"ARTNA"),\
     # (u"NASDAQ", u"ARTC"),\
     # (u"NASDAQ", u"ARTW"),\
     # (u"NASDAQ", u"ARUN"),\
     # (u"NASDAQ", u"ASBB"),\
     # (u"NASDAQ", u"ASNA"),\
     # (u"NASDAQ", u"ASCMA"),\
     # (u"NASDAQ", u"ASTI"),\
     # (u"NASDAQ", u"AERL"),\
     # (u"NASDAQ", u"APWC"),\
     # (u"NASDAQ", u"ASIA"),\
     # (u"NASDAQ", u"ASMI"),\
     # (u"NASDAQ", u"ASML"),\
     # (u"NASDAQ", u"AZPN"),\
     # (u"NASDAQ", u"APPY"),\
     # (u"NASDAQ", u"AACC"),\
     # (u"NASDAQ", u"ASBC"),\
     # (u"NASDAQ", u"ASBCW"),\
     # (u"NASDAQ", u"ASFI"),\
     # (u"NASDAQ", u"ATEA"),\
     # (u"NASDAQ", u"ASTE"),\
     # (u"NASDAQ", u"ASTX"),\
     # (u"NASDAQ", u"ALOT"),\
     # (u"NASDAQ", u"ATRO"),\
     # (u"NASDAQ", u"ASTC"),\
     # (u"NASDAQ", u"ASUR"),\
     # (u"NASDAQ", u"ATAI"),\
     # (u"NASDAQ", u"ATHN"),\
     # (u"NASDAQ", u"AFCB"),\
     # (u"NASDAQ", u"ATHX"),\
     # (u"NASDAQ", u"AAME"),\
     # (u"NASDAQ", u"ACFC"),\
     # (u"NASDAQ", u"ATNI"),\
     # (u"NASDAQ", u"AAWW"),\
     # (u"NASDAQ", u"ATML"),\
     # (u"NASDAQ", u"ATMI"),\
     # (u"NASDAQ", u"ATPG"),\
     # (u"NASDAQ", u"ATRC"),\
     # (u"NASDAQ", u"ATRI"),\
     # (u"NASDAQ", u"AUBN"),\
     # (u"NASDAQ", u"ADNC"),\
     # (u"NASDAQ", u"AUDC"),\
     # (u"NASDAQ", u"AAC"),\
     # (u"NASDAQ", u"AACOU"),\
     # (u"NASDAQ", u"AACOW"),\
     # (u"NASDAQ", u"AUTH"),\
     # (u"NASDAQ", u"ADAT"),\
     # (u"NASDAQ", u"ABTL"),\
     # (u"NASDAQ", u"ADSK"),\
     # (u"NASDAQ", u"ADP"),\
     # (u"NASDAQ", u"AMAP"),\
     # (u"NASDAQ", u"AUXL"),\
     # (u"NASDAQ", u"AVGO"),\
     # (u"NASDAQ", u"AVNR"),\
     # (u"NASDAQ", u"AVEO"),\
     # (u"NASDAQ", u"AVII"),\
     # (u"NASDAQ", u"AVNW"),\
     # (u"NASDAQ", u"AVID"),\
     # (u"NASDAQ", u"CAR"),\
     # (u"NASDAQ", u"AWRE"),\
     # (u"NASDAQ", u"ACLS"),\
     # (u"NASDAQ", u"AXTI"),\
     # (u"NASDAQ", u"BCOM"),\
     # (u"NASDAQ", u"BOSC"),\
     # (u"NASDAQ", u"BIDU"),\
     # (u"NASDAQ", u"BCPC"),\
     # (u"NASDAQ", u"BWINA"),\
     # (u"NASDAQ", u"BWINB"),\
     # (u"NASDAQ", u"BLDP"),\
     # (u"NASDAQ", u"BANF"),\
     # (u"NASDAQ", u"BANFP"),\
     # (u"NASDAQ", u"BTFG"),\
     # (u"NASDAQ", u"BKMU"),\
     # (u"NASDAQ", u"BOCH"),\
     # (u"NASDAQ", u"BMRC"),\
     # (u"NASDAQ", u"BKSC"),\
     # (u"NASDAQ", u"BOTJ"),\
     # (u"NASDAQ", u"OZRK"),\
     # (u"NASDAQ", u"BOVA"),\
     # (u"NASDAQ", u"BBXT"),\
     # (u"NASDAQ", u"BFIN"),\
     # (u"NASDAQ", u"BANR"),\
     # (u"NASDAQ", u"BBSI"),\
     # (u"NASDAQ", u"BSET"),\
     # (u"NASDAQ", u"BV"),\
     # (u"NASDAQ", u"BBCN"),\
     # (u"NASDAQ", u"BCBP"),\
     # (u"NASDAQ", u"BCDS"),\
     # (u"NASDAQ", u"BCSB"),\
     # (u"NASDAQ", u"BEAV"),\
     # (u"NASDAQ", u"BFED"),\
     # (u"NASDAQ", u"BECN"),\
     # (u"NASDAQ", u"BBGI"),\
     # (u"NASDAQ", u"BEBE"),\
     # (u"NASDAQ", u"BBBY"),\
     # (u"NASDAQ", u"BELFA"),\
     # (u"NASDAQ", u"BELFB"),\
     # (u"NASDAQ", u"BNCL"),\
     # (u"NASDAQ", u"BNHN"),\
     # (u"NASDAQ", u"BERK"),\
     # (u"NASDAQ", u"BHLB"),\
     # (u"NASDAQ", u"BGMD"),\
     # (u"NASDAQ", u"BGCP"),\
     # (u"NASDAQ", u"BGSC"),\
     # (u"NASDAQ", u"BGSCU"),\
     # (u"NASDAQ", u"BGSCW"),\
     # (u"NASDAQ", u"BIDZ"),\
     # (u"NASDAQ", u"BGFV"),\
     # (u"NASDAQ", u"BASI"),\
     # (u"NASDAQ", u"BIOC"),\
     # (u"NASDAQ", u"BCRX"),\
     # (u"NASDAQ", u"BIOD"),\
     # (u"NASDAQ", u"BDSI"),\
     # (u"NASDAQ", u"BIOF"),\
     # (u"NASDAQ", u"BIIB"),\
     # (u"NASDAQ", u"BIOL"),\
     # (u"NASDAQ", u"BLRX"),\
     # (u"NASDAQ", u"BMRN"),\
     # (u"NASDAQ", u"BMTI"),\
     # (u"NASDAQ", u"BRLI"),\
     # (u"NASDAQ", u"BPAX"),\
     # (u"NASDAQ", u"BIOS"),\
     # (u"NASDAQ", u"BSTC"),\
     # (u"NASDAQ", u"BSPM"),\
     # (u"NASDAQ", u"BDMS"),\
     # (u"NASDAQ", u"BJRI"),\
     # (u"NASDAQ", u"BBOX"),\
     # (u"NASDAQ", u"BDE"),\
     # (u"NASDAQ", u"BLKB"),\
     # (u"NASDAQ", u"BKCC"),\
     # (u"NASDAQ", u"ADRA"),\
     # (u"NASDAQ", u"ADRD"),\
     # (u"NASDAQ", u"ADRE"),\
     # (u"NASDAQ", u"ADRU"),\
     # (u"NASDAQ", u"BCOR"),\
     # (u"NASDAQ", u"NILE"),\
     # (u"NASDAQ", u"MNGL"),\
     # (u"NASDAQ", u"MNGLU"),\
     # (u"NASDAQ", u"MNGLW"),\
     # (u"NASDAQ", u"BFLY"),\
     # (u"NASDAQ", u"BKEP"),\
     # (u"NASDAQ", u"BKEPP"),\
     # (u"NASDAQ", u"BPHX"),\
     # (u"NASDAQ", u"BMC"),\
     # (u"NASDAQ", u"BNCN"),\
     # (u"NASDAQ", u"BOBE"),\
     # (u"NASDAQ", u"BODY"),\
     # (u"NASDAQ", u"BOFI"),\
     # (u"NASDAQ", u"WIFI"),\
     # (u"NASDAQ", u"BOKF"),\
     # (u"NASDAQ", u"BOLT"),\
     # (u"NASDAQ", u"BONA"),\
     # (u"NASDAQ", u"BNSO"),\
     # (u"NASDAQ", u"BAMM"),\
     # (u"NASDAQ", u"BPFH"),\
     # (u"NASDAQ", u"BPFHW"),\
     # (u"NASDAQ", u"EPAY"),\
     # (u"NASDAQ", u"BBRG"),\
     # (u"NASDAQ", u"BBEP"),\
     # (u"NASDAQ", u"BDGE"),\
     # (u"NASDAQ", u"BBNK"),\
     # (u"NASDAQ", u"BLIN"),\
     # (u"NASDAQ", u"BRID"),\
     # (u"NASDAQ", u"BCOV"),\
     # (u"NASDAQ", u"CELL"),\
     # (u"NASDAQ", u"BKBK"),\
     # (u"NASDAQ", u"BRCM"),\
     # (u"NASDAQ", u"BSFT"),\
     # (u"NASDAQ", u"BVSN"),\
     # (u"NASDAQ", u"BYFC"),\
     # (u"NASDAQ", u"BWEN"),\
     # (u"NASDAQ", u"BRCD"),\
     # (u"NASDAQ", u"BRKL"),\
     # (u"NASDAQ", u"BRKS"),\
     # (u"NASDAQ", u"BRKR"),\
     # (u"NASDAQ", u"BMTC"),\
     # (u"NASDAQ", u"BLMT"),\
     # (u"NASDAQ", u"BSDM"),\
     # (u"NASDAQ", u"BSQR"),\
     # (u"NASDAQ", u"BTUI"),\
     # (u"NASDAQ", u"BWLD"),\
     # (u"NASDAQ", u"BLDR"),\
     # (u"NASDAQ", u"BUR"),\
     # (u"NASDAQ", u"CFFI"),\
     # (u"NASDAQ", u"CHRW"),\
     # (u"NASDAQ", u"CA"),\
     # (u"NASDAQ", u"CCMP"),\
     # (u"NASDAQ", u"CACH"),\
     # (u"NASDAQ", u"CDNS"),\
     # (u"NASDAQ", u"CADX"),\
     # (u"NASDAQ", u"CDZI"),\
     # (u"NASDAQ", u"CZR"),\
     # (u"NASDAQ", u"CSTE"),\
     # (u"NASDAQ", u"PRSS"),\
     # (u"NASDAQ", u"CLMS"),\
     # (u"NASDAQ", u"CAMP"),\
     # (u"NASDAQ", u"CVGW"),\
     # (u"NASDAQ", u"CFNB"),\
     # (u"NASDAQ", u"CALD"),\
     # (u"NASDAQ", u"CALM"),\
     # (u"NASDAQ", u"CLMT"),\
     # (u"NASDAQ", u"ABCD"),\
     # (u"NASDAQ", u"CAFI"),\
     # (u"NASDAQ", u"CAC"),\
     # (u"NASDAQ", u"CAMT"),\
     # (u"NASDAQ", u"CSIQ"),\
     # (u"NASDAQ", u"CPHC"),\
     # (u"NASDAQ", u"CBNJ"),\
     # (u"NASDAQ", u"CPLA"),\
     # (u"NASDAQ", u"CBKN"),\
     # (u"NASDAQ", u"CCBG"),\
     # (u"NASDAQ", u"CPLP"),\
     # (u"NASDAQ", u"CSWC"),\
     # (u"NASDAQ", u"CFFN"),\
     # (u"NASDAQ", u"CPST"),\
     # (u"NASDAQ", u"CARB"),\
     # (u"NASDAQ", u"CRDC"),\
     # (u"NASDAQ", u"CFNL"),\
     # (u"NASDAQ", u"CRME"),\
     # (u"NASDAQ", u"BEAT"),\
     # (u"NASDAQ", u"CSII"),\
     # (u"NASDAQ", u"CATM"),\
     # (u"NASDAQ", u"CECO"),\
     # (u"NASDAQ", u"CBOU"),\
     # (u"NASDAQ", u"CKEC"),\
     # (u"NASDAQ", u"CLBH"),\
     # (u"NASDAQ", u"CART"),\
     # (u"NASDAQ", u"CRZO"),\
     # (u"NASDAQ", u"CRRB"),\
     # (u"NASDAQ", u"TAST"),\
     # (u"NASDAQ", u"CARV"),\
     # (u"NASDAQ", u"CASM"),\
     # (u"NASDAQ", u"CACB"),\
     # (u"NASDAQ", u"CSCD"),\
     # (u"NASDAQ", u"CWST"),\
     # (u"NASDAQ", u"CASY"),\
     # (u"NASDAQ", u"CASS"),\
     # (u"NASDAQ", u"CMRG"),\
     # (u"NASDAQ", u"CHSI"),\
     # (u"NASDAQ", u"CPRX"),\
     # (u"NASDAQ", u"CATY"),\
     # (u"NASDAQ", u"CVCO"),\
     # (u"NASDAQ", u"CAVM"),\
     # (u"NASDAQ", u"CAZA"),\
     # (u"NASDAQ", u"CAZAU"),\
     # (u"NASDAQ", u"CAZAW"),\
     # (u"NASDAQ", u"CBEY"),\
     # (u"NASDAQ", u"CBOE"),\
     # (u"NASDAQ", u"CDII"),\
     # (u"NASDAQ", u"CFK"),\
     # (u"NASDAQ", u"CECE"),\
     # (u"NASDAQ", u"CELG"),\
     # (u"NASDAQ", u"CELGZ"),\
     # (u"NASDAQ", u"CTIC"),\
     # (u"NASDAQ", u"CLDX"),\
     # (u"NASDAQ", u"CLSN"),\
     # (u"NASDAQ", u"CEMP"),\
     # (u"NASDAQ", u"CNBC"),\
     # (u"NASDAQ", u"CSFL"),\
     # (u"NASDAQ", u"CEBK"),\
     # (u"NASDAQ", u"CEDC"),\
     # (u"NASDAQ", u"CETV"),\
     # (u"NASDAQ", u"CFBK"),\
     # (u"NASDAQ", u"CENT"),\
     # (u"NASDAQ", u"CENTA"),\
     # (u"NASDAQ", u"CVCY"),\
     # (u"NASDAQ", u"CENX"),\
     # (u"NASDAQ", u"CNBKA"),\
     # (u"NASDAQ", u"CNTY"),\
     # (u"NASDAQ", u"CPHD"),\
     # (u"NASDAQ", u"CRDN"),\
     # (u"NASDAQ", u"CRNT"),\
     # (u"NASDAQ", u"CERP"),\
     # (u"NASDAQ", u"CERE"),\
     # (u"NASDAQ", u"CERN"),\
     # (u"NASDAQ", u"CERS"),\
     # (u"NASDAQ", u"CEVA"),\
     # (u"NASDAQ", u"CITZ"),\
     # (u"NASDAQ", u"CHMP"),\
     # (u"NASDAQ", u"CYOU"),\
     # (u"NASDAQ", u"CTHR"),\
     # (u"NASDAQ", u"CHRM"),\
     # (u"NASDAQ", u"CHRS"),\
     # (u"NASDAQ", u"GTLS"),\
     # (u"NASDAQ", u"CHTR"),\
     # (u"NASDAQ", u"CHFN"),\
     # (u"NASDAQ", u"CHKP"),\
     # (u"NASDAQ", u"CHTP"),\
     # (u"NASDAQ", u"CEMI"),\
     # (u"NASDAQ", u"CHFC"),\
     # (u"NASDAQ", u"CCXI"),\
     # (u"NASDAQ", u"CHKE"),\
     # (u"NASDAQ", u"CHEV"),\
     # (u"NASDAQ", u"CBNK"),\
     # (u"NASDAQ", u"CADC"),\
     # (u"NASDAQ", u"CALI"),\
     # (u"NASDAQ", u"CAAS"),\
     # (u"NASDAQ", u"CBAK"),\
     # (u"NASDAQ", u"CBPO"),\
     # (u"NASDAQ", u"CCCL"),\
     # (u"NASDAQ", u"CCCLU"),\
     # (u"NASDAQ", u"CCCLW"),\
     # (u"NASDAQ", u"JRJC"),\
     # (u"NASDAQ", u"CHOP"),\
     # (u"NASDAQ", u"CGEI"),\
     # (u"NASDAQ", u"CGEIU"),\
     # (u"NASDAQ", u"CGEIW"),\
     # (u"NASDAQ", u"HGSH"),\
     # (u"NASDAQ", u"CHLN"),\
     # (u"NASDAQ", u"CNIT"),\
     # (u"NASDAQ", u"CJJD"),\
     # (u"NASDAQ", u"HTHT"),\
     # (u"NASDAQ", u"CHNR"),\
     # (u"NASDAQ", u"NKBP"),\
     # (u"NASDAQ", u"CPSL"),\
     # (u"NASDAQ", u"CREG"),\
     # (u"NASDAQ", u"CPGI"),\
     # (u"NASDAQ", u"CSUN"),\
     # (u"NASDAQ", u"CNTF"),\
     # (u"NASDAQ", u"CTDC"),\
     # (u"NASDAQ", u"CTFO"),\
     # (u"NASDAQ", u"CVVT"),\
     # (u"NASDAQ", u"CXDC"),\
     # (u"NASDAQ", u"CNYD"),\
     # (u"NASDAQ", u"CCIH"),\
     # (u"NASDAQ", u"CAST"),\
     # (u"NASDAQ", u"CEDU"),\
     # (u"NASDAQ", u"CNET"),\
     # (u"NASDAQ", u"CHDX"),\
     # (u"NASDAQ", u"IMOS"),\
     # (u"NASDAQ", u"CHSCP"),\
     # (u"NASDAQ", u"CHDN"),\
     # (u"NASDAQ", u"CHYR"),\
     # (u"NASDAQ", u"CIEN"),\
     # (u"NASDAQ", u"DFR"),\
     # (u"NASDAQ", u"CIMT"),\
     # (u"NASDAQ", u"CINF"),\
     # (u"NASDAQ", u"CIDM"),\
     # (u"NASDAQ", u"CTAS"),\
     # (u"NASDAQ", u"CRUS"),\
     # (u"NASDAQ", u"CSCO"),\
     # (u"NASDAQ", u"CTRN"),\
     # (u"NASDAQ", u"CZNC"),\
     # (u"NASDAQ", u"CZWI"),\
     # (u"NASDAQ", u"CZFC"),\
     # (u"NASDAQ", u"CIZN"),\
     # (u"NASDAQ", u"CRBC"),\
     # (u"NASDAQ", u"CSBC"),\
     # (u"NASDAQ", u"CTXS"),\
     # (u"NASDAQ", u"CHCO"),\
     # (u"NASDAQ", u"CTEL"),\
     # (u"NASDAQ", u"CWEI"),\
     # (u"NASDAQ", u"CDTI"),\
     # (u"NASDAQ", u"CLNE"),\
     # (u"NASDAQ", u"CLNT"),\
     # (u"NASDAQ", u"CLFD"),\
     # (u"NASDAQ", u"CLRO"),\
     # (u"NASDAQ", u"CLIR"),\
     # (u"NASDAQ", u"CLWR"),\
     # (u"NASDAQ", u"CBLI"),\
     # (u"NASDAQ", u"CKSW"),\
     # (u"NASDAQ", u"CSBK"),\
     # (u"NASDAQ", u"CLVS"),\
     # (u"NASDAQ", u"CME"),\
     # (u"NASDAQ", u"CMSB"),\
     # (u"NASDAQ", u"CCNE"),\
     # (u"NASDAQ", u"CISG"),\
     # (u"NASDAQ", u"COBZ"),\
     # (u"NASDAQ", u"COBR"),\
     # (u"NASDAQ", u"COKE"),\
     # (u"NASDAQ", u"CDXS"),\
     # (u"NASDAQ", u"CVLY"),\
     # (u"NASDAQ", u"JVA"),\
     # (u"NASDAQ", u"CCOI"),\
     # (u"NASDAQ", u"CGNX"),\
     # (u"NASDAQ", u"CTSH"),\
     # (u"NASDAQ", u"COGO"),\
     # (u"NASDAQ", u"COHR"),\
     # (u"NASDAQ", u"COHU"),\
     # (u"NASDAQ", u"CSTR"),\
     # (u"NASDAQ", u"CWTR"),\
     # (u"NASDAQ", u"CCIX"),\
     # (u"NASDAQ", u"CLCT"),\
     # (u"NASDAQ", u"COBK"),\
     # (u"NASDAQ", u"CBAN"),\
     # (u"NASDAQ", u"COLB"),\
     # (u"NASDAQ", u"CBRX"),\
     # (u"NASDAQ", u"COLM"),\
     # (u"NASDAQ", u"CMCO"),\
     # (u"NASDAQ", u"CBMX"),\
     # (u"NASDAQ", u"CBMXW"),\
     # (u"NASDAQ", u"CMCSA"),\
     # (u"NASDAQ", u"CMCSK"),\
     # (u"NASDAQ", u"CBSH"),\
     # (u"NASDAQ", u"CNAF"),\
     # (u"NASDAQ", u"CVGI"),\
     # (u"NASDAQ", u"CTCH"),\
     # (u"NASDAQ", u"JCS"),\
     # (u"NASDAQ", u"CBIN"),\
     # (u"NASDAQ", u"CFFC"),\
     # (u"NASDAQ", u"CPBC"),\
     # (u"NASDAQ", u"CTBI"),\
     # (u"NASDAQ", u"CWBC"),\
     # (u"NASDAQ", u"CVLT"),\
     # (u"NASDAQ", u"GNOM"),\
     # (u"NASDAQ", u"GSJK"),\
     # (u"NASDAQ", u"CCRT"),\
     # (u"NASDAQ", u"CGEN"),\
     # (u"NASDAQ", u"CPSI"),\
     # (u"NASDAQ", u"CTGX"),\
     # (u"NASDAQ", u"CPWR"),\
     # (u"NASDAQ", u"SCOR"),\
     # (u"NASDAQ", u"CHCI"),\
     # (u"NASDAQ", u"CMTL"),\
     # (u"NASDAQ", u"CMVT"),\
     # (u"NASDAQ", u"CPTS"),\
     # (u"NASDAQ", u"CNQR"),\
     # (u"NASDAQ", u"CCUR"),\
     # (u"NASDAQ", u"CNMD"),\
     # (u"NASDAQ", u"CTWS"),\
     # (u"NASDAQ", u"CONN"),\
     # (u"NASDAQ", u"CNSL"),\
     # (u"NASDAQ", u"CWCO"),\
     # (u"NASDAQ", u"CTCT"),\
     # (u"NASDAQ", u"CPSS"),\
     # (u"NASDAQ", u"CPNO"),\
     # (u"NASDAQ", u"CPRT"),\
     # (u"NASDAQ", u"CORT"),\
     # (u"NASDAQ", u"CORE"),\
     # (u"NASDAQ", u"COCO"),\
     # (u"NASDAQ", u"CSOD"),\
     # (u"NASDAQ", u"CRTX"),\
     # (u"NASDAQ", u"CNDO"),\
     # (u"NASDAQ", u"CRVL"),\
     # (u"NASDAQ", u"COSI"),\
     # (u"NASDAQ", u"CPWM"),\
     # (u"NASDAQ", u"CSGP"),\
     # (u"NASDAQ", u"COST"),\
     # (u"NASDAQ", u"CRRC"),\
     # (u"NASDAQ", u"CVTI"),\
     # (u"NASDAQ", u"COWN"),\
     # (u"NASDAQ", u"CRAI"),\
     # (u"NASDAQ", u"CBRL"),\
     # (u"NASDAQ", u"BREW"),\
     # (u"NASDAQ", u"CRAY"),\
     # (u"NASDAQ", u"CACC"),\
     # (u"NASDAQ", u"CRED"),\
     # (u"NASDAQ", u"CREE"),\
     # (u"NASDAQ", u"CRFN"),\
     # (u"NASDAQ", u"CRESW"),\
     # (u"NASDAQ", u"CRESY"),\
     # (u"NASDAQ", u"CXPO"),\
     # (u"NASDAQ", u"CROX"),\
     # (u"NASDAQ", u"ATX"),\
     # (u"NASDAQ", u"CCRN"),\
     # (u"NASDAQ", u"CRDS"),\
     # (u"NASDAQ", u"XTXI"),\
     # (u"NASDAQ", u"XTEX"),\
     # (u"NASDAQ", u"CRWS"),\
     # (u"NASDAQ", u"CRWN"),\
     # (u"NASDAQ", u"CRMB"),\
     # (u"NASDAQ", u"CRMBU"),\
     # (u"NASDAQ", u"CRMBW"),\
     # (u"NASDAQ", u"CRYP"),\
     # (u"NASDAQ", u"CSGS"),\
     # (u"NASDAQ", u"CSPI"),\
     # (u"NASDAQ", u"CSRE"),\
     # (u"NASDAQ", u"CTCM"),\
     # (u"NASDAQ", u"CTIB"),\
     # (u"NASDAQ", u"CTRP"),\
     # (u"NASDAQ", u"CBST"),\
     # (u"NASDAQ", u"CUI"),\
     # (u"NASDAQ", u"CPIX"),\
     # (u"NASDAQ", u"CMLS"),\
     # (u"NASDAQ", u"CRIS"),\
     # (u"NASDAQ", u"CUTR"),\
     # (u"NASDAQ", u"CVBF"),\
     # (u"NASDAQ", u"CVV"),\
     # (u"NASDAQ", u"CYAN"),\
     # (u"NASDAQ", u"CYBX"),\
     # (u"NASDAQ", u"CYBE"),\
     # (u"NASDAQ", u"CYBI"),\
     # (u"NASDAQ", u"CYCC"),\
     # (u"NASDAQ", u"CYCCP"),\
     # (u"NASDAQ", u"CYMI"),\
     # (u"NASDAQ", u"CYNO"),\
     # (u"NASDAQ", u"CY"),\
     # (u"NASDAQ", u"CYTK"),\
     # (u"NASDAQ", u"CYTX"),\
     # (u"NASDAQ", u"CYTXW"),\
     # (u"NASDAQ", u"CYTR"),\
     # (u"NASDAQ", u"DMED"),\
     # (u"NASDAQ", u"DAEG"),\
     # (u"NASDAQ", u"DJCO"),\
     # (u"NASDAQ", u"DAKT"),\
     # (u"NASDAQ", u"DARA"),\
     # (u"NASDAQ", u"DAIO"),\
     # (u"NASDAQ", u"DTLK"),\
     # (u"NASDAQ", u"DRAM"),\
     # (u"NASDAQ", u"DWCH"),\
     # (u"NASDAQ", u"DWSN"),\
     # (u"NASDAQ", u"DSTI"),\
     # (u"NASDAQ", u"TRAK"),\
     # (u"NASDAQ", u"DECK"),\
     # (u"NASDAQ", u"DEER"),\
     # (u"NASDAQ", u"DHRM"),\
     # (u"NASDAQ", u"DCTH"),\
     # (u"NASDAQ", u"DLIA"),\
     # (u"NASDAQ", u"DELL"),\
     # (u"NASDAQ", u"DGAS"),\
     # (u"NASDAQ", u"PROJ"),\
     # (u"NASDAQ", u"DNDN"),\
     # (u"NASDAQ", u"DENN"),\
     # (u"NASDAQ", u"XRAY"),\
     # (u"NASDAQ", u"DEPO"),\
     # (u"NASDAQ", u"DSCI"),\
     # (u"NASDAQ", u"DEST"),\
     # (u"NASDAQ", u"DSWL"),\
     # (u"NASDAQ", u"DXCM"),\
     # (u"NASDAQ", u"DLLR"),\
     # (u"NASDAQ", u"DIAL"),\
     # (u"NASDAQ", u"DLGC"),\
     # (u"NASDAQ", u"DMND"),\
     # (u"NASDAQ", u"DHFT"),\
     # (u"NASDAQ", u"DHIL"),\
     # (u"NASDAQ", u"DCIX"),\
     # (u"NASDAQ", u"DGII"),\
     # (u"NASDAQ", u"DMRC"),\
     # (u"NASDAQ", u"DRAD"),\
     # (u"NASDAQ", u"DGLY"),\
     # (u"NASDAQ", u"DCIN"),\
     # (u"NASDAQ", u"DGIT"),\
     # (u"NASDAQ", u"DRIV"),\
     # (u"NASDAQ", u"DCOM"),\
     # (u"NASDAQ", u"DIOD"),\
     # (u"NASDAQ", u"MKTS"),\
     # (u"NASDAQ", u"DTV"),\
     # (u"NASDAQ", u"DISCA"),\
     # (u"NASDAQ", u"DISCB"),\
     # (u"NASDAQ", u"DISCK"),\
     # (u"NASDAQ", u"DSCO"),\
     # (u"NASDAQ", u"DISH"),\
     # (u"NASDAQ", u"DITC"),\
     # (u"NASDAQ", u"DNBF"),\
     # (u"NASDAQ", u"DLTR"),\
     # (u"NASDAQ", u"DGICA"),\
     # (u"NASDAQ", u"DGICB"),\
     # (u"NASDAQ", u"DMLP"),\
     # (u"NASDAQ", u"DORM"),\
     # (u"NASDAQ", u"HILL"),\
     # (u"NASDAQ", u"DBLE"),\
     # (u"NASDAQ", u"DBLEP"),\
     # (u"NASDAQ", u"DOVR"),\
     # (u"NASDAQ", u"DRWI"),\
     # (u"NASDAQ", u"DWA"),\
     # (u"NASDAQ", u"DRYS"),\
     # (u"NASDAQ", u"DSPG"),\
     # (u"NASDAQ", u"DTSI"),\
     # (u"NASDAQ", u"DUCK"),\
     # (u"NASDAQ", u"DNKN"),\
     # (u"NASDAQ", u"DRRX"),\
     # (u"NASDAQ", u"DUSA"),\
     # (u"NASDAQ", u"DXPE"),\
     # (u"NASDAQ", u"DYAX"),\
     # (u"NASDAQ", u"DYII"),\
     # (u"NASDAQ", u"BOOM"),\
     # (u"NASDAQ", u"DRCO"),\
     # (u"NASDAQ", u"DYSL"),\
     # (u"NASDAQ", u"DYNT"),\
     # (u"NASDAQ", u"DVAX"),\
     # (u"NASDAQ", u"DVOX"),\
     # (u"NASDAQ", u"ETFC"),\
     # (u"NASDAQ", u"EBMT"),\
     # (u"NASDAQ", u"EGBN"),\
     # (u"NASDAQ", u"EGLE"),\
     # (u"NASDAQ", u"EROC"),\
     # (u"NASDAQ", u"ELNK"),\
     # (u"NASDAQ", u"EWBC"),\
     # (u"NASDAQ", u"EML"),\
     # (u"NASDAQ", u"EIHI"),\
     # (u"NASDAQ", u"EVBS"),\
     # (u"NASDAQ", u"ESIC"),\
     # (u"NASDAQ", u"EBAY"),\
     # (u"NASDAQ", u"EBIX"),\
     # (u"NASDAQ", u"ELON"),\
     # (u"NASDAQ", u"ECHO"),\
     # (u"NASDAQ", u"ECTE"),\
     # (u"NASDAQ", u"SATS"),\
     # (u"NASDAQ", u"EEI"),\
     # (u"NASDAQ", u"ECTY"),\
     # (u"NASDAQ", u"EDAC"),\
     # (u"NASDAQ", u"EDAP"),\
     # (u"NASDAQ", u"EF"),\
     # (u"NASDAQ", u"EDGR"),\
     # (u"NASDAQ", u"EDGW"),\
     # (u"NASDAQ", u"EDMC"),\
     # (u"NASDAQ", u"EDUC"),\
     # (u"NASDAQ", u"EVAC"),\
     # (u"NASDAQ", u"EFUT"),\
     # (u"NASDAQ", u"EGAN"),\
     # (u"NASDAQ", u"EHTH"),\
     # (u"NASDAQ", u"BAGL"),\
     # (u"NASDAQ", u"EMITF"),\
     # (u"NASDAQ", u"ESLT"),\
     # (u"NASDAQ", u"ESYS"),\
     # (u"NASDAQ", u"ELRC"),\
     # (u"NASDAQ", u"ESIO"),\
     # (u"NASDAQ", u"EA"),\
     # (u"NASDAQ", u"EFII"),\
     # (u"NASDAQ", u"ELSE"),\
     # (u"NASDAQ", u"RDEN"),\
     # (u"NASDAQ", u"ESBK"),\
     # (u"NASDAQ", u"LONG"),\
     # (u"NASDAQ", u"ELTK"),\
     # (u"NASDAQ", u"EMCI"),\
     # (u"NASDAQ", u"EMCF"),\
     # (u"NASDAQ", u"EMKR"),\
     # (u"NASDAQ", u"EMMS"),\
     # (u"NASDAQ", u"EMMSP"),\
     # (u"NASDAQ", u"NYNY"),\
     # (u"NASDAQ", u"EBTX"),\
     # (u"NASDAQ", u"ECPG"),\
     # (u"NASDAQ", u"WIRE"),\
     # (u"NASDAQ", u"ENDP"),\
     # (u"NASDAQ", u"ECYT"),\
     # (u"NASDAQ", u"ELGX"),\
     # (u"NASDAQ", u"ERII"),\
     # (u"NASDAQ", u"EXXI"),\
     # (u"NASDAQ", u"ENOC"),\
     # (u"NASDAQ", u"ENG"),\
     # (u"NASDAQ", u"ENPH"),\
     # (u"NASDAQ", u"ESGR"),\
     # (u"NASDAQ", u"ENTG"),\
     # (u"NASDAQ", u"ETRM"),\
     # (u"NASDAQ", u"EBTC"),\
     # (u"NASDAQ", u"EFSC"),\
     # (u"NASDAQ", u"ENMD"),\
     # (u"NASDAQ", u"ENTR"),\
     # (u"NASDAQ", u"ENVI"),\
     # (u"NASDAQ", u"ENZN"),\
     # (u"NASDAQ", u"EONC"),\
     # (u"NASDAQ", u"EPIQ"),\
     # (u"NASDAQ", u"PLUS"),\
     # (u"NASDAQ", u"EPHC"),\
     # (u"NASDAQ", u"EPOC"),\
     # (u"NASDAQ", u"EQIX"),\
     # (u"NASDAQ", u"ERT"),\
     # (u"NASDAQ", u"EAC"),\
     # (u"NASDAQ", u"ERIC"),\
     # (u"NASDAQ", u"ERIE"),\
     # (u"NASDAQ", u"ESBF"),\
     # (u"NASDAQ", u"ESCA"),\
     # (u"NASDAQ", u"ESMC"),\
     # (u"NASDAQ", u"ESSA"),\
     # (u"NASDAQ", u"ESSX"),\
     # (u"NASDAQ", u"CLWT"),\
     # (u"NASDAQ", u"EEFT"),\
     # (u"NASDAQ", u"ESEA"),\
     # (u"NASDAQ", u"EVEP"),\
     # (u"NASDAQ", u"EVOL"),\
     # (u"NASDAQ", u"EXAS"),\
     # (u"NASDAQ", u"EXAC"),\
     # (u"NASDAQ", u"EXAR"),\
     # (u"NASDAQ", u"EDS"),\
     # (u"NASDAQ", u"EXEL"),\
     # (u"NASDAQ", u"EXFO"),\
     # (u"NASDAQ", u"XIDE"),\
     # (u"NASDAQ", u"EXLS"),\
     # (u"NASDAQ", u"EXPE"),\
     # (u"NASDAQ", u"EXPD"),\
     # (u"NASDAQ", u"EXPO"),\
     # (u"NASDAQ", u"ESRX"),\
     # (u"NASDAQ", u"EXLP"),\
     # (u"NASDAQ", u"EXTR"),\
     # (u"NASDAQ", u"EZCH"),\
     # (u"NASDAQ", u"EZPW"),\
     # (u"NASDAQ", u"FFIV"),\
     # (u"NASDAQ", u"FB"),\
     # (u"NASDAQ", u"FRP"),\
     # (u"NASDAQ", u"FALC"),\
     # (u"NASDAQ", u"DAVE"),\
     # (u"NASDAQ", u"FARM"),\
     # (u"NASDAQ", u"FFKT"),\
     # (u"NASDAQ", u"FMNB"),\
     # (u"NASDAQ", u"FARO"),\
     # (u"NASDAQ", u"FAST"),\
     # (u"NASDAQ", u"FBSS"),\
     # (u"NASDAQ", u"FBRC"),\
     # (u"NASDAQ", u"FDML"),\
     # (u"NASDAQ", u"FFCO"),\
     # (u"NASDAQ", u"FEIC"),\
     # (u"NASDAQ", u"FHCO"),\
     # (u"NASDAQ", u"FFDF"),\
     # (u"NASDAQ", u"FSBI"),\
     # (u"NASDAQ", u"ONEQ"),\
     # (u"NASDAQ", u"LION"),\
     # (u"NASDAQ", u"FDUS"),\
     # (u"NASDAQ", u"FRGI"),\
     # (u"NASDAQ", u"FSC"),\
     # (u"NASDAQ", u"FITB"),\
     # (u"NASDAQ", u"FITBP"),\
     # (u"NASDAQ", u"FNGN"),\
     # (u"NASDAQ", u"FISI"),\
     # (u"NASDAQ", u"FNSR"),\
     # (u"NASDAQ", u"FABK"),\
     # (u"NASDAQ", u"FBNC"),\
     # (u"NASDAQ", u"FNLC"),\
     # (u"NASDAQ", u"BUSE"),\
     # (u"NASDAQ", u"FBIZ"),\
     # (u"NASDAQ", u"FCAL"),\
     # (u"NASDAQ", u"FCVA"),\
     # (u"NASDAQ", u"FCAP"),\
     # (u"NASDAQ", u"FCFS"),\
     # (u"NASDAQ", u"FCZA"),\
     # (u"NASDAQ", u"FCNCA"),\
     # (u"NASDAQ", u"FCLF"),\
     # (u"NASDAQ", u"FCBC"),\
     # (u"NASDAQ", u"FCCO"),\
     # (u"NASDAQ", u"FBNK"),\
     # (u"NASDAQ", u"FDEF"),\
     # (u"NASDAQ", u"FFBH"),\
     # (u"NASDAQ", u"FFNM"),\
     # (u"NASDAQ", u"FFBC"),\
     # (u"NASDAQ", u"FFBCW"),\
     # (u"NASDAQ", u"FFIN"),\
     # (u"NASDAQ", u"THFF"),\
     # (u"NASDAQ", u"FFCH"),\
     # (u"NASDAQ", u"FFNW"),\
     # (u"NASDAQ", u"FFKY"),\
     # (u"NASDAQ", u"FIBK"),\
     # (u"NASDAQ", u"FMFC"),\
     # (u"NASDAQ", u"FRME"),\
     # (u"NASDAQ", u"FMBI"),\
     # (u"NASDAQ", u"FNFG"),\
     # (u"NASDAQ", u"BANC"),\
     # (u"NASDAQ", u"BANCL"),\
     # (u"NASDAQ", u"FRCCO"),\
     # (u"NASDAQ", u"FSFG"),\
     # (u"NASDAQ", u"FSGI"),\
     # (u"NASDAQ", u"FSLR"),\
     # (u"NASDAQ", u"FSBK"),\
     # (u"NASDAQ", u"BICK"),\
     # (u"NASDAQ", u"CU"),\
     # (u"NASDAQ", u"PLTM"),\
     # (u"NASDAQ", u"CARZ"),\
     # (u"NASDAQ", u"SKYY"),\
     # (u"NASDAQ", u"QABA"),\
     # (u"NASDAQ", u"FONE"),\
     # (u"NASDAQ", u"GRID"),\
     # (u"NASDAQ", u"QCLN"),\
     # (u"NASDAQ", u"QQEW"),\
     # (u"NASDAQ", u"QQXT"),\
     # (u"NASDAQ", u"QTEC"),\
     # (u"NASDAQ", u"FUNC"),\
     # (u"NASDAQ", u"FBMI"),\
     # (u"NASDAQ", u"FCFC"),\
     # (u"NASDAQ", u"SVVC"),\
     # (u"NASDAQ", u"FMER"),\
     # (u"NASDAQ", u"FSRV"),\
     # (u"NASDAQ", u"FISV"),\
     # (u"NASDAQ", u"FSCI"),\
     # (u"NASDAQ", u"FLML"),\
     # (u"NASDAQ", u"FLXS"),\
     # (u"NASDAQ", u"FLEX"),\
     # (u"NASDAQ", u"FLIR"),\
     # (u"NASDAQ", u"FLOW"),\
     # (u"NASDAQ", u"FLDM"),\
     # (u"NASDAQ", u"FFIC"),\
     # (u"NASDAQ", u"FNBN"),\
     # (u"NASDAQ", u"FMCN"),\
     # (u"NASDAQ", u"FONR"),\
     # (u"NASDAQ", u"VIFL"),\
     # (u"NASDAQ", u"FES"),\
     # (u"NASDAQ", u"FORM"),\
     # (u"NASDAQ", u"FORTY"),\
     # (u"NASDAQ", u"FORR"),\
     # (u"NASDAQ", u"FTNT"),\
     # (u"NASDAQ", u"FWRD"),\
     # (u"NASDAQ", u"FORD"),\
     # (u"NASDAQ", u"FOSL"),\
     # (u"NASDAQ", u"FWLT"),\
     # (u"NASDAQ", u"FXCB"),\
     # (u"NASDAQ", u"FRAN"),\
     # (u"NASDAQ", u"FELE"),\
     # (u"NASDAQ", u"FRNK"),\
     # (u"NASDAQ", u"FRED"),\
     # (u"NASDAQ", u"FREE"),\
     # (u"NASDAQ", u"RAIL"),\
     # (u"NASDAQ", u"FEIM"),\
     # (u"NASDAQ", u"FFN"),\
     # (u"NASDAQ", u"FTR"),\
     # (u"NASDAQ", u"FFEX"),\
     # (u"NASDAQ", u"FSII"),\
     # (u"NASDAQ", u"FSYS"),\
     # (u"NASDAQ", u"FTEK"),\
     # (u"NASDAQ", u"FCEL"),\
     # (u"NASDAQ", u"FULL"),\
     # (u"NASDAQ", u"FULT"),\
     # (u"NASDAQ", u"FURX"),\
     # (u"NASDAQ", u"FSIN"),\
     # (u"NASDAQ", u"FFHL"),\
     # (u"NASDAQ", u"FXEN"),\
     # (u"NASDAQ", u"GKSR"),\
     # (u"NASDAQ", u"WILC"),\
     # (u"NASDAQ", u"GAIA"),\
     # (u"NASDAQ", u"GALT"),\
     # (u"NASDAQ", u"GALTU"),\
     # (u"NASDAQ", u"GALTW"),\
     # (u"NASDAQ", u"GALE"),\
     # (u"NASDAQ", u"GPIC"),\
     # (u"NASDAQ", u"GRMN"),\
     # (u"NASDAQ", u"GKNT"),\
     # (u"NASDAQ", u"GENC"),\
     # (u"NASDAQ", u"GNCMA"),\
     # (u"NASDAQ", u"GFN"),\
     # (u"NASDAQ", u"GFNCL"),\
     # (u"NASDAQ", u"GFNCZ"),\
     # (u"NASDAQ", u"GENE"),\
     # (u"NASDAQ", u"GNMK"),\
     # (u"NASDAQ", u"GHDX"),\
     # (u"NASDAQ", u"GPRO"),\
     # (u"NASDAQ", u"GNTX"),\
     # (u"NASDAQ", u"GENT"),\
     # (u"NASDAQ", u"GTIV"),\
     # (u"NASDAQ", u"GNVC"),\
     # (u"NASDAQ", u"GEOY"),\
     # (u"NASDAQ", u"GMET"),\
     # (u"NASDAQ", u"GMETP"),\
     # (u"NASDAQ", u"GEOI"),\
     # (u"NASDAQ", u"GABC"),\
     # (u"NASDAQ", u"GERN"),\
     # (u"NASDAQ", u"GEVO"),\
     # (u"NASDAQ", u"ROCK"),\
     # (u"NASDAQ", u"GIGM"),\
     # (u"NASDAQ", u"GIGA"),\
     # (u"NASDAQ", u"GIII"),\
     # (u"NASDAQ", u"GILT"),\
     # (u"NASDAQ", u"GILD"),\
     # (u"NASDAQ", u"GIVN"),\
     # (u"NASDAQ", u"GBCI"),\
     # (u"NASDAQ", u"GLAD"),\
     # (u"NASDAQ", u"GLADP"),\
     # (u"NASDAQ", u"GOOD"),\
     # (u"NASDAQ", u"GOODN"),\
     # (u"NASDAQ", u"GOODO"),\
     # (u"NASDAQ", u"GOODP"),\
     # (u"NASDAQ", u"GAIN"),\
     # (u"NASDAQ", u"GAINP"),\
     # (u"NASDAQ", u"GLCH"),\
     # (u"NASDAQ", u"GLBZ"),\
     # (u"NASDAQ", u"GLGL"),\
     # (u"NASDAQ", u"EAGL"),\
     # (u"NASDAQ", u"EAGLU"),\
     # (u"NASDAQ", u"EAGLW"),\
     # (u"NASDAQ", u"GBLI"),\
     # (u"NASDAQ", u"GLPW"),\
     # (u"NASDAQ", u"GSOL"),\
     # (u"NASDAQ", u"QQQM"),\
     # (u"NASDAQ", u"QQQV"),\
     # (u"NASDAQ", u"SOCL"),\
     # (u"NASDAQ", u"QQQC"),\
     # (u"NASDAQ", u"GSAT"),\
     # (u"NASDAQ", u"GAI"),\
     # (u"NASDAQ", u"GSM"),\
     # (u"NASDAQ", u"GCOM"),\
     # (u"NASDAQ", u"GLBS"),\
     # (u"NASDAQ", u"GLUU"),\
     # (u"NASDAQ", u"GLNG"),\
     # (u"NASDAQ", u"GMLP"),\
     # (u"NASDAQ", u"GLDC"),\
     # (u"NASDAQ", u"GOLF"),\
     # (u"NASDAQ", u"GBDC"),\
     # (u"NASDAQ", u"GTIM"),\
     # (u"NASDAQ", u"GOOG"),\
     # (u"NASDAQ", u"GMAN"),\
     # (u"NASDAQ", u"LOPE"),\
     # (u"NASDAQ", u"GCFB"),\
     # (u"NASDAQ", u"GRVY"),\
     # (u"NASDAQ", u"GRMH"),\
     # (u"NASDAQ", u"GLDD"),\
     # (u"NASDAQ", u"GSBC"),\
     # (u"NASDAQ", u"GRNB"),\
     # (u"NASDAQ", u"GMCR"),\
     # (u"NASDAQ", u"GPRE"),\
     # (u"NASDAQ", u"GCBC"),\
     # (u"NASDAQ", u"GLRE"),\
     # (u"NASDAQ", u"GRIF"),\
     # (u"NASDAQ", u"GRFS"),\
     # (u"NASDAQ", u"GRPN"),\
     # (u"NASDAQ", u"OMAB"),\
     # (u"NASDAQ", u"GGAL"),\
     # (u"NASDAQ", u"GSIG"),\
     # (u"NASDAQ", u"GSIT"),\
     # (u"NASDAQ", u"GSVC"),\
     # (u"NASDAQ", u"GTAT"),\
     # (u"NASDAQ", u"GTSI"),\
     # (u"NASDAQ", u"GTXI"),\
     # (u"NASDAQ", u"GPRC"),\
     # (u"NASDAQ", u"GBNK"),\
     # (u"NASDAQ", u"GFED"),\
     # (u"NASDAQ", u"GUID"),\
     # (u"NASDAQ", u"GIFI"),\
     # (u"NASDAQ", u"GURE"),\
     # (u"NASDAQ", u"GPOR"),\
     # (u"NASDAQ", u"GYRO"),\
     # (u"NASDAQ", u"HEES"),\
     # (u"NASDAQ", u"HNRG"),\
     # (u"NASDAQ", u"HALL"),\
     # (u"NASDAQ", u"HALO"),\
     # (u"NASDAQ", u"HBNK"),\
     # (u"NASDAQ", u"HMPR"),\
     # (u"NASDAQ", u"HBHC"),\
     # (u"NASDAQ", u"HNH"),\
     # (u"NASDAQ", u"HAFC"),\
     # (u"NASDAQ", u"HNSN"),\
     # (u"NASDAQ", u"HSOL"),\
     # (u"NASDAQ", u"HDNG"),\
     # (u"NASDAQ", u"HARL"),\
     # (u"NASDAQ", u"HLIT"),\
     # (u"NASDAQ", u"TINY"),\
     # (u"NASDAQ", u"HPOL"),\
     # (u"NASDAQ", u"HBIO"),\
     # (u"NASDAQ", u"HAS"),\
     # (u"NASDAQ", u"HAST"),\
     # (u"NASDAQ", u"HAUP"),\
     # (u"NASDAQ", u"HA"),\
     # (u"NASDAQ", u"HCOM"),\
     # (u"NASDAQ", u"HWKN"),\
     # (u"NASDAQ", u"HWBK"),\
     # (u"NASDAQ", u"HAYN"),\
     # (u"NASDAQ", u"HCSG"),\
     # (u"NASDAQ", u"HSTM"),\
     # (u"NASDAQ", u"HWAY"),\
     # (u"NASDAQ", u"HTLD"),\
     # (u"NASDAQ", u"HTLF"),\
     # (u"NASDAQ", u"HTWR"),\
     # (u"NASDAQ", u"HLYS"),\
     # (u"NASDAQ", u"HSII"),\
     # (u"NASDAQ", u"HELE"),\
     # (u"NASDAQ", u"HMNY"),\
     # (u"NASDAQ", u"HSIC"),\
     # (u"NASDAQ", u"HERO"),\
     # (u"NASDAQ", u"HTBK"),\
     # (u"NASDAQ", u"HFWA"),\
     # (u"NASDAQ", u"HBOS"),\
     # (u"NASDAQ", u"HEOP"),\
     # (u"NASDAQ", u"HCCI"),\
     # (u"NASDAQ", u"MLHR"),\
     # (u"NASDAQ", u"HSKA"),\
     # (u"NASDAQ", u"HFFC"),\
     # (u"NASDAQ", u"HIBB"),\
     # (u"NASDAQ", u"HTCO"),\
     # (u"NASDAQ", u"HKAC"),\
     # (u"NASDAQ", u"HKACU"),\
     # (u"NASDAQ", u"HKACW"),\
     # (u"NASDAQ", u"HIHO"),\
     # (u"NASDAQ", u"HIMX"),\
     # (u"NASDAQ", u"HIFS"),\
     # (u"NASDAQ", u"HSFT"),\
     # (u"NASDAQ", u"HITK"),\
     # (u"NASDAQ", u"HITT"),\
     # (u"NASDAQ", u"HMNF"),\
     # (u"NASDAQ", u"HMSY"),\
     # (u"NASDAQ", u"HOKU"),\
     # (u"NASDAQ", u"HOLI"),\
     # (u"NASDAQ", u"HOLL"),\
     # (u"NASDAQ", u"HOLX"),\
     # (u"NASDAQ", u"HBCP"),\
     # (u"NASDAQ", u"HOMB"),\
     # (u"NASDAQ", u"HOME"),\
     # (u"NASDAQ", u"HFBL"),\
     # (u"NASDAQ", u"HMIN"),\
     # (u"NASDAQ", u"HLSS"),\
     # (u"NASDAQ", u"AWAY"),\
     # (u"NASDAQ", u"HCII"),\
     # (u"NASDAQ", u"HCIIP"),\
     # (u"NASDAQ", u"HCIIW"),\
     # (u"NASDAQ", u"HMST"),\
     # (u"NASDAQ", u"HPJ"),\
     # (u"NASDAQ", u"HOFT"),\
     # (u"NASDAQ", u"HFBC"),\
     # (u"NASDAQ", u"HBNC"),\
     # (u"NASDAQ", u"HZNP"),\
     # (u"NASDAQ", u"HRZN"),\
     # (u"NASDAQ", u"ZINC"),\
     # (u"NASDAQ", u"HOTT"),\
     # (u"NASDAQ", u"HWCC"),\
     # (u"NASDAQ", u"HOVNP"),\
     # (u"NASDAQ", u"HSNI"),\
     # (u"NASDAQ", u"HUBG"),\
     # (u"NASDAQ", u"HCBK"),\
     # (u"NASDAQ", u"HSON"),\
     # (u"NASDAQ", u"HDSN"),\
     # (u"NASDAQ", u"HGSI"),\
     # (u"NASDAQ", u"HBAN"),\
     # (u"NASDAQ", u"HBANP"),\
     # (u"NASDAQ", u"HPCCP"),\
     # (u"NASDAQ", u"HURC"),\
     # (u"NASDAQ", u"HURN"),\
     # (u"NASDAQ", u"HTCH"),\
     # (u"NASDAQ", u"HYGS"),\
     # (u"NASDAQ", u"IDSY"),\
     # (u"NASDAQ", u"IACI"),\
     # (u"NASDAQ", u"IBKC"),\
     # (u"NASDAQ", u"ICAD"),\
     # (u"NASDAQ", u"IEP"),\
     # (u"NASDAQ", u"ICFI"),\
     # (u"NASDAQ", u"ICGE"),\
     # (u"NASDAQ", u"ICLR"),\
     # (u"NASDAQ", u"ICON"),\
     # (u"NASDAQ", u"ICUI"),\
     # (u"NASDAQ", u"IDIX"),\
     # (u"NASDAQ", u"INVE"),\
     # (u"NASDAQ", u"IDRA"),\
     # (u"NASDAQ", u"IDXX"),\
     # (u"NASDAQ", u"IROQ"),\
     # (u"NASDAQ", u"IGTE"),\
     # (u"NASDAQ", u"IRG"),\
     # (u"NASDAQ", u"IGOI"),\
     # (u"NASDAQ", u"IIVI"),\
     # (u"NASDAQ", u"IKAN"),\
     # (u"NASDAQ", u"IKNX"),\
     # (u"NASDAQ", u"ILMN"),\
     # (u"NASDAQ", u"ISNS"),\
     # (u"NASDAQ", u"IMMR"),\
     # (u"NASDAQ", u"ICCC"),\
     # (u"NASDAQ", u"IMGN"),\
     # (u"NASDAQ", u"IMMU"),\
     # (u"NASDAQ", u"IPXL"),\
     # (u"NASDAQ", u"IPSU"),\
     # (u"NASDAQ", u"IMRS"),\
     # (u"NASDAQ", u"SAAS"),\
     # (u"NASDAQ", u"INCY"),\
     # (u"NASDAQ", u"INDB"),\
     # (u"NASDAQ", u"IBCP"),\
     # (u"NASDAQ", u"IBCPO"),\
     # (u"NASDAQ", u"INCB"),\
     # (u"NASDAQ", u"IDSA"),\
     # (u"NASDAQ", u"INFN"),\
     # (u"NASDAQ", u"INFI"),\
     # (u"NASDAQ", u"IPCC"),\
     # (u"NASDAQ", u"INFA"),\
     # (u"NASDAQ", u"III"),\
     # (u"NASDAQ", u"IFON"),\
     # (u"NASDAQ", u"INFY"),\
     # (u"NASDAQ", u"IMKTA"),\
     # (u"NASDAQ", u"INWK"),\
     # (u"NASDAQ", u"INOD"),\
     # (u"NASDAQ", u"IPHS"),\
     # (u"NASDAQ", u"IOSP"),\
     # (u"NASDAQ", u"INOC"),\
     # (u"NASDAQ", u"ISSC"),\
     # (u"NASDAQ", u"NSIT"),\
     # (u"NASDAQ", u"ISIG"),\
     # (u"NASDAQ", u"INSM"),\
     # (u"NASDAQ", u"IIIN"),\
     # (u"NASDAQ", u"PODD"),\
     # (u"NASDAQ", u"IART"),\
     # (u"NASDAQ", u"INMD"),\
     # (u"NASDAQ", u"IDTI"),\
     # (u"NASDAQ", u"IESC"),\
     # (u"NASDAQ", u"ISSI"),\
     # (u"NASDAQ", u"INTC"),\
     # (u"NASDAQ", u"IPCI"),\
     # (u"NASDAQ", u"IPAR"),\
     # (u"NASDAQ", u"IBKR"),\
     # (u"NASDAQ", u"ININ"),\
     # (u"NASDAQ", u"IDCC"),\
     # (u"NASDAQ", u"IFSIA"),\
     # (u"NASDAQ", u"IMI"),\
     # (u"NASDAQ", u"ITMN"),\
     # (u"NASDAQ", u"INAP"),\
     # (u"NASDAQ", u"IBOC"),\
     # (u"NASDAQ", u"ISCA"),\
     # (u"NASDAQ", u"IGLD"),\
     # (u"NASDAQ", u"IIJI"),\
     # (u"NASDAQ", u"PTNT"),\
     # (u"NASDAQ", u"INPH"),\
     # (u"NASDAQ", u"INTX"),\
     # (u"NASDAQ", u"ISIL"),\
     # (u"NASDAQ", u"IILG"),\
     # (u"NASDAQ", u"IBCA"),\
     # (u"NASDAQ", u"INTT"),\
     # (u"NASDAQ", u"IVAC"),\
     # (u"NASDAQ", u"INTL"),\
     # (u"NASDAQ", u"IIN"),\
     # (u"NASDAQ", u"INTU"),\
     # (u"NASDAQ", u"ISRG"),\
     # (u"NASDAQ", u"SNAK"),\
     # (u"NASDAQ", u"ISBC"),\
     # (u"NASDAQ", u"IRET"),\
     # (u"NASDAQ", u"IRETP"),\
     # (u"NASDAQ", u"ITIC"),\
     # (u"NASDAQ", u"IPAS"),\
     # (u"NASDAQ", u"IPCM"),\
     # (u"NASDAQ", u"IPGP"),\
     # (u"NASDAQ", u"IRIX"),\
     # (u"NASDAQ", u"IRDM"),\
     # (u"NASDAQ", u"IRDMU"),\
     # (u"NASDAQ", u"IRDMW"),\
     # (u"NASDAQ", u"IRDMZ"),\
     # (u"NASDAQ", u"IRIS"),\
     # (u"NASDAQ", u"IRBT"),\
     # (u"NASDAQ", u"IRWD"),\
     # (u"NASDAQ", u"FCHI"),\
     # (u"NASDAQ", u"IFSM"),\
     # (u"NASDAQ", u"IFAS"),\
     # (u"NASDAQ", u"IFEU"),\
     # (u"NASDAQ", u"IFGL"),\
     # (u"NASDAQ", u"IFNA"),\
     # (u"NASDAQ", u"SOXX"),\
     # (u"NASDAQ", u"AXFN"),\
     # (u"NASDAQ", u"ACWX"),\
     # (u"NASDAQ", u"ACWI"),\
     # (u"NASDAQ", u"AAXJ"),\
     # (u"NASDAQ", u"EMFN"),\
     # (u"NASDAQ", u"EMMT"),\
     # (u"NASDAQ", u"EUFN"),\
     # (u"NASDAQ", u"FEFN"),\
     # (u"NASDAQ", u"IBB"),\
     # (u"NASDAQ", u"EMIF"),\
     # (u"NASDAQ", u"ICLN"),\
     # (u"NASDAQ", u"NUCL"),\
     # (u"NASDAQ", u"WOOD"),\
     # (u"NASDAQ", u"INDY"),\
     # (u"NASDAQ", u"ISHG"),\
     # (u"NASDAQ", u"IGOV"),\
     # (u"NASDAQ", u"GNMA"),\
     # (u"NASDAQ", u"AXJS"),\
     # (u"NASDAQ", u"AAIT"),\
     # (u"NASDAQ", u"EEML"),\
     # (u"NASDAQ", u"EEMA"),\
     # (u"NASDAQ", u"EMDI"),\
     # (u"NASDAQ", u"EEME"),\
     # (u"NASDAQ", u"EMEY"),\
     # (u"NASDAQ", u"EGRW"),\
     # (u"NASDAQ", u"EVAL"),\
     # (u"NASDAQ", u"ISIS"),\
     # (u"NASDAQ", u"ISLE"),\
     # (u"NASDAQ", u"ISRL"),\
     # (u"NASDAQ", u"ITRI"),\
     # (u"NASDAQ", u"ITRN"),\
     # (u"NASDAQ", u"IVAN"),\
     # (u"NASDAQ", u"XXIA"),\
     # (u"NASDAQ", u"IXYS"),\
     # (u"NASDAQ", u"JJSF"),\
     # (u"NASDAQ", u"JAX"),\
     # (u"NASDAQ", u"MAYS"),\
     # (u"NASDAQ", u"JBHT"),\
     # (u"NASDAQ", u"JCOM"),\
     # (u"NASDAQ", u"JASO"),\
     # (u"NASDAQ", u"JCDA"),\
     # (u"NASDAQ", u"JKHY"),\
     # (u"NASDAQ", u"JACK"),\
     # (u"NASDAQ", u"JXSB"),\
     # (u"NASDAQ", u"JAXB"),\
     # (u"NASDAQ", u"JAKK"),\
     # (u"NASDAQ", u"JMBA"),\
     # (u"NASDAQ", u"JRCC"),\
     # (u"NASDAQ", u"JAZZ"),\
     # (u"NASDAQ", u"JDAS"),\
     # (u"NASDAQ", u"JDSU"),\
     # (u"NASDAQ", u"JFBI"),\
     # (u"NASDAQ", u"JBLU"),\
     # (u"NASDAQ", u"JCTCF"),\
     # (u"NASDAQ", u"DATE"),\
     # (u"NASDAQ", u"JST"),\
     # (u"NASDAQ", u"JIVE"),\
     # (u"NASDAQ", u"JOEZ"),\
     # (u"NASDAQ", u"JBSS"),\
     # (u"NASDAQ", u"JOUT"),\
     # (u"NASDAQ", u"JSDA"),\
     # (u"NASDAQ", u"JOSB"),\
     # (u"NASDAQ", u"KALU"),\
     # (u"NASDAQ", u"KFFG"),\
     # (u"NASDAQ", u"KNDI"),\
     # (u"NASDAQ", u"KCLI"),\
     # (u"NASDAQ", u"KRNY"),\
     # (u"NASDAQ", u"KIPO"),\
     # (u"NASDAQ", u"KELYA"),\
     # (u"NASDAQ", u"KELYB"),\
     # (u"NASDAQ", u"KNSY"),\
     # (u"NASDAQ", u"KFFB"),\
     # (u"NASDAQ", u"KERX"),\
     # (u"NASDAQ", u"KEQU"),\
     # (u"NASDAQ", u"KTEC"),\
     # (u"NASDAQ", u"KTCC"),\
     # (u"NASDAQ", u"KEYN"),\
     # (u"NASDAQ", u"KFRC"),\
     # (u"NASDAQ", u"KBALB"),\
     # (u"NASDAQ", u"KGJI"),\
     # (u"NASDAQ", u"KINS"),\
     # (u"NASDAQ", u"KONE"),\
     # (u"NASDAQ", u"KIOR"),\
     # (u"NASDAQ", u"KIPS"),\
     # (u"NASDAQ", u"KIRK"),\
     # (u"NASDAQ", u"KITD"),\
     # (u"NASDAQ", u"KLAC"),\
     # (u"NASDAQ", u"KMGB"),\
     # (u"NASDAQ", u"VLCCF"),\
     # (u"NASDAQ", u"KNOL"),\
     # (u"NASDAQ", u"KCAP"),\
     # (u"NASDAQ", u"KONA"),\
     # (u"NASDAQ", u"KONG"),\
     # (u"NASDAQ", u"KOPN"),\
     # (u"NASDAQ", u"KOSS"),\
     # (u"NASDAQ", u"KTOS"),\
     # (u"NASDAQ", u"KSW"),\
     # (u"NASDAQ", u"KSWS"),\
     # (u"NASDAQ", u"KUTV"),\
     # (u"NASDAQ", u"KLIC"),\
     # (u"NASDAQ", u"KVHI"),\
     (u"NASDAQ", u"LLEN"),\
     (u"NASDAQ", u"FSTR"),\
     (u"NASDAQ", u"BOOT"),\
     (u"NASDAQ", u"LSBK"),\
     (u"NASDAQ", u"LBAI"),\
     (u"NASDAQ", u"LKFN"),\
     (u"NASDAQ", u"LAKE"),\
     (u"NASDAQ", u"LACO"),\
     (u"NASDAQ", u"LRCX"),\
     (u"NASDAQ", u"LAMR"),\
     (u"NASDAQ", u"LANC"),\
     (u"NASDAQ", u"LNDC"),\
     (u"NASDAQ", u"LARK"),\
     (u"NASDAQ", u"LSTR"),\
     (u"NASDAQ", u"LTRX"),\
     (u"NASDAQ", u"LPSB"),\
     (u"NASDAQ", u"LSCC"),\
     (u"NASDAQ", u"LAWS"),\
     (u"NASDAQ", u"LAYN"),\
     (u"NASDAQ", u"LCAV"),\
     (u"NASDAQ", u"LCNB"),\
     (u"NASDAQ", u"GAGA"),\
     (u"NASDAQ", u"LBIX"),\
     (u"NASDAQ", u"LEAP"),\
     (u"NASDAQ", u"LTRE"),\
     (u"NASDAQ", u"LCRY"),\
     (u"NASDAQ", u"LGCY"),\
     (u"NASDAQ", u"LMAT"),\
     (u"NASDAQ", u"LXRX"),\
     (u"NASDAQ", u"LHCG"),\
     (u"NASDAQ", u"LBTYA"),\
     (u"NASDAQ", u"LBTYB"),\
     (u"NASDAQ", u"LBTYK"),\
     (u"NASDAQ", u"LINTA"),\
     (u"NASDAQ", u"LINTB"),\
     (u"NASDAQ", u"LMCA"),\
     (u"NASDAQ", u"LMCB"),\
     (u"NASDAQ", u"LPHI"),\
     (u"NASDAQ", u"LIFE"),\
     (u"NASDAQ", u"LPNT"),\
     (u"NASDAQ", u"LCUT"),\
     (u"NASDAQ", u"LWAY"),\
     (u"NASDAQ", u"LGND"),\
     (u"NASDAQ", u"LTBR"),\
     (u"NASDAQ", u"LPTH"),\
     (u"NASDAQ", u"LIWA"),\
     (u"NASDAQ", u"LIME"),\
     (u"NASDAQ", u"LLNW"),\
     (u"NASDAQ", u"LMNR"),\
     (u"NASDAQ", u"LLGX"),\
     (u"NASDAQ", u"LNCR"),\
     (u"NASDAQ", u"LINC"),\
     (u"NASDAQ", u"LECO"),\
     (u"NASDAQ", u"LLTC"),\
     (u"NASDAQ", u"LTON"),\
     (u"NASDAQ", u"LINE"),\
     (u"NASDAQ", u"LIOX"),\
     (u"NASDAQ", u"LQDT"),\
     (u"NASDAQ", u"LFUS"),\
     (u"NASDAQ", u"LIVE"),\
     (u"NASDAQ", u"LPSN"),\
     (u"NASDAQ", u"LZEN"),\
     (u"NASDAQ", u"JADE"),\
     (u"NASDAQ", u"LKQ"),\
     (u"NASDAQ", u"LMIA"),\
     (u"NASDAQ", u"LMLP"),\
     (u"NASDAQ", u"LNBB"),\
     (u"NASDAQ", u"LOCM"),\
     (u"NASDAQ", u"LNET"),\
     (u"NASDAQ", u"LOGI"),\
     (u"NASDAQ", u"LOGM"),\
     (u"NASDAQ", u"LOJN"),\
     (u"NASDAQ", u"LOOK"),\
     (u"NASDAQ", u"LORL"),\
     (u"NASDAQ", u"LABC"),\
     (u"NASDAQ", u"LAEC"),\
     (u"NASDAQ", u"LPLA"),\
     (u"NASDAQ", u"LRAD"),\
     (u"NASDAQ", u"LSBI"),\
     (u"NASDAQ", u"LYTS"),\
     (u"NASDAQ", u"LTXC"),\
     (u"NASDAQ", u"LUFK"),\
     (u"NASDAQ", u"LULU"),\
     (u"NASDAQ", u"LMNX"),\
     (u"NASDAQ", u"LMOS"),\
     (u"NASDAQ", u"LUNA"),\
     (u"NASDAQ", u"MBTF"),\
     (u"NASDAQ", u"MTSI"),\
     (u"NASDAQ", u"MCBC"),\
     (u"NASDAQ", u"MFNC"),\
     (u"NASDAQ", u"MAGS"),\
     (u"NASDAQ", u"MGLN"),\
     (u"NASDAQ", u"MPET"),\
     (u"NASDAQ", u"MGIC"),\
     (u"NASDAQ", u"CALL"),\
     (u"NASDAQ", u"MAG"),\
     (u"NASDAQ", u"MGYR"),\
     (u"NASDAQ", u"MHLD"),\
     (u"NASDAQ", u"MSFG"),\
     (u"NASDAQ", u"COOL"),\
     (u"NASDAQ", u"MMUS"),\
     (u"NASDAQ", u"MMYT"),\
     (u"NASDAQ", u"MKTAY"),\
     (u"NASDAQ", u"MAKO"),\
     (u"NASDAQ", u"MLVF"),\
     (u"NASDAQ", u"MANH"),\
     (u"NASDAQ", u"LOAN"),\
     (u"NASDAQ", u"MNTX"),\
     (u"NASDAQ", u"MTEX"),\
     (u"NASDAQ", u"MNKD"),\
     (u"NASDAQ", u"MANT"),\
     (u"NASDAQ", u"MAPP"),\
     (u"NASDAQ", u"MCHX"),\
     (u"NASDAQ", u"MARPS"),\
     (u"NASDAQ", u"LEDR"),\
     (u"NASDAQ", u"MKTX"),\
     (u"NASDAQ", u"MRLN"),\
     (u"NASDAQ", u"MSHL"),\
     (u"NASDAQ", u"MRTN"),\
     (u"NASDAQ", u"MMLP"),\
     (u"NASDAQ", u"MRVL"),\
     (u"NASDAQ", u"MASI"),\
     (u"NASDAQ", u"MASC"),\
     (u"NASDAQ", u"MTRX"),\
     (u"NASDAQ", u"MAT"),\
     (u"NASDAQ", u"MATR"),\
     (u"NASDAQ", u"MATW"),\
     (u"NASDAQ", u"MFRM"),\
     (u"NASDAQ", u"MTSN"),\
     (u"NASDAQ", u"MXIM"),\
     (u"NASDAQ", u"MXWL"),\
     (u"NASDAQ", u"MAXY"),\
     (u"NASDAQ", u"MFLR"),\
     (u"NASDAQ", u"MBFI"),\
     (u"NASDAQ", u"MCGC"),\
     (u"NASDAQ", u"MGRC"),\
     (u"NASDAQ", u"MDCA"),\
     (u"NASDAQ", u"MEAD"),\
     (u"NASDAQ", u"MEAS"),\
     (u"NASDAQ", u"MCOX"),\
     (u"NASDAQ", u"TAXI"),\
     (u"NASDAQ", u"MDAS"),\
     (u"NASDAQ", u"MDTH"),\
     (u"NASDAQ", u"MDCI"),\
     (u"NASDAQ", u"MNOV"),\
     (u"NASDAQ", u"MDSO"),\
     (u"NASDAQ", u"MDVN"),\
     (u"NASDAQ", u"MEDW"),\
     (u"NASDAQ", u"MTOX"),\
     (u"NASDAQ", u"MELA"),\
     (u"NASDAQ", u"MPEL"),\
     (u"NASDAQ", u"MLNX"),\
     (u"NASDAQ", u"MEMP"),\
     (u"NASDAQ", u"MEMS"),\
     (u"NASDAQ", u"MENT"),\
     (u"NASDAQ", u"MTSL"),\
     (u"NASDAQ", u"MELI"),\
     (u"NASDAQ", u"MBWM"),\
     (u"NASDAQ", u"MERC"),\
     (u"NASDAQ", u"MBVT"),\
     (u"NASDAQ", u"MRCY"),\
     (u"NASDAQ", u"MRGE"),\
     (u"NASDAQ", u"VIVO"),\
     (u"NASDAQ", u"EBSB"),\
     (u"NASDAQ", u"MMSI"),\
     (u"NASDAQ", u"MACK"),\
     (u"NASDAQ", u"MERU"),\
     (u"NASDAQ", u"MSLI"),\
     (u"NASDAQ", u"MLAB"),\
     (u"NASDAQ", u"CASH"),\
     (u"NASDAQ", u"MBLX"),\
     (u"NASDAQ", u"MEOH"),\
     (u"NASDAQ", u"METR"),\
     (u"NASDAQ", u"MCBI"),\
     (u"NASDAQ", u"MFRI"),\
     (u"NASDAQ", u"MGEE"),\
     (u"NASDAQ", u"MGPI"),\
     (u"NASDAQ", u"MDH"),\
     (u"NASDAQ", u"MCRL"),\
     (u"NASDAQ", u"MCHP"),\
     (u"NASDAQ", u"MFI"),\
     (u"NASDAQ", u"MU"),\
     (u"NASDAQ", u"NOIZ"),\
     (u"NASDAQ", u"MCRS"),\
     (u"NASDAQ", u"MSCC"),\
     (u"NASDAQ", u"MSFT"),\
     (u"NASDAQ", u"MSTR"),\
     (u"NASDAQ", u"MVIS"),\
     (u"NASDAQ", u"MVISW"),\
     (u"NASDAQ", u"MPB"),\
     (u"NASDAQ", u"MCEP"),\
     (u"NASDAQ", u"MBRG"),\
     (u"NASDAQ", u"MSEX"),\
     (u"NASDAQ", u"MOFG"),\
     (u"NASDAQ", u"SMCG"),\
     (u"NASDAQ", u"MNDO"),\
     (u"NASDAQ", u"MSPD"),\
     (u"NASDAQ", u"MIPS"),\
     (u"NASDAQ", u"MSON"),\
     (u"NASDAQ", u"MSW"),\
     (u"NASDAQ", u"MIND"),\
     (u"NASDAQ", u"MITK"),\
     (u"NASDAQ", u"MITL"),\
     (u"NASDAQ", u"MKSI"),\
     (u"NASDAQ", u"MODL"),\
     (u"NASDAQ", u"MINI"),\
     (u"NASDAQ", u"MOCO"),\
     (u"NASDAQ", u"MPAC"),\
     (u"NASDAQ", u"MLNK"),\
     (u"NASDAQ", u"MOLX"),\
     (u"NASDAQ", u"MOLXA"),\
     (u"NASDAQ", u"MNTA"),\
     (u"NASDAQ", u"MCRI"),\
     (u"NASDAQ", u"MCBF"),\
     (u"NASDAQ", u"MNRK"),\
     (u"NASDAQ", u"MNRKP"),\
     (u"NASDAQ", u"MPWR"),\
     (u"NASDAQ", u"TYPE"),\
     (u"NASDAQ", u"MNRO"),\
     (u"NASDAQ", u"MNST"),\
     (u"NASDAQ", u"MHGC"),\
     (u"NASDAQ", u"MORN"),\
     (u"NASDAQ", u"MOSY"),\
     (u"NASDAQ", u"MPAA"),\
     (u"NASDAQ", u"MOTR"),\
     (u"NASDAQ", u"MOVE"),\
     (u"NASDAQ", u"MSBF"),\
     (u"NASDAQ", u"MNTG"),\
     (u"NASDAQ", u"MTSC"),\
     (u"NASDAQ", u"MBND"),\
     (u"NASDAQ", u"LABL"),\
     (u"NASDAQ", u"MFLX"),\
     (u"NASDAQ", u"MGAM"),\
     (u"NASDAQ", u"MFSF"),\
     (u"NASDAQ", u"MWIV"),\
     (u"NASDAQ", u"MYL"),\
     (u"NASDAQ", u"MYRG"),\
     (u"NASDAQ", u"MYRX"),\
     (u"NASDAQ", u"MYGN"),\
     (u"NASDAQ", u"NABI"),\
     (u"NASDAQ", u"NANO"),\
     (u"NASDAQ", u"NSPH"),\
     (u"NASDAQ", u"NSSC"),\
     (u"NASDAQ", u"NASB"),\
     (u"NASDAQ", u"QQQX"),\
     (u"NASDAQ", u"NAFC"),\
     (u"NASDAQ", u"NATH"),\
     (u"NASDAQ", u"NAUH"),\
     (u"NASDAQ", u"NKSH"),\
     (u"NASDAQ", u"FIZZ"),\
     (u"NASDAQ", u"NCMI"),\
     (u"NASDAQ", u"NATI"),\
     (u"NASDAQ", u"NATL"),\
     (u"NASDAQ", u"NPBC"),\
     (u"NASDAQ", u"NPBCO"),\
     (u"NASDAQ", u"NRCI"),\
     (u"NASDAQ", u"NSEC"),\
     (u"NASDAQ", u"NTSC"),\
     (u"NASDAQ", u"NWLI"),\
     (u"NASDAQ", u"NAII"),\
     (u"NASDAQ", u"NATR"),\
     (u"NASDAQ", u"BABY"),\
     (u"NASDAQ", u"NVSL"),\
     (u"NASDAQ", u"NMAR"),\
     (u"NASDAQ", u"NMARW"),\
     (u"NASDAQ", u"NAVR"),\
     (u"NASDAQ", u"NBTF"),\
     (u"NASDAQ", u"NBTB"),\
     (u"NASDAQ", u"NCIT"),\
     (u"NASDAQ", u"NKTR"),\
     (u"NASDAQ", u"NEOG"),\
     (u"NASDAQ", u"NEON"),\
     (u"NASDAQ", u"NEPT"),\
     (u"NASDAQ", u"UEPS"),\
     (u"NASDAQ", u"NETC"),\
     (u"NASDAQ", u"NTAP"),\
     (u"NASDAQ", u"NTES"),\
     (u"NASDAQ", u"NFLX"),\
     (u"NASDAQ", u"NTGR"),\
     (u"NASDAQ", u"NLST"),\
     (u"NASDAQ", u"NTCT"),\
     (u"NASDAQ", u"NTWK"),\
     (u"NASDAQ", u"NTSP"),\
     (u"NASDAQ", u"NEI"),\
     (u"NASDAQ", u"NWK"),\
     (u"NASDAQ", u"NBIX"),\
     (u"NASDAQ", u"NGSX"),\
     (u"NASDAQ", u"NURO"),\
     (u"NASDAQ", u"IQNT"),\
     (u"NASDAQ", u"NCBC"),\
     (u"NASDAQ", u"NEBS"),\
     (u"NASDAQ", u"NOOF"),\
     (u"NASDAQ", u"NHTB"),\
     (u"NASDAQ", u"HAVNP"),\
     (u"NASDAQ", u"NYMT"),\
     (u"NASDAQ", u"NBBC"),\
     (u"NASDAQ", u"NEWL"),\
     (u"NASDAQ", u"NLNK"),\
     (u"NASDAQ", u"NFSB"),\
     (u"NASDAQ", u"NEWP"),\
     (u"NASDAQ", u"NWS"),\
     (u"NASDAQ", u"NWSA"),\
     (u"NASDAQ", u"NEWS"),\
     (u"NASDAQ", u"NEWT"),\
     (u"NASDAQ", u"NXST"),\
     (u"NASDAQ", u"NEXS"),\
     (u"NASDAQ", u"NFEC"),\
     (u"NASDAQ", u"NGPC"),\
     (u"NASDAQ", u"EGOV"),\
     (u"NASDAQ", u"NICE"),\
     (u"NASDAQ", u"NICK"),\
     (u"NASDAQ", u"NIHD"),\
     (u"NASDAQ", u"NINE"),\
     (u"NASDAQ", u"NNBR"),\
     (u"NASDAQ", u"NOBH"),\
     (u"NASDAQ", u"NDSN"),\
     (u"NASDAQ", u"NSYS"),\
     (u"NASDAQ", u"NTK"),\
     (u"NASDAQ", u"FFFD"),\
     (u"NASDAQ", u"NOVB"),\
     (u"NASDAQ", u"NBN"),\
     (u"NASDAQ", u"NECB"),\
     (u"NASDAQ", u"NTIC"),\
     (u"NASDAQ", u"NTRS"),\
     (u"NASDAQ", u"NFBK"),\
     (u"NASDAQ", u"NRIM"),\
     (u"NASDAQ", u"NWBI"),\
     (u"NASDAQ", u"NWPX"),\
     (u"NASDAQ", u"NWFL"),\
     (u"NASDAQ", u"NVMI"),\
     (u"NASDAQ", u"NVDQ"),\
     (u"NASDAQ", u"NVTL"),\
     (u"NASDAQ", u"NVAX"),\
     (u"NASDAQ", u"NVGN"),\
     (u"NASDAQ", u"NPSP"),\
     (u"NASDAQ", u"NTLS"),\
     (u"NASDAQ", u"NUAN"),\
     (u"NASDAQ", u"NMRX"),\
     (u"NASDAQ", u"PATH"),\
     (u"NASDAQ", u"NUTR"),\
     (u"NASDAQ", u"NTRI"),\
     (u"NASDAQ", u"NUVA"),\
     (u"NASDAQ", u"NVEC"),\
     (u"NASDAQ", u"NVDA"),\
     (u"NASDAQ", u"NXPI"),\
     (u"NASDAQ", u"NXTM"),\
     (u"NASDAQ", u"NYMX"),\
     (u"NASDAQ", u"OIIM"),\
     (u"NASDAQ", u"BKOR"),\
     (u"NASDAQ", u"OVLY"),\
     (u"NASDAQ", u"OBAF"),\
     (u"NASDAQ", u"OMPI"),\
     (u"NASDAQ", u"OBCI"),\
     (u"NASDAQ", u"OPTT"),\
     (u"NASDAQ", u"ORIG"),\
     (u"NASDAQ", u"OSHC"),\
     (u"NASDAQ", u"OCFC"),\
     (u"NASDAQ", u"OCLR"),\
     (u"NASDAQ", u"OFED"),\
     (u"NASDAQ", u"OCLS"),\
     (u"NASDAQ", u"OCZ"),\
     (u"NASDAQ", u"OMEX"),\
     (u"NASDAQ", u"OPAY"),\
     (u"NASDAQ", u"OLCB"),\
     (u"NASDAQ", u"OVBC"),\
     (u"NASDAQ", u"ODFL"),\
     (u"NASDAQ", u"OLBK"),\
     (u"NASDAQ", u"OPOF"),\
     (u"NASDAQ", u"OSBC"),\
     (u"NASDAQ", u"OSBCP"),\
     (u"NASDAQ", u"ZEUS"),\
     (u"NASDAQ", u"OFLX"),\
     (u"NASDAQ", u"OMER"),\
     (u"NASDAQ", u"OABC"),\
     (u"NASDAQ", u"OMCL"),\
     (u"NASDAQ", u"OVTI"),\
     (u"NASDAQ", u"ASGN"),\
     (u"NASDAQ", u"ONNN"),\
     (u"NASDAQ", u"OTIV"),\
     (u"NASDAQ", u"OGXI"),\
     (u"NASDAQ", u"ONCY"),\
     (u"NASDAQ", u"ONTY"),\
     (u"NASDAQ", u"ONFC"),\
     (u"NASDAQ", u"ORCC"),\
     (u"NASDAQ", u"ONSM"),\
     (u"NASDAQ", u"ONVI"),\
     (u"NASDAQ", u"ONXX"),\
     (u"NASDAQ", u"OTEX"),\
     (u"NASDAQ", u"OPEN"),\
     (u"NASDAQ", u"OPXA"),\
     (u"NASDAQ", u"OPXAW"),\
     (u"NASDAQ", u"OPLK"),\
     (u"NASDAQ", u"OPXT"),\
     (u"NASDAQ", u"OBAS"),\
     (u"NASDAQ", u"OCC"),\
     (u"NASDAQ", u"OPTR"),\
     (u"NASDAQ", u"OPHC"),\
     (u"NASDAQ", u"ORCL"),\
     (u"NASDAQ", u"OSUR"),\
     (u"NASDAQ", u"ORBC"),\
     (u"NASDAQ", u"ORBT"),\
     (u"NASDAQ", u"ORBK"),\
     (u"NASDAQ", u"OSH"),\
     (u"NASDAQ", u"ORCT"),\
     (u"NASDAQ", u"ORLY"),\
     (u"NASDAQ", u"OREX"),\
     (u"NASDAQ", u"SEED"),\
     (u"NASDAQ", u"ORIT"),\
     (u"NASDAQ", u"ORRF"),\
     (u"NASDAQ", u"OFIX"),\
     (u"NASDAQ", u"OSIS"),\
     (u"NASDAQ", u"OSIR"),\
     (u"NASDAQ", u"OSN"),\
     (u"NASDAQ", u"OTT"),\
     (u"NASDAQ", u"OTTR"),\
     (u"NASDAQ", u"OUTD"),\
     (u"NASDAQ", u"OVRL"),\
     (u"NASDAQ", u"OSTK"),\
     (u"NASDAQ", u"OXLC"),\
     (u"NASDAQ", u"OXGN"),\
     (u"NASDAQ", u"OXBT"),\
     (u"NASDAQ", u"OYOG"),\
     (u"NASDAQ", u"PFIN"),\
     (u"NASDAQ", u"PTSI"),\
     (u"NASDAQ", u"PFCB"),\
     (u"NASDAQ", u"PCAR"),\
     (u"NASDAQ", u"PACR"),\
     (u"NASDAQ", u"PACB"),\
     (u"NASDAQ", u"PCBC"),\
     (u"NASDAQ", u"PCBK"),\
     (u"NASDAQ", u"PEIX"),\
     (u"NASDAQ", u"PMBC"),\
     (u"NASDAQ", u"PPBI"),\
     (u"NASDAQ", u"PSUN"),\
     (u"NASDAQ", u"PCRX"),\
     (u"NASDAQ", u"PACW"),\
     (u"NASDAQ", u"PTIE"),\
     (u"NASDAQ", u"PLMT"),\
     (u"NASDAQ", u"PMTI"),\
     (u"NASDAQ", u"PAAS"),\
     (u"NASDAQ", u"PNRA"),\
     (u"NASDAQ", u"PSOF"),\
     (u"NASDAQ", u"PZZA"),\
     (u"NASDAQ", u"PAMT"),\
     (u"NASDAQ", u"PMTC"),\
     (u"NASDAQ", u"PRXL"),\
     (u"NASDAQ", u"PSTB"),\
     (u"NASDAQ", u"PKBK"),\
     (u"NASDAQ", u"PRKR"),\
     (u"NASDAQ", u"PKOH"),\
     (u"NASDAQ", u"PTNR"),\
     (u"NASDAQ", u"PBHC"),\
     (u"NASDAQ", u"PATK"),\
     (u"NASDAQ", u"PNBK"),\
     (u"NASDAQ", u"PATR"),\
     (u"NASDAQ", u"PDCO"),\
     (u"NASDAQ", u"PTEN"),\
     (u"NASDAQ", u"PLCC"),\
     (u"NASDAQ", u"PAYX"),\
     (u"NASDAQ", u"PCCC"),\
     (u"NASDAQ", u"MALL"),\
     (u"NASDAQ", u"PCTI"),\
     (u"NASDAQ", u"PDFS"),\
     (u"NASDAQ", u"PDII"),\
     (u"NASDAQ", u"PDLI"),\
     (u"NASDAQ", u"PGC"),\
     (u"NASDAQ", u"PRLS"),\
     (u"NASDAQ", u"PEET"),\
     (u"NASDAQ", u"PEGA"),\
     (u"NASDAQ", u"PCO"),\
     (u"NASDAQ", u"PENX"),\
     (u"NASDAQ", u"PENN"),\
     (u"NASDAQ", u"PFLT"),\
     (u"NASDAQ", u"PNNT"),\
     (u"NASDAQ", u"PWOD"),\
     (u"NASDAQ", u"PNSN"),\
     (u"NASDAQ", u"PEBO"),\
     (u"NASDAQ", u"PEBK"),\
     (u"NASDAQ", u"PEDH"),\
     (u"NASDAQ", u"PEOP"),\
     (u"NASDAQ", u"PFBX"),\
     (u"NASDAQ", u"PBCT"),\
     (u"NASDAQ", u"PRCP"),\
     (u"NASDAQ", u"PPHM"),\
     (u"NASDAQ", u"PWRD"),\
     (u"NASDAQ", u"PRFT"),\
     (u"NASDAQ", u"PTIX"),\
     (u"NASDAQ", u"PERF"),\
     (u"NASDAQ", u"PSEM"),\
     (u"NASDAQ", u"PERI"),\
     (u"NASDAQ", u"PESI"),\
     (u"NASDAQ", u"PRGO"),\
     (u"NASDAQ", u"PERY"),\
     (u"NASDAQ", u"PVSW"),\
     (u"NASDAQ", u"PETS"),\
     (u"NASDAQ", u"PETD"),\
     (u"NASDAQ", u"PETM"),\
     (u"NASDAQ", u"PFSW"),\
     (u"NASDAQ", u"PGTI"),\
     (u"NASDAQ", u"PCYC"),\
     (u"NASDAQ", u"ANTP"),\
     (u"NASDAQ", u"PHII"),\
     (u"NASDAQ", u"PHIIK"),\
     (u"NASDAQ", u"PHMD"),\
     (u"NASDAQ", u"PLAB"),\
     (u"NASDAQ", u"FACE"),\
     (u"NASDAQ", u"PICO"),\
     (u"NASDAQ", u"PNFP"),\
     (u"NASDAQ", u"PXLW"),\
     (u"NASDAQ", u"PZZI"),\
     (u"NASDAQ", u"PLNR"),\
     (u"NASDAQ", u"PLXS"),\
     (u"NASDAQ", u"PLUG"),\
     (u"NASDAQ", u"PLBC"),\
     (u"NASDAQ", u"PSTI"),\
     (u"NASDAQ", u"PLXT"),\
     (u"NASDAQ", u"PMCS"),\
     (u"NASDAQ", u"PMFG"),\
     (u"NASDAQ", u"PBSK"),\
     (u"NASDAQ", u"PTSX"),\
     (u"NASDAQ", u"PNTR"),\
     (u"NASDAQ", u"PCOM"),\
     (u"NASDAQ", u"PTEK"),\
     (u"NASDAQ", u"PLCM"),\
     (u"NASDAQ", u"POOL"),\
     (u"NASDAQ", u"POPE"),\
     (u"NASDAQ", u"BPOP"),\
     (u"NASDAQ", u"BPOPM"),\
     (u"NASDAQ", u"BPOPN"),\
     (u"NASDAQ", u"PBIB"),\
     (u"NASDAQ", u"PRAA"),\
     (u"NASDAQ", u"PSTR"),\
     (u"NASDAQ", u"PCH"),\
     (u"NASDAQ", u"POWL"),\
     (u"NASDAQ", u"POWI"),\
     (u"NASDAQ", u"PWER"),\
     (u"NASDAQ", u"POWR"),\
     (u"NASDAQ", u"PSCC"),\
     (u"NASDAQ", u"PSCD"),\
     (u"NASDAQ", u"PSCE"),\
     (u"NASDAQ", u"PSCF"),\
     (u"NASDAQ", u"PSCH"),\
     (u"NASDAQ", u"PSCI"),\
     (u"NASDAQ", u"PSCM"),\
     (u"NASDAQ", u"PSCT"),\
     (u"NASDAQ", u"PSCU"),\
     (u"NASDAQ", u"PRFZ"),\
     (u"NASDAQ", u"PAGG"),\
     (u"NASDAQ", u"PKOL"),\
     (u"NASDAQ", u"PSAU"),\
     (u"NASDAQ", u"PSTL"),\
     (u"NASDAQ", u"PWND"),\
     (u"NASDAQ", u"PMNA"),\
     (u"NASDAQ", u"PNQI"),\
     (u"NASDAQ", u"QQQ"),\
     (u"NASDAQ", u"PWAV"),\
     (u"NASDAQ", u"POZN"),\
     (u"NASDAQ", u"PRAN"),\
     (u"NASDAQ", u"PFBC"),\
     (u"NASDAQ", u"PLPC"),\
     (u"NASDAQ", u"PRXI"),\
     (u"NASDAQ", u"PFBI"),\
     (u"NASDAQ", u"PRWT"),\
     (u"NASDAQ", u"PLFE"),\
     (u"NASDAQ", u"PRST"),\
     (u"NASDAQ", u"PRGX"),\
     (u"NASDAQ", u"PCLN"),\
     (u"NASDAQ", u"PSMT"),\
     (u"NASDAQ", u"PBMD"),\
     (u"NASDAQ", u"PACQ"),\
     (u"NASDAQ", u"PACQU"),\
     (u"NASDAQ", u"PACQW"),\
     (u"NASDAQ", u"PNRG"),\
     (u"NASDAQ", u"PRMW"),\
     (u"NASDAQ", u"PRIM"),\
     (u"NASDAQ", u"PNBC"),\
     (u"NASDAQ", u"PVTB"),\
     (u"NASDAQ", u"PVTBP"),\
     (u"NASDAQ", u"PKT"),\
     (u"NASDAQ", u"PDEX"),\
     (u"NASDAQ", u"PGNX"),\
     (u"NASDAQ", u"PRGS"),\
     (u"NASDAQ", u"PFPT"),\
     (u"NASDAQ", u"PRPH"),\
     (u"NASDAQ", u"BIB"),\
     (u"NASDAQ", u"BIS"),\
     (u"NASDAQ", u"TQQQ"),\
     (u"NASDAQ", u"SQQQ"),\
     (u"NASDAQ", u"PSEC"),\
     (u"NASDAQ", u"PWX"),\
     (u"NASDAQ", u"PROV"),\
     (u"NASDAQ", u"PBIP"),\
     (u"NASDAQ", u"PSBH"),\
     (u"NASDAQ", u"PSDV"),\
     (u"NASDAQ", u"PSSI"),\
     (u"NASDAQ", u"PMD"),\
     (u"NASDAQ", u"PULB"),\
     (u"NASDAQ", u"PURE"),\
     (u"NASDAQ", u"PCYO"),\
     (u"NASDAQ", u"PVFC"),\
     (u"NASDAQ", u"QADA"),\
     (u"NASDAQ", u"QADB"),\
     (u"NASDAQ", u"QCCO"),\
     (u"NASDAQ", u"QCRH"),\
     (u"NASDAQ", u"QGEN"),\
     (u"NASDAQ", u"QKLS"),\
     (u"NASDAQ", u"QLIK"),\
     (u"NASDAQ", u"QLGC"),\
     (u"NASDAQ", u"QLTI"),\
     (u"NASDAQ", u"QCOM"),\
     (u"NASDAQ", u"QLTY"),\
     (u"NASDAQ", u"QSII"),\
     (u"NASDAQ", u"QBAK"),\
     (u"NASDAQ", u"QTWW"),\
     (u"NASDAQ", u"QSFT"),\
     (u"NASDAQ", u"QCOR"),\
     (u"NASDAQ", u"QUIK"),\
     (u"NASDAQ", u"QDEL"),\
     (u"NASDAQ", u"QNST"),\
     (u"NASDAQ", u"DFZ"),\
     (u"NASDAQ", u"RRD"),\
     (u"NASDAQ", u"RADA"),\
     (u"NASDAQ", u"RDCM"),\
     (u"NASDAQ", u"ROIA"),\
     (u"NASDAQ", u"ROIAK"),\
     (u"NASDAQ", u"RSYS"),\
     (u"NASDAQ", u"RDNT"),\
     (u"NASDAQ", u"RDWR"),\
     (u"NASDAQ", u"RMKR"),\
     (u"NASDAQ", u"RMBS"),\
     (u"NASDAQ", u"RMTR"),\
     (u"NASDAQ", u"RAND"),\
     (u"NASDAQ", u"RLOG"),\
     (u"NASDAQ", u"GOLD"),\
     (u"NASDAQ", u"RPTP"),\
     (u"NASDAQ", u"RAVN"),\
     (u"NASDAQ", u"ROLL"),\
     (u"NASDAQ", u"RCMT"),\
     (u"NASDAQ", u"RDA"),\
     (u"NASDAQ", u"RLOC"),\
     (u"NASDAQ", u"RDI"),\
     (u"NASDAQ", u"RDIB"),\
     (u"NASDAQ", u"RSOL"),\
     (u"NASDAQ", u"RNWK"),\
     (u"NASDAQ", u"RP"),\
     (u"NASDAQ", u"RCON"),\
     (u"NASDAQ", u"RECV"),\
     (u"NASDAQ", u"RRGB"),\
     (u"NASDAQ", u"REDF"),\
     (u"NASDAQ", u"REED"),\
     (u"NASDAQ", u"REGN"),\
     (u"NASDAQ", u"REIS"),\
     (u"NASDAQ", u"RELV"),\
     (u"NASDAQ", u"MARK"),\
     (u"NASDAQ", u"RNST"),\
     (u"NASDAQ", u"REGI"),\
     (u"NASDAQ", u"RCII"),\
     (u"NASDAQ", u"RENT"),\
     (u"NASDAQ", u"RGEN"),\
     (u"NASDAQ", u"RPRX"),\
     (u"NASDAQ", u"RPRXW"),\
     (u"NASDAQ", u"RPRXZ"),\
     (u"NASDAQ", u"RJET"),\
     (u"NASDAQ", u"RBCAA"),\
     (u"NASDAQ", u"FRBK"),\
     (u"NASDAQ", u"REFR"),\
     (u"NASDAQ", u"RIMM"),\
     (u"NASDAQ", u"REXI"),\
     (u"NASDAQ", u"RECN"),\
     (u"NASDAQ", u"RGDX"),\
     (u"NASDAQ", u"MKTG"),\
     (u"NASDAQ", u"ROIC"),\
     (u"NASDAQ", u"ROICU"),\
     (u"NASDAQ", u"ROICW"),\
     (u"NASDAQ", u"RTLX"),\
     (u"NASDAQ", u"REXX"),\
     (u"NASDAQ", u"RFIL"),\
     (u"NASDAQ", u"RFMD"),\
     (u"NASDAQ", u"RFMI"),\
     (u"NASDAQ", u"RGCO"),\
     (u"NASDAQ", u"RELL"),\
     (u"NASDAQ", u"RICK"),\
     (u"NASDAQ", u"RIGL"),\
     (u"NASDAQ", u"RNET"),\
     (u"NASDAQ", u"RIMG"),\
     (u"NASDAQ", u"RITT"),\
     (u"NASDAQ", u"RIVR"),\
     (u"NASDAQ", u"RVBD"),\
     (u"NASDAQ", u"RVSB"),\
     (u"NASDAQ", u"ROCM"),\
     (u"NASDAQ", u"RCKB"),\
     (u"NASDAQ", u"RMTI"),\
     (u"NASDAQ", u"RCKY"),\
     (u"NASDAQ", u"RMCF"),\
     (u"NASDAQ", u"RSTI"),\
     (u"NASDAQ", u"ROIQ"),\
     (u"NASDAQ", u"ROIQU"),\
     (u"NASDAQ", u"ROIQW"),\
     (u"NASDAQ", u"ROMA"),\
     (u"NASDAQ", u"ROSG"),\
     (u"NASDAQ", u"ROSE"),\
     (u"NASDAQ", u"ROST"),\
     (u"NASDAQ", u"ROVI"),\
     (u"NASDAQ", u"RBPAA"),\
     (u"NASDAQ", u"RGLD"),\
     (u"NASDAQ", u"ROYL"),\
     (u"NASDAQ", u"FUND"),\
     (u"NASDAQ", u"RPXC"),\
     (u"NASDAQ", u"RRST"),\
     (u"NASDAQ", u"RTIX"),\
     (u"NASDAQ", u"RBCN"),\
     (u"NASDAQ", u"RTEC"),\
     (u"NASDAQ", u"RUE"),\
     (u"NASDAQ", u"RBNF"),\
     (u"NASDAQ", u"RUSHA"),\
     (u"NASDAQ", u"RUSHB"),\
     (u"NASDAQ", u"SGGG"),\
     (u"NASDAQ", u"SCOG"),\
     (u"NASDAQ", u"SCTR"),\
     (u"NASDAQ", u"SCLP"),\
     (u"NASDAQ", u"RUTH"),\
     (u"NASDAQ", u"RYAAY"),\
     (u"NASDAQ", u"STBA"),\
     (u"NASDAQ", u"SANW"),\
     (u"NASDAQ", u"SANWW"),\
     (u"NASDAQ", u"SANWZ"),\
     (u"NASDAQ", u"SYBT"),\
     (u"NASDAQ", u"SYBTP"),\
     (u"NASDAQ", u"SABA"),\
     (u"NASDAQ", u"SBRA"),\
     (u"NASDAQ", u"SAFT"),\
     (u"NASDAQ", u"SGNT"),\
     (u"NASDAQ", u"SAIA"),\
     (u"NASDAQ", u"SALM"),\
     (u"NASDAQ", u"SLXP"),\
     (u"NASDAQ", u"SAFM"),\
     (u"NASDAQ", u"SNDK"),\
     (u"NASDAQ", u"SASR"),\
     (u"NASDAQ", u"SGMO"),\
     (u"NASDAQ", u"SANM"),\
     (u"NASDAQ", u"GCVRZ"),\
     (u"NASDAQ", u"SNTS"),\
     (u"NASDAQ", u"SPNS"),\
     (u"NASDAQ", u"SAPE"),\
     (u"NASDAQ", u"SATC"),\
     (u"NASDAQ", u"SVNT"),\
     (u"NASDAQ", u"SBAC"),\
     (u"NASDAQ", u"SCSC"),\
     (u"NASDAQ", u"SCBT"),\
     (u"NASDAQ", u"SCGQ"),\
     (u"NASDAQ", u"SMIT"),\
     (u"NASDAQ", u"SCHN"),\
     (u"NASDAQ", u"SCHL"),\
     (u"NASDAQ", u"SCHS"),\
     (u"NASDAQ", u"SCLN"),\
     (u"NASDAQ", u"SGMS"),\
     (u"NASDAQ", u"SCIL"),\
     (u"NASDAQ", u"SQI"),\
     (u"NASDAQ", u"SEAC"),\
     (u"NASDAQ", u"SBCF"),\
     (u"NASDAQ", u"STX"),\
     (u"NASDAQ", u"SHIP"),\
     (u"NASDAQ", u"SHLD"),\
     (u"NASDAQ", u"SGEN"),\
     (u"NASDAQ", u"SNFCA"),\
     (u"NASDAQ", u"SEIC"),\
     (u"NASDAQ", u"SCSS"),\
     (u"NASDAQ", u"SLTC"),\
     (u"NASDAQ", u"SIGI"),\
     (u"NASDAQ", u"LEDS"),\
     (u"NASDAQ", u"SMTC"),\
     (u"NASDAQ", u"SENEA"),\
     (u"NASDAQ", u"SENEB"),\
     (u"NASDAQ", u"SNMX"),\
     (u"NASDAQ", u"SQNM"),\
     (u"NASDAQ", u"SREV"),\
     (u"NASDAQ", u"SEV"),\
     (u"NASDAQ", u"SAPX"),\
     (u"NASDAQ", u"SVBI"),\
     (u"NASDAQ", u"SGOC"),\
     (u"NASDAQ", u"GAME"),\
     (u"NASDAQ", u"SMED"),\
     (u"NASDAQ", u"SHEN"),\
     (u"NASDAQ", u"VALV"),\
     (u"NASDAQ", u"SHLO"),\
     (u"NASDAQ", u"BEST"),\
     (u"NASDAQ", u"SHPGY"),\
     (u"NASDAQ", u"SCVL"),\
     (u"NASDAQ", u"SHBI"),\
     (u"NASDAQ", u"SHOR"),\
     (u"NASDAQ", u"SHFL"),\
     (u"NASDAQ", u"SFLY"),\
     (u"NASDAQ", u"SIFI"),\
     (u"NASDAQ", u"SIEB"),\
     (u"NASDAQ", u"BSRR"),\
     (u"NASDAQ", u"SWIR"),\
     (u"NASDAQ", u"SIFY"),\
     (u"NASDAQ", u"SIGA"),\
     (u"NASDAQ", u"SIGM"),\
     (u"NASDAQ", u"SIAL"),\
     (u"NASDAQ", u"SGMA"),\
     (u"NASDAQ", u"SBNY"),\
     (u"NASDAQ", u"SBNYW"),\
     (u"NASDAQ", u"SLGN"),\
     (u"NASDAQ", u"SILC"),\
     (u"NASDAQ", u"SGI"),\
     (u"NASDAQ", u"SIMG"),\
     (u"NASDAQ", u"SLAB"),\
     (u"NASDAQ", u"SIMO"),\
     (u"NASDAQ", u"SPIL"),\
     (u"NASDAQ", u"SSRI"),\
     (u"NASDAQ", u"SFNC"),\
     (u"NASDAQ", u"SLP"),\
     (u"NASDAQ", u"SINA"),\
     (u"NASDAQ", u"SBGI"),\
     (u"NASDAQ", u"SCEI"),\
     (u"NASDAQ", u"SCOK"),\
     (u"NASDAQ", u"SINO"),\
     (u"NASDAQ", u"SVA"),\
     (u"NASDAQ", u"SIRI"),\
     (u"NASDAQ", u"SIRO"),\
     (u"NASDAQ", u"SKUL"),\
     (u"NASDAQ", u"MOBI"),\
     (u"NASDAQ", u"SPU"),\
     (u"NASDAQ", u"SKBI"),\
     (u"NASDAQ", u"SKYW"),\
     (u"NASDAQ", u"SWKS"),\
     (u"NASDAQ", u"ISM"),\
     (u"NASDAQ", u"JSM"),\
     (u"NASDAQ", u"OSM"),\
     (u"NASDAQ", u"SLM"),\
     (u"NASDAQ", u"SLMAP"),\
     (u"NASDAQ", u"SLMBP"),\
     (u"NASDAQ", u"SMBL"),\
     (u"NASDAQ", u"SMT"),\
     (u"NASDAQ", u"HEAT"),\
     (u"NASDAQ", u"SPRO"),\
     (u"NASDAQ", u"SWHC"),\
     (u"NASDAQ", u"SMSI"),\
     (u"NASDAQ", u"SMTX"),\
     (u"NASDAQ", u"LNCE"),\
     (u"NASDAQ", u"SCKT"),\
     (u"NASDAQ", u"SODA"),\
     (u"NASDAQ", u"SOHU"),\
     (u"NASDAQ", u"SLRC"),\
     (u"NASDAQ", u"SUNS"),\
     (u"NASDAQ", u"SZYM"),\
     (u"NASDAQ", u"SLTM"),\
     (u"NASDAQ", u"SOMX"),\
     (u"NASDAQ", u"SOMH"),\
     (u"NASDAQ", u"SONC"),\
     (u"NASDAQ", u"SOFO"),\
     (u"NASDAQ", u"SONS"),\
     (u"NASDAQ", u"SORL"),\
     (u"NASDAQ", u"SDBT"),\
     (u"NASDAQ", u"FIRE"),\
     (u"NASDAQ", u"SOCB"),\
     (u"NASDAQ", u"SCMF"),\
     (u"NASDAQ", u"SCMFO"),\
     (u"NASDAQ", u"SFST"),\
     (u"NASDAQ", u"SMBC"),\
     (u"NASDAQ", u"SONA"),\
     (u"NASDAQ", u"SBSI"),\
     (u"NASDAQ", u"OKSB"),\
     (u"NASDAQ", u"OKSBP"),\
     (u"NASDAQ", u"SPBC"),\
     (u"NASDAQ", u"SPAN"),\
     (u"NASDAQ", u"SBSA"),\
     (u"NASDAQ", u"SGRP"),\
     (u"NASDAQ", u"SPAR"),\
     (u"NASDAQ", u"SPTN"),\
     (u"NASDAQ", u"SPPI"),\
     (u"NASDAQ", u"SPEX"),\
     (u"NASDAQ", u"SPIR"),\
     (u"NASDAQ", u"SAVE"),\
     (u"NASDAQ", u"SPLK"),\
     (u"NASDAQ", u"SPCHA"),\
     (u"NASDAQ", u"SPCHB"),\
     (u"NASDAQ", u"SPRD"),\
     (u"NASDAQ", u"SPSC"),\
     (u"NASDAQ", u"STRC"),\
     (u"NASDAQ", u"SRSL"),\
     (u"NASDAQ", u"SSNC"),\
     (u"NASDAQ", u"STAA"),\
     (u"NASDAQ", u"STMP"),\
     (u"NASDAQ", u"STND"),\
     (u"NASDAQ", u"SMSC"),\
     (u"NASDAQ", u"STAN"),\
     (u"NASDAQ", u"STLY"),\
     (u"NASDAQ", u"SPLS"),\
     (u"NASDAQ", u"SBLK"),\
     (u"NASDAQ", u"CIGX"),\
     (u"NASDAQ", u"SBUX"),\
     (u"NASDAQ", u"STFC"),\
     (u"NASDAQ", u"STBZ"),\
     (u"NASDAQ", u"SIBC"),\
     (u"NASDAQ", u"GASS"),\
     (u"NASDAQ", u"STEC"),\
     (u"NASDAQ", u"STLD"),\
     (u"NASDAQ", u"SMRT"),\
     (u"NASDAQ", u"STNR"),\
     (u"NASDAQ", u"STEL"),\
     (u"NASDAQ", u"STEM"),\
     (u"NASDAQ", u"STXS"),\
     (u"NASDAQ", u"SRCL"),\
     (u"NASDAQ", u"STRL"),\
     (u"NASDAQ", u"STSA"),\
     (u"NASDAQ", u"SHOO"),\
     (u"NASDAQ", u"SSFN"),\
     (u"NASDAQ", u"STEI"),\
     (u"NASDAQ", u"SSYS"),\
     (u"NASDAQ", u"SDIX"),\
     (u"NASDAQ", u"STRT"),\
     (u"NASDAQ", u"STRS"),\
     (u"NASDAQ", u"STRA"),\
     (u"NASDAQ", u"STRM"),\
     (u"NASDAQ", u"STB"),\
     (u"NASDAQ", u"SCMP"),\
     (u"NASDAQ", u"SUBK"),\
     (u"NASDAQ", u"SUMR"),\
     (u"NASDAQ", u"SMMF"),\
     (u"NASDAQ", u"SSBI"),\
     (u"NASDAQ", u"SNBC"),\
     (u"NASDAQ", u"SUNH"),\
     (u"NASDAQ", u"SNHY"),\
     (u"NASDAQ", u"SNSS"),\
     (u"NASDAQ", u"STKL"),\
     (u"NASDAQ", u"SPWR"),\
     (u"NASDAQ", u"SSH"),\
     (u"NASDAQ", u"SMCI"),\
     (u"NASDAQ", u"SCON"),\
     (u"NASDAQ", u"SGC"),\
     (u"NASDAQ", u"SPMD"),\
     (u"NASDAQ", u"SUPN"),\
     (u"NASDAQ", u"SPPR"),\
     (u"NASDAQ", u"SPPRO"),\
     (u"NASDAQ", u"SPPRP"),\
     (u"NASDAQ", u"SUPX"),\
     (u"NASDAQ", u"SPRT"),\
     (u"NASDAQ", u"SURW"),\
     (u"NASDAQ", u"SRDX"),\
     (u"NASDAQ", u"SUSQ"),\
     (u"NASDAQ", u"SUSS"),\
     (u"NASDAQ", u"SBBX"),\
     (u"NASDAQ", u"SUTR"),\
     (u"NASDAQ", u"STRN"),\
     (u"NASDAQ", u"SIVB"),\
     (u"NASDAQ", u"SIVBO"),\
     (u"NASDAQ", u"SWSH"),\
     (u"NASDAQ", u"SXCI"),\
     (u"NASDAQ", u"SCMR"),\
     (u"NASDAQ", u"SYKE"),\
     (u"NASDAQ", u"SYMC"),\
     (u"NASDAQ", u"SYMM"),\
     (u"NASDAQ", u"SYNC"),\
     (u"NASDAQ", u"GEVA"),\
     (u"NASDAQ", u"SYNL"),\
     (u"NASDAQ", u"SYNA"),\
     (u"NASDAQ", u"SNCR"),\
     (u"NASDAQ", u"SURG"),\
     (u"NASDAQ", u"SGYP"),\
     (u"NASDAQ", u"SGYPU"),\
     (u"NASDAQ", u"SGYPW"),\
     (u"NASDAQ", u"ELOS"),\
     (u"NASDAQ", u"SNPS"),\
     (u"NASDAQ", u"SNTA"),\
     (u"NASDAQ", u"SYNT"),\
     (u"NASDAQ", u"SYMX"),\
     (u"NASDAQ", u"SYNM"),\
     (u"NASDAQ", u"SYUT"),\
     (u"NASDAQ", u"SYPR"),\
     (u"NASDAQ", u"TROW"),\
     (u"NASDAQ", u"TAIT"),\
     (u"NASDAQ", u"TTWO"),\
     (u"NASDAQ", u"TBAC"),\
     (u"NASDAQ", u"TLF"),\
     (u"NASDAQ", u"TNGO"),\
     (u"NASDAQ", u"TRGT"),\
     (u"NASDAQ", u"TASR"),\
     (u"NASDAQ", u"TATT"),\
     (u"NASDAQ", u"TAYC"),\
     (u"NASDAQ", u"TAYCP"),\
     (u"NASDAQ", u"TAYD"),\
     (u"NASDAQ", u"TCPC"),\
     (u"NASDAQ", u"TSTF"),\
     (u"NASDAQ", u"TEAR"),\
     (u"NASDAQ", u"TECD"),\
     (u"NASDAQ", u"TECH"),\
     (u"NASDAQ", u"TCCO"),\
     (u"NASDAQ", u"TTGT"),\
     (u"NASDAQ", u"TECUA"),\
     (u"NASDAQ", u"TECUB"),\
     (u"NASDAQ", u"TGAL"),\
     (u"NASDAQ", u"TKMR"),\
     (u"NASDAQ", u"TSYS"),\
     (u"NASDAQ", u"TNAV"),\
     (u"NASDAQ", u"TSTC"),\
     (u"NASDAQ", u"TTEC"),\
     (u"NASDAQ", u"TELK"),\
     (u"NASDAQ", u"TLAB"),\
     (u"NASDAQ", u"WRLS"),\
     (u"NASDAQ", u"TNGN"),\
     (u"NASDAQ", u"TBNK"),\
     (u"NASDAQ", u"TESO"),\
     (u"NASDAQ", u"TSLA"),\
     (u"NASDAQ", u"TESS"),\
     (u"NASDAQ", u"TSRA"),\
     (u"NASDAQ", u"TTEK"),\
     (u"NASDAQ", u"TCBI"),\
     (u"NASDAQ", u"TCBIW"),\
     (u"NASDAQ", u"TXN"),\
     (u"NASDAQ", u"TXRH"),\
     (u"NASDAQ", u"THRD"),\
     (u"NASDAQ", u"TFSL"),\
     (u"NASDAQ", u"TGE"),\
     (u"NASDAQ", u"ABCO"),\
     (u"NASDAQ", u"ANDE"),\
     (u"NASDAQ", u"TBBK"),\
     (u"NASDAQ", u"BKYF"),\
     (u"NASDAQ", u"BONT"),\
     (u"NASDAQ", u"CG"),\
     (u"NASDAQ", u"CAKE"),\
     (u"NASDAQ", u"CHEF"),\
     (u"NASDAQ", u"PLCE"),\
     (u"NASDAQ", u"DSGX"),\
     (u"NASDAQ", u"DXYN"),\
     (u"NASDAQ", u"ENSG"),\
     (u"NASDAQ", u"FINL"),\
     (u"NASDAQ", u"FBMS"),\
     (u"NASDAQ", u"FLIC"),\
     (u"NASDAQ", u"TFM"),\
     (u"NASDAQ", u"HCKT"),\
     (u"NASDAQ", u"HAIN"),\
     (u"NASDAQ", u"CUBA"),\
     (u"NASDAQ", u"INTG"),\
     (u"NASDAQ", u"KEYW"),\
     (u"NASDAQ", u"MSG"),\
     (u"NASDAQ", u"TMNG"),\
     (u"NASDAQ", u"MDCO"),\
     (u"NASDAQ", u"MIDD"),\
     (u"NASDAQ", u"NDAQ"),\
     (u"NASDAQ", u"NAVG"),\
     (u"NASDAQ", u"PTRY"),\
     (u"NASDAQ", u"PRSC"),\
     (u"NASDAQ", u"SAVB"),\
     (u"NASDAQ", u"SPNC"),\
     (u"NASDAQ", u"ULTI"),\
     (u"NASDAQ", u"WTSLA"),\
     (u"NASDAQ", u"YORW"),\
     (u"NASDAQ", u"NCTY"),\
     (u"NASDAQ", u"THER"),\
     (u"NASDAQ", u"THRX"),\
     (u"NASDAQ", u"KOOL"),\
     (u"NASDAQ", u"TST"),\
     (u"NASDAQ", u"TCRD"),\
     (u"NASDAQ", u"TPGI"),\
     (u"NASDAQ", u"THOR"),\
     (u"NASDAQ", u"THQI"),\
     (u"NASDAQ", u"THLD"),\
     (u"NASDAQ", u"THTI"),\
     (u"NASDAQ", u"OINK"),\
     (u"NASDAQ", u"TIBB"),\
     (u"NASDAQ", u"TIBX"),\
     (u"NASDAQ", u"TICC"),\
     (u"NASDAQ", u"TIGR"),\
     (u"NASDAQ", u"TIII"),\
     (u"NASDAQ", u"TMWE"),\
     (u"NASDAQ", u"TSBK"),\
     (u"NASDAQ", u"TITN"),\
     (u"NASDAQ", u"TIVO"),\
     (u"NASDAQ", u"TISA"),\
     (u"NASDAQ", u"TOPS"),\
     (u"NASDAQ", u"TORM"),\
     (u"NASDAQ", u"TRMD"),\
     (u"NASDAQ", u"TRNX"),\
     (u"NASDAQ", u"TOFC"),\
     (u"NASDAQ", u"TWGP"),\
     (u"NASDAQ", u"TSEM"),\
     (u"NASDAQ", u"TWER"),\
     (u"NASDAQ", u"CLUB"),\
     (u"NASDAQ", u"TOWN"),\
     (u"NASDAQ", u"TPCG"),\
     (u"NASDAQ", u"TSCO"),\
     (u"NASDAQ", u"TWMC"),\
     (u"NASDAQ", u"TSON"),\
     (u"NASDAQ", u"TACT"),\
     (u"NASDAQ", u"TRNS"),\
     (u"NASDAQ", u"TSPT"),\
     (u"NASDAQ", u"TGA"),\
     (u"NASDAQ", u"TTHI"),\
     (u"NASDAQ", u"TXCC"),\
     (u"NASDAQ", u"TZYM"),\
     (u"NASDAQ", u"TZOO"),\
     (u"NASDAQ", u"TREE"),\
     (u"NASDAQ", u"TCBK"),\
     (u"NASDAQ", u"TRS"),\
     (u"NASDAQ", u"TRMB"),\
     (u"NASDAQ", u"TRIB"),\
     (u"NASDAQ", u"TRIO"),\
     (u"NASDAQ", u"TRIP"),\
     (u"NASDAQ", u"TQNT"),\
     (u"NASDAQ", u"TRIT"),\
     (u"NASDAQ", u"TSRX"),\
     (u"NASDAQ", u"TROV"),\
     (u"NASDAQ", u"TROVU"),\
     (u"NASDAQ", u"TRLG"),\
     (u"NASDAQ", u"TBOW"),\
     (u"NASDAQ", u"TRST"),\
     (u"NASDAQ", u"TRMK"),\
     (u"NASDAQ", u"TSRI"),\
     (u"NASDAQ", u"TTMI"),\
     (u"NASDAQ", u"TUDO"),\
     (u"NASDAQ", u"TUES"),\
     (u"NASDAQ", u"TFCO"),\
     (u"NASDAQ", u"TWTC"),\
     (u"NASDAQ", u"TWIN"),\
     (u"NASDAQ", u"USCR"),\
     (u"NASDAQ", u"PRTS"),\
     (u"NASDAQ", u"USEG"),\
     (u"NASDAQ", u"GROW"),\
     (u"NASDAQ", u"USHS"),\
     (u"NASDAQ", u"USPH"),\
     (u"NASDAQ", u"UBNT"),\
     (u"NASDAQ", u"UFPT"),\
     (u"NASDAQ", u"ULTA"),\
     (u"NASDAQ", u"UCTT"),\
     (u"NASDAQ", u"ULBI"),\
     (u"NASDAQ", u"ULTR"),\
     (u"NASDAQ", u"UTEK"),\
     (u"NASDAQ", u"UMBF"),\
     (u"NASDAQ", u"UMPQ"),\
     (u"NASDAQ", u"UNAM"),\
     (u"NASDAQ", u"UNIS"),\
     (u"NASDAQ", u"UNB"),\
     (u"NASDAQ", u"UDRL"),\
     (u"NASDAQ", u"UBSH"),\
     (u"NASDAQ", u"UNXL"),\
     (u"NASDAQ", u"UBCP"),\
     (u"NASDAQ", u"UBOH"),\
     (u"NASDAQ", u"UBSI"),\
     (u"NASDAQ", u"UCBA"),\
     (u"NASDAQ", u"UCBI"),\
     (u"NASDAQ", u"UCFC"),\
     (u"NASDAQ", u"UBNK"),\
     (u"NASDAQ", u"UFCS"),\
     (u"NASDAQ", u"UNFI"),\
     (u"NASDAQ", u"UNTD"),\
     (u"NASDAQ", u"UBFO"),\
     (u"NASDAQ", u"USBI"),\
     (u"NASDAQ", u"USLM"),\
     (u"NASDAQ", u"USTR"),\
     (u"NASDAQ", u"UTHR"),\
     (u"NASDAQ", u"UG"),\
     (u"NASDAQ", u"UNTK"),\
     (u"NASDAQ", u"UNTY"),\
     (u"NASDAQ", u"UBPS"),\
     (u"NASDAQ", u"UBPSU"),\
     (u"NASDAQ", u"UBPSW"),\
     (u"NASDAQ", u"PANL"),\
     (u"NASDAQ", u"UEIC"),\
     (u"NASDAQ", u"UFPI"),\
     (u"NASDAQ", u"USAP"),\
     (u"NASDAQ", u"UACL"),\
     (u"NASDAQ", u"UVSP"),\
     (u"NASDAQ", u"UPIP"),\
     (u"NASDAQ", u"URRE"),\
     (u"NASDAQ", u"URBN"),\
     (u"NASDAQ", u"ULGX"),\
     (u"NASDAQ", u"UPI"),\
     (u"NASDAQ", u"ECOL"),\
     (u"NASDAQ", u"USMO"),\
     (u"NASDAQ", u"USAT"),\
     (u"NASDAQ", u"USATP"),\
     (u"NASDAQ", u"USATZ"),\
     (u"NASDAQ", u"USAK"),\
     (u"NASDAQ", u"UTMD"),\
     (u"NASDAQ", u"UTIW"),\
     (u"NASDAQ", u"UTSI"),\
     (u"NASDAQ", u"VLNC"),\
     (u"NASDAQ", u"VYFC"),\
     (u"NASDAQ", u"VLYWW"),\
     (u"NASDAQ", u"VALU"),\
     (u"NASDAQ", u"VCLK"),\
     (u"NASDAQ", u"VVTV"),\
     (u"NASDAQ", u"VNDA"),\
     (u"NASDAQ", u"VGIT"),\
     (u"NASDAQ", u"VCIT"),\
     (u"NASDAQ", u"VNQI"),\
     (u"NASDAQ", u"VCLT"),\
     (u"NASDAQ", u"VGLT"),\
     (u"NASDAQ", u"VMBS"),\
     (u"NASDAQ", u"VONE"),\
     (u"NASDAQ", u"VONG"),\
     (u"NASDAQ", u"VONV"),\
     (u"NASDAQ", u"VTWO"),\
     (u"NASDAQ", u"VTWG"),\
     (u"NASDAQ", u"VTWV"),\
     (u"NASDAQ", u"VTHR"),\
     (u"NASDAQ", u"VGSH"),\
     (u"NASDAQ", u"VCSH"),\
     (u"NASDAQ", u"VXUS"),\
     (u"NASDAQ", u"VDSI"),\
     (u"NASDAQ", u"VASC"),\
     (u"NASDAQ", u"WOOF"),\
     (u"NASDAQ", u"VECO"),\
     (u"NASDAQ", u"VELT"),\
     (u"NASDAQ", u"VTUS"),\
     (u"NASDAQ", u"VRA"),\
     (u"NASDAQ", u"VSTM"),\
     (u"NASDAQ", u"VRNM"),\
     (u"NASDAQ", u"VRNT"),\
     (u"NASDAQ", u"VRSN"),\
     (u"NASDAQ", u"VRSK"),\
     (u"NASDAQ", u"VRML"),\
     (u"NASDAQ", u"VSNT"),\
     (u"NASDAQ", u"VRTX"),\
     (u"NASDAQ", u"VRTA"),\
     (u"NASDAQ", u"VRTB"),\
     (u"NASDAQ", u"VIA"),\
     (u"NASDAQ", u"VIAB"),\
     (u"NASDAQ", u"VSAT"),\
     (u"NASDAQ", u"VIAS"),\
     (u"NASDAQ", u"VICL"),\
     (u"NASDAQ", u"VICR"),\
     (u"NASDAQ", u"VIDE"),\
     (u"NASDAQ", u"VPFG"),\
     (u"NASDAQ", u"VBFC"),\
     (u"NASDAQ", u"VLGEA"),\
     (u"NASDAQ", u"VIMC"),\
     (u"NASDAQ", u"VIRC"),\
     (u"NASDAQ", u"VMED"),\
     (u"NASDAQ", u"VCBI"),\
     (u"NASDAQ", u"VPHM"),\
     (u"NASDAQ", u"VSCP"),\
     (u"NASDAQ", u"VRTS"),\
     (u"NASDAQ", u"VRTU"),\
     (u"NASDAQ", u"VISN"),\
     (u"NASDAQ", u"VSCI"),\
     (u"NASDAQ", u"VIST"),\
     (u"NASDAQ", u"VPRT"),\
     (u"NASDAQ", u"VITC"),\
     (u"NASDAQ", u"VTSS"),\
     (u"NASDAQ", u"VTNC"),\
     (u"NASDAQ", u"VVUS"),\
     (u"NASDAQ", u"VOCS"),\
     (u"NASDAQ", u"VOD"),\
     (u"NASDAQ", u"VOLC"),\
     (u"NASDAQ", u"VLTR"),\
     (u"NASDAQ", u"VOXX"),\
     (u"NASDAQ", u"VSBN"),\
     (u"NASDAQ", u"VSEC"),\
     (u"NASDAQ", u"WACLY"),\
     (u"NASDAQ", u"WCRX"),\
     (u"NASDAQ", u"WRES"),\
     (u"NASDAQ", u"WWVY"),\
     (u"NASDAQ", u"WBCO"),\
     (u"NASDAQ", u"WAFD"),\
     (u"NASDAQ", u"WAFDW"),\
     (u"NASDAQ", u"WASH"),\
     (u"NASDAQ", u"WSBF"),\
     (u"NASDAQ", u"WAVX"),\
     (u"NASDAQ", u"WAYN"),\
     (u"NASDAQ", u"WSTG"),\
     (u"NASDAQ", u"WDFC"),\
     (u"NASDAQ", u"WWWW"),\
     (u"NASDAQ", u"WBMD"),\
     (u"NASDAQ", u"WEBM"),\
     (u"NASDAQ", u"WBSN"),\
     (u"NASDAQ", u"WEBK"),\
     (u"NASDAQ", u"WEN"),\
     (u"NASDAQ", u"WERN"),\
     (u"NASDAQ", u"WSBC"),\
     (u"NASDAQ", u"WTBA"),\
     (u"NASDAQ", u"WCBO"),\
     (u"NASDAQ", u"WMAR"),\
     (u"NASDAQ", u"WABC"),\
     (u"NASDAQ", u"WSTL"),\
     (u"NASDAQ", u"WDC"),\
     (u"NASDAQ", u"WLBC"),\
     (u"NASDAQ", u"WFD"),\
     (u"NASDAQ", u"WEST"),\
     (u"NASDAQ", u"WLB"),\
     (u"NASDAQ", u"WLBPZ"),\
     (u"NASDAQ", u"WPRT"),\
     (u"NASDAQ", u"WWAY"),\
     (u"NASDAQ", u"WEYS"),\
     (u"NASDAQ", u"WFM"),\
     (u"NASDAQ", u"WILN"),\
     (u"NASDAQ", u"WVVI"),\
     (u"NASDAQ", u"WLDN"),\
     (u"NASDAQ", u"WLFC"),\
     (u"NASDAQ", u"WLFCP"),\
     (u"NASDAQ", u"WIBC"),\
     (u"NASDAQ", u"WIN"),\
     (u"NASDAQ", u"WINA"),\
     (u"NASDAQ", u"WWIN"),\
     (u"NASDAQ", u"WTFC"),\
     (u"NASDAQ", u"WTFCW"),\
     (u"NASDAQ", u"RNIN"),\
     (u"NASDAQ", u"WETF"),\
     (u"NASDAQ", u"GULF"),\
     (u"NASDAQ", u"EMCB"),\
     (u"NASDAQ", u"WBKC"),\
     (u"NASDAQ", u"WWD"),\
     (u"NASDAQ", u"WRLD"),\
     (u"NASDAQ", u"XWES"),\
     (u"NASDAQ", u"WHRT"),\
     (u"NASDAQ", u"BWOW"),\
     (u"NASDAQ", u"BWOWU"),\
     (u"NASDAQ", u"BWOWW"),\
     (u"NASDAQ", u"WPCS"),\
     (u"NASDAQ", u"WPPGY"),\
     (u"NASDAQ", u"WMGI"),\
     (u"NASDAQ", u"WSB"),\
     (u"NASDAQ", u"WSFS"),\
     (u"NASDAQ", u"WSCI"),\
     (u"NASDAQ", u"WUHN"),\
     (u"NASDAQ", u"WVFC"),\
     (u"NASDAQ", u"WYNN"),\
     (u"NASDAQ", u"XATA"),\
     (u"NASDAQ", u"XBKS"),\
     (u"NASDAQ", u"XNPT"),\
     (u"NASDAQ", u"XLNX"),\
     (u"NASDAQ", u"XOMA"),\
     (u"NASDAQ", u"XRTX"),\
     (u"NASDAQ", u"YAVY"),\
     (u"NASDAQ", u"YHOO"),\
     (u"NASDAQ", u"YNDX"),\
     (u"NASDAQ", u"YONG"),\
     (u"NASDAQ", u"YOD"),\
     (u"NASDAQ", u"YDNT"),\
     (u"NASDAQ", u"YRCW"),\
     (u"NASDAQ", u"YTEC"),\
     (u"NASDAQ", u"ZAGG"),\
     (u"NASDAQ", u"ZLCS"),\
     (u"NASDAQ", u"ZAZA"),\
     (u"NASDAQ", u"ZBRA"),\
     (u"NASDAQ", u"ZLTQ"),\
     (u"NASDAQ", u"ZHNE"),\
     (u"NASDAQ", u"HOGS"),\
     (u"NASDAQ", u"Z"),\
     (u"NASDAQ", u"ZN"),\
     (u"NASDAQ", u"ZNWAL"),\
     (u"NASDAQ", u"ZNWAW"),\
     (u"NASDAQ", u"ZNWAZ"),\
     (u"NASDAQ", u"ZION"),\
     (u"NASDAQ", u"ZIONW"),\
     (u"NASDAQ", u"ZIOP"),\
     (u"NASDAQ", u"ZIP"),\
     (u"NASDAQ", u"ZIPR"),\
     (u"NASDAQ", u"ZIXI"),\
     (u"NASDAQ", u"ZGNX"),\
     (u"NASDAQ", u"ZOLT"),\
     (u"NASDAQ", u"ZOOM"),\
     (u"NASDAQ", u"ZUMZ"),\
     (u"NASDAQ", u"ZIGO"),\
     (u"NASDAQ", u"ZNGA")]
    


if __name__ == '__main__':
    fh = codecs.open('news.csv', encoding='utf-8', mode='w+')
    for ticker in tickers():
        try:
            apply(PSVForTicker, (ticker[0], ticker[1], fh))
        except:
            continue
    fh.close()



