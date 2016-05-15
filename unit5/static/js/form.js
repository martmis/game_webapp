
var multiCheckbox = document.getElementById("multiCheckbox");
var multiDivArray = document.getElementsByClassName("div-multi");

var singleCheckbox = document.getElementById("singleCheckbox");
var singleDivArray = document.getElementsByClassName("div-single");

var resignRadioButton = document.getElementById("resignRadio");
var resignDivArray = document.getElementsByClassName("div-resign");

var guildRadioButton = document.getElementById("guildRadio");
var guildDivArray = document.getElementsByClassName("div-guild");

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

window.onload = function() {
    showSingleDiv();
    showMultiDiv();
    showResignDiv();
    showGuildDiv();
}