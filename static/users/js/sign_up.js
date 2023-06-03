const form = document.querySelector("form");
const inputs = document.querySelectorAll(".form-control");
const lang = document.getElementById("language_code").value;
// const progressBar = document.getElementById("progress-bar");
let firstname, lastname, email, password, confirmPass;

const errorDisplay = (tag, message, valid) => {
  const container = document.querySelector("." + tag + "-container");
  // console.log(container);
  const span = document.querySelector("." + tag + "-container > span");

  if (!valid) {
    container.classList.add("error");
    span.textContent = message;
  } else {
    container.classList.remove("error");
    span.textContent = message;
  }
};

const firstnamechecker = (input_name, value) => {
  if (value.length > 0 && (value.length < 2 || value.length > 50)) {
    errorDisplay(
      input_name,
      lang === "fr"
        ? "Le prénom doit contenir entre 2 et 50 caractères"
        : "The first name must contain between 2 and 50 characters."
    );
    firstname = null;
  } else if (!value.match(/^[a-zA-Z -]*$/)) {
    errorDisplay(
      input_name,
      lang === "fr"
        ? "Le prénom ne doit pas contenir de caractères spéciaux"
        : "The first name must not contain any special characters."
    );
    firstname = null;
  } else {
    errorDisplay(input_name, "", true);
    firstname = value;
  }
};

const lastnamechecker = (input_name, value) => {
  if (value.length > 0 && (value.length < 2 || value.length > 50)) {
    errorDisplay(
      input_name,
      lang === "fr"
        ? "Le nom doit contenir entre 2 et 50 caractères"
        : "The last name must contain between 2 and 50 characters."
    );
    lastname = null;
  } else if (!value.match(/^[a-zA-Z -]*$/)) {
    errorDisplay(
      input_name,
      lang === "fr"
        ? "Le nom ne doit pas contenir de caractères spéciaux"
        : "The last name must not contain any special characters."
    );
    lastname = null;
  } else {
    errorDisplay(input_name, "", true);
    lastname = value;
  }
};

const emailChecker = (input_name, value) => {
  if (!value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/)) {
    errorDisplay(
      "email",
      lang === "fr" ? "L'e-mail n'est pas valide" : "Invalid e-mail"
    );
    email = null;
  } else {
    errorDisplay(input_name, "", true);
    email = value;
  }
};

const passwordChecker = (input_name, value) => {
  //   progressBar.classList = "";

  if (
    !value.match(
      /^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$/
    )
  ) {
    errorDisplay(
      input_name,
      lang === "fr"
        ? "Le mot de passe doit contenir au moins 8 caractères, une lettre majuscule, un chiffre et un caractère spécial."
        : "The password must contain at least 8 characters, a capital letter, a number and a special character."
    );
    // progressBar.classList.add("progressRed");
    password = null;
  } else if (value.length < 12) {
    // progressBar.classList.add("progressBlue");
    errorDisplay(input_name, "", true);
    password = value;
  } else {
    // progressBar.classList.add("progressGreen");
    errorDisplay(input_name, "", true);
    password = value;
  }
  if (confirmPass) confirmChecker(confirmPass);
};

const confirmChecker = (input_name, value) => {
  if (value !== password) {
    errorDisplay(
      input_name,
      lang === "fr"
        ? "Les mots de passe ne correspondent pas"
        : "Passwords do not match"
    );
    confirmPass = false;
  } else {
    errorDisplay(input_name, "", true);
    confirmPass = true;
  }
};

inputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    // console.log(e.target.name);
    switch (e.target.name) {
      case "first_name":
        firstnamechecker(e.target.name, e.target.value);
        break;
      case "last_name":
        lastnamechecker(e.target.name, e.target.value);
        break;
      case "email":
        emailChecker(e.target.name, e.target.value);
        break;
      case "password":
        passwordChecker(e.target.name, e.target.value);
        break;
      case "confirm_password":
        confirmChecker(e.target.name, e.target.value);
        break;
      default:
        nul;
    }
  });
});

// form.addEventListener("submit", (e) => {
//   e.preventDefault();

//   if (firstname && email && password && confirmPass) {
//     const data = {
//       firstname,
//       email,
//       password,
//     };
//     console.log(data);

//   //   inputs.forEach((input) => (input.value = ""));
//   //   // progressBar.classList = "";

//   //   firstname = null;
//   //   email = null;
//   //   password = null;
//   //   confirmPass = null;
//   //   alert("Inscription validée !");
//   // } else {
//   //   alert("veuillez remplir correctement les champs");
//   }
// });
