
var tableDivId = "table";


var colDefs = [
    { key: "ticker", label: "Ticker" },
    { key: "action", label: "Action" },
    { key: "news", label: "News" },
];

var myDataSource = new YAHOO.util.XHRDataSource("/tickers");
myDataSource.responseType = YAHOO.util.XHRDataSource.TYPE_JSON;
myDataSource.responseSchema = {
    resultsList : "response.results", // String pointer to result data
    // Field order doesn't matter and not all data is required to have a field
    fields : [
        { key: "ticker" }, 
        { key: "news" },   
        { key: "action" }  
    ],
    metaFields : {
        // oParsedResponse.meta.totalRecords === 1358
        totalRecords : "response.total", 
        //something : "Important.to.me"
    }
};

// DataTable constructor syntax
var myDataTable = new YAHOO.widget.DataTable(tableDivId, colDefs, myDataSource);