const notif_alerte = document.getElementById("nav-nofit-alert");
const url = "http://127.0.0.1:8000/notifications/data/";
let data;

const api_notif = async () => {
  const api = await fetch(url, {
    method: "GET",
  })
    .then((response) => response.json())
    // .then((response) => console.log(response.data))
    .then((response) => {
      data = response.data;
      // console.log(data);
      if (data.filter((notif) => notif.seen === false).length > 0) {
        // notif_alerte.style.visibility = "visible";

        notif_alerte.textContent = data.filter(
          (notif) => notif.seen === false
        ).length;
        notif_alerte.style.display = "flex";
      } else {
        // notif_alerte.classList.remove("display-none");
        // notif_alerte.style.visibility = "hidden";
        notif_alerte.style.display = "none";
        // notif_alerte.style.zIndex = "-1";
      }
    })
    .catch();

  return api;
};

document.addEventListener("DOMContentLoaded", () => {
  setInterval(() => {
    api_notif();
  }, 3000);
});
