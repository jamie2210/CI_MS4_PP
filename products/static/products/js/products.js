/**
 * [Product sorting/image updates
 * Credit: Code Institute project Boutique Ado ]
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


/** Event listener to stop up to top arrow
 * button scroll beyond the footer */

window.addEventListener('scroll', function() {
    let button = document.querySelector('.arrow-button');
    let footer = document.querySelector('footer');
    let footerHeight = footer.offsetHeight; // return the height of the footer
    let footerOffset = footer.offsetTop; // gets distance between footer and closest ancestor
    let scrollPosition = document.documentElement.scrollTop; // gets current scroll position of page

    if (scrollPosition + window.innerHeight >= footerOffset - 20) {
        // Button reached or passed the footer
        var distanceToFooter = (scrollPosition + window.innerHeight) - footerOffset + 20; // calculates distance between butt0n and footer
        var adjustedBottom = Math.max(20, distanceToFooter); // ensures distance between button and footer is 20px
        button.style.bottom = adjustedBottom + 'px';
    } else {
        // Button is above the footer
        button.style.bottom = '20px';
    }

})