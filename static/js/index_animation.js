//code used to suppress unnecessary warnings found on https://greensock.com/forums/topic/22491-gsap3-target-object-not-found/
gsap.config({
  nullTargetWarn: false,
});
//LOGO AND TEXT REVEALS FOR NAVBAR
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