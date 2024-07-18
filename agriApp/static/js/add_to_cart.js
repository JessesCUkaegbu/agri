//  $('.add-to-cart').on("click", function() {
//         let quantity = $('#product_quantity').val();
//         let product_title = $('.product_title').val();
//         let product_id = $('.product_id').val();
//         let product_price = $('.current_price').text().replace('$', '');  // Remove the dollar sign
//         let product_image = $('.image').val();
//         let this_val = $(this);

//         $.ajax({
//             url: "/add_to_cart",
//             data: {
//                 'id': product_id,
//                 'qty': quantity,
//                 'product_title': product_title,
//                 'product_price': product_price,
//                 'product_image': product_image,
//             },
//             dataType: 'json',
//             beforeSend: function() {
//                 console.log("Product is still adding.....")
//             },
//             success: function(response) {
//                 this_val.html("Item added to cart");
//                 console.log("Product is added successfully");
//                 $('.cart-items-count').text(response.totalcartItem);
//                 // Update the total cost display if necessary
//                 $('.header__cart__price span').text('$' + response.total_cost);
//             },
//             // error: function(xhr, status, error) {
//             //     console.error("Error adding product: " + error);
//             // }
//         });
//     });


$(document).ready(function() {
    $('.add-to-cart').on('click', function() {
        let product_id = $(this).data('id');
        let product_title = $(this).data('title');
        let product_price = $(this).data('price');
        let product_image = $(this).data('image');
        let quantity = 1; // Default quantity is 1

        $.ajax({
            url: "/add_to_cart/",
            data: {
                'id': product_id,
                'qty': quantity,
                'product_title': product_title,
                'product_price': product_price,
                'product_image': product_image,
            },
            dataType: 'json',
            beforeSend: function() {
                console.log("Adding product to cart...");
            },
            success: function(response) {
                console.log("Product added to cart successfully");
                $('.cart-items-count').text(response.totalcartItem);

                // Display SweetAlert success message
                Swal.fire({
                    title: 'Success!',
                    text: 'Product added to cart successfully.',
                    icon: 'success',
                    confirmButtonText: 'OK'
                });
            },
            error: function(xhr, status, error) {
                console.log("Error adding product to cart:", error);

                // Display SweetAlert error message
                Swal.fire({
                    title: 'Error!',
                    text: 'There was an error adding the product to the cart.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        });
    });
});


// $(document).ready(function() {
//     $('.add-to-cart').on('click', function() {
//         let product_id = $(this).data('id');
//         let product_title = $(this).data('title');
//         let product_price = $(this).data('price').replace('$', ''); // Remove the dollar sign
//         let product_image = $(this).data('image');
//         let quantity = 1; // Default quantity is 1

//         $.ajax({
//             url: "/add_to_cart/",
//             data: {
//                 'id': product_id,
//                 'qty': quantity,
//                 'product_title': product_title,
//                 'product_price': product_price,
//                 'product_image': product_image,
//             },
//             dataType: 'json',
//             beforeSend: function() {
//                 console.log("Adding product to cart...");
//             },
//             success: function(response) {
//                 console.log("Product added to cart successfully");
//                 $('.cart-items-count').text(response.totalcartItem);

//                 // Update the total cost display if necessary
//                 $('.header__cart__price span').text('$' + response.total_cost);

//                 // Display SweetAlert success message
//                 Swal.fire({
//                     title: 'Success!',
//                     text: 'Product added to cart successfully.',
//                     icon: 'success',
//                     confirmButtonText: 'OK'
//                 });

//                 // Update the cart items in the header (if applicable)
//                 let cartItemsHtml = '';
//                 response.cart_items.forEach(item => {
//                     cartItemsHtml += `
//                         <li>${item.product.title} <span>${item.quantity} x $${item.product.price}</span></li>
//                     `;
//                 });
//                 $('.cart-items-list').html(cartItemsHtml); // Update the cart items list in the header
//             },
//             error: function(xhr, status, error) {
//                 console.log("Error adding product to cart:", error);

//                 // Display SweetAlert error message
//                 Swal.fire({
//                     title: 'Error!',
//                     text: 'There was an error adding the product to the cart.',
//                     icon: 'error',
//                     confirmButtonText: 'OK'
//                 });
//             }
//         });
//     });
// });