class InputForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      postId: props.postId,
      classTogglePostDetail: props.classTogglePostDetail,
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile,
      handleAddComment: props.handleAddComment,
      msg: "",
    };
  }

  handleSubmit(e) {
    e.preventDefault();
    this.state.handleAddComment({
      payload: {
        post_id: this.state.postId,
        msg: this.state.msg,
      },
    });
  }

  render() {
    return (
      <form
        onSubmit={(e) => {
          this.handleSubmit(e);
          this.setState({ msg: "" });
        }}
      >
        {/* // <form> */}
        <div className="form-comment-container-input">
          <div className="form-content-comment">
            <img src={this.state.imgProfile} />
            <input
              type="text"
              name="message"
              id={"input_message_comment-" + this.state.postId}
              className="input_message_comment_id"
              autoComplete="off"
              placeholder="Ajouter un commentaire..."
              required
              value={this.state.msg}
              onChange={(e) => this.setState({ msg: e.target.value })}
            />
            <input
              type="hidden"
              name="post_id_comment"
              id={"input_hidden_post_comment-" + this.state.postId}
              value={this.state.postId}
            />
            <input
              type="hidden"
              name="post_id_comment2"
              id={"input_hidden_post_comment2-" + this.state.postId}
              value=""
            />
          </div>
          <button
            className="btn-send-comment"
            type="submit"
            name="submit_c_form"
            title={this.state.postId}
          >
            <img src="/static/home/svg/send.svg" />
          </button>
        </div>
      </form>
    );
  }
}
