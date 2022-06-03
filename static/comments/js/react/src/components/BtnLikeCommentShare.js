class BtnLikeCommentShare extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="box-action-icon">
        <button onClick={() => this.props.handleLikeorUnlike()}>
          <img
            src={
              this.props.isLike
                ? "/static/home/svg/like.svg"
                : "/static/home/svg/unlike.svg"
            }
          />
          <span style={{ color: this.props.isLike ? "#1abc9c" : "#f1f1f1" }}>
            J'aime
          </span>
        </button>

        <button onClick={() => this.props.handleClickToggle()}>
          <img src="/static/home/svg/comment.svg" />
          <span>Commenter</span>
        </button>

        <button>
          <img src="/static/home/svg/share.svg" />
          <span>Partager</span>
        </button>
      </div>
    );
  }
}
