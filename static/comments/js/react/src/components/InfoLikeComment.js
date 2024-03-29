class InfoLikeComment extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="count-likes-comments">
        <div>
          <span>
            {this.props.nberLike > 1
              ? this.props.nberLike + " Likes"
              : this.props.nberLike + " Like"}
          </span>
        </div>
        <div className="comments-count-post">
          <span id="comments-num" onClick={() => this.props.handleClickToggle()}>
            {this.props.nberComment > 1
              ? this.props.nberComment + (this.props.lang === "fr" ? " commentaires" : " comments")
              : this.props.nberComment + (this.props.lang === "fr" ? " commentaire" : " comment")}
          </span>
        </div>
      </div>
    );
  }
}
