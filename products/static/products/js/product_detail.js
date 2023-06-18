/**
 * [Incrememnting and decrementing quantity
 * Credit: Code Institute project Boutique Ado ]
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

document.addEventListener('DOMContentLoaded', function() {
    const satinPrint = document.querySelector('[data-product-price="19.99"]');
    const satinForm = document.querySelector('.satin-form');
  
    const mattPrint = document.querySelector('[data-product-price="14.99"]');
    const mattForm = document.querySelector('.matt-form');
  
    // Check if the satin-print element exists
    if (satinPrint) {
        satinForm.style.display = 'block';
        mattForm.style.display = 'none';
    }
  
    // Check if the matt-print element exists
    if (mattPrint) {
        mattForm.style.display = 'block';
        satinForm.style.display = 'none';
    }
});

/**
 * Update price that reflects size selected
 */
const selectElement1 = document.getElementById('id_product_size1');
const selectElement2 = document.getElementById('id_product_size2');
const priceDisplay = document.getElementById('price-display');

selectElement1.addEventListener('change', function(){
    const selectedValue = selectElement1.value;
    priceDisplay.textContent = `£${getOptionPrice1(selectedValue)}`;
});

function getOptionPrice1(value) {
    const itemPrice = selectElement1.getAttribute('data-item-price');
    const prices = itemPrice.split(';').map(entry => entry.split(':'));

    for (const [optionValue, price] of prices) {
        if (optionValue === value) {
          return price;
        }
      }
    return itemPrice
}

selectElement2.addEventListener('change', function(){
    const selectedValue = selectElement2.value;
    priceDisplay.textContent = `£${getOptionPrice2(selectedValue)}`;
});

function getOptionPrice2(value) {
    const itemPrice = selectElement2.getAttribute('data-item-price');
    const prices = itemPrice.split(';').map(entry => entry.split(':'));

    for (const [optionValue, price] of prices) {
        if (optionValue === value) {
          return price;
        }
      }
    return itemPrice
}