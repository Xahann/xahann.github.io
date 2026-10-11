(() => {
  const cards = Array.from(document.querySelectorAll("[data-photo-card]"));
  if (!cards.length) return;

  const filterButtons = Array.from(document.querySelectorAll("[data-filter]"));
  const searchInput = document.querySelector("[data-photo-search]");
  const galleryTitle = document.querySelector("[data-gallery-title]");
  const visibleCount = document.querySelector("[data-visible-count]");
  const noResults = document.querySelector("[data-no-results]");
  const inspectorImage = document.querySelector("[data-inspector-image]");
  const inspectorPreview = document.querySelector(".inspector-preview");
  const inspectorAction = document.querySelector("[data-inspector-action]");
  const inspectorInstagram = document.querySelector("[data-inspector-instagram]");
  const originalDialog = document.querySelector("[data-original-dialog]");
  const originalPreview = document.querySelector("[data-original-preview]");
  const originalTitle = document.querySelector("[data-original-title]");
  const inspectorTitle = document.querySelector("[data-inspector-title]");
  const inspectorCategory = document.querySelector("[data-inspector-category]");
  const inspectorDescription = document.querySelector("[data-inspector-description]");
  const selectedIndex = document.querySelector("[data-selected-index]");
  const grid = document.querySelector("[data-photo-grid]");
  let activeFilter = "all";

  const showOriginal = (image, title, alt) => {
    if (!image) return;

    originalPreview.src = image;
    originalPreview.alt = alt;
    originalTitle.textContent = title;
    originalDialog.showModal();
  };

  const updateGallery = () => {
    const query = searchInput.value.trim().toLocaleLowerCase();
    let count = 0;

    cards.forEach((card) => {
      const matchesFilter = activeFilter === "all" || card.dataset.category === activeFilter;
      const matchesQuery = !query || card.dataset.search.includes(query);
      card.hidden = !(matchesFilter && matchesQuery);
      if (!card.hidden) count += 1;
    });

    visibleCount.textContent = count;
    noResults.hidden = count > 0;
  };

  filterButtons.forEach((button) => {
    const filter = button.dataset.filter;
    const count = cards.filter((card) => filter === "all" || card.dataset.category === filter).length;
    const countNode = document.querySelector(`[data-filter-count="${filter}"]`);
    if (countNode) countNode.textContent = count;

    button.addEventListener("click", () => {
      activeFilter = filter;
      filterButtons.forEach((item) => {
        const active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", String(active));
      });
      galleryTitle.textContent = button.dataset.filterLabel;
      updateGallery();
    });
  });

  searchInput.addEventListener("input", updateGallery);

  document.querySelectorAll("[data-photo-select], [data-select-photo]").forEach((button) => {
    button.addEventListener("click", () => {
      const index = Number(button.dataset.photoSelect || button.dataset.selectPhoto);
      const card = cards[index];
      const photo = card && card.querySelector("[data-photo-select]");
      if (!photo) return;

      document.querySelectorAll("[data-photo-select]").forEach((item) => {
        const selected = item === photo;
        item.classList.toggle("is-selected", selected);
        item.setAttribute("aria-pressed", String(selected));
      });
      document.querySelectorAll(".filmstrip-item").forEach((item) => {
        const selected = Number(item.dataset.selectPhoto) === index;
        item.classList.toggle("is-selected", selected);
        item.setAttribute("aria-pressed", String(selected));
      });
      document.querySelectorAll(".collection-item").forEach((item) => {
        item.classList.toggle("is-current", Number(item.dataset.selectPhoto) === index);
      });

      inspectorTitle.textContent = photo.dataset.title;
      inspectorCategory.textContent = photo.dataset.categoryLabel;
      inspectorDescription.textContent = photo.dataset.description;
      inspectorImage.alt = photo.dataset.alt;
      inspectorImage.hidden = !photo.dataset.image;
      inspectorPreview.classList.toggle("has-no-image", !photo.dataset.image);
      inspectorPreview.disabled = !photo.dataset.image;
      if (photo.dataset.image) inspectorImage.src = photo.dataset.image;
      inspectorPreview.setAttribute("aria-label", `View ${photo.dataset.title} at full quality`);
      inspectorPreview.dataset.originalImage = photo.dataset.originalImage || "";
      inspectorPreview.dataset.title = photo.dataset.title;
      inspectorPreview.dataset.alt = photo.dataset.alt;
      inspectorAction.dataset.originalImage = photo.dataset.originalImage || "";
      inspectorAction.dataset.title = photo.dataset.title;
      inspectorAction.dataset.alt = photo.dataset.alt;
      inspectorAction.disabled = !photo.dataset.originalImage;
      inspectorInstagram.hidden = !photo.dataset.instagramUrl;
      if (photo.dataset.instagramUrl) {
        inspectorInstagram.href = photo.dataset.instagramUrl;
      } else {
        inspectorInstagram.removeAttribute("href");
      }
      selectedIndex.textContent = index + 1;
    });
  });

  [inspectorPreview, inspectorAction].forEach((button) => {
    button.addEventListener("click", () => {
      showOriginal(button.dataset.originalImage, button.dataset.title, button.dataset.alt);
    });
  });

  document.querySelector("[data-original-close]").addEventListener("click", () => originalDialog.close());
  originalDialog.addEventListener("click", (event) => {
    if (event.target === originalDialog) originalDialog.close();
  });

  const viewToggle = document.querySelector("[data-view-toggle]");
  viewToggle.addEventListener("click", () => {
    const compact = grid.classList.toggle("is-compact");
    viewToggle.setAttribute("aria-pressed", String(compact));
    viewToggle.setAttribute("aria-label", compact ? "Switch to comfortable view" : "Switch to compact view");
  });

  updateGallery();
})();
