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
  const inspectorLink = document.querySelector("[data-inspector-link]");
  const inspectorAction = document.querySelector("[data-inspector-action]");
  const inspectorTitle = document.querySelector("[data-inspector-title]");
  const inspectorCategory = document.querySelector("[data-inspector-category]");
  const inspectorDescription = document.querySelector("[data-inspector-description]");
  const selectedIndex = document.querySelector("[data-selected-index]");
  const grid = document.querySelector("[data-photo-grid]");
  let activeFilter = "all";

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
      if (photo.dataset.image) inspectorImage.src = photo.dataset.image;
      inspectorLink.href = photo.dataset.url;
      inspectorAction.href = photo.dataset.url;
      selectedIndex.textContent = index + 1;
    });
  });

  const viewToggle = document.querySelector("[data-view-toggle]");
  viewToggle.addEventListener("click", () => {
    const compact = grid.classList.toggle("is-compact");
    viewToggle.setAttribute("aria-pressed", String(compact));
    viewToggle.setAttribute("aria-label", compact ? "Switch to comfortable view" : "Switch to compact view");
  });

  updateGallery();
})();
