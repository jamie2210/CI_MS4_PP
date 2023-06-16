/**
 * [Toast functionality
 * Credit: Code Institute project Boutique Ado and Bootstrap Toasts demo ]
 */

document.addEventListener('DOMContentLoaded', function () {
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
  });