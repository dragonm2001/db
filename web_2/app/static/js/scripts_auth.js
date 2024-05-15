function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    const passwordToggle = document.querySelector('.password-toggle');
    const isActive = passwordToggle.classList.contains('active');

    if (isActive) {
        passwordInput.type = 'password';
    } else {
        passwordInput.type = 'text';
    }

    passwordToggle.classList.toggle('active');
}