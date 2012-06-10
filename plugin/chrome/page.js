function getIndicator(anchor, title, ticker){
    var req = new XMLHttpRequest();
    req.open(
        "GET",
        "http://127.0.0.1:3000/news/" + title,
        true);
    req.onload = function() {
        resp = req.responseText;
        console.log(resp);
        if(resp.indexOf("Increase") != -1) {
            anchor.innerHTML = anchor.innerHTML + "<img src='http://localhost:3000/plus.jpg' />";
        } else if (resp.indexOf("Decrease") != -1) {
            anchor.innerHTML = anchor.innerHTML + "<img src='http://localhost:3000/minus.jpg' />";
        }
    };
    req.send(null);
}

function getTicker(){
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == "q") {
            return pair[1].split(":")[1];
        }
    }    
}

var alex_divs = document.getElementsByClassName("g-section news sfe-break-bottom-16");
var alex_ticker = getTicker();

for(adiv in alex_divs) {
    if (alex_divs[adiv].getElementsByTagName) {
        var anchors = alex_divs[adiv].getElementsByTagName("a");
        if (anchors) {
            for (a in anchors) {
                var title = anchors[a].innerHTML;
                if(title && title.indexOf("Related articles")){
                    title.replace("\n", "");
                    console.log(title);
                    getIndicator(anchors[a], encodeURIComponent(title), alex_ticker);
                }
            }
        }
    }
}



