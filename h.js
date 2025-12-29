/* Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Segoe UI", Tahoma, sans-serif;
}

/* Body */
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    color: #e5e7eb;
}

/* Container */
.container {
    background: linear-gradient(145deg, #0f172a, #111827);
    padding: 40px 50px;
    border-radius: 20px;
    width: 100%;
    max-width: 450px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.7);
    transition: transform 0.3s ease;
}

.container:hover {
    transform: translateY(-5px);
}

/* Form title */
h2 {
    text-align: center;
    margin-bottom: 25px;
    color: #38bdf8;
    letter-spacing: 1px;
    font-size: 28px;
}

/* Form group */
.form-group {
    margin-bottom: 20px;
}

/* Labels */
label {
    display: block;
    margin-bottom: 6px;
    font-weight: 600;
}

/* Inputs */
input {
    width: 100%;
    padding: 14px 16px;
    border-radius: 12px;
    border: 1px solid #1e293b;
    background: #111827;
    color: #e5e7eb;
    outline: none;
    font-size: 15px;
    transition: 0.3s;
    box-shadow: inset 0 2px 5px rgba(0,0,0,0.3);
}

input:focus {
    border-color: #38bdf8;
    box-shadow: 0 0 8px rgba(56,189,248,0.5);
}

/* Error messages */
.error-message {
    color: #f87171;
    font-size: 13px;
    margin-top: 5px;
    min-height: 18px;
}

/* Success message */
.success-message {
    color: #4ade80;
    text-align: center;
    margin-top: 15px;
    font-weight: bold;
}

/* Button */
button {
    width: 100%;
    padding: 14px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(135deg, #38bdf8, #2563eb);
    color: white;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 15px;
    box-shadow: 0 8px 20px rgba(56,189,248,0.4);
}

button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

button:hover:not(:disabled) {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(56,189,248,0.5);
}

/* Responsive */
@media (max-width: 480px) {
    .container {
        padding: 30px 25px;
    }
    h2 {
        font-size: 24px;
    }
}
