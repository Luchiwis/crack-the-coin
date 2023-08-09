// Get all elements and store them in an array
const elements = document.querySelectorAll(".capture");

// Set the initial focus index to the first element
let currentFocusIndex = 0;
let current_element = elements[currentFocusIndex];
current_element.classList.add("focused");

// gamepad variables
let gamepad;
let controllerIndex = 0;
let releasedButtons = {
  A: true,
  B: true,
  Up: true,
  Down: true,
  Left: true,
  Right: true,
};

function audioPlay(audioName) {
  audio = document.querySelector("#" + audioName + "_audio")
  audio.currentTime = 0;
  audio.play();
}

let lastPressedTimestamp = getCurrentTimestamp();
function getCurrentTimestamp() {
  return new Date().getTime();
}

window.addEventListener("gamepadconnected", (event) => {
  console.log("A gamepad connected:");
  console.log(event.gamepad);
  const gamepad = event.gamepad;
  controllerIndex = gamepad.index;
});

window.addEventListener("gamepaddisconnected", (event) => {
  console.log("A gamepad disconnected:");
  console.log(event.gamepad);
});

function backspace() {
  console.log("Backspace pressed");
  //check if is an input text and if it has some text
  if (
    current_element.tagName == "INPUT" &&
    current_element.type == "text" &&
    current_element.value.length > 0
  ) {
    current_element.value = current_element.value.slice(0, -1);
  }
  else if (current_element.value.length <= 0){
    audioPlay("error");
  }
}

function update() {
  gamepad = navigator.getGamepads()[controllerIndex];

  if (
    gamepad &&
    (!lastPressedTimestamp ||
      getCurrentTimestamp() - lastPressedTimestamp > 100)
  ) {
    if (gamepad.buttons[0].pressed && releasedButtons["A"]) {
      console.log("A pressed");
      current_element.click();

      releasedButtons["A"] = false;
    } else if (!gamepad.buttons[0].pressed) {
      releasedButtons["A"] = true;
    }

    if (gamepad.buttons[1].pressed && releasedButtons["B"]) {
      console.log("B pressed");
      backspace();
      releasedButtons["B"] = false;
    } else if (!gamepad.buttons[1].pressed) {
      releasedButtons["B"] = true;
    }

    if (gamepad.axes[0] > 0.5 && releasedButtons["Up"]) {
      console.log("Up pressed");
      currentFocusIndex--;
      audioPlay("chk");
      releasedButtons["Up"] = false;
    } else if (gamepad.axes[0] < 0.5) {
      releasedButtons["Up"] = true;
    }

    if (gamepad.axes[0] < -0.5 && releasedButtons["Down"]) {
      console.log("Down pressed");
      currentFocusIndex++;
      audioPlay("chk");
      releasedButtons["Down"] = false;
    } else if (gamepad.axes[0] > -0.5) {
      releasedButtons["Down"] = true;
    }

    if (gamepad.axes[1] > 0.5 && releasedButtons["Right"]) {
      console.log("Right pressed");
      audioPlay("chk");
      releasedButtons["Right"] = false;
    } else if (gamepad.axes[1] <= 0.5) {
      releasedButtons["Right"] = true;
    }

    if (gamepad.axes[1] < -0.5 && releasedButtons["Left"]) {
      console.log("Left pressed");
      audioPlay("chk");
      releasedButtons["Left"] = false;
    } else if (gamepad.axes[1] >= -0.5) {
      releasedButtons["Left"] = true;
    }

    // Add the 'focused' class to the new focused element
    if (currentFocusIndex < 0) {
      currentFocusIndex = elements.length - 1;
    } else if (currentFocusIndex >= elements.length) {
      currentFocusIndex = 0;
    }
    current_element.classList.remove("focused");
    current_element = elements[currentFocusIndex];
    current_element.classList.add("focused");
    current_element.focus();
  }
  requestAnimationFrame(update);
}

requestAnimationFrame(update);
