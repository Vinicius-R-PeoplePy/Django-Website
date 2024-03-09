// common.js
function toggleForm(formName) {
    var loginContainer = document.getElementById('login-container');
    var signupContainer = document.getElementById('signup-container');

    if (formName === 'signup') {
        loginContainer.style.display = 'none';
        signupContainer.style.display = 'block';
    } else {
        loginContainer.style.display = 'block';
        signupContainer.style.display = 'none';
    }
}

function submitRegistrationForm() {
    var form = document.getElementById('registration-form');
    var formData = new FormData(form);

    fetch('/register/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => {
        if (response.ok) {
            // Optionally, show a success message or do other actions
            console.log('Registration successful');
            // Clear form fields
            form.reset();
            // Redirect to the login page
            window.location.href = "/";
        } else {
            console.error('Failed to create account.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
