// Get all elements and store them in an array
const elements = document.querySelectorAll(".capture");

// Set the initial focus index to the first element
let currentFocusIndex = 0;
let cooldown = false;
const cooldownTime = 200; // Set the cooldown time in milliseconds
let current_element = elements[currentFocusIndex];
current_element.classList.add("focused");

document.addEventListener("keydown", (event) => {
  const key = event.key;

  if (cooldown) {
    return; // If cooldown is active, don't do anything
  }


  // Update the currentFocusIndex based on the arrow key pressed
  if ((key === "ArrowDown" || key === "ArrowRight") && currentFocusIndex < elements.length - 1) {
    // Remove the 'focused' class from the currently focused element
    current_element.classList.remove("focused");
    currentFocusIndex++;
    current_element = elements[currentFocusIndex];
  } else if ((key === "ArrowUp" || key === "ArrowLeft") && currentFocusIndex > 0) {
    // Remove the 'focused' class from the currently focused element
    current_element.classList.remove("focused");
    currentFocusIndex--;
    current_element = elements[currentFocusIndex];
  } else if (key === "Enter") {
    // If the user presses Enter, click the currently focused element
    current_element.click();
  }else {
    return;
  }

  // Add the 'focused' class to the new focused element
  current_element.classList.add("focused");
  setTimeout(() => {current_element.scrollIntoView({ behavior: "smooth" });}, 200);


  current_element.focus();


  cooldown = true;
  setTimeout(() => {
    cooldown = false;
  }, cooldownTime);

  console.log(currentFocusIndex);
});

// ------------------------------
