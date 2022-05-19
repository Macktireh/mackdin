class Option extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      comment: props.comment,
      toggle: false,
      handleEditingComment: props.handleEditingComment,
    };
  }

  handleClickToggle() {
    const toggle = this.state.toggle;
    this.setState({ toggle: !toggle });
  }

  render() {
    return (
      <React.Fragment>
        <div
          id={this.state.comment.id}
          className="comment-options-btn"
          onClick={() => this.handleClickToggle()}
        >
          <span id="btn-point"></span>
          <span id="btn-point"></span>
          <span id="btn-point"></span>
        </div>

        <div
          id={"comment-options-container" + this.state.comment.id}
          className={
            this.state.toggle
              ? "comment-options-actions-container"
              : "comment-options-actions-container display-none"
          }
        >
          <ul>
            <div
              className="comment-options-item comment-options-item-edit"
              id={this.state.comment.id}
              onClick={() => this.state.handleEditingComment()}
            >
              <img
                src="/static/home/svg/edit.svg"
                id={this.state.comment.id}
                className="comment-options-item-img"
              />
              <span
                className="btn-edit-comment comment-options-item-span"
                id={this.state.comment.id}
              >
                Modifier
              </span>
            </div>

            <div
              className="comment-options-item comment-options-item-delete"
              id={this.state.comment.id}
              title={this.state.comment.post_id}
            >
              <img
                src="/static/home/svg/delete.svg"
                id={this.state.comment.id}
                className="comment-options-item-img"
              />
              <span
                className="btn-del-comment comment-options-item-span"
                id={this.state.comment.id}
                title={this.state.comment.post_id}
              >
                Supprimer
              </span>
            </div>
          </ul>
        </div>
      </React.Fragment>
    );
  }
}
