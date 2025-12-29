const form = document.getElementById('registrationForm');
const username = document.getElementById('username');
const fullName = document.getElementById('fullName');
const email = document.getElementById('email');
const password = document.getElementById('password');
const submitBtn = form.querySelector('button');

// اضافه کردن event listener برای هر input
username.addEventListener('input', validateForm);
fullName.addEventListener('input', validateForm);
email.addEventListener('input', validateForm);
password.addEventListener('input', validateForm);

function validateForm() {
    let isValid = true;

    // --- Username Validation ---
    if (username.value.length < 3 || username.value.length > 15) {
        username.nextElementSibling.textContent = "Username must be between 3 and 15 characters";
        isValid = false;
    } else if (!/^[a-zA-Z0-9]+$/.test(username.value)) {
        username.nextElementSibling.textContent = "Username can only contain letters and numbers";
        isValid = false;
    } else {
        username.nextElementSibling.textContent = "";
    }

    // --- Full Name Validation ---
    if (!/^[a-zA-Z]+\s[a-zA-Z]+/.test(fullName.value.trim())) {
        fullName.nextElementSibling.textContent = "Please enter your full name (first and last name)";
        isValid = false;
    } else {
        fullName.nextElementSibling.textContent = "";
    }

    // --- Email Validation ---
    if (!/^\S+@\S+\.\S+$/.test(email.value)) {
        email.nextElementSibling.textContent = "Please enter a valid email address";
        isValid = false;
    } else {
        email.nextElementSibling.textContent = "";
    }

    // --- Password Validation ---
    const passwordValue = password.value;
    const hasNumberOrSymbol = /[0-9!@#$%^&*]/.test(passwordValue);
    const containsName = fullName.value && passwordValue.toLowerCase().includes(fullName.value.toLowerCase());
    const containsEmail = email.value && passwordValue.toLowerCase().includes(email.value.toLowerCase());

    if (
        passwordValue.length < 8 ||
        !hasNumberOrSymbol ||
        containsName ||
        containsEmail
    ) {
        password.nextElementSibling.textContent = "Password must be at least 8 characters, include a number or symbol, and not contain your name or email";
        isValid = false;
    } else {
        password.nextElementSibling.textContent = "";
    }

    // فعال/غیرفعال کردن دکمه submit
    submitBtn.disabled = !isValid;
}

// --- Form Submission ---
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
