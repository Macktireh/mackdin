class InfoLikeComment extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      nberLike: props.nberLike,
      nberComment: props.nberComment,
    };
  }

  render() {
    return (
      <div className="count-likes-comments">
        <div id="likes-count{{post.id}}">
          <span id="likes-num{{post.id}}">
            {this.props.nberLike > 1
              ? this.props.nberLike + " Likes"
              : this.props.nberLike + " Like"}
          </span>
          {/* <span id="text-plural{{post.id}}"></span> */}
        </div>
        <div className="comments-count-post" id="comments-count{{post.id}}">
          <span id="comments-num{{post.id}}">
            {this.props.nberComment > 1
              ? this.props.nberComment + " commentaires"
              : this.props.nberComment + " commentaire"}
          </span>
          {/* <span id="text-plural-comments{{post.id}}">
            commentaire{this.state.nberComment > 0 && "s"}
          </span> */}
        </div>
      </div>
    );
  }
}
