var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var AppLikeComment = function (_React$Component) {
  _inherits(AppLikeComment, _React$Component);

  function AppLikeComment(props) {
    _classCallCheck(this, AppLikeComment);

    var _this = _possibleConstructorReturn(this, (AppLikeComment.__proto__ || Object.getPrototypeOf(AppLikeComment)).call(this, props));

    _this.state = {
      postId: props.postId,
      classTogglePostDetail: props.classTogglePostDetail.toString() === "1",
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile,
      urlGetData: props.urlGetData,
      listComments: [],
      isLike: props.isLike,
      nberLike: props.nberLike,
      nberComment: props.nberComment
    };

    _this.handlIsLike = _this.handlIsLike.bind(_this);
    _this.handleLikeorUnlike = _this.handleLikeorUnlike.bind(_this);

    _this.handleClickToggle = _this.handleClickToggle.bind(_this);

    _this.handleAddComment = _this.handleAddComment.bind(_this);
    _this.handleEditComment = _this.handleEditComment.bind(_this);
    _this.handleDeleteComment = _this.handleDeleteComment.bind(_this);
    return _this;
  }

  _createClass(AppLikeComment, [{
    key: "handleClickToggle",
    value: function handleClickToggle() {
      var toggle = this.state.classTogglePostDetail;
      this.setState({ classTogglePostDetail: !toggle });
    }
  }, {
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this2 = this;

      fetch(this.state.urlGetData, { method: "GET" }).then(function (res) {
        return res.json();
      }).then(function (res) {
        return _this2.setState({ listComments: res.data });
      });
    }
  }, {
    key: "handlIsLike",
    value: function handlIsLike(type) {
      if (type === "Unlike") {
        this.setState({ isLike: false });
      } else if (type === "Like") {
        this.setState({ isLike: true });
      }
    }
  }, {
    key: "updateNberLike",
    value: function updateNberLike(type) {
      var num = parseInt(this.state.nberLike);
      if (type === "Like") {
        this.setState({ nberLike: num + 1 });
      } else {
        this.setState({ nberLike: num - 1 });
      }
    }
  }, {
    key: "updateNberComment",
    value: function updateNberComment(type) {
      var num = parseInt(this.state.nberComment);
      if (type === "ADD") {
        this.setState({ nberComment: num + 1 });
      } else if (type === "DELETE") {
        this.setState({ nberComment: num - 1 });
      }
    }
  }, {
    key: "configFetch",
    value: function configFetch(url, method, data) {
      var request = new Request(url, {
        method: method,
        headers: {
          Accept: "application/json",
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": this.state.csrfToken
        },
        body: data
      });
      return request;
    }
  }, {
    key: "handleLikeorUnlike",
    value: function handleLikeorUnlike() {
      var _this3 = this;

      var formData = new FormData();
      formData.append("post_id", this.state.postId);

      fetch(this.configFetch("/feed/like/", "POST", formData)).then(function (res) {
        return res.json();
      }).then(function (res) {
        _this3.handlIsLike(res.value);
        _this3.updateNberLike(res.value);
      });
    }
  }, {
    key: "handleAddComment",
    value: function handleAddComment(action) {
      var _this4 = this;

      var data = JSON.stringify({
        message: action.payload.msg,
        id_post: action.payload.post_id,
        id_comment: null
      });

      fetch(this.configFetch(this.state.urlAddUpdateComment, "POST", data)).then(function (res) {
        return res.json();
      }).then(function (res) {
        var commentData = _this4.state.listComments.slice();
        commentData.push(res);
        _this4.setState({ listComments: commentData });
      }).then(function () {
        _this4.updateNberComment("ADD");
      });
    }
  }, {
    key: "handleEditComment",
    value: function handleEditComment(action) {
      var _this5 = this;

      var data = JSON.stringify({
        message: action.payload.msg,
        id_post: action.payload.post_id,
        id_comment: action.payload.comment_id
      });

      fetch(this.configFetch(this.state.urlAddUpdateComment, "POST", data)).then(function () {
        var commentData1 = _this5.state.listComments.slice();
        commentData1.filter(function (comment) {
          if (comment.id === action.payload.comment_id) {
            comment.comment_message = action.payload.msg;
            _this5.setState({ listComments: commentData1 });
          }
        });
      });
    }
  }, {
    key: "handleDeleteComment",
    value: function handleDeleteComment(id) {
      var _this6 = this;

      var formData = new FormData();
      formData.append("id_comment", id);
      if (window.confirm("Vous êtes sûr de vouloir supprimer")) {
        fetch(this.configFetch("/comment/delete-comment/", "POST", formData)).then(function () {
          var filteredListComments = _this6.state.listComments.filter(function (t) {
            return t.id !== id;
          });
          _this6.setState({ listComments: filteredListComments });
          _this6.updateNberComment("DELETE");
        });
      }
    }
  }, {
    key: "render",
    value: function render() {
      var _this7 = this;

      return React.createElement(
        React.Fragment,
        null,
        React.createElement(
          "div",
          { className: "post-footer" },
          React.createElement(InfoLikeComment, {
            nberComment: this.state.nberComment,
            nberLike: this.state.nberLike
          }),
          React.createElement("hr", null),
          React.createElement(BtnLikeCommentShare, {
            handleClickToggle: this.handleClickToggle,
            handleLikeorUnlike: this.handleLikeorUnlike,
            isLike: this.state.isLike
          })
        ),
        React.createElement(
          "div",
          {
            className: this.state.classTogglePostDetail ? "form-comment-list-input-container-global D-none_V-hidden_O-0" : "form-comment-list-input-container-global"
          },
          React.createElement(InputForm, {
            postId: this.state.postId,
            imgProfile: this.state.imgProfile,
            handleAddComment: this.handleAddComment
          }),
          React.createElement(
            "div",
            { className: "container-global-comment-list" },
            this.state.listComments.length > 0 && this.state.listComments.map(function (comment) {
              return React.createElement(ListComments, {
                key: comment.id,
                comment: comment,
                handleEditComment: _this7.handleEditComment,
                handleDeleteComment: _this7.handleDeleteComment
              });
            })
          )
        )
      );
    }
  }]);

  return AppLikeComment;
}(React.Component);