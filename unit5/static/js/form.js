var multiCheckbox = document.getElementById("multiCheckbox");
var multiDivArray = document.getElementsByClassName("div-multi");

var singleCheckbox = document.getElementById("singleCheckbox");
var singleDivArray = document.getElementsByClassName("div-single");

var resignRadioButton = document.getElementById("resignRadio");
var resignDivArray = document.getElementsByClassName("div-resign");

var guildRadioButton = document.getElementById("guildRadio");
var guildDivArray = document.getElementsByClassName("div-guild");

var anchorTop = "anchorTop"; // anchored to <body> tag

function showSingleDiv(){

    var iterator;

    if (singleCheckbox.checked){
        for (iterator=0; iterator < singleDivArray.length; iterator++){
            singleDivArray[iterator].style.display = "block";
        }
    }
    else {
        for (iterator=0; iterator < singleDivArray.length; iterator++){
            singleDivArray[iterator].style.display = "none";
        }
    }
}

function showMultiDiv(){

    var iterator;

    if (multiCheckbox.checked){
        for (iterator=0; iterator < multiDivArray.length; iterator++){
            multiDivArray[iterator].style.display = "block";
        }
    }
    else {
        for (iterator=0; iterator < multiDivArray.length; iterator++){
            multiDivArray[iterator].style.display = "none";
        }
    }
}

function showResignDiv(){

    var iterator;

    if (resignRadioButton.checked){
        for (iterator=0; iterator < resignDivArray.length; iterator++){
            resignDivArray[iterator].style.display = "block";
        }
    }
    else {
        for (iterator=0; iterator < resignDivArray.length; iterator++){
            resignDivArray[iterator].style.display = "none";
        }
    }
}

function showGuildDiv(){

    var iterator;

    if (guildRadioButton.checked){
        for (iterator=0; iterator < guildDivArray.length; iterator++){
            guildDivArray[iterator].style.display = "block";
        }
    }
    else {
        for (iterator=0; iterator < guildDivArray.length; iterator++){
            guildDivArray[iterator].style.display = "none";
        }
    }
}

function ScrollTop(){
    // Set delay for <a href> accordion links
    setTimeout(function(){
        smoothScroll(anchorTop);
    }, 150);
}

/////////////////////////////////////////////////////////////////////////////// Smooth Scroll Function Block
function smoothScroll(eID) {
    var startY = currentYPosition();
    var stopY = elmYPosition(eID);
    var distance = stopY > startY ? stopY - startY : startY - stopY;
    if (distance < 100) {
        scrollTo(0, stopY); return;
    }
    var speed = Math.round(distance / 100);
    if (speed >= 20) speed = 20;
    var step = Math.round(distance / 25);
    var leapY = stopY > startY ? startY + step : startY - step;
    var timer = 0;
    if (stopY > startY) {
        for ( var i=startY; i<stopY; i+=step ) {
            setTimeout("window.scrollTo(0, "+leapY+")", timer * speed);
            leapY += step; if (leapY > stopY) leapY = stopY; timer++;
        } return;
    }
    for ( var i=startY; i>stopY; i-=step ) {
        setTimeout("window.scrollTo(0, "+leapY+")", timer * speed);
        leapY -= step; if (leapY < stopY) leapY = stopY; timer++;
    }
}

function currentYPosition() {
    // Firefox, Chrome, Opera, Safari
    if (self.pageYOffset) return self.pageYOffset;
    // Internet Explorer 6 - standards mode
    if (document.documentElement && document.documentElement.scrollTop)
        return document.documentElement.scrollTop;
    // Internet Explorer 6, 7 and 8
    if (document.body.scrollTop) return document.body.scrollTop;
    return 0;
}

function elmYPosition(eID) {
    var elm = document.getElementById(eID);
    var y = elm.offsetTop;
    var node = elm;
    while (node.offsetParent && node.offsetParent != document.body) {
        node = node.offsetParent;
        y += node.offsetTop;
    } return y;
}
///////////////////////////////////////////////////////////////////////////////

window.onload = function() {
    showSingleDiv();
    showMultiDiv();
    showResignDiv();
    showGuildDiv();
}