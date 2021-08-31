const menuBars=document.querySelector(".menu_bars");
const menuClose=document.querySelector(".menu_close");
const menu=document.querySelector(".menu");
const navItem=document.querySelectorAll(".menu .nav_list .nav_link .nav_item")
const nav=document.querySelector(".navbar");
const scrollUpBtn=document.querySelector(".scroll_up_btn")

menuBars.addEventListener("click",function(){
    menu.classList.add("show")
    menu.classList.remove("hide")
})

menuClose.addEventListener("click",function(){
    menu.classList.add("hide")
    menu.classList.remove("show")
})

window.addEventListener("load",function(){
    document.querySelector(".page_loader").style.display="none";
})
window.addEventListener("mouseup",function(e){
    if(e.target != menu){
        menu.classList.add("hide")
    }
})

window.addEventListener("scroll",function(){
    if(this.scrollY>50){
        nav.classList.add("shadow")
    }else{
        nav.classList.remove("shadow")
    }
    if(this.scrollY>500){
        scrollUpBtn.classList.add("show")
    }else{
        scrollUpBtn.classList.remove("show")
    }
})

scrollUpBtn.addEventListener("click",function(){
    window.scroll({
        top: 0,
        behavior: "smooth"
    })
})

const swiper1 = new Swiper(".mySwiper-1", {
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    loop: true,
    grabCursor: true,
    spaceBetween: 30,
    breakpoints: {
        576: {
            slidesPerView: 2,
            
        },
        992: {
            slidesPerView: 3,
            
        }
    }
});

const swiper2 = new Swiper(".mySwiper-2", {
    autoplay: {
        delay: 10000,
        disableOnInteraction: false,
    },
    loop: true,
    grabCursor: true,
    navigation: {
    nextEl: ".next_btn",
    prevEl: ".prev_btn",
    },
    spaceBetween: 30,
    breakpoints: {
        576: {
            slidesPerView: 2,
            
        },
        992: {
            slidesPerView: 3,
            
        }
    }
});

const swiper3 = new Swiper(".mySwiper-3", {
    loop: true,
    grabCursor: true,
    autoplay: {
      delay: 3500,
      disableOnInteraction: false,
    },
    spaceBetween: 30,
    breakpoints: {
        250: {
            slidesPerView: 1,
          },
        360: {
            slidesPerView: 2,
        },
      768: {
        slidesPerView: 3,
      },
      1024: {
        slidesPerView: 5,
      },
    },
  });


const clc = document.querySelectorAll(".team .team_cards .card .left_container .cancel");
const arr = document.querySelectorAll(".team .team_cards .card .arr_container");
const left_container = document.querySelectorAll(".team .team_cards .card .left_container");

    for(let i=0;i<arr.length;i++){
        arr[i].addEventListener("click", ()=>{
            arr[i].classList.add("active_arr");
                if(left_container[i].classList.contains("off")){
                    left_container[i].classList.remove("off");
                    left_container[i].classList.add("active");
                }
            });
    }
    

    for(let i=0;i<clc.length;i++){
        clc[i].addEventListener("click", ()=>{
            arr[i].classList.remove("active_arr");
            if(left_container[i].classList.contains("active")){
                left_container[i].classList.remove("active");
                left_container[i].classList.add("off");
            }
        });
    }
    

//Form validation in js

function validateInput(){
    const formName=document.getElementById("name");
    const nameError=document.getElementById("nameerror");
    const surname=document.getElementById("surname");
    const surnameError=document.getElementById("surnameerror");
    const email=document.getElementById("email");
    const emailError=document.getElementById("emailerror");
    const number=document.getElementById("number");
    const numberError=document.getElementById("numbererror");
    const message=document.getElementById("message");
    const messageError=document.getElementById("messageerror");

    if(formName.value === ""){
        nameError.style.visibility = "visible";
        formName.style.borderColor = "red";
        nameError.innerHTML = "Bu sahə boş ola bilməz";
        return false;
    }
    else{
        nameError.style.visibility = "hidden";
        formName.style.borderColor = "green";
    }
    if(surname.value === ""){
        surnameError.style.visibility = "visible";
        surname.style.borderColor = "red";
        surnameError.innerHTML = "Bu sahə boş ola bilməz";
        return false;
    }
    else{
        surnameError.style.visibility = "hidden";
        surname.style.borderColor = "green";
    }
    if(email.value === ""){
        emailError.style.visibility = "visible";
        email.style.borderColor = "red";
        emailError.innerHTML = "Bu sahə boş ola bilməz";
        return false;
    }
    else if(!isValidEmail(email.value)) {
        emailError.style.visibility = "visible";
        email.style.borderColor = "red";
        emailError.innerHTML = "Zəhmət olmasa düzgün email daxil edin";
        return false;
    }
    else{
        emailError.style.visibility = "hidden";
        email.style.borderColor = "green";
    }
    if(number.value === ""){
        numberError.style.visibility = "visible";
        number.style.borderColor = "red";
        numberError.innerHTML = "Bu sahə boş ola bilməz";
        return false;
    }
    else{
        numberError.style.visibility = "hidden";
        number.style.borderColor = "green";
    }
    if(message.value === ""){
        messageError.style.visibility = "visible";
        message.style.borderColor = "red";
        messageError.innerHTML = "Bu sahə boş ola bilməz";
        return false;
    }
    else{
        messageError.style.visibility = "hidden";
        message.style.borderColor = "green";
    }
}

function isValidEmail(email){
    return /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}
