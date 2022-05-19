class LikeFormButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      postId: props.postId,
      classTogglePostDetail: props.classTogglePostDetail,
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile,
      handleAddComment: props.handleAddComment,
      msg: "",
    };
  }

  render() {
    return (
      <form className="like-form">
        <input type="hidden" name="post_id" value="{{post.id}}" />
        <button type="submit" className="like-btn{{post.id}}">
          {/* {% if user not in post.liked.all %} */}
          <img
            id="like-img{{post.id}}"
            className="icon-like-comment-share"
            src="/static/home/svg/unlike.svg"
          />
          <span className="like-text{{post.id}} label-like-comment-share">
            J'aime
          </span>
          {/* {% else %} */}
          {/* <img
            id="like-img{{post.id}}"
            className="icon-like-comment-share"
            src="/static/home/svg/like.svg"
          />
          <span className="like-text{{post.id}} text-like_unlike-span label-like-comment-share">
            J'aime
          </span> */}
          {/* {% endif %} */}
        </button>
      </form>
    );
  }
}
