//code used to suppress unnecessary warnings found on https://greensock.com/forums/topic/22491-gsap3-target-object-not-found/
gsap.config({
  nullTargetWarn: false,
});
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