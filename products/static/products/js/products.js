/**
 * Product sorting/image updates
 * Credit: Code Institute project Boutique Ado
 */
$('.arrow-button').click(function(e) {
    window.scrollTo(0,0);
});
$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);
    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
        window.location.replace(currentUrl);
    }
});


/** 
 * Event listener to stop 'up-to-top' arrow
 * button scroll beyond the footer
 * Hides button at top of page and displays once scrolled passed 1000px
 */

window.addEventListener('scroll', function() {
    let button = document.querySelector('.arrow-button');

    if (!button) {
        return; // Exit the function if the button is not present
    }

    let footer = document.querySelector('footer');
    let footerOffset = footer.offsetTop; // gets distance between footer and closest ancestor
    let scrollPosition = document.documentElement.scrollTop; // gets current scroll position of page
    
    if (scrollPosition > 1000) {
        button.style.display = "block";
        button.classList.add('fade-in');
        button.classList.remove('fade-out');
    } else {
        button.style.display = "none";
        button.classList.remove('fade-in');
        button.classList.add('fade-out');
    }

    if (scrollPosition + window.innerHeight >= footerOffset - 20) {
        // Button reached or passed the footer
        var distanceToFooter = (scrollPosition + window.innerHeight) - footerOffset + 20; // calculates distance between button and footer
        var adjustedBottom = Math.max(20, distanceToFooter); // ensures distance between button and footer is 20px
        button.style.bottom = adjustedBottom + 'px';
    } else {
        // Button is above the footer
        button.style.bottom = '20px';
    }

});

/** 
 * Set File name display for new image uploads
 * Credit: Code Institute project Boutique Ado
 */
$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

$('#new-image2').change(function() {
    var file = $('#new-image2')[0].files[0];
    $('#filename2').text(`Image will be set to: ${file.name}`);
});

/** 
 * Disables and hides new-image2 url and input unless new-image
 * has image uploaded
 */
document.addEventListener('DOMContentLoaded', function() {
    const newImageInput = document.getElementById('new-image');
    const newImage2Input = document.getElementById('new-image2');
    const imageButton = document.getElementById('image2-button');
    const imageUrl = document.getElementById('div_id_image2_url');
  
    newImageInput.addEventListener('change', function() {
        if (!newImageInput) {
            return; // Exit the function if the newImageInput is not present
        }
        if (newImageInput.value) {
            newImage2Input.disabled = false;
            imageButton.hidden = false;
            imageUrl.hidden = false;
        } else {
            newImage2Input.disabled = true;
            imageButton.hidden = true;
            imageUrl.hidden = true;
        }
    });
  
    // Disable / hide new-image2 and url initially if new-image is empty
    if (!newImageInput.value) {
      newImage2Input.disabled = true;
      imageButton.hidden = true;
      imageUrl.hidden = true;
    }
  });