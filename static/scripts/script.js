function ToggleEvent() {
    const sidebar = document.getElementById('sidebar')
    const content = document.querySelector('.main-content');
    // Toggelbar in action
    // if(sidebar.style.left === '-250px'){
    //     sidebar.style.left = '0px';
    // }
    // else{
    //     sidebar.style.left = '-250px';
    // }
    // Toggle between open and closed states with animation
    if (sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
        sidebar.classList.add('closed');
        content.classList.remove('shifted');
    } else {
        sidebar.classList.remove('closed');
        sidebar.classList.add('open');
        content.classList.add('shifted');
    }
}
