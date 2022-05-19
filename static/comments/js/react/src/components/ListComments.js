class ListComments extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      comment: props.comment,
      isEditingComment: false,
    };
    this.handleEditingComment = this.handleEditingComment.bind(this);
  }

  handleEditingComment() {
    const isEditingComment = this.state.isEditingComment;
    // console.log(this);
    this.setState({ isEditingComment: !isEditingComment });
  }

  render() {
    return (
      <div
        className="container-comment-list"
        id={"container-comment-list" + this.state.comment.id}
      >
        <Option
          comment={this.state.comment}
          handleEditingComment={this.handleEditingComment}
        />
        <a href="">
          {/* <a href="{% url 'profiles:profile' pseudo=comment.author.profile.pseudo  %}"> */}
          <img
            id="container-comment-list-img-profile"
            src={this.state.comment.user_img_profile}
          />
        </a>
        <div className="comment-content-box">
          <div className="comment-info-content">
            <div
              className="comment-info-content-I"
              id={"comment-info-content-I-" + this.state.comment.id}
            >
              <strong>
                <a href="">
                  {/* <a href="{% url 'profiles:profile' pseudo=comment.author.profile.pseudo  %}"> */}
                  {this.state.comment.comment_author_first_name}{" "}
                  {this.state.comment.comment_author_last_name}
                </a>
                {this.state.comment.comment_author ===
                this.state.comment.post_author ? (
                  <span id="author_post_and_comment">Auteur</span>
                ) : null}
              </strong>
              <p id="comment-author-profile-title">
                {this.state.comment.user_bio}
              </p>
            </div>
            <small>{this.state.comment.comment_date_added}</small>
          </div>
          <div className="comment-text-content">
            {this.state.isEditingComment ? (
              <input
                className={"msg-text-p-" + this.state.comment.id}
                id={this.state.comment.post_id}
                defaultValue={this.state.comment.comment_message}
              />
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
