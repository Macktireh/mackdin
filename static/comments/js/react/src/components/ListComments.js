class ListComments extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isEditingComment: false,
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
      <div className="container-comment-list">
        {this.props.comment.current_user ===
        this.props.comment.comment_author ? (
          <OptionComment
            comment={this.props.comment}
            handleIsEditingComment={this.handleIsEditingComment}
            handleDeleteComment={this.props.handleDeleteComment}
          />
        ) : null}
        <a href={`/profile/${this.props.comment.user_profile_pseudo}/`}>
          <img
            id="container-comment-list-img-profile"
            src={this.props.comment.user_profile_img}
          />
        </a>
        <div className="comment-content-box">
          <div className="comment-info-content">
            <div className="comment-info-content-I">
              <strong>
                <a href={`/profile/${this.props.comment.user_profile_pseudo}/`}>
                  {this.props.comment.comment_author_first_name}{" "}
                  {this.props.comment.comment_author_last_name}
                </a>
                {this.props.comment.comment_author ===
                this.props.comment.post_author ? (
                  <span id="author_post_and_comment">{this.props.lang === "fr" ? "Auteur" : "Author"}</span>
                ) : null}
              </strong>
              <p id="comment-author-profile-title">
                {this.props.comment.user_profile_bio}
              </p>
            </div>
            <small>{this.props.comment.comment_date_added}</small>
          </div>
          {/* <div className="comment-text-content"> */}
          {this.state.isEditingComment ? (
            <form>
              <textarea
                autoFocus
                defaultValue={this.props.comment.comment_message}
                onChange={(e) => this.setState({ msg: e.target.value })}
              />
              <div className="box-btn">
                <button
                  onClick={(e) => {
                    e.preventDefault();
                    if (this.state.msg !== "") {
                      this.props.handleEditComment({
                        payload: {
                          msg: this.state.msg,
                          post_id: this.props.comment.post_id,
                          comment_id: this.props.comment.id,
                        },
                      });
                    }
                    this.handleIsEditingComment();
                  }}
                  disabled={this.state.msg === ""}
                >
                  {this.props.lang === "fr" ? "Valider" : "Save"}
                </button>
                <div
                  className="cancel"
                  onClick={() => this.handleIsEditingComment()}
                >
                  {this.props.lang === "fr" ? "Annuler" : "Cancel"}
                </div>
              </div>
            </form>
          ) : (
            <p>{this.props.comment.comment_message}</p>
          )}
          {/* </div> */}
        </div>
        <span></span>
        <div className="comment-like-container">
          <span
            className={
              this.props.comment.comment_is_like ? "comment-like active" : "comment-like"
            }
            onClick={() =>
              this.props.handleLikeorUnlikeComment(this.props.comment.id)
            }
          >
            {this.props.lang === "fr" ? "J'aime" : "Like"}
          </span>
          <span className="sep"></span>
          <div>
            <img src="/static/home/svg/unlike.svg" alt=" button like" />
            {this.props.comment.comment_number_like}
          </div>
          <span className="sep2">|</span>
          <span className="comment-like">{this.props.lang === "fr" ? "Répondre" : "Reply"}</span>
        </div>
      </div>
    );
  }
}
