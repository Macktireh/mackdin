try {
  const previous_container = document.querySelector(".previous-new-add-post");
  const previous_p_img_container = document.querySelector(".previous-post-img");
  const input_img = document.querySelector(".form-input-file");
  const input_text = document.getElementById("textarea_id");
  const p_text = document.getElementById("previous-message");
  const p_img = document.getElementById("previous-post-image");
  const cancel_add_post = document.getElementById("btn-cancel-add-post");

  let val;
  // console.log(previous_container);

  input_text.addEventListener("input", (e) => {
    val = e.target.value;
    //   console.log(val);
    if (val.length >= 1 || input_img.value) {
      previous_container.classList.remove("display-none");
      previous_container.classList.add("display-block");
      p_text.textContent = val;
    } else {
      previous_container.classList.remove("display-none");
      previous_container.classList.remove("display-block");
      p_text.textContent = val;
    }
  });

  input_img.addEventListener("change", function () {
    const file = this.files[0];
    //   console.log(file);
    if (file) {
      const reader = new FileReader();

      previous_container.classList.remove("display-none");
      previous_container.classList.add("display-block");

      previous_p_img_container.classList.remove("display-none");
      previous_p_img_container.classList.add("display-block");

      reader.addEventListener("load", function () {
        //   console.log(this);
        //   console.log(this.result);
        p_img.setAttribute("src", this.result);
      });
      reader.readAsDataURL(file);
    } else {
      previous_container.classList.remove("display-none");
      previous_container.classList.remove("display-block");

      previous_p_img_container.classList.remove("display-none");
      previous_p_img_container.classList.remove("display-block");
      p_img.setAttribute("src", "");
    }
  });

  // annuler le post
  cancel_add_post.addEventListener("click", () => {
    input_text.value = "";
    input_img.value = "";
    val = "";
    p_text.textContent = val;
    p_img.setAttribute("src", "");
    previous_p_img_container.classList.add("display-none");
    previous_container.classList.add("display-none");
  });
} catch (error) {}

// toggle button options post
try {
  const options_btn = document.querySelectorAll(".options-btn");
  options_btn.forEach((element) => {
    element.addEventListener("click", (e) => {
      ops_container = document.getElementById("options-container" + element.id);
      ops_container.classList.toggle("display-none");
    });
  });
} catch (error) {
  const options_btn = document.querySelector(".options-btn");
  options_btn.addEventListener("click", (e) => {
    ops_container = document.getElementById("options-container" + element.id);
    ops_container.classList.toggle("display-none");
  });
}

// toggle button display section comment
try {
  const btn_container_comment_toggle = document.querySelectorAll(
    ".btn-container-comment-toggle"
  );
  btn_container_comment_toggle.forEach((element) => {
    element.addEventListener("click", (e) => {
      document
        .getElementById(
          "form-comment-list-input-container-global" + e.target.id
        )
        .classList.toggle("D-none_V-hidden_O-0");
    });
  });
} catch (error) {
  const btn_container_comment_toggle = document.querySelector(
    ".btn-container-comment-toggle"
  );
  btn_container_comment_toggle.addEventListener("click", (e) => {
    document
      .getElementById("form-comment-list-input-container-global" + e.target.id)
      .classList.toggle("D-none_V-hidden_O-0");
  });
}
