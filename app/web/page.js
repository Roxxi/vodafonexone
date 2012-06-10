function getIndicator(anchor, title){
    var req = new XMLHttpRequest();
    req.open(
        "GET",
        "http://127.0.0.1:3000/news/" + title,
        true);
    req.onload = function() {
        resp = req.responseText;
        console.log(resp);
        if(resp == "Increase") {
            anchor.innerHTML = anchor.innerHTML + "<img src='http://localhost:3000/plus.jpg' />";
        } else if (resp == "Decrease") {
            anchor.innerHTML = anchor.innerHTML + "<img src='http://localhost:3000/minus.jpg' />";
        }
    };
    req.send(null);
}

var alex_divs = document.getElementsByClassName("g-section news sfe-break-bottom-16");
for(adiv in alex_divs) {
    if (alex_divs[adiv].getElementsByTagName) {
        var anchors = alex_divs[adiv].getElementsByTagName("a");
        if (anchors) {
            for (a in anchors) {
                var title = anchors[a].innerHTML;
                if(title && title.indexOf("Related articles")){
                    title.replace("\n", "");
                    console.log(title);
                    getIndicator(anchors[a], encodeURIComponent(title));
                }
            }
        }
    }
}

