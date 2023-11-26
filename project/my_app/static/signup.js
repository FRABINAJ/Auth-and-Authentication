nameValue = document.getElementById("name")
emailValue = document.getElementById("email")
passwordValue = document.getElementById("password")

nameError = document.getElementById("name-error")
emailError = document.getElementById("email-error")
passwordError = document.getElementById("password-error")

btn = document.getElementById("btn-id")

// NAME VALIDATION

function validateName() {
    const name = nameValue.value;

    if (name.length == 0) {
        nameError.textContent = "Name is required";
        btn.disabled = true;
        return false;
    }

    if (!name.match(/^[A-Za-z]{3,}\s{1,}[a-zA-Z]+$/))// \s means blank space
    {
        nameError.textContent = `Enter full name`;
        btn.disabled = true;
        return false;
    }

    nameError.innerHTML = `<i class='fas fa-check-circle icon'></i>`;
    btn.disabled = false;
    return true;
}

nameValue.addEventListener("keyup", validateName);
nameValue.addEventListener("blur", validateName);

// EMAIL VALIDATION

function validateEmail() {
    const email = emailValue.value;

    if (email.length == 0) {
        emailError.textContent = "Email is required"
        btn.disabled = true
        return false
    }
    if (!email.match(/^[a-zA-Z0-9\._\-]{3,}[@][a-zA-Z]+[\.][a-z]{2,4}$/)) {
        emailError.textContent = "Wrong email"
        btn.disabled = true
        return false
    }
    emailError.innerHTML = `<i class='fas fa-check-circle icon'></i>`;
    btn.disabled = false
    return true
}

emailValue.addEventListener("keyup", validateEmail);
emailValue.addEventListener("blur", validateEmail);

// Password Error
function validatePassword() {
    const password = passwordValue.value;
    if (password == 0) {
        passwordError.textContent = "Password is required"
        btn.disabled = true
        return false
    }
    if (!password.match(/^[A-Za-z1-9]{6,}$/)) {
        passwordError.textContent = "Password must be morethan 6 characters"
        btn.disabled = true
        return false
    }
    passwordError.innerHTML = `<i class='fas fa-check-circle icon'></i>`;
    btn.disabled = false
    return true
}

passwordValue.addEventListener("keyup", validatePassword);
passwordValue.addEventListener("blur", validatePassword);
