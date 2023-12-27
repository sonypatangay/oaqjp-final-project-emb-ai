let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = "For the given statement, the system response is " + xhttp.responseText;
        }
    };
  
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);

    xhttp.send();
}
