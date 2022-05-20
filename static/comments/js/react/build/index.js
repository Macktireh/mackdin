document.querySelectorAll(".root-comments").forEach(function (div) {
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
  root.render(React.createElement(AppLikeComment, {
    postId: postId,
    classTogglePostDetail: classTogglePostDetail,
    urlAddUpdateComment: urlAddUpdateComment,
    csrfToken: csrfToken,
    imgProfile: imgProfile,
    urlGetData: urlGetData,
    nberLike: nberLike,
    nberComment: nberComment,
    isLike: isLike
  }));
});