// ... (start of your JS code)

// Handle crime report form submission
const form = document.getElementById("crimeForm");
if (form) {
  form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const status = document.getElementById("status");
      status.textContent = "Submitting report...";
      status.style.color = "#00eaff";

      const formData = new FormData(form);
      const data = Object.fromEntries(formData);

      try {
          const response = await fetch("/submit", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(data)
          });

          const result = await response.json();

          if (result.success) {
              // --- CHANGED: Now redirects to /index ---
              status.textContent = "Report submitted successfully! Submit another report below.";
              status.style.color = "#00ffb0";

              // Clear the form after submission
              form.reset();

              // No redirect needed if staying on the same page, but we'll remove the success message after a delay
              setTimeout(() => {
                  status.textContent = "";
              }, 3000);

          } else {
              status.textContent = "Submission failed. Try again.";
              status.style.color = "#ff6b6b";
          }
      } catch (error) {
          status.textContent = "Error connecting to server.";
          status.style.color = "#ff6b6b";
      }
  });
}

// ... (rest of your JS code remains the same)