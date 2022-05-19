const comment_options_btn = document.querySelectorAll(".comment-options-btn");

comment_options_btn.forEach((element) => {
  element.addEventListener("click", (e) => {
    comment_ops_container = document.getElementById(
      "comment-options-container" + element.id
    );
    // console.log(comment_ops_container);
    comment_ops_container.classList.toggle("display-none");
  });
});

funct_toggle_options = function () {
  const comment_options_btn = document.querySelectorAll(".comment-options-btn");

  comment_options_btn.forEach((element) => {
    element.addEventListener("click", (e) => {
      comment_ops_container = document.getElementById(
        "comment-options-container" + element.id
      );
      // console.log(comment_ops_container);
      comment_ops_container.classList.toggle("display-none");
    });
  });
};

// ##############################################""
// bouton d'option de modification et suppression

const comment_options_item_edits = document.querySelectorAll(
  ".comment-options-item-edit"
);

comment_options_item_edits.forEach((element) => {
  element.addEventListener("click", (e) => {
    const msg = document.querySelector(".msg-text-p-" + e.target.id);
    // console.log(e.target.id);
    // console.log(msg.id);

    document.getElementById("input_message_comment-" + msg.id).value =
      msg.textContent;
    document.getElementById("input_hidden_post_comment2-" + msg.id).value =
      e.target.id;
  });
});

// ##############################################""
// ajout et modification des commentaires

let num_comment;

const fonc_text_plural2 = (n, balise) => {
  if (n > 1) {
    balise.textContent("Likes");
  } else {
    balise.textContent("Like");
  }
};

const form_comments = document.querySelectorAll(
  ".form-comment-list-input-container-global"
);

form_comments.forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const input_text_comment = document.getElementById(
      "input_message_comment-" + e.target.title
    ).value;
    const input_hidden_post_comment = document.getElementById(
      "input_hidden_post_comment-" + e.target.title
    ).value;
    const input_hidden_post_comment2 = document.getElementById(
      "input_hidden_post_comment2-" + e.target.title
    ).value;
    // alert(`${input_text_comment} - ${input_hidden_post_comment}`)
    const container_list_comment = document.getElementById(
      "container-global-comment-list-" + e.target.title
    );
    const count_num_comment = parseInt(
      document.getElementById("comments-num" + e.target.title).textContent
    );

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

    fetch(e.target.action, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({
        message: input_text_comment,
        id_post: input_hidden_post_comment,
        id_comment: input_hidden_post_comment2,
      }),
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        // console.log(data);
        // console.log(data.comment_message);

        const verif_img = (v) => {
          if (v) {
            return `<img id="container-comment-list-img-profile" src="${v}" />`;
            // return `<img id="container-comment-list-img-profile" src="http://127.0.0.1:8000${v}" />`;
          } else {
            return `<img id="container-comment-list-img-profile" src="static/home/img/default-img-profile.jpg" />`;
          }
        };

        const verif_author = (author_comment, author_post) => {
          if (author_comment === author_post) {
            return `<span id="author_post_and_comment">Auteur</span>`;
          } else {
            return "";
          }
        };
        //

        if (!input_hidden_post_comment2) {
          const div = document.createElement("div");
          div.classList.add("container-comment-list");
          div.id = `container-comment-list${data.id}`;
          div.innerHTML = /*html*/ `
            <div id="${data.id}" class="comment-options-btn">
              <span id="btn-point"></span>
              <span id="btn-point"></span>
              <span id="btn-point"></span>
            </div>

            <div 
              id="comment-options-container${data.id}" 
              class="comment-options-actions-container display-none">
              <ul>
                <div class="comment-options-item comment-options-item-edit"
                  id="${data.id}">
                  <img src="/static/home/svg/edit.svg" 
                    id="${data.id}"
                    class="comment-options-item-img">
                  <span
                    class="btn-edit-comment comment-options-item-span"
                    id="${data.id}">Modifier
                  </span>
                </div>

                <div class="comment-options-item comment-options-item-delete"
                  id="${data.id}"  
                  title="${data.post_id}">
                  <img src="/static/home/svg/delete.svg"
                    id="${data.id}"
                    class="comment-options-item-img">
                  <span class="btn-del-comment comment-options-item-span" 
                    id="${data.id}" 
                    title="${data.post_id}">Supprimer
                  </span>
                </div>
              </ul>
            </div>

            <a href="/profile/${data.user_profile_pseudo}/">
              ${verif_img(data.user_profile_img)}
            </a>

            <div class="comment-content-box">
              <div class="comment-info-content">
                <div 
                  class="comment-info-content-I" 
                  id="comment-info-content-I-${data.post_id}">

                  <strong>${data.comment_author_first_name}
                    ${data.comment_author_last_name}
                    ${verif_author(data.comment_author, data.post_author)}
                  </strong>
                  <p id="comment-author-profile-title">
                    ${data.user_profile_bio}
                  </p>
                </div>
                <small>${data.comment_date_added}</small>
              </div>
              <div class="comment-text-content">
                <p class="msg-text-p-${data.id}" id="${data.post_id}">
                  ${data.comment_message}
                </p>
              </div>
            </div>
          `;

          container_list_comment.appendChild(div);
          // console.log(div);

          // container_list_comment.innerHTML += `
          //   <div class="container-comment-list"  id="container-comment-list${
          //     data.id
          //   }">

          //     <div id="${data.id}" class="comment-options-btn">
          //       <span id="btn-point"></span>
          //       <span id="btn-point"></span>
          //       <span id="btn-point"></span>
          //     </div>

          //     <div id="comment-options-container${
          //       data.id
          //     }" class="comment-options-actions-container display-none">
          //       <ul>
          //         <div class="comment-options-item comment-options-item-edit" title="${
          //           data.id
          //         }">
          //           <img src="http://127.0.0.1:8000/static/comments/img/edit.svg" id="${
          //             data.id
          //           }" class="comment-options-item-img">
          //           <span class="btn-edit-comment comment-options-item-span" id="${
          //             data.id
          //           }">Modifier</span>
          //         </div>
          //         <div class="comment-options-item comment-options-item-delete" id="${
          //           data.id
          //         }"  title="${data.post_id}">
          //           <img src="http://127.0.0.1:8000/static/comments/img/delete.svg" id="${
          //             data.id
          //           }" class="comment-options-item-img">
          //           <span class="btn-del-comment comment-options-item-span" id="${
          //             data.id
          //           }"   title="${data.post_id}">Supprimer</span>
          //         </div>
          //       </ul>
          //     </div>

          //       ${verif_img(data.user_profile_img)}

          //       <div class="comment-content-box">
          //         <div class="comment-info-content">
          //           <div class="comment-info-content-I" id="comment-info-content-I-${
          //             data.post_id
          //           }">
          //             <strong>${data.comment_author_first_name}
          //               ${data.comment_author_last_name}
          //               ${verif_author(data.comment_author, data.post_author)}
          //             </strong>
          //             <small>${data.comment_date_added}</small>
          //           </div>
          //           <p id="comment-author-profile-title">${
          //             data.user_profile_bio
          //           }</p>
          //         </div>
          //         <div class="comment-text-content">
          //           <p class="msg-text-p-${data.id}" id="${data.post_id}">
          //             ${data.comment_message}
          //           </p>
          //         </div>
          //       </div>
          //   </div>`;

          num_comment = count_num_comment + 1;
          document.getElementById("comments-num" + e.target.title).textContent =
            num_comment;
          if (num_comment > 1) {
            document.getElementById(
              "text-plural-comments" + e.target.title
            ).textContent = "Commentaires";
          } else {
            document.getElementById(
              "text-plural-comments" + e.target.title
            ).textContent = "Commentaire";
          }
        } else {
          document.querySelector(".msg-text-p-" + data.id).textContent =
            data.comment_message;
        }
      });

    document.getElementById("input_message_comment-" + e.target.title).value =
      "";
    document.getElementById(
      "input_hidden_post_comment2-" + e.target.title
    ).value = "";
  });
});

// ##############################################""
// suppression des commentaires

const comment_options_item_deletes = document.querySelectorAll(
  ".comment-options-item-delete"
);

comment_options_item_deletes.forEach((element) => {
  element.addEventListener("click", (e) => {
    const url_delete_comment = document.getElementById(
      "input_hidden_url_delete_comment"
    ).value;
    // console.log(element);
    // console.log(e.target.id);
    // console.log(e);
    if (confirm("Voullez vous vraiment supprimer !")) {
      const com = document.getElementById(
        "container-comment-list" + e.target.id
      );
      const count_num_comment = parseInt(
        document.getElementById("comments-num" + e.target.title).textContent
      );

      // console.log(
      //   document.getElementById("text-plural-comments" + e.target.title)
      // );

      // const input_hidden_post_comment_edit2 = document.getElementById(
      //   "input_hidden_post_comment2-" + e.target.title
      // ).value;

      function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
          const cookies = document.cookie.split(";");
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
              cookieValue = decodeURIComponent(
                cookie.substring(name.length + 1)
              );
              break;
            }
          }
        }
        return cookieValue;
      }
      const csrftoken = getCookie("csrftoken");

      const formData = new FormData();
      formData.append("id_comment", e.target.id);

      const request = new Request(url_delete_comment, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": csrftoken,
        },
        body: formData,
      });

      fetch(request)
        .then((response) => response.json())
        .then((result) => {
          // console.log(result);
        });

      com.style.display = "none";
      // com.classList.add("display-none");
      num_comment = count_num_comment - 1;
      document.getElementById("comments-num" + e.target.title).textContent =
        num_comment;

      if (num_comment > 1) {
        document.getElementById(
          "text-plural-comments" + e.target.title
        ).textContent = "Commentaires";
      } else {
        document.getElementById(
          "text-plural-comments" + e.target.title
        ).textContent = "Commentaire";
      }
      // document.getElementById("input_message_comment-" + msg.id).value =
      //   msg.textContent;
      // document.getElementById("input_hidden_post_comment2-" + msg.id).value =
      //   e.target.id;
    }
  });
});
