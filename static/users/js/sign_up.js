const form = document.querySelector("form");
const inputs = document.querySelectorAll(".form-control");
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
      "Le prénom doit contenir entre 2 et 50 caractères"
    );
    firstname = null;
  } else if (!value.match(/^[a-zA-Z -]*$/)) {
    errorDisplay(
      input_name,
      "Le prénom ne doit pas contenir de caractères spéciaux"
    );
    firstname = null;
  } else {
    errorDisplay(input_name, "", true);
    firstname = value;
  }
};

const lastnamechecker = (input_name, value) => {
  if (value.length > 0 && (value.length < 2 || value.length > 50)) {
    errorDisplay(input_name, "Le nom doit contenir entre 2 et 50 caractères");
    lastname = null;
  } else if (!value.match(/^[a-zA-Z -]*$/)) {
    errorDisplay(
      input_name,
      "Le nom ne doit pas contenir de caractères spéciaux"
    );
    lastname = null;
  } else {
    errorDisplay(input_name, "", true);
    lastname = value;
  }
};

const emailChecker = (input_name, value) => {
  if (!value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/)) {
    errorDisplay("email", "Le mail n'est pas valide");
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
      "Minimum de 8 caractères, une majuscule, un chiffre et un caractère spécial"
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
    errorDisplay(input_name, "Les mots de passe ne correspondent pas");
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
