// Increase and Decrease Quantity
function quantity_inc() {
    var quantity = parseInt(document.getElementById('quantity').value);
    var total_units = parseInt(document.getElementById('units').innerText);
    if (quantity != total_units) {
        quantity += 1;
    }
    document.getElementById('quantity').value = quantity;
}

function quantity_dec() {
    var quantity = parseInt(document.getElementById('quantity').value);
    if (quantity != 1) {
        quantity -= 1;
    }
    document.getElementById('quantity').value = quantity;
}