class BtnLikeCommentShare extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="box-action-icon">
        <button
          className="like-btn"
          onClick={() => this.props.handleLikeorUnlike()}
        >
          <img
            className="icon-like-comment-share"
            src={
              this.props.isLike
                ? "/static/home/svg/like.svg"
                : "/static/home/svg/unlike.svg"
            }
          />
          <span
            className="label-like-comment-share"
            style={{ color: this.props.isLike ? "#1abc9c" : "#f1f1f1" }}
          >
            J'aime
          </span>
        </button>

        <button
          className="action-icon box-comment btn-container-comment-toggle"
          onClick={() => this.props.handleClickToggle()}
        >
          <img
            src="/static/home/svg/comment.svg"
            className="icon-like-comment-share"
          />
          <span className="label-like-comment-share">Commenter</span>
        </button>

        <button className="action-icon box-share">
          <img
            src="/static/home/svg/share.svg"
            className="icon-like-comment-share"
          />
          <span className="label-like-comment-share">Partager</span>
        </button>
      </div>
    );
  }
}
