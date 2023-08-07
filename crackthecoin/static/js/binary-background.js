// Generate the binary code for the background
function generateBinaryCode() {
    const binaryChars = ['0', '1'];
    const binaryCodeLength = Math.floor(window.innerWidth); // Adjust the length as needed
    let binaryCode = '';
  
    for (let i = 0; i < binaryCodeLength; i++) {
      const randomBinaryChar = binaryChars[Math.floor(Math.random() * binaryChars.length)];
      binaryCode += randomBinaryChar;
    }
  
    return binaryCode;
  }
  
  // Create the binary hacker background
  function createBinaryBackground() {
    const binaryBackground = document.createElement('div');
    binaryBackground.classList.add('binary-background');
  
    const lines = Math.floor(window.innerHeight); // Adjust line count based on screen height
    for (let i = 0; i < lines; i++) {
      const binaryText = document.createElement('div');
      binaryText.classList.add('binary-text');
      binaryText.textContent = generateBinaryCode();
      binaryBackground.appendChild(binaryText);
    }
  
    document.body.appendChild(binaryBackground);
  }
  
  // Update the binary text
  function updateBinaryText() {
    const binaryTexts = document.querySelectorAll('.binary-text');
    binaryTexts.forEach((textElement) => {
      textElement.textContent = generateBinaryCode();
    });
  }
  
  // Call createBinaryBackground on page load
  window.addEventListener('load', createBinaryBackground);
  
  // Update the binary text every 3 seconds (adjust as needed)
  setInterval(updateBinaryText, 3000);