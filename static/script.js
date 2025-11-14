document.getElementById("crimeForm").addEventListener("submit", function(e) {
    e.preventDefault();
    document.getElementById("status").textContent =
        "Your crime report has been submitted successfully!";
});
