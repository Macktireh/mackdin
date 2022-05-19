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
      comment: props.comment,
      isEditingComment: false,
      handleEditComment: props.handleEditComment,
      handleDeleteComment: props.handleDeleteComment,
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
        {
          className: "container-comment-list",
          id: "container-comment-list" + this.state.comment.id
        },
        this.state.comment.current_user === this.state.comment.comment_author ? React.createElement(Option, {
          comment: this.state.comment,
          handleIsEditingComment: this.handleIsEditingComment,
          handleDeleteComment: this.state.handleDeleteComment
        }) : null,
        React.createElement(
          "a",
          { href: "/profile/" + this.state.comment.user_profile_pseudo + "/" },
          React.createElement("img", {
            id: "container-comment-list-img-profile",
            src: this.state.comment.user_profile_img
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
              {
                className: "comment-info-content-I",
                id: "comment-info-content-I-" + this.state.comment.id
              },
              React.createElement(
                "strong",
                null,
                React.createElement(
                  "a",
                  { href: "/profile/" + this.state.comment.user_profile_pseudo + "/" },
                  this.state.comment.comment_author_first_name,
                  " ",
                  this.state.comment.comment_author_last_name
                ),
                this.state.comment.comment_author === this.state.comment.post_author ? React.createElement(
                  "span",
                  { id: "author_post_and_comment" },
                  "Auteur"
                ) : null
              ),
              React.createElement(
                "p",
                { id: "comment-author-profile-title" },
                this.state.comment.user_profile_bio
              )
            ),
            React.createElement(
              "small",
              null,
              this.state.comment.comment_date_added
            )
          ),
          React.createElement(
            "div",
            { className: "comment-text-content" },
            this.state.isEditingComment ? React.createElement(
              "form",
              null,
              React.createElement("textarea", {
                autoFocus: true,
                className: "msg-text-p-" + this.state.comment.id,
                id: this.state.comment.post_id,
                defaultValue: this.state.comment.comment_message,
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
                        _this2.state.handleEditComment({
                          payload: {
                            msg: _this2.state.msg,
                            post_id: _this2.state.comment.post_id,
                            comment_id: _this2.state.comment.id
                          }
                        });
                      }
                      _this2.handleIsEditingComment();
                    },
                    disabled: this.state.msg === ""
                  },
                  "Valider"
                ),
                React.createElement(
                  "div",
                  {
                    className: "cancel",
                    onClick: function onClick() {
                      return _this2.handleIsEditingComment();
                    }
                  },
                  "Annuler"
                )
              )
            ) : React.createElement(
              "p",
              {
                className: "msg-text-p-" + this.state.comment.id,
                id: this.state.comment.post_id
              },
              this.state.comment.comment_message
            )
          )
        )
      );
    }
  }]);

  return ListComments;
}(React.Component);