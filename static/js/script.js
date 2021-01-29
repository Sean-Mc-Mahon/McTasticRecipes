//MATERIALIZE FUNCTIONS
$(document).ready(function(){
        $('.sidenav').sidenav({edge: "right",inDuration: 1000,});
        $('.collapsible').collapsible();
        $('.tooltipped').tooltip();
        $('select').formSelect();
        $('.tabs').tabs();
        $('.parallax').parallax();
        $('.materialboxed').materialbox();
        $('.modal').modal();
        
        //code taken from Materialize Form Validation lesson by Tim Nelson as part of Code Institute Data Centric Development Module: https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/196c000dd670458cafc7b2dc9d4a8245/f2ad3c6775ce4890a53e62de35245c0a/?child=first
        validateMaterializeSelect();
            function validateMaterializeSelect() {
                let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
                let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
                if ($("select.validate").prop("required")) {
                    $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
                }
                $(".select-wrapper input.select-dropdown").on("focusin", function () {
                    $(this).parent(".select-wrapper").on("change", function () {
                        if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                            $(this).children("input").css(classValid);
                        }
                    });
                }).on("click", function () {
                    if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                        $(this).parent(".select-wrapper").children("input").css(classValid);
                    } else {
                        $(".select-wrapper input.select-dropdown").on("focusout", function () {
                            if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                                if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                                    $(this).parent(".select-wrapper").children("input").css(classInvalid);
                                }
                            }
                        });
                    }
                });
            }
        });


//SEND MAIL AND ALERT FOR NEWSLETTER SIGNUP
function sendMail(contactForm) {
    emailjs.send("gmail", "mctastic", {
        "from_email": contactForm.emailaddress.value
    })
    //custom alert from https://sweetalert.js.org/
    .then(
        function response (response) {
          swal({
      title: "Thanks for signing up!",
      text: "You'll recieve the newsletter every sunday",
      icon: "success",
      button: "All Done",
    });
      },
      function (error) {
        swal({
          title: "Sorry, looks like something went wrong...",
          text: "Please try again",
          icon: "error",
          button: "OK",
        });
    }
    );
    //clear form when submitting
    $("#formContact").val("");
    return false;  // To block from loading a new page
}

//FADE BLANK IMAGE HEADER ON HOVER
$('.overlay').hover(
       function(){ $('.image_header').addClass('header_fade') },
       function(){ $('.image_header').removeClass('header_fade') }
);

//IMAGE AND TEXT REVEALS FOR SINGLE_RECIPE
//code modified from tutorial as part of Creative Javascript Course @ https://developedbyed.com/
if (window.location.pathname=='/') {
    function animateNav() {
    //Select Slides
    const sliders = document.querySelectorAll(".slide");
    //loop over each slide
    sliders.forEach((slide) => {
    const revealLinks = slide.querySelector(".nav-links");
    const revealLogo = slide.querySelector(".logo-img");
    const revealLogoText = slide.querySelector(".logo-text");
    //gsap
    const slideTl = gsap.timeline({
        defaults: { duration: 1.5, ease: "power1.inOut" },
    });
    slideTl.fromTo(revealLinks, { x: "150%" }, { x: "0%" });
    slideTl.fromTo(revealLogo, { x: "-250%" }, { x: "0%" }, "-=1.5");
    slideTl.fromTo(revealLogoText, { y: "-250%" }, { y: "0%" }, "-=1.5");
    });
    }
    animateNav();
}




//IMAGE AND TEXT REVEALS FOR SINGLE_RECIPE
//code modified from tutorial as part of Creative Javascript Course @ https://developedbyed.com/
function animateSlides() {
    //Select Slides
    const sliders = document.querySelectorAll(".slide");
    //loop over each slide
    sliders.forEach((slide) => {
    const revealImg = slide.querySelector(".reveal-img");
    const revealText = slide.querySelectorAll(".reveal-text");
    //gsap
    const slideTl = gsap.timeline({
      defaults: { duration: 1.5, ease: "power1.inOut" },
    });
    slideTl.fromTo(revealText, { y: "0%" }, { y: "100%" });
    slideTl.fromTo(revealImg, { x: "0%" }, { x: "-100%" }, "-=1.3");
  });
}
animateSlides();

//TEMPERATURE CONVERSION
//Code modified from YouTube Tutorial by whatsdev: https://youtu.be/8mRGfLL1nzE
if (window.location.pathname=='/units') {
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
}

//WEIGHT CONVERSION
//Code modified from YouTube Tutorial by whatsdev: https://youtu.be/8mRGfLL1nzE
if (window.location.pathname=='/units') {
    const gramsInput = document.querySelector('#grams > input');
    const ouncesInput = document.querySelector('#ounces > input');
    const cupsInput = document.querySelector('#cups > input');
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
}

//CUP CONVERSION
//Code modified from YouTube Tutorial by whatsdev: https://youtu.be/8mRGfLL1nzE
if (window.location.pathname=='/units') {
    const gramsInput = document.querySelector('#grams2 > input');
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
    function gramsToOthers() {
        //parse to convert string to integer
        const gWeight = parseFloat(gramsInput.value);
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
        gramsInput.value = roundNum(gWeight);
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
        gramsInput.value = roundNum(gWeight);
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
        gramsInput.value = roundNum(gWeight);
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
        gramsInput.value = roundNum(gWeight);
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
        gramsInput.value = roundNum(gWeight);
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
        gramsInput.value = roundNum(gWeight);
        dryCupsInput.value = roundNum(dryCupWeight);
        wetCupsInput.value = roundNum(wetCupWeight);
        butterCupsInput.value = roundNum(butterCupWeight);
        breadCupsInput.value = roundNum(breadCupWeight);
        oatCupsInput.value = roundNum(oatCupWeight);
    }
    
    //Event listeners
    gramsInput.addEventListener('input', gramsToOthers);
    dryCupsInput.addEventListener('input', dryCupsToOthers);
    wetCupsInput.addEventListener('input', wetCupsToOthers);
    butterCupsInput.addEventListener('input', butterCupsToOthers);
    breadCupsInput.addEventListener('input', breadCupsToOthers);
    oatCupsInput.addEventListener('input', oatCupsToOthers);
    sugarCupsInput.addEventListener('input', sugarCupsToOthers);

}

//VOLUME CONVERSION
if (window.location.pathname=='/units') {
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
}