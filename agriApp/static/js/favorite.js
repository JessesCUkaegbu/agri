 // Add to favorites functionality
 $('.add-to-favorites').on("click", function() {
    let product_id = $(this).data('product-id');

    $.ajax({
        url: "/add_to_favorites",
        data: {
            'id': product_id,
            // You can add other necessary data here
        },
        dataType: 'json',
        beforeSend: function() {
            console.log("Adding to favorites.....");
        },
        success: function(response) {
            console.log("Product is added to favorites successfully");
            $('.favorites-count').text(response.totalFavoritesItem);
            Swal.fire({
                icon: 'success',
                title: 'Added to favorites',
                showConfirmButton: false,
                timer: 1500
            });
        }
    });
});