/* =================== Responsive navbar =================== */

try {
  const hamburger = document.querySelector(".nav-profil");
  const navMenu = document.querySelector(".list-box");

  hamburger.addEventListener("click", () => {
    // hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
  });
} catch (error) {}

function paginatorWithAjax(url, className, csrfToken, h, isPagePosts = false) {
  let page = 1;
  let isPageEmpty = false;
  let canRequest = false;
  const spinnerHTML = `
    <div class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
  `;

  window.addEventListener("scroll", (e) => {
    const marginY = document.body.clientHeight - window.innerHeight - h;
    // console.table([{clientHeight:document.body.clientHeight, innerHeight:window.innerHeight, marginY, pageYOffset: window.pageYOffset}]);
    if (window.pageYOffset > marginY && !isPageEmpty && !canRequest) {
      canRequest = true;
      page += 1;

      let container = document.querySelector(className);
      container.innerHTML += spinnerHTML;

      const spinner = container.querySelector(".spinner-border");

      fetch(`${url}?page=${page}`, {
        method: "GET",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": csrfToken,
        },
      })
        .then((res) => res.text())
        .then((data) => {
          // console.log(data);
          if (data === "") {
            isPageEmpty = true;
            container.removeChild(spinner);
          } else {
            container.removeChild(spinner);
            container.innerHTML += data;
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
        });
    }
  });
}
