// Function to change the paragraph text when the button is clicked
function changeText() {
    document.getElementById("textParagraph").innerText = "The text has been changed using JavaScript!";
}

// Handle greeting form submission
document.getElementById("nameForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevents the page from refreshing
    let name = document.getElementById("nameInput").value;
    document.getElementById("greetingMessage").innerText = "Hello, " + name + "!";
});

// Array of favorite foods
let foods = ["Pizza", "Sushi", "Tacos", "Pasta", "Ice Cream"];
let foodList = document.getElementById("foodList");

// Loop through foods and add each to the unordered list
for (let i = 0; i < foods.length; i++) {
    let li = document.createElement("li");
    li.innerText = foods[i];
    foodList.appendChild(li);
}

// Show selected courses using an alert
function showCourses() {
    let courses = document.querySelectorAll('input[name="course"]:checked');
    let selectedCourses = [];

    // Collect values from checked boxes
    courses.forEach((checkbox) => {
        selectedCourses.push(checkbox.value);
    });

    // Alert the user with the selected courses
    alert("You have taken: " + selectedCourses.join(", "));
}

console.log("main.js loaded successfully!");
