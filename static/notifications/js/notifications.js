const notif_alerte = document.getElementById("nav-nofit-alert");
const notif_alerte_chat = document.getElementById("nav-nofit-alert-chat");
let data;

const api_notif = async (url, element) => {
  const api = await fetch(url, {
    method: "GET",
  })
    .then((response) => response.json())
    // .then((response) => console.log(response.data))
    .then((response) => {
      data = response.data;
      // console.log(data);
      if (data.filter((notif) => notif.seen === false).length > 0) {
        element.textContent = data.filter(
          (notif) => notif.seen === false
        ).length;
        element.style.display = "flex";
      } else {
        element.style.display = "none";
      }
    })
    .catch();

  return api;
};

document.addEventListener("DOMContentLoaded", () => {
  setInterval(() => {
    try {
      api_notif("/notifications/data/", notif_alerte);
      setTimeout(() => {
        api_notif("/messagerie/chat-api-notif/", notif_alerte_chat);
      }, 3000);
    } catch (error) {
      api_notif("/notifications/data/", notif_alerte);
      setTimeout(() => {
        api_notif("/messagerie/chat-api-notif/", notif_alerte_chat);
      }, 2000);
    }
  }, 5000);
});
