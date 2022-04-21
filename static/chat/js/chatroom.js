const other_user_id = document.getElementById("other_user_id").value;
const chat_textarea_msg = document.getElementById("chat-textarea-msg");
const chat_form = document.getElementById("form-chat");
const url_ajax_chat = `/messagerie/load-data/${other_user_id}/`;
let msg;

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

const send_message_chat = async () => {
  msg = chat_textarea_msg.value;
  if (msg === "") {
    return;
  } else {
    chat_textarea_msg.value = "";

    const formData = new FormData();
    formData.append("msg", msg);

    const request_chat = new Request(url_ajax_chat, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,
      },
      body: formData,
    });

    fetch(request_chat)
      .then((messages) => messages.json())
      .then((response) => {
        const data_chat = response.data;
        try {
          for (const message of data_chat) {
            display_message_chat(message);
          }
        } catch (error) {
          display_message_chat(messages);
        }
      });
  }
};

const load_message_chat = async () => {
  const load_data = await fetch(url_ajax_chat)
    .then((messages) => messages.json())
    .then((response) => {
      const data_chat = response.data;
      // console.log(data_chat);
      try {
        for (const message of data_chat) {
          display_message_chat(message);
        }
      } catch (error) {
        display_message_chat(messages);
      }
    })
    .catch();
  return load_data;
};

const display_message_chat = (message) => {
  const chat_container = document.querySelector(".main-chat");
  // console.log(message.msg);
  // console.log(message.sent);
  const class_name = message.sent;

  const div = document.createElement("div");
  div.classList.add(`box-message-${class_name}`);
  div.innerHTML = `
    <div class="msg">
      <p>${message.msg}</p>
      <em>${message.date_created}</em>
    </div>
  `;
  chat_container.appendChild(div);
  div.scrollIntoView();
};

chat_form.addEventListener("submit", (e) => {
  e.preventDefault();
  // console.log('submit');
  send_message_chat();
});

setInterval(() => {
  load_message_chat();
}, 5000);
