function toggleTextA() {
    var longText = document.querySelector(".long-text-a");
    var button = document.querySelector(".read-more-btn-a");
    var card = document.querySelector(".about-card-a");

    // Get the current display value of the longText element
    var currentDisplay = window.getComputedStyle(longText).display;

    // Toggle the display of the long text
    if (currentDisplay === "none") {
        longText.style.display = "block"; // Show the text
        button.innerHTML = "Read Less";
        card.classList.add("expanded-card-a");  // Add class to expand the card's height
    } else {
        longText.style.display = "none"; // Hide the text
        button.innerHTML = "Read More..";
        card.classList.remove("expanded-card-a");  // Remove class to reset card height
    }
}

function toggleTextB() {
    var longText = document.querySelector(".long-text-b");
    var button = document.querySelector(".read-more-btn-b");
    var card = document.querySelector(".about-card-b");

    // Get the current display value of the longText element
    var currentDisplay = window.getComputedStyle(longText).display;

    // Toggle the display of the long text
    if (currentDisplay === "none") {
        longText.style.display = "block"; // Show the text
        button.innerHTML = "Read Less";
        card.classList.add("expanded-card-b");  // Add class to expand the card's height
    } else {
        longText.style.display = "none"; // Hide the text
        button.innerHTML = "Read More..";
        card.classList.remove("expanded-card-b");  // Remove class to reset card height
    }
}