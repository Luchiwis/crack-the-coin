// Get all elements and store them in an array
const elements = document.querySelectorAll(".capture");

// Set the initial focus index to the first element
let currentFocusIndex = 0;
let cooldown = false;
const cooldownTime = 500; // Set the cooldown time in milliseconds
let current_element = elements[currentFocusIndex];
current_element.classList.add("focused");

document.addEventListener("keydown", (event) => {
  const key = event.key;

  if (cooldown) {
    return; // If cooldown is active, don't do anything
  }

  // Remove the 'focused' class from the currently focused element
  current_element.classList.remove("focused");

  // Update the currentFocusIndex based on the arrow key pressed
  if (key === "ArrowDown" && currentFocusIndex < elements.length - 1) {
    currentFocusIndex++;
    current_element = elements[currentFocusIndex];
  } else if (key === "ArrowUp" && currentFocusIndex > 0) {
    currentFocusIndex--;
    current_element = elements[currentFocusIndex];
  } else {
    return;
  }

  // Add the 'focused' class to the new focused element
  current_element.classList.add("focused");
  setTimeout(() => {current_element.scrollIntoView({ behavior: "smooth" });}, 200);

  if (current_element.classList.contains("acc-item")) {
    current_element.querySelector("button").click();
    current_element.querySelector("input").focus();
  } else {
    current_element.focus();
  }

  cooldown = true;
  setTimeout(() => {
    cooldown = false;
  }, cooldownTime);

  console.log(currentFocusIndex);
});

// ------------------------------
