function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("collapsed");
}

function toggleSunflowerMode() {
  const body = document.body;
  const btn = document.querySelector(".sunflower-mode-btn");
  body.classList.toggle("sunflower-mode");
  btn.classList.toggle("active");

  if (body.classList.contains("sunflower-mode")) {
    createPetals();
  }
}

function createPetals() {
  const petals = ["🌻", "🌼", "🌺", "🌸"];
  for (let i = 0; i < 15; i++) {
    setTimeout(() => {
      const petal = document.createElement("div");
      petal.className = "petal";
      petal.textContent = petals[Math.floor(Math.random() * petals.length)];
      petal.style.left = Math.random() * 100 + "%";
      petal.style.animationDuration = Math.random() * 2 + 3 + "s";
      document.body.appendChild(petal);

      setTimeout(() => petal.remove(), 4000);
    }, i * 200);
  }
}

function completeActivity(element) {
  const checkbox = element.querySelector(".activity-checkbox");
  checkbox.innerHTML = "✓";
  checkbox.style.background = "linear-gradient(135deg, #FFD700, #FFA500)";
  checkbox.style.color = "#1a1a1a";

  // Animar florescimento
  const sunflower = document.createElement("div");
  sunflower.textContent = "🌻";
  sunflower.style.position = "fixed";
  sunflower.style.fontSize = "3rem";
  sunflower.style.left = element.getBoundingClientRect().left + "px";
  sunflower.style.top = element.getBoundingClientRect().top + "px";
  sunflower.style.zIndex = "10000";
  sunflower.style.pointerEvents = "none";
  sunflower.style.animation = "bloom 1s ease-out forwards";
  document.body.appendChild(sunflower);

  setTimeout(() => {
    element.style.opacity = "0.5";
    element.style.textDecoration = "line-through";
    sunflower.remove();
  }, 1000);
}

// Animação inicial das barras de progresso
window.addEventListener("load", () => {
  const fills = document.querySelectorAll(".progress-fill");
  fills.forEach((fill) => {
    const width = fill.style.width;
    fill.style.width = "0";
    setTimeout(() => {
      fill.style.width = width;
    }, 300);
  });
});