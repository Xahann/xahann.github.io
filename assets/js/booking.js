(() => {
  const form = document.querySelector("[data-booking-form]");
  if (!form) return;

  const error = form.querySelector("[data-booking-error]");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const recipient = form.dataset.recipient.trim();
    if (!recipient) {
      error.textContent = "Booking email is not configured yet. Please contact Xane through Instagram.";
      error.hidden = false;
      return;
    }

    const values = new FormData(form);
    const subject = `Photography booking inquiry — ${values.get("name")}`;
    const message = [
      `Name: ${values.get("name")}`,
      `Email: ${values.get("email")}`,
      `Project type: ${values.get("project")}`,
      `Preferred date: ${values.get("date") || "Flexible"}`,
      "",
      "Project details:",
      values.get("message")
    ].join("\n");
    window.location.href = `mailto:${recipient}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(message)}`;
  });
})();
