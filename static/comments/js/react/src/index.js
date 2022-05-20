document.querySelectorAll(".root-comments").forEach((div) => {
  const postId = div.dataset.postId;
  const classTogglePostDetail = div.dataset.classTogglePostDetail;
  const urlAddUpdateComment = div.dataset.urlAddUpdateComment;
  const csrfToken = div.dataset.csrfToken;
  const imgProfile = div.dataset.imgProfile;
  const urlGetData = div.dataset.urlGetData;
  const nberLike = div.dataset.nberLike;
  const nberComment = div.dataset.nberComment;
  const isLike = +div.dataset.isLike === 1;

  const root = ReactDOM.createRoot(div);
  root.render(
    <AppLikeComment
      postId={postId}
      classTogglePostDetail={classTogglePostDetail}
      urlAddUpdateComment={urlAddUpdateComment}
      csrfToken={csrfToken}
      imgProfile={imgProfile}
      urlGetData={urlGetData}
      nberLike={nberLike}
      nberComment={nberComment}
      isLike={isLike}
    />
  );
});
