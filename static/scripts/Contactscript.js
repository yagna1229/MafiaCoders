const container = document.querySelector('.container');

container.addEventListener('mousemove', (e) => {
    const { width, height, left, top } = container.getBoundingClientRect();
    const mouseX = e.clientX - left;
    const mouseY = e.clientY - top;

    // Calculate the X and Y offset in relation to the card's size
    const offsetX = (mouseX / width) * 2 - 1; // This will give values between -1 and 1
    const offsetY = (mouseY / height) * 2 - 1; // Same here for Y-axis

    // Apply 3D rotation based on the cursor's position
    container.style.transform = `rotateX(${offsetY * 15}deg) rotateY(${offsetX * 15}deg)`;
});

container.addEventListener('mouseleave', () => {
    // Reset the 3D transformation when the mouse leaves the card
    container.style.transform = 'rotateX(0deg) rotateY(0deg)';
});
