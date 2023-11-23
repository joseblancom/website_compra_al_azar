function deleteCart(cartId) {
    fetch("/delete-cart", {
        method: 'POST',
        body: JSON.stringify({cartId: cartId})
    }).then((_res) => {
        window.location.href = "/cart";
    });
}