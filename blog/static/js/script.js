/**
 * WEBSITE: https://themefisher.com
 * TWITTER: https://twitter.com/themefisher
 * FACEBOOK: https://www.facebook.com/themefisher
 * GITHUB: https://github.com/themefisher/
 */

(function ($) {
  "use strict";

  $(window).on("load", function () {
    // PreLoader Init
    function preLoader() {
      $("body").addClass("loaded");
      $(".preloader-wrapper").addClass("loaded");
    }
    preLoader();
  });

  $(document).ready(function () {
    // navbarToggle Init
    function navbarToggle() {
      $(".nav-toggle").on("click", function () {
        $(".sidenav").toggleClass("show");
        $(".nav-toggle span").toggleClass("fa-times fa-bars");
        $(".nav-toggle-overlay").toggleClass("show");
      });
      $(".nav-toggle-overlay").on("click", function () {
        $(".sidenav").removeClass("show");
        $(".nav-toggle span").toggleClass("fa-bars fa-times");
        $(".nav-toggle-overlay").removeClass("show");
      });
    }
    navbarToggle();

    // form validation (only for this page)
    window.addEventListener(
      "load",
      function () {
        var forms = document.getElementsByClassName("needs-validation");
        var validation = Array.prototype.filter.call(forms, function (form) {
          form.addEventListener(
            "submit",
            function (event) {
              if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
              }
              form.classList.add("was-validated");
            },
            false
          );
        });
      },
      false
    );
  });
})(jQuery);


function openWidget(evt, cityName) {
    // Declare all variables
    let i, tabcontent, tablinks;

    // Get all elements with class="tab-content" and hide them
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tab-links" and remove the class "active"
    tablinks = document.getElementsByClassName("tab-links");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();


// comment form
function openForm(){
  let form = document.getElementById('comment-form');

  if (form.style.display === 'none') {
    // 👇️ this SHOWS the form
    form.style.display = 'block';
  } else {
    // 👇️ this HIDES the form
    form.style.display = 'none';
  }
}
