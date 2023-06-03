class AppLikeComment extends React.Component {
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
      isLike: props.isLike,
      nberLike: props.nberLike,
      nberComment: props.nberComment,
      isLikeComment: false,
      nberLikeCommnet: 0,
      page: 2,
      canRequest: true,
      lang: "fr",
    };

    this.handleGetComment = this.handleGetComment.bind(this);
    this.handleGetCommentPaginator = this.handleGetCommentPaginator.bind(this);

    this.handlIsLike = this.handlIsLike.bind(this);
    this.handleLikeorUnlike = this.handleLikeorUnlike.bind(this);
    this.handleLikeorUnlikeComment = this.handleLikeorUnlikeComment.bind(this);

    this.handleClickToggle = this.handleClickToggle.bind(this);

    this.handleAddComment = this.handleAddComment.bind(this);
    this.handleEditComment = this.handleEditComment.bind(this);
    this.handleDeleteComment = this.handleDeleteComment.bind(this);
  }

  componentDidMount() {
    this.handleGetComment();
    const lang = document.getElementById("language_code").value;
    this.setState({ lang: lang });
  }

  configFetch(url, method, data) {
    const request = new Request(url, {
      method: method,
      headers: {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": this.state.csrfToken,
      },
      body: data,
    });
    return request;
  }

  handleClickToggle() {
    const toggle = this.state.classTogglePostDetail;
    this.setState({ classTogglePostDetail: !toggle });
  }

  handleGetComment() {
    fetch(this.state.urlGetData, { method: "GET" })
      .then((res) => res.json())
      .then((res) => this.setState({ listComments: res.data }));
  }

  handleGetCommentPaginator(params = "") {
    fetch(`${this.state.urlGetData}?page=${this.state.page}`, { method: "GET" })
      .then((res) => {
        if (res.status === 200) {
          return res.json();
        } else {
          this.setState({ canRequest: false });
        }
      })
      .then((res) => {
        if (res.data.length > 0) {
          // return res.json();

          copyComment = this.state.listComments.slice();
          comments = [...copyComment];
          res.data.forEach((item2) => {
            const foundIndex = comments.findIndex(
              (item1) => item1.id === item2.id
            );
            if (foundIndex === -1) {
              comments.push(item2);
            } else {
              comments[foundIndex] = item2;
            }
          });
          this.setState({ listComments: comments });
          this.setState({ page: this.state.page + 1 });
          console.log("res", res.data);
          console.log("comments", comments);
          console.log("page", this.state.page);
        }
      });
  }

  handlIsLike(obj, type) {
    if (obj === "post") {
      if (type === "Unlike") {
        this.setState({ isLike: false });
      } else if (type === "Like") {
        this.setState({ isLike: true });
      }
    }
  }

  updateNberLike(type) {
    const num = parseInt(this.state.nberLike);
    if (type === "Like") {
      this.setState({ nberLike: num + 1 });
    } else {
      this.setState({ nberLike: num - 1 });
    }
  }

  updateNberLikeComment(id, type) {
    let copyComment = this.state.listComments.slice();
    let comments = [...copyComment];
    comments = comments.map((item) => {
      if (item.id === id) {
        if (type === "Unlike") {
          item.comment_is_like = false;
          item.comment_number_like = item.comment_number_like - 1;
        } else if (type === "Like") {
          item.comment_is_like = true;
          item.comment_number_like = item.comment_number_like + 1;
        }
        return item;
      }
      return item;
    });
    this.setState({ listComments: comments });
  }

  handleLikeorUnlikeComment(comment_id) {
    const formData = new FormData();
    formData.append("comment_id", comment_id);

    fetch(this.configFetch(`/${this.state.lang}/comment/like/`, "POST", formData))
      .then((res) => res.json())
      .then((res) => {
        this.handlIsLike("comment", res.value);
        this.updateNberLikeComment(comment_id, res.value);
      });
  }

  handleLikeorUnlike() {
    const formData = new FormData();
    formData.append("post_id", this.state.postId);

    fetch(this.configFetch(`/${this.state.lang}/feed/like/`, "POST", formData))
      .then((res) => res.json())
      .then((res) => {
        this.handlIsLike("post", res.value);
        this.updateNberLike(res.value);
      });
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
    const data = JSON.stringify({
      message: action.payload.msg,
      id_post: action.payload.post_id,
      id_comment: null,
    });

    fetch(this.configFetch(this.state.urlAddUpdateComment, "POST", data))
      .then((res) => res.json())
      .then((res) => {
        const commentData = this.state.listComments.slice();
        commentData.push(res);
        this.setState({ listComments: commentData });
      })
      .then(() => {
        this.updateNberComment("ADD");
      });
  }

  handleEditComment(action) {
    const data = JSON.stringify({
      message: action.payload.msg,
      id_post: action.payload.post_id,
      id_comment: action.payload.comment_id,
    });

    fetch(this.configFetch(this.state.urlAddUpdateComment, "POST", data)).then(
      () => {
        const commentData1 = this.state.listComments.slice();
        commentData1.filter((comment) => {
          if (comment.id === action.payload.comment_id) {
            comment.comment_message = action.payload.msg;
            this.setState({ listComments: commentData1 });
          }
        });
      }
    );
  }

  handleDeleteComment(id) {
    const formData = new FormData();
    formData.append("id_comment", id);
    if (window.confirm(`${this.props.lang === "fr" ? "Vous êtes sûr de vouloir supprimer" : "Are you sure you want to delete"}`)) {
      fetch(
        this.configFetch(`/${this.state.lang}/comment/delete-comment/`, "POST", formData)
      ).then(() => {
        const filteredListComments = this.state.listComments.filter(
          (t) => t.id !== id
        );
        this.setState({ listComments: filteredListComments });
        this.updateNberComment("DELETE");
      });
    }
  }

  render() {
    return (
      <React.Fragment>
        <div className="post-footer">
          <InfoLikeComment
            nberComment={this.state.nberComment}
            nberLike={this.state.nberLike}
            handleClickToggle={this.handleClickToggle}
            lang={this.state.lang}
          />
          <hr />
          <BtnLikeCommentShare
            handleClickToggle={this.handleClickToggle}
            handleLikeorUnlike={this.handleLikeorUnlike}
            isLike={this.state.isLike}
            lang={this.state.lang}
          />
        </div>

        <div
          className={
            this.state.classTogglePostDetail
              ? "form-comment-list-input-container-global D-none_V-hidden_O-0"
              : "form-comment-list-input-container-global"
          }
          style={{
            display: this.state.classTogglePostDetail ? "none" : "flex",
          }}
        >
          <InputForm
            postId={this.state.postId}
            imgProfile={this.state.imgProfile}
            handleAddComment={this.handleAddComment}
            lang={this.state.lang}
          />
          <div className="container-global-comment-list">
            {this.state.listComments.length > 0 &&
              this.state.listComments
                .sort(
                  (a, b) =>
                    new Date(a.created_at).getTime() -
                    new Date(b.created_at).getTime()
                )
                .map((comment) => (
                  <ListComments
                    key={comment.id}
                    comment={comment}
                    handleEditComment={this.handleEditComment}
                    handleDeleteComment={this.handleDeleteComment}
                    handleLikeorUnlikeComment={this.handleLikeorUnlikeComment}
                    isLikeComment={this.state.isLikeComment}
                    nberLikeCommnet={this.state.nberLikeCommnet}
                  />
                ))}
          </div>
          {this.state.canRequest &&
            this.state.nberComment > this.state.listComments.length && (
              <div
                className="voir-plus"
                onClick={this.handleGetCommentPaginator}
              >
                voir plus
              </div>
            )}
        </div>
      </React.Fragment>
    );
  }
}
