import growler, time, urllib, json

myGrowler=growler.Growler()

# myGrowler.alert("Yes!", "No!")
# myGrowler.alert("No!", "No!")
# myGrowler.alert("Indicator", "Headline")

tickers=["VOD", "FB", "ALU", "GOOG"]

def checkTicker(ticker):
    url = 'http://localhost:3000/news/ticker/'+ticker
    u = urllib.urlopen(url)
    data = u.read()
    print data;
    resp = json.loads(data);
    return resp;


while(1):
    try:
        time.sleep(1)
        for t in tickers:
            result = checkTicker(t);
            print result
            if result.has_key(u"interest"):
                myGrowler.alert(result[u"ticker"] +" - " +result[u"interest"],
                                result[u"headline"])
    except KeyboardInterrupt:
        break;









