// Form validation on Registration Page
document.addEventListener("DOMContentLoaded", function() {
    const registerForm = document.querySelector("form");
    registerForm.addEventListener("submit", function(event) {
        const firstName = document.querySelector('input[name="first_name"]');
        const voterId = document.querySelector('input[name="voter_id"]');
        const aadharId = document.querySelector('input[name="aadhar_id"]');
        const email = document.querySelector('input[name="email"]');
        
        // Validation checks
        if (!firstName.value || !voterId.value || !aadharId.value || !email.value) {
            alert("Please fill in all fields!");
            event.preventDefault();  // Prevent form submission
        } else if (!validateEmail(email.value)) {
            alert("Please enter a valid email!");
            event.preventDefault();
        }
    });

    function validateEmail(email) {
        const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return regex.test(email);
    }
});
