class InputForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "",
    };
  }

  handleSubmit(e) {
    e.preventDefault();
    this.props.handleAddComment({
      payload: {
        post_id: this.props.postId,
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
        <div className="form-comment-container-input">
          <div className="form-content-comment">
            <img src={this.props.imgProfile} />
            <textarea
              className="input_message_comment_id"
              autoComplete="off"
              placeholder="Ajouter un commentaire..."
              required
              value={this.state.msg}
              onChange={(e) => this.setState({ msg: e.target.value })}
            />
          </div>
          <button
            className="btn-send-comment"
            type="submit"
            disabled={this.state.msg === ""}
          >
            <img src="/static/home/svg/send.svg" />
          </button>
        </div>
      </form>
    );
  }
}
