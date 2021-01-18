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

//ADD INSTRUCTIONS FOR ADD_RECIPE
if (window.location.pathname=='/add_recipe') {
    //SELECTORS
    const instructionInput = document.querySelector('.instruction-input');
    const instructionButton = document.querySelector('.instruction-button');
    const instructionList = document.querySelector('.instruction-list');

    //EVENT LISTENERS
    instructionButton.addEventListener('click', addInstruction);
    instructionList.addEventListener('click', deletebtn);

    //FUNCTIONS

    function addInstruction(event){
        //instruction div
        const instructionDiv = document.createElement('div');
        instructionDiv.classList.add('instruction');
        //create li
        const newInstruction = document.createElement('li');
        newInstruction.innerText = instructionInput.value;
        newInstruction.classList.add('instruction-item');
        newInstruction.setAttribute ('name', 'recipe_instructions');
        instructionDiv.appendChild(newInstruction);
        //delete button
        const trashButton = document.createElement('button');
        trashButton.innerHTML = '<i class="fas fa-trash"></i>';
        trashButton.classList.add("trash-btn");
        instructionDiv.appendChild(trashButton);
        //append to list
        instructionList.appendChild(instructionDiv);
        //clear instruction input value
        instructionInput.value = "";
    }

    function deletebtn(e){
        const item = e.target;
        //delete instruction
        if(item.classList[0] === "trash-btn") {
            console.log('hello');
            const instruction = item.parentElement;
            instruction.remove();
        }
    }
}


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

//IMAGE AND TEXT REVEALS FOR SINGLE_RECIPE
//code used to suppress unnecessary warnings found on https://greensock.com/forums/topic/22491-gsap3-target-object-not-found/
gsap.config({
  nullTargetWarn: false,
});
//code modified from tutorial as part of Creative Javascript Course @ https://developedbyed.com/
function animateSlides() {
    //Select Slides
    const sliders = document.querySelectorAll(".slide");
    //loop over each slide
    sliders.forEach((slide) => {
    const revealImg = slide.querySelector(".reveal-img");
    const img = slide.querySelector("img");
    const revealText = slide.querySelectorAll(".reveal-text");
    //gsap
    const slideTl = gsap.timeline({
      defaults: { duration: 1.5, ease: "power1.inOut" },
    });
    slideTl.fromTo(revealText, { y: "0%" }, { y: "100%" });
    slideTl.fromTo(revealImg, { x: "0%" }, { x: "-100%" }, "-=1.3");
    slideTl.fromTo(img, { scale: 2.5 }, { scale: 1 }, "-=1.5");
  });
}

animateSlides();