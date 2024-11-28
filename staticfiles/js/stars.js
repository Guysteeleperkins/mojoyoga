
document.addEventListener("DOMContentLoaded", function () {
    // Find all elements with the 'star-rating' class
    const starRatings = document.querySelectorAll('.star-rating');

    starRatings.forEach(function (starRating) {
        // Get the rating value from the data-rating attribute
        const rating = parseInt(starRating.getAttribute('data-rating'));

        // Clear any existing stars
        starRating.innerHTML = '';

        // Generate stars (5 total)
        for (let i = 1; i <= 5; i++) {
            if (i <= rating) {
                // Filled star
                starRating.innerHTML += '<i class="fas fa-star"></i>';
            } else {
                // Empty star
                starRating.innerHTML += '<i class="far fa-star"></i>';
            }
        }
    });
});