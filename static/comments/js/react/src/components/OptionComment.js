class OptionComment extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      comment: props.comment,
      toggle: false,
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
          className="comment-options-btn"
          onClick={() => this.handleClickToggle()}
        >
          <span id="btn-point"></span>
          <span id="btn-point"></span>
          <span id="btn-point"></span>
        </div>

        <div
          className={
            this.state.toggle
              ? "comment-options-actions-container"
              : "comment-options-actions-container display-none"
          }
        >
          <ul>
            <div
              className="comment-options-item comment-options-item-edit"
              onClick={() => {
                this.props.handleIsEditingComment();
                this.handleClickToggle();
              }}
            >
              <img
                src="/static/home/svg/edit.svg"
                className="comment-options-item-img"
              />
              <span className="btn-edit-comment comment-options-item-span">
                {this.props.lang === "fr" ? "Modifier" : "Edit"}
              </span>
            </div>

            <div
              className="comment-options-item comment-options-item-delete"
              onClick={() => {
                this.props.handleDeleteComment(this.state.comment.id);
                this.handleClickToggle();
              }}
            >
              <img
                src="/static/home/svg/delete.svg"
                className="comment-options-item-img"
              />
              <span className="btn-del-comment comment-options-item-span">
              {this.props.lang === "fr" ? "Supprimer" : "Delete"}
              </span>
            </div>
          </ul>
        </div>
      </React.Fragment>
    );
  }
}
