class ListComments extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      comment: props.comment,
      isEditingComment: false,
      handleEditComment: props.handleEditComment,
      handleDeleteComment: props.handleDeleteComment,
      msg: "",
    };
    this.handleIsEditingComment = this.handleIsEditingComment.bind(this);
  }

  handleIsEditingComment() {
    const isEditingComment = this.state.isEditingComment;
    this.setState({ isEditingComment: !isEditingComment });
  }

  render() {
    return (
      <div
        className="container-comment-list"
        id={"container-comment-list" + this.state.comment.id}
      >
        {this.state.comment.current_user ===
        this.state.comment.comment_author ? (
          <Option
            comment={this.state.comment}
            handleIsEditingComment={this.handleIsEditingComment}
            handleDeleteComment={this.state.handleDeleteComment}
          />
        ) : null}
        <a href={`/profile/${this.state.comment.user_profile_pseudo}/`}>
          <img
            id="container-comment-list-img-profile"
            src={this.state.comment.user_profile_img}
          />
        </a>
        <div className="comment-content-box">
          <div className="comment-info-content">
            <div
              className="comment-info-content-I"
              id={"comment-info-content-I-" + this.state.comment.id}
            >
              <strong>
                <a href={`/profile/${this.state.comment.user_profile_pseudo}/`}>
                  {this.state.comment.comment_author_first_name}{" "}
                  {this.state.comment.comment_author_last_name}
                </a>
                {this.state.comment.comment_author ===
                this.state.comment.post_author ? (
                  <span id="author_post_and_comment">Auteur</span>
                ) : null}
              </strong>
              <p id="comment-author-profile-title">
                {this.state.comment.user_profile_bio}
              </p>
            </div>
            <small>{this.state.comment.comment_date_added}</small>
          </div>
          <div className="comment-text-content">
            {this.state.isEditingComment ? (
              <form>
                <textarea
                  autoFocus
                  className={"msg-text-p-" + this.state.comment.id}
                  id={this.state.comment.post_id}
                  defaultValue={this.state.comment.comment_message}
                  onChange={(e) => this.setState({ msg: e.target.value })}
                />
                <div className="box-btn">
                  <button
                    onClick={(e) => {
                      e.preventDefault();
                      if (this.state.msg !== "") {
                        this.state.handleEditComment({
                          payload: {
                            msg: this.state.msg,
                            post_id: this.state.comment.post_id,
                            comment_id: this.state.comment.id,
                          },
                        });
                      }
                      this.handleIsEditingComment();
                    }}
                    disabled={this.state.msg === ""}
                  >
                    Valider
                  </button>
                  <div
                    className="cancel"
                    onClick={() => this.handleIsEditingComment()}
                  >
                    Annuler
                  </div>
                </div>
              </form>
            ) : (
              <p
                className={"msg-text-p-" + this.state.comment.id}
                id={this.state.comment.post_id}
              >
                {this.state.comment.comment_message}
              </p>
            )}
          </div>
        </div>
      </div>
    );
  }
}
