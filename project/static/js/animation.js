addToCartButton = document.querySelectorAll(".add-to-cart-button");

document.querySelectorAll('.add-to-cart-button').forEach(function(addToCartButton) {
    addToCartButton.addEventListener('click', function() {
        addToCartButton.classList.add('added');
        setTimeout(function(){
            addToCartButton.classList.remove('added');
        }, 2000);
    });
});






// https://bootstrap-menu.com/detail-autohide.html
document.addEventListener("DOMContentLoaded", function(){

  el_autohide = document.querySelector('.autohide');
  
  // add padding-top to bady (if necessary)
  navbar_height = document.querySelector('.navbar').offsetHeight;
  document.body.style.paddingTop = navbar_height + 'px';

  if(el_autohide){
    var last_scroll_top = 0;
    window.addEventListener('scroll', function() {
          let scroll_top = window.scrollY;
         if(scroll_top < last_scroll_top) {
              el_autohide.classList.remove('scrolled-down');
              el_autohide.classList.add('scrolled-up');
          }
          else {
              el_autohide.classList.remove('scrolled-up');
              el_autohide.classList.add('scrolled-down');
          }
          last_scroll_top = scroll_top;
    }); 
    // window.addEventListener
  }
  // if

}); 




// search

$(document).ready(function() {

	$(".fa-search").click(function() {
	   $(".togglesearch").toggle();
	   $("input[type='text']").focus();
	 });

});

// show password or not


function showSignUpConfirmPassword(){
    var newpassword1 = document.getElementById("id_password1");
    var newpassword2 = document.getElementById("id_password2");
    show2Password(newpassword1,newpassword2);
}

function showResetConfirmPassword(){
    var password1 = document.getElementById("id_new_password1");
    var password2 = document.getElementById("id_new_password2");
    show2Password(password1,password2);
}



function show2Password(pass1,pass2){
    
    if(pass1.type && pass2.type === "password"){
        pass1.type = "text";
        pass2.type = "text";
    }
    else{
        pass1.type = "password";
        pass2.type = "password";
    }
}

function showPassword(){
    var mypassinput = document.getElementById("id_password");
    return mypassinput.type === "password"? mypassinput.type = "text":mypassinput.type = "password";

}

