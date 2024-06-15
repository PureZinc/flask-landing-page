document.addEventListener('DOMContentLoaded', () => {
    const menu = document.getElementById('nav-menu');
    const navLinks = document.querySelector('.nav-links');

    menu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
});
