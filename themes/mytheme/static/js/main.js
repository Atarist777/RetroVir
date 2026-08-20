// Подсветка активной ссылки в меню
document.addEventListener('DOMContentLoaded', function() {
    const currentLocation = location.pathname;
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        // Убираем якорь у dropdown ссылки
        if (link.getAttribute('href') !== '#' && link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });
});