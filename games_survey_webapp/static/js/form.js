var gamerTypeID = "gamerDiv";
var singleDivClass = "div-single";
var multiDivClass = "div-multi";

var resignRadioButton = document.getElementById("resignRadio");
var resignDivClass = "div-resign";

var guildRadioButton = document.getElementById("guildRadio");
var guildDivClass = "div-guild";

var anchorTop = "anchorTop"; // anchored to <body> tag

var multiTitlesCheckboxGrpID = 'MultiTitlesCheckboxGrp';
var resignChoiceCheckboxGrpID = 'ResignChoiceCheckboxGrp';
var guildWhyCheckboxGrpID = 'GuildWhyCheckboxGrp';

var survey = document.getElementById("survey");
var surveyCollapse2 = "collapse2";
var surveyCollapse3 = "collapse3";
var accordionBtn1 = document.getElementById("accordion_btn_1");
var accordionBtn2 = document.getElementById("accordion_btn_2");
var accordionSubmit1 = document.getElementById("accordion_submit_1");
var accordionSubmit2 = document.getElementById("accordion_submit_2");


function validateInitialization(){
    accordionBtn1.classList.add("hidden");
    accordionBtn2.classList.add("hidden");
    accordionSubmit1.classList.remove("hidden");
    accordionSubmit2.classList.remove("hidden");
    survey.onsubmit = function(){
        return false;
    }
    setRequireAttrToAll(surveyCollapse2,false);
    setRequireAttrToAll(surveyCollapse3,false);
}

function validateForm(buttonNumber){
    switch(buttonNumber){
        case 1:
            if(survey.checkValidity()) {
                accordionBtn1.click();
                setTimeout(function(){
                    setRequireAttrToAll(surveyCollapse2, true);
                    checkboxRequireAll();
                }, 100);
            }
            break;
        case 2:
            setRequireAttrToAll(surveyCollapse3, false);
            if(survey.checkValidity()) {
                accordionBtn2.click();
                setTimeout(function(){
                    setRequireAttrToAll(surveyCollapse3, true);
                    showGamerDiv();
                    showResignDiv();
                    showGuildDiv();
                }, 100);
            }
            break;
        case 3:
            if(survey.checkValidity()) {
                survey.submit();
            }
            break;
    }
}

function showGamerDiv(){
    var inputsAll = document.querySelectorAll('#' + gamerTypeID + ' input');
    var input;
    var i;

    for(i =0; i< inputsAll.length;i++){
        input = inputsAll[i];
        if(input.checked == true){
            switch(i) {
                case 0:
                    showSingleDiv('show');
                    showMultiDiv('hide');
                    break;
                case 1:
                    showSingleDiv('hide');
                    showMultiDiv('show');
                    break;
                case 2:
                    showSingleDiv('show');
                    showMultiDiv('show');
                    break;
                default:
                    break;
            }
        }
    }
}

function showSingleDiv(action){

    var iterator;
    var singleDivArray = document.getElementsByClassName(singleDivClass);

    if (action == 'show') {
        for (iterator = 0; iterator < singleDivArray.length; iterator++) {
            singleDivArray[iterator].style.display = "block";
        }
        uncheckAll(singleDivClass, 'show');
        checkboxRequireAll();
    }
    else {
        for (iterator = 0; iterator < singleDivArray.length; iterator++) {
            singleDivArray[iterator].style.display = "none";
        }
        uncheckAll(singleDivClass, 'hide');
        checkboxRequireAll();
    }
}

function showMultiDiv(action){

    var iterator;
    var multiDivArray = document.getElementsByClassName(multiDivClass);

    if (action == 'show'){
        for (iterator=0; iterator < multiDivArray.length; iterator++){
            multiDivArray[iterator].style.display = "block";
        }
        uncheckAll(multiDivClass,'show');
        checkboxRequireAll();
    }
    else {
        for (iterator=0; iterator < multiDivArray.length; iterator++){
            multiDivArray[iterator].style.display = "none";
        }
        uncheckAll(multiDivClass,'hide');
        checkboxRequireAll();
    }
}

function showResignDiv(){

    var iterator;
    var resignDivArray = document.getElementsByClassName(resignDivClass);

    if (resignRadioButton.checked){
        for (iterator=0; iterator < resignDivArray.length; iterator++){
            resignDivArray[iterator].style.display = "block";
        }
        uncheckAll(resignDivClass,'show');
        checkboxRequireAll();
    }
    else {
        for (iterator=0; iterator < resignDivArray.length; iterator++){
            resignDivArray[iterator].style.display = "none";
        }
        uncheckAll(resignDivClass,'hide');
        checkboxRequireAll();
    }
}

function showGuildDiv(){

    var iterator;
    var guildDivArray = document.getElementsByClassName("div-guild");

    if (guildRadioButton.checked){
        for (iterator=0; iterator < guildDivArray.length; iterator++){
            guildDivArray[iterator].style.display = "block";
        }
        uncheckAll(guildDivClass,'show');
        checkboxRequireAll();
    }
    else {
        for (iterator=0; iterator < guildDivArray.length; iterator++){
            guildDivArray[iterator].style.display = "none";
        }
        uncheckAll(guildDivClass,'hide');
        checkboxRequireAll();
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

function uncheckAll(divClass, actionString) {
    var inputsAll = document.querySelectorAll('div.' + divClass + ' input');
    var inputsHidden = document.querySelectorAll('div.' + divClass + ' div.hidden' + ' input');
    var input;
    var i;

    switch(actionString){
        case 'hide':
            for(i =0; i< inputsAll.length;i++){
                input = inputsAll[i];
                input.checked = false;
                input.required = false;
            }
            for(i =0; i< inputsHidden.length;i++){
                input = inputsHidden[i];
                input.checked = true;
            }
            break;

        case 'show':
            for(i =0; i< inputsAll.length;i++){
                input = inputsAll[i];
                input.required = true;
            }
            for(i =0; i< inputsHidden.length;i++){
                input = inputsHidden[i];
                input.checked = false;
            }
            break;

        default:
            break;
    }
}

function checkboxRequireAll(){

    var checkboxGrpArray = [multiTitlesCheckboxGrpID, resignChoiceCheckboxGrpID, guildWhyCheckboxGrpID];

    for (var i in checkboxGrpArray){
        checkboxRequire(checkboxGrpArray[i]);
    }
}

function checkboxRequire(divID) {
    var inputsAll = document.querySelectorAll('#' + divID + ' input');
    var input;
    var i;

    for(i =0; i< inputsAll.length;i++){
        input = inputsAll[i];
        if(input.checked == true) {
            setRequireAttrToAll(divID, false);
            break;
        }
        else if (i == inputsAll.length - 1){
            setRequireAttrToAll(divID, true);
            input.required = false;
        }
    }
}

function setRequireAttrToAll(divID, actionBool){
    // actionBool is either true or false
    var inputsAll = document.querySelectorAll('#' + divID + ' input');
    var input;
    var i;

    for(i =0; i< inputsAll.length;i++){
        input = inputsAll[i];
        input.required = actionBool;
    }

    inputsAll = document.querySelectorAll('#' + divID + ' select');
    for(i =0; i< inputsAll.length;i++){
        input = inputsAll[i];
        input.required = actionBool;
    }
}

window.onload = function() {
    showResignDiv();
    showGuildDiv();
    showSingleDiv('hide');
    showMultiDiv('hide');
    checkboxRequireAll();
    validateInitialization();
}

window.onscroll = function(){
    var navbar = document.getElementsByClassName('navbar')[0]
    if(this.scrollY > 200){
        navbar.classList.add('hidden');
    }
    else {
        navbar.classList.remove('hidden');
    }
}