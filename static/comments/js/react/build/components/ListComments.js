var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var ListComments = function (_React$Component) {
  _inherits(ListComments, _React$Component);

  function ListComments(props) {
    _classCallCheck(this, ListComments);

    var _this = _possibleConstructorReturn(this, (ListComments.__proto__ || Object.getPrototypeOf(ListComments)).call(this, props));

    _this.state = {
      isEditingComment: false,
      msg: ""
    };
    _this.handleIsEditingComment = _this.handleIsEditingComment.bind(_this);
    return _this;
  }

  _createClass(ListComments, [{
    key: "handleIsEditingComment",
    value: function handleIsEditingComment() {
      var isEditingComment = this.state.isEditingComment;
      this.setState({ isEditingComment: !isEditingComment });
    }
  }, {
    key: "render",
    value: function render() {
      var _this2 = this;

      return React.createElement(
        "div",
        { className: "container-comment-list" },
        this.props.comment.current_user === this.props.comment.comment_author ? React.createElement(OptionComment, {
          comment: this.props.comment,
          handleIsEditingComment: this.handleIsEditingComment,
          handleDeleteComment: this.props.handleDeleteComment
        }) : null,
        React.createElement(
          "a",
          { href: "/profile/" + this.props.comment.user_profile_pseudo + "/" },
          React.createElement("img", {
            id: "container-comment-list-img-profile",
            src: this.props.comment.user_profile_img
          })
        ),
        React.createElement(
          "div",
          { className: "comment-content-box" },
          React.createElement(
            "div",
            { className: "comment-info-content" },
            React.createElement(
              "div",
              { className: "comment-info-content-I" },
              React.createElement(
                "strong",
                null,
                React.createElement(
                  "a",
                  { href: "/profile/" + this.props.comment.user_profile_pseudo + "/" },
                  this.props.comment.comment_author_first_name,
                  " ",
                  this.props.comment.comment_author_last_name
                ),
                this.props.comment.comment_author === this.props.comment.post_author ? React.createElement(
                  "span",
                  { id: "author_post_and_comment" },
                  this.props.lang === "fr" ? "Auteur" : "Author"
                ) : null
              ),
              React.createElement(
                "p",
                { id: "comment-author-profile-title" },
                this.props.comment.user_profile_bio
              )
            ),
            React.createElement(
              "small",
              null,
              this.props.comment.comment_date_added
            )
          ),
          this.state.isEditingComment ? React.createElement(
            "form",
            null,
            React.createElement("textarea", {
              autoFocus: true,
              defaultValue: this.props.comment.comment_message,
              onChange: function onChange(e) {
                return _this2.setState({ msg: e.target.value });
              }
            }),
            React.createElement(
              "div",
              { className: "box-btn" },
              React.createElement(
                "button",
                {
                  onClick: function onClick(e) {
                    e.preventDefault();
                    if (_this2.state.msg !== "") {
                      _this2.props.handleEditComment({
                        payload: {
                          msg: _this2.state.msg,
                          post_id: _this2.props.comment.post_id,
                          comment_id: _this2.props.comment.id
                        }
                      });
                    }
                    _this2.handleIsEditingComment();
                  },
                  disabled: this.state.msg === ""
                },
                this.props.lang === "fr" ? "Valider" : "Save"
              ),
              React.createElement(
                "div",
                {
                  className: "cancel",
                  onClick: function onClick() {
                    return _this2.handleIsEditingComment();
                  }
                },
                this.props.lang === "fr" ? "Annuler" : "Cancel"
              )
            )
          ) : React.createElement(
            "p",
            null,
            this.props.comment.comment_message
          )
        ),
        React.createElement("span", null),
        React.createElement(
          "div",
          { className: "comment-like-container" },
          React.createElement(
            "span",
            {
              className: this.props.comment.comment_is_like ? "comment-like active" : "comment-like",
              onClick: function onClick() {
                return _this2.props.handleLikeorUnlikeComment(_this2.props.comment.id);
              }
            },
            this.props.lang === "fr" ? "J'aime" : "Like"
          ),
          React.createElement("span", { className: "sep" }),
          React.createElement(
            "div",
            null,
            React.createElement("img", { src: "/static/home/svg/unlike.svg", alt: " button like" }),
            this.props.comment.comment_number_like
          ),
          React.createElement(
            "span",
            { className: "sep2" },
            "|"
          ),
          React.createElement(
            "span",
            { className: "comment-like" },
            this.props.lang === "fr" ? "Répondre" : "Reply"
          )
        )
      );
    }
  }]);

  return ListComments;
}(React.Component);