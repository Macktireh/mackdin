/* =================== Responsive navbar =================== */

try {
  const hamburger = document.querySelector(".nav-profil");
  const navMenu = document.querySelector(".list-box");

  hamburger.addEventListener("click", () => {
    // hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
  });
} catch (error) {}
