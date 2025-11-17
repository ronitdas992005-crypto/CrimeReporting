// Toggle Password Visibility
function togglePassword() {
    const passField = document.getElementById("password");
    passField.type = passField.type === "password" ? "text" : "password";
}

// Form Validation (Basic)
function validateForm() {
    const fullName = document.getElementById("full_name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (fullName === "" || email === "" || password === "") {
        alert("All fields are required!");
        return false;
    }

    if (!email.includes("@")) {
        alert("Enter a valid email.");
        return false;
    }

    return true;
}

// Logout confirmation popup
function confirmLogout() {
    return confirm("Are you sure you want to log out?");
}

// Upload preview (optional future feature)
function previewImage(event) {
    const file = event.target.files[0];
    const preview = document.getElementById("preview");

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
    }
}