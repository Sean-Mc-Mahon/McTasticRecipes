//MATERIALIZE FUNCTIONS
$(document).ready(function(){
        $('.sidenav').sidenav({edge: "right",inDuration: 1000,});
        $('.collapsible').collapsible();
        $('.tooltipped').tooltip();
        $('select').formSelect();
        $('.tabs').tabs();
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
    $("#emailaddress").val("");
    return false;  // To block from loading a new page
}

//RECIPE PLACEHOLDER IMAGE
// Allowed extensions to image address
let url_types = ["jpg", "jpeg", "png"];


//update placeholder image with recipe title
recipeName = document.getElementById('recipe_name')
recipeName.addEventListener('input', function() {
    document.getElementById('placename').innerText = recipeName.value;
    document.getElementById('placename').style.zIndex = '5';
})
// If the image address is valid, update src attr of #img and change z-index of placename to 0
document.getElementById("recipe_image").addEventListener("input", function() {
    let arr = document.getElementById("recipe_image").value.split(".");
    let pop = arr.pop().toLowerCase();
    if (pop === url_types[0] || pop === url_types[1] || pop === url_types[2]) {
        document.getElementById('placename').style.display = 'none';
        document.getElementById('img').style.display = 'block';
        document.getElementById("img").setAttribute("src", document.getElementById("recipe_image").value);
    } else {
        document.getElementById('placename').style.display = 'block';
        document.getElementById("img").style.display = 'none';
    }
});
