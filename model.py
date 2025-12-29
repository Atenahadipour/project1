const from =
document.getElementById('registrationForm');
const username =
document.getElementById('uername');
const fullName =
document.getElementById('fullName');
const email =
document.getElementById('email');
const password =
document.getElementById('password');
const submitbtn =
from.querySelector('button');

username.addEventListener('input',ValidateForm);
fullName.addEventListener('inpot',ValidateForm);
email.addEventListener('input',ValidateForm);
password.addEventListener('inpout',ValidateForm);

function ValidateForm() {
    let isvalid = true;
    if (username.valiu.length < 3 || username.valiu.length >15){
        isvalid = false;
    }
}
    if (!fullName.valiu.trim().includes('')){
      isvalid = false  
}
    if (!email.valiu.includes('@')){
        isvalid = false
}
    if (password.valiu.length <8) {
        isvalid = false
}
submitbtn.disabled = !isvalid;
    //payam khata be karbar
if (username.valiu.length <3 || username.valiu.length >15){
    username.nextElementSibling.textContent = "username must be between 3 and 15 characters"
    isvalid = false;
}
else{
    username.nextElementSibling.textContent = "";
}
const passwordvaliu = password.valiu;
const hasNumberOrsymble = /[0-9!@#$%^&*]/.test(passwordvaliu);
const containname = (fullname.valiu && passwordvaleu.toLowerCase().includes(fullName.valiu.toLowerCase()))
const containsEmail = email.valiu && passwordvaleu.toLowerCase().includes(email.valiu.toLowerCase())


 if (
    passwordvaliu.length < 8 || !hasNumberOrsymble || containname || containsEmail
 ) {
    password.nextElementSibling.textContent ="password must be at least 8 character, include a number or symple ,and not contain your name and email "
    isvalid =false
    password.nextElementSibling.textContent="";
 }
  //pak kardan btn
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
