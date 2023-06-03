/* =================== Responsive navbar =================== */

try {
  const hamburger = document.querySelector(".nav-profil");
  const navMenu = document.querySelector(".list-box");

  hamburger.addEventListener("click", () => {
    // hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
  });
} catch (error) {}

function paginatorWithAjax(
  url,
  classContainerData,
  classContainerSpinner,
  csrfToken,
  h,
  isPagePosts = false
) {
  let page = 1;
  let isPageEmpty = false;
  let canRequest = false;
  const spinnerHTML = `<div class="spinner-loader" role="status"></div>`;

  window.addEventListener("scroll", async (e) => {
    const marginY = document.body.clientHeight - window.innerHeight - h;
    if (window.pageYOffset > marginY && !isPageEmpty && !canRequest) {
      canRequest = true;
      page += 1;

      let containerData = document.querySelector(classContainerData);
      let containerSpinner = document.querySelector(classContainerSpinner);
      containerSpinner.innerHTML += spinnerHTML;

      const spinner = containerSpinner.querySelector(".spinner-loader");

      try {
        const response = await fetch(`${url}?page=${page}`, {
          method: "GET",
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken,
          },
        });
        if (response.status === 200) {
          let data = await response.text();

          if (data === "") {
            isPageEmpty = true;
            containerSpinner.removeChild(spinner);
          } else {
            containerSpinner.removeChild(spinner);
            containerData.innerHTML += data;
            canRequest = false;

            if (isPagePosts === true) {
              document
                // .querySelectorAll(`.root-comments-isAjax-${page}`)
                .querySelectorAll(`.root-comments`)
                .forEach(function (div) {
                  var postId = div.dataset.postId;
                  var classTogglePostDetail = div.dataset.classTogglePostDetail;
                  var urlAddUpdateComment = div.dataset.urlAddUpdateComment;
                  var csrfToken = div.dataset.csrfToken;
                  var imgProfile = div.dataset.imgProfile;
                  var urlGetData = div.dataset.urlGetData;
                  var nberLike = div.dataset.nberLike;
                  var nberComment = div.dataset.nberComment;
                  var isLike = +div.dataset.isLike === 1;

                  var root = ReactDOM.createRoot(div);
                  root.render(
                    React.createElement(AppLikeComment, {
                      postId: postId,
                      classTogglePostDetail: classTogglePostDetail,
                      urlAddUpdateComment: urlAddUpdateComment,
                      csrfToken: csrfToken,
                      imgProfile: imgProfile,
                      urlGetData: urlGetData,
                      nberLike: nberLike,
                      nberComment: nberComment,
                      isLike: isLike,
                    })
                  );
                });
            }
          }
        }
      else {
        containerSpinner.removeChild(spinner);
      }
      } catch (error) {}

      // .then((res) => res.text())
    }
  });
}


const lang_ = document.getElementById("language_code").value;
const langLink = document.getElementById("language_code_link");
langLink.addEventListener("click", () => {
  // location.reload();
  console.log("lang_", lang_);
  let url = location.href;
  // console.log("1 - url:", url);
  if (lang_ === "fr") {
    url = url.replace("fr", "en");
  } else {
    url = url.replace("en", "fr");
  }
  // console.log("2 - url:", url);
  location.href = url;
})