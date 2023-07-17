document.addEventListener('DOMContentLoaded', () => {
  // Get all "navbar-burger" elements
  const navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
  // Check if there are any navbar burgers
  if (navbarBurgers.length > 0) {
    // Add a click event listener to each burger
    navbarBurgers.forEach((navbarBurger) => {
      navbarBurger.addEventListener('click', () => {
        // Get the target from the "data-target" attribute
        const target = navbarBurger.dataset.target;
        const menu = document.getElementById(target);
  
        // Toggle the "is-active" class on both the burger and the menu
        navbarBurger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
      });
    });
  }
});
