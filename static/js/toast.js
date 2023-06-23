/**
 * [Toast functionality
 * Credit: Code Institute project Boutique Ado and Bootstrap Toasts demo ]
 */

document.addEventListener('DOMContentLoaded', function () {
    // toasts functionality
    var toastElements = document.querySelectorAll('.toast');
    toastElements.forEach(function (toastElement) {
        let option = {
            animation: true,
            autohide: true,
            delay: 5000,
        };
      var toast = new bootstrap.Toast(toastElement, option);
      toast.show();
    });

  // Updates the copyright year in footer with the current year
  const year = document.querySelector('#current-year');
  year.innerHTML = new Date().getFullYear();

});

