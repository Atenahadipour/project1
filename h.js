<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Registration Form</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- CSS -->
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>

    <div class="container">
        <form id="registrationForm" novalidate>

            <h1>User Registration</h1>

            <!-- Username -->
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username">
                <small class="error-message"></small>
            </div>

            <!-- Full Name -->
            <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName">
                <small class="error-message"></small>
            </div>

            <!-- Email -->
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email">
                <small class="error-message"></small>
            </div>

            <!-- Password -->
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password">
                <small class="error-message"></small>
            </div>

            <!-- Submit Button -->
            <button type="submit" id="submitBtn" disabled>
                Register
            </button>

            <!-- Success Message -->
            <p class="success-message" id="successMessage"></p>

        </form>
    </div>

    <!-- JavaScript -->
    <script src="js/script.js"></script>

</body>
</html>
