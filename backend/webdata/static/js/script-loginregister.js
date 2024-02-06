const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const logitnBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

logitnBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

