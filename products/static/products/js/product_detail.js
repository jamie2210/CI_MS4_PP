/**
 * Incrememnting and decrementing quantity
 * Credit: Code Institute project Boutique Ado
 */

// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue + 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue - 1);
   var itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
});

/**
 * Target correct sizing menu based on id
 */

var priceInput = document.getElementById('price-input');
var selectElement = document.getElementById('id_product_size');
var priceDisplay = document.getElementById('price-display');

if (selectElement !== null) {
    selectElement.addEventListener('change', function() {
        var selectedValue = selectElement.value;
        var optionPrice = getOptionPrice(selectedValue);

        priceDisplay.textContent = optionPrice;
        priceInput.value = optionPrice;
    });


    var getOptionPrice = function(value) {
        var itemPrice = selectElement.getAttribute('data-item-price');
        var prices = itemPrice.split(';').map(entry => entry.split(':'));

        for (var i = 0; i < prices.length; i++) {
            if (prices[i][0] === value) {
                return prices[i][1];
            }
        }
        return itemPrice;
    };
}

// Retrieve the price value from the hidden input field
var priceInput = document.getElementById('price-input');
var priceValue = priceInput.value;

// Store the price value in the session
sessionStorage.setItem('priceValue', priceValue);

/**
 * Create tooltip banner for favourties star icon depending
 * on if poster in favourites or not
 */
const addStar = document.querySelector('.add');
const removeStar = document.querySelector('.remove');
const toolOne = document.querySelector('.tool1');
const toolTwo = document.querySelector('.tool2');

// function to toggle visibility
function toggleVisibility(element, isVisible) {
    element.style.visibility = isVisible ? 'visible' : 'hidden';
}

// Event handler for mouseover events
const handleMouseOver = function (event) {
    const target = event.target;
    if (target === addStar) {
      toggleVisibility(toolOne, true);
    } else if (target === removeStar) {
      toggleVisibility(toolTwo, true);
    }
};

// Event handler for mouseout events
const handleMouseOut = function (event) {
    const target = event.target;
    if (target === addStar) {
      toggleVisibility(toolOne, false);
    } else if (target === removeStar) {
      toggleVisibility(toolTwo, false);
    }
};

// Attach the event listeners
document.addEventListener('mouseover', handleMouseOver);
document.addEventListener('mouseout', handleMouseOut);


// Add free delivery banner
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("delivery-banner").style.display = "block";
});
