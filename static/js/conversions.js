// jshint esversion: 6
//TEMPERATURE CONVERSION
//Code modified from YouTube Tutorial by whatsdev: https://youtu.be/8mRGfLL1nzE
const celciusInput = document.querySelector('#celcius > input');
const fahrenheitInput = document.querySelector('#fahrenheit > input');
const kelvinInput = document.querySelector('#kelvin > input');

//Round to two decimal places
function roundNum(num) {
    return Math.round(num*100)/100;
}

//Celcius to Fahrenheit and Kelvin
function celciusToFahrenheitAndKelvin() {
    //parse to convert string to integer
    const cTemp = parseFloat(celciusInput.value);
    const fTemp = (cTemp * (9/5)) + 32;
    const kTemp = cTemp + 273.15;
    fahrenheitInput.value = roundNum(fTemp);
    kelvinInput.value = roundNum(kTemp);
}

//Fahrenheit to Celcius and Kelvin
function fahrenheitToCelciusAndKelvin() {
    const fTemp = parseFloat(fahrenheitInput.value);
    const cTemp = (fTemp - 32) * (5/9);
    const kTemp = cTemp + 273.15;
    celciusInput.value = roundNum(cTemp);
    kelvinInput.value = roundNum(kTemp);
}

//Kelvin to Celcius and Fahrenheit
function kelvinToCelciusAndFahrenheit() {
    const kTemp = parseFloat(kelvinInput.value);
    const cTemp = kTemp - 273.15;
    const fTemp = (cTemp * (9/5)) + 32;
    celciusInput.value = roundNum(cTemp);
    fahrenheitInput.value = roundNum(fTemp);
}

//Event listeners
celciusInput.addEventListener('input', celciusToFahrenheitAndKelvin);
fahrenheitInput.addEventListener('input', fahrenheitToCelciusAndKelvin);
kelvinInput.addEventListener('input', kelvinToCelciusAndFahrenheit);


//WEIGHT CONVERSION
//Code modified from YouTube Tutorial by whatsdev: https://youtu.be/8mRGfLL1nzE
const gramsInput = document.querySelector('#grams > input');
const ouncesInput = document.querySelector('#ounces > input');
const tbspInput = document.querySelector('#tbsp > input');
const tspInput = document.querySelector('#tsp > input');

//Round to two decimal places
function roundNum(num) {
    return Math.round(num*100)/100;
}

//Grams to all Other Weights
function gramsToOthers() {
    //parse to convert string to integer
    const gWeight = parseFloat(gramsInput.value);
    const oWeight = gWeight / 28.3495;
    const tbspWeight = gWeight / 14.3;
    const tspWeight = tbspWeight * 3;
    ouncesInput.value = roundNum(oWeight);
    tbspInput.value = roundNum(tbspWeight);
    tspInput.value = roundNum(tspWeight);
}

//Ounces to all Other Weights
function ouncesToOthers() {
    //parse to convert string to integer
    const oWeight = parseFloat(ouncesInput.value);
    const gWeight = oWeight * 28.3495;
    const tbspWeight = oWeight * 2;
    const tspWeight = tbspWeight * 3;
    gramsInput.value = roundNum(gWeight);
    tbspInput.value = roundNum(tbspWeight);
    tspInput.value = roundNum(tspWeight);
}

//Tbsp to all Other Weights
function tbspToOthers() {
    //parse to convert string to integer
    const tbspWeight = parseFloat(tbspInput.value);
    const oWeight = tbspWeight / 2;
    const tspWeight = tbspWeight * 3;
    const gWeight = oWeight * 28.3495;
    gramsInput.value = roundNum(gWeight);
    ouncesInput.value = roundNum(oWeight);
    tspInput.value = roundNum(tspWeight);
}

//Tsp to all Other Weights
function tspToOthers() {
    //parse to convert string to integer
    const tspWeight = parseFloat(tspInput.value);
    const tbspWeight = tspWeight / 3;
    const oWeight = tbspWeight / 2;
    const gWeight = oWeight * 28.3495;
    gramsInput.value = roundNum(gWeight);
    ouncesInput.value = roundNum(oWeight);
    tbspInput.value = roundNum(tbspWeight);
}

//Event listeners
gramsInput.addEventListener('input', gramsToOthers);
ouncesInput.addEventListener('input', ouncesToOthers);
tbspInput.addEventListener('input', tbspToOthers);
tspInput.addEventListener('input', tspToOthers);


//CUP CONVERSION
//Code modified from YouTube Tutorial by whatsdev: https://youtu.be/8mRGfLL1nzE
const gramsInputCup = document.querySelector('#grams2 > input');
const dryCupsInput = document.querySelector('#drycups > input');
const wetCupsInput = document.querySelector('#wetcups > input');
const butterCupsInput = document.querySelector('#buttercups > input');
const breadCupsInput = document.querySelector('#breadcups > input');
const oatCupsInput = document.querySelector('#oatcups > input');
const sugarCupsInput = document.querySelector('#sugarcups > input');

//Round to two decimal places
function roundNum(num) {
    return Math.round(num*100)/100;
}

//Grams to all Other Weights
function gramsToOthersCups() {
    //parse to convert string to integer
    const gWeight = parseFloat(gramsInputCup.value);
    const dryCupWeight = gWeight / 128;
    const wetCupWeight = gWeight / 340;
    const butterCupWeight = gWeight / 227;
    const breadCupWeight = gWeight / 136;
    const oatCupWeight = gWeight / 85;
    const sugarCupWeight = gWeight / 201;
    dryCupsInput.value = roundNum(dryCupWeight);
    wetCupsInput.value = roundNum(wetCupWeight);
    butterCupsInput.value = roundNum(butterCupWeight);
    breadCupsInput.value = roundNum(breadCupWeight);
    oatCupsInput.value = roundNum(oatCupWeight);
    sugarCupsInput.value = roundNum(sugarCupWeight);
}

//Dry Goods Cups to all Other Weights
function dryCupsToOthers() {
    //parse to convert string to integer
    const dryCupWeight = parseFloat(dryCupsInput.value);
    const gWeight = dryCupWeight * 128;
    const wetCupWeight = gWeight / 340;
    const butterCupWeight = gWeight / 227;
    const breadCupWeight = gWeight / 136;
    const oatCupWeight = gWeight / 85;
    const sugarCupWeight = gWeight / 201;
    gramsInputCup.value = roundNum(gWeight);
    wetCupsInput.value = roundNum(wetCupWeight);
    butterCupsInput.value = roundNum(butterCupWeight);
    breadCupsInput.value = roundNum(breadCupWeight);
    oatCupsInput.value = roundNum(oatCupWeight);
    sugarCupsInput.value = roundNum(sugarCupWeight);
}

//Wet Goods Cups to all Other Weights
function wetCupsToOthers() {
    //parse to convert string to integer
    const wetCupWeight = parseFloat(wetCupsInput.value);
    const gWeight = wetCupWeight * 340;
    const dryCupWeight = gWeight / 128;
    const butterCupWeight = gWeight / 227;
    const breadCupWeight = gWeight / 136;
    const oatCupWeight = gWeight / 85;
    const sugarCupWeight = gWeight / 201;
    gramsInputCup.value = roundNum(gWeight);
    dryCupsInput.value = roundNum(dryCupWeight);
    butterCupsInput.value = roundNum(butterCupWeight);
    breadCupsInput.value = roundNum(breadCupWeight);
    oatCupsInput.value = roundNum(oatCupWeight);
    sugarCupsInput.value = roundNum(sugarCupWeight);
}

//Butter Cups to all Other Weights
function butterCupsToOthers() {
    //parse to convert string to integer
    const butterCupWeight = parseFloat(butterCupsInput.value);
    const gWeight = butterCupWeight * 227;
    const dryCupWeight = gWeight / 128;
    const wetCupWeight = gWeight / 340;
    const breadCupWeight = gWeight / 136;
    const oatCupWeight = gWeight / 85;
    const sugarCupWeight = gWeight / 201;
    gramsInputCup.value = roundNum(gWeight);
    dryCupsInput.value = roundNum(dryCupWeight);
    wetCupsInput.value = roundNum(wetCupWeight);
    breadCupsInput.value = roundNum(breadCupWeight);
    oatCupsInput.value = roundNum(oatCupWeight);
    sugarCupsInput.value = roundNum(sugarCupWeight);
}

//Bread Cups to all Other Weights
function breadCupsToOthers() {
    //parse to convert string to integer
    const breadCupWeight = parseFloat(breadCupsInput.value);
    const gWeight = breadCupWeight * 136;
    const dryCupWeight = gWeight / 128;
    const wetCupWeight = gWeight / 340;
    const butterCupWeight = gWeight / 227;
    const oatCupWeight = gWeight / 85;
    const sugarCupWeight = gWeight / 201;
    gramsInputCup.value = roundNum(gWeight);
    dryCupsInput.value = roundNum(dryCupWeight);
    wetCupsInput.value = roundNum(wetCupWeight);
    butterCupsInput.value = roundNum(butterCupWeight);
    oatCupsInput.value = roundNum(oatCupWeight);
    sugarCupsInput.value = roundNum(sugarCupWeight);
}

//Oat Cups to all Other Weights
function oatCupsToOthers() {
    //parse to convert string to integer
    const oatCupWeight = parseFloat(oatCupsInput.value);
    const gWeight = oatCupWeight * 85;
    const dryCupWeight = gWeight / 128;
    const wetCupWeight = gWeight / 340;
    const butterCupWeight = gWeight / 227;
    const breadCupWeight = gWeight / 136;
    const sugarCupWeight = gWeight / 201;
    gramsInputCup.value = roundNum(gWeight);
    dryCupsInput.value = roundNum(dryCupWeight);
    wetCupsInput.value = roundNum(wetCupWeight);
    butterCupsInput.value = roundNum(butterCupWeight);
    breadCupsInput.value = roundNum(breadCupWeight);
    sugarCupsInput.value = roundNum(sugarCupWeight);
}

//Sugar Cups to all Other Weights
function sugarCupsToOthers() {
    //parse to convert string to integer
    const sugarCupWeight = parseFloat(sugarCupsInput.value);
    const gWeight = sugarCupWeight * 201;
    const dryCupWeight = gWeight / 128;
    const wetCupWeight = gWeight / 340;
    const butterCupWeight = gWeight / 227;
    const breadCupWeight = gWeight / 136;
    const oatCupWeight = gWeight / 85;
    gramsInputCup.value = roundNum(gWeight);
    dryCupsInput.value = roundNum(dryCupWeight);
    wetCupsInput.value = roundNum(wetCupWeight);
    butterCupsInput.value = roundNum(butterCupWeight);
    breadCupsInput.value = roundNum(breadCupWeight);
    oatCupsInput.value = roundNum(oatCupWeight);
}

//Event listeners
gramsInputCup.addEventListener('input', gramsToOthersCups);
dryCupsInput.addEventListener('input', dryCupsToOthers);
wetCupsInput.addEventListener('input', wetCupsToOthers);
butterCupsInput.addEventListener('input', butterCupsToOthers);
breadCupsInput.addEventListener('input', breadCupsToOthers);
oatCupsInput.addEventListener('input', oatCupsToOthers);
sugarCupsInput.addEventListener('input', sugarCupsToOthers);

//VOLUME CONVERSION
const millilitresInput = document.querySelector('#millilitres > input');
const fluidOuncesInput = document.querySelector('#fl_ounces > input');
const cupInput = document.querySelector('#cup_vol > input');

//Round to two decimal places
function roundNum(num) {
    return Math.round(num*100)/100;
}

//Millilitres to Others
function millilitresToOthers() {
    //parse to convert string to integer
    const mlVol = parseFloat(millilitresInput.value);
    const flozVol = mlVol / 30;
    const cupVol = mlVol / 240;
    fluidOuncesInput.value = roundNum(flozVol);
    cupInput.value = roundNum(cupVol);
}

//Fuid Ounces to Others
function fluidOuncesToOthers() {
    //parse to convert string to integer
    const flozVol = parseFloat(fluidOuncesInput.value);
    const mlVol = flozVol * 30;
    const cupVol = mlVol / 240;
    millilitresInput.value = roundNum(mlVol);
    cupInput.value = roundNum(cupVol);
}

//Cups to Others
function cupsToOthers() {
    //parse to convert string to integer
    const cupVol = parseFloat(cupInput.value);
    const mlVol = cupVol * 240;
    const flozVol = mlVol / 30;
    millilitresInput.value = roundNum(mlVol);
    fluidOuncesInput.value = roundNum(flozVol);
}

//Event listeners
millilitresInput.addEventListener('input', millilitresToOthers);
fluidOuncesInput.addEventListener('input', fluidOuncesToOthers);
cupInput.addEventListener('input', cupsToOthers);
