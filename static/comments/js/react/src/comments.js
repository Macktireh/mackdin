class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      postId: props.postId,
      classTogglePostDetail: props.classTogglePostDetail,
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile,
      urlGetData: props.urlGetData,
      listComments: [],
    };
  }

  componentDidMount() {
    fetch(this.state.urlGetData, { method: "GET" })
      .then((response) => response.json())
      .then((res) => this.setState({ listComments: res.data }));
  }

  render() {
    return (
      <form
        title={this.state.postId}
        className="form-comment-list-input-container-global"
        id="form-comment-list-input-container-global{{post.id}}"
        method="post"
      >
        <InputForm
          postId={this.state.postId}
          classTogglePostDetail={this.state.classTogglePostDetail}
          urlAddUpdateComment={this.state.urlAddUpdateComment}
          csrfToken={this.state.csrfToken}
          imgProfile={this.state.imgProfile}
        />
        <div
          className="container-global-comment-list"
          id={"container-global-comment-list-" + this.state.postId}
        >
          {this.state.listComments.length > 0 &&
            this.state.listComments.map((comment) => (
              <ListComments key={comment.id} comment={comment} />
            ))}
        </div>
      </form>
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

  const root = ReactDOM.createRoot(div);
  root.render(
    <App
      postId={postId}
      classTogglePostDetail={classTogglePostDetail}
      urlAddUpdateComment={urlAddUpdateComment}
      csrfToken={csrfToken}
      imgProfile={imgProfile}
      urlGetData={urlGetData}
    />
  );
});
