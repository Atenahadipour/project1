const form = document.getElementById('registrationForm');
const username = document.getElementById('username');
const fullName = document.getElementById('fullName');
const email = document.getElementById('email');
const password = document.getElementById('password');
const submitBtn = form.querySelector('button');

username.addEventListener('input', validateForm);
fullName.addEventListener('input', validateForm);
email.addEventListener('input', validateForm);
password.addEventListener('input', validateForm);

function validateForm() {
    let isValid = true;

    // Username
    if (username.value.length < 3 || username.value.length > 15) {
        username.nextElementSibling.textContent = "Username must be 3-15 characters";
        isValid = false;
    } else if (!/^[a-zA-Z0-9]+$/.test(username.value)) {
        username.nextElementSibling.textContent = "Username can only contain letters and numbers";
        isValid = false;
    } else {
        username.nextElementSibling.textContent = "";
    }

    // Full Name
    if (!/^[a-zA-Z]+\s[a-zA-Z]+$/.test(fullName.value.trim())) {
        fullName.nextElementSibling.textContent = "Enter first and last name";
        isValid = false;
    } else {
        fullName.nextElementSibling.textContent = "";
    }

    // Email
    if (!/^\S+@\S+\.\S+$/.test(email.value)) {
        email.nextElementSibling.textContent = "Enter a valid email";
        isValid = false;
    } else {
        email.nextElementSibling.textContent = "";
    }

    // Password
    const pw = password.value;
    const hasNumberOrSymbol = /[0-9!@#$%^&*]/.test(pw);
    const containsName = fullName.value && pw.toLowerCase().includes(fullName.value.toLowerCase());
    const containsEmail = email.value && pw.toLowerCase().includes(email.value.toLowerCase());

    if (pw.length < 8 || !hasNumberOrSymbol || containsName || containsEmail) {
        password.nextElementSibling.textContent = "Password must be 8+, include number/symbol, not contain name/email";
        isValid = false;
    } else {
        password.nextElementSibling.textContent = "";
    }

    submitBtn.disabled = !isValid;
}

// Form submit
form.addEventListener('submit', function(e) {
    e.preventDefault();
    console.log({
        username: username.value,
        fullName: fullName.value,
        email: email.value,
        password: "*******"
    });
    alert("Registration successful!");
    form.reset();
    submitBtn.disabled = true;
});
