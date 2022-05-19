class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      postId: props.postId,
      classTogglePostDetail: props.classTogglePostDetail.toString() === "1",
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile,
      urlGetData: props.urlGetData,
      listComments: [],
      nberLike: props.nberLike,
      nberComment: props.nberComment,
    };
    this.handleAddComment = this.handleAddComment.bind(this);
    this.handleEditComment = this.handleEditComment.bind(this);
    this.handleDeleteComment = this.handleDeleteComment.bind(this);
  }
  // D-none_V-hidden_O-0
  handleClickToggle() {
    const toggle = this.state.classTogglePostDetail;
    this.setState({ classTogglePostDetail: !toggle });
  }

  componentDidMount() {
    fetch(this.state.urlGetData, { method: "GET" })
      .then((response) => response.json())
      .then((res) => this.setState({ listComments: res.data }));
  }

  updateNberComment(type) {
    const num = parseInt(this.state.nberComment);
    if (type === "ADD") {
      this.setState({ nberComment: num + 1 });
    } else if (type === "DELETE") {
      this.setState({ nberComment: num - 1 });
    }
  }

  handleAddComment(action) {
    fetch(this.state.urlAddUpdateComment, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": this.state.csrfToken,
      },
      body: JSON.stringify({
        message: action.payload.msg,
        id_post: action.payload.post_id,
        id_comment: null,
      }),
    })
      .then((res) => res.json())
      .then((res) => {
        // console.log(res);
        const commentData = this.state.listComments.slice();
        commentData.push(res);
        this.setState({ listComments: commentData });
      })
      .then(() => {
        this.updateNberComment("ADD");
      });
  }

  handleEditComment(action) {
    fetch(this.state.urlAddUpdateComment, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": this.state.csrfToken,
      },
      body: JSON.stringify({
        message: action.payload.msg,
        id_post: action.payload.post_id,
        id_comment: action.payload.comment_id,
      }),
    }).then(() => {
      const commentData1 = this.state.listComments.slice();
      commentData1.filter((comment) => {
        if (comment.id === action.payload.comment_id) {
          comment.comment_message = action.payload.msg;
          this.setState({ listComments: commentData1 });
        }
      });
    });
  }

  handleDeleteComment(id) {
    const formData = new FormData();
    formData.append("id_comment", id);

    fetch("/comment/delete-comment/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": this.state.csrfToken,
      },
      body: formData,
    })
      .then(() => {
        window.confirm("Vous êtes sûr de vouloir supprimer") &&
          this.componentDidMount();
      })
      .then(() => {
        this.updateNberComment("DELETE");
      });
  }

  render() {
    return (
      <React.Fragment>
        <div className="post-footer">
          <InfoLikeComment
            nberComment={this.state.nberComment}
            nberLike={this.state.nberLike}
          />
          <hr />
          <div className="box-action-icon">
            <LikeFormButton />
            <button
              className="action-icon box-comment btn-container-comment-toggle"
              id="{{post.id}}"
              onClick={() => this.handleClickToggle()}
            >
              <img
                src="/static/home/svg/comment.svg"
                className="icon-like-comment-share"
                id="{{post.id}}"
              />
              <span id="{{post.id}}" className="label-like-comment-share">
                Commenter
              </span>
            </button>
            <button className="action-icon box-share">
              <img
                src="/static/home/svg/share.svg"
                className="icon-like-comment-share"
              />
              <span className="label-like-comment-share">Partager</span>
            </button>
          </div>
        </div>

        <div
          title={this.state.postId}
          className={
            this.state.classTogglePostDetail
              ? "form-comment-list-input-container-global D-none_V-hidden_O-0"
              : "form-comment-list-input-container-global"
          }
          id={"form-comment-list-input-container-global" + this.state.postId}
          method="post"
        >
          <InputForm
            postId={this.state.postId}
            classTogglePostDetail={this.state.classTogglePostDetail}
            urlAddUpdateComment={this.state.urlAddUpdateComment}
            csrfToken={this.state.csrfToken}
            imgProfile={this.state.imgProfile}
            handleAddComment={this.handleAddComment}
          />
          <div
            className="container-global-comment-list"
            id={"container-global-comment-list-" + this.state.postId}
          >
            {this.state.listComments.length > 0 &&
              this.state.listComments.map((comment) => (
                <ListComments
                  key={comment.id}
                  comment={comment}
                  handleEditComment={this.handleEditComment}
                  handleDeleteComment={this.handleDeleteComment}
                />
              ))}
          </div>
        </div>
      </React.Fragment>
    );
  }
}

// export default index;

document.querySelectorAll(".root-comments").forEach((div) => {
  const postId = div.dataset.postId;
  const classTogglePostDetail = div.dataset.classTogglePostDetail;
  const urlAddUpdateComment = div.dataset.urlAddUpdateComment;
  const csrfToken = div.dataset.csrfToken;
  const imgProfile = div.dataset.imgProfile;
  const urlGetData = div.dataset.urlGetData;
  const nberLike = div.dataset.nberLike;
  const nberComment = div.dataset.nberComment;

  const root = ReactDOM.createRoot(div);
  root.render(
    <App
      postId={postId}
      classTogglePostDetail={classTogglePostDetail}
      urlAddUpdateComment={urlAddUpdateComment}
      csrfToken={csrfToken}
      imgProfile={imgProfile}
      urlGetData={urlGetData}
      nberLike={nberLike}
      nberComment={nberComment}
    />
  );
});
