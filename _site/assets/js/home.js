(() => {
  const carousel = document.querySelector("[data-home-carousel]");
  if (!carousel) return;

  const photosNode = carousel.querySelector("[data-carousel-photos]");
  const image = carousel.querySelector("[data-carousel-image]");
  const title = carousel.querySelector("[data-carousel-title]");
  const category = carousel.querySelector("[data-carousel-category]");
  const count = carousel.querySelector("[data-carousel-count]");
  const toggle = carousel.querySelector("[data-carousel-toggle]");
  const photos = JSON.parse(photosNode.textContent);
  if (!photos.length) return;

  for (let index = photos.length - 1; index > 0; index -= 1) {
    const swapIndex = Math.floor(Math.random() * (index + 1));
    [photos[index], photos[swapIndex]] = [photos[swapIndex], photos[index]];
  }

  const selectedPhotos = photos.slice(0, Math.min(6, photos.length));
  let currentIndex = 0;
  let timer;
  let paused = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const showPhoto = (index) => {
    currentIndex = (index + selectedPhotos.length) % selectedPhotos.length;
    const photo = selectedPhotos[currentIndex];
    image.src = photo.image;
    image.alt = photo.alt;
    title.textContent = photo.title;
    category.textContent = photo.category;
    count.textContent = `${currentIndex + 1} / ${selectedPhotos.length}`;
  };

  const stopTimer = () => {
    window.clearInterval(timer);
    timer = undefined;
  };

  const startTimer = () => {
    stopTimer();
    if (!paused && selectedPhotos.length > 1) {
      timer = window.setInterval(() => showPhoto(currentIndex + 1), 6000);
    }
    toggle.textContent = paused ? "Play" : "Pause";
    toggle.setAttribute("aria-label", paused ? "Play slideshow" : "Pause slideshow");
  };

  carousel.querySelector("[data-carousel-previous]").addEventListener("click", () => {
    showPhoto(currentIndex - 1);
    startTimer();
  });
  carousel.querySelector("[data-carousel-next]").addEventListener("click", () => {
    showPhoto(currentIndex + 1);
    startTimer();
  });
  toggle.addEventListener("click", () => {
    paused = !paused;
    startTimer();
  });
  carousel.addEventListener("mouseenter", stopTimer);
  carousel.addEventListener("mouseleave", startTimer);
  carousel.addEventListener("focusin", stopTimer);
  carousel.addEventListener("focusout", (event) => {
    if (!carousel.contains(event.relatedTarget)) startTimer();
  });

  showPhoto(Math.floor(Math.random() * selectedPhotos.length));
  startTimer();
})();
