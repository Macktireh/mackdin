var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } else { return Array.from(arr); } }

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
      nberComment: props.nberComment,
      isLikeComment: false,
      nberLikeCommnet: 0,
      page: 2,
      canRequest: true
    };

    _this.handleGetComment = _this.handleGetComment.bind(_this);
    _this.handleGetCommentPaginator = _this.handleGetCommentPaginator.bind(_this);

    _this.handlIsLike = _this.handlIsLike.bind(_this);
    _this.handleLikeorUnlike = _this.handleLikeorUnlike.bind(_this);
    _this.handleLikeorUnlikeComment = _this.handleLikeorUnlikeComment.bind(_this);

    _this.handleClickToggle = _this.handleClickToggle.bind(_this);

    _this.handleAddComment = _this.handleAddComment.bind(_this);
    _this.handleEditComment = _this.handleEditComment.bind(_this);
    _this.handleDeleteComment = _this.handleDeleteComment.bind(_this);
    return _this;
  }

  _createClass(AppLikeComment, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      this.handleGetComment();
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
    key: "handleClickToggle",
    value: function handleClickToggle() {
      var toggle = this.state.classTogglePostDetail;
      this.setState({ classTogglePostDetail: !toggle });
    }
  }, {
    key: "handleGetComment",
    value: function handleGetComment() {
      var _this2 = this;

      fetch(this.state.urlGetData, { method: "GET" }).then(function (res) {
        return res.json();
      }).then(function (res) {
        return _this2.setState({ listComments: res.data });
      });
    }
  }, {
    key: "handleGetCommentPaginator",
    value: function handleGetCommentPaginator() {
      var _this3 = this;

      var params = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : "";

      fetch(this.state.urlGetData + "?page=" + this.state.page, { method: "GET" }).then(function (res) {
        if (res.status === 200) {
          return res.json();
        } else {
          _this3.setState({ canRequest: false });
        }
      }).then(function (res) {
        if (res.data.length > 0) {
          // return res.json();

          copyComment = _this3.state.listComments.slice();
          comments = [].concat(_toConsumableArray(copyComment));
          res.data.forEach(function (item2) {
            var foundIndex = comments.findIndex(function (item1) {
              return item1.id === item2.id;
            });
            if (foundIndex === -1) {
              comments.push(item2);
            } else {
              comments[foundIndex] = item2;
            }
          });
          _this3.setState({ listComments: comments });
          _this3.setState({ page: _this3.state.page + 1 });
          console.log("res", res.data);
          console.log("comments", comments);
          console.log("page", _this3.state.page);
        }
      });
    }
  }, {
    key: "handlIsLike",
    value: function handlIsLike(obj, type) {
      if (obj === "post") {
        if (type === "Unlike") {
          this.setState({ isLike: false });
        } else if (type === "Like") {
          this.setState({ isLike: true });
        }
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
    key: "updateNberLikeComment",
    value: function updateNberLikeComment(id, type) {
      var copyComment = this.state.listComments.slice();
      var comments = [].concat(_toConsumableArray(copyComment));
      comments = comments.map(function (item) {
        if (item.id === id) {
          if (type === "Unlike") {
            item.comment_is_like = false;
            item.comment_number_like = item.comment_number_like - 1;
          } else if (type === "Like") {
            item.comment_is_like = true;
            item.comment_number_like = item.comment_number_like + 1;
          }
          return item;
        }
        return item;
      });
      this.setState({ listComments: comments });
    }
  }, {
    key: "handleLikeorUnlikeComment",
    value: function handleLikeorUnlikeComment(comment_id) {
      var _this4 = this;

      var formData = new FormData();
      formData.append("comment_id", comment_id);

      fetch(this.configFetch("/comment/like/", "POST", formData)).then(function (res) {
        return res.json();
      }).then(function (res) {
        _this4.handlIsLike("comment", res.value);
        _this4.updateNberLikeComment(comment_id, res.value);
      });
    }
  }, {
    key: "handleLikeorUnlike",
    value: function handleLikeorUnlike() {
      var _this5 = this;

      var formData = new FormData();
      formData.append("post_id", this.state.postId);

      fetch(this.configFetch("/feed/like/", "POST", formData)).then(function (res) {
        return res.json();
      }).then(function (res) {
        _this5.handlIsLike("post", res.value);
        _this5.updateNberLike(res.value);
      });
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
    key: "handleAddComment",
    value: function handleAddComment(action) {
      var _this6 = this;

      var data = JSON.stringify({
        message: action.payload.msg,
        id_post: action.payload.post_id,
        id_comment: null
      });

      fetch(this.configFetch(this.state.urlAddUpdateComment, "POST", data)).then(function (res) {
        return res.json();
      }).then(function (res) {
        var commentData = _this6.state.listComments.slice();
        commentData.push(res);
        _this6.setState({ listComments: commentData });
      }).then(function () {
        _this6.updateNberComment("ADD");
      });
    }
  }, {
    key: "handleEditComment",
    value: function handleEditComment(action) {
      var _this7 = this;

      var data = JSON.stringify({
        message: action.payload.msg,
        id_post: action.payload.post_id,
        id_comment: action.payload.comment_id
      });

      fetch(this.configFetch(this.state.urlAddUpdateComment, "POST", data)).then(function () {
        var commentData1 = _this7.state.listComments.slice();
        commentData1.filter(function (comment) {
          if (comment.id === action.payload.comment_id) {
            comment.comment_message = action.payload.msg;
            _this7.setState({ listComments: commentData1 });
          }
        });
      });
    }
  }, {
    key: "handleDeleteComment",
    value: function handleDeleteComment(id) {
      var _this8 = this;

      var formData = new FormData();
      formData.append("id_comment", id);
      if (window.confirm("Vous êtes sûr de vouloir supprimer")) {
        fetch(this.configFetch("/comment/delete-comment/", "POST", formData)).then(function () {
          var filteredListComments = _this8.state.listComments.filter(function (t) {
            return t.id !== id;
          });
          _this8.setState({ listComments: filteredListComments });
          _this8.updateNberComment("DELETE");
        });
      }
    }
  }, {
    key: "render",
    value: function render() {
      var _this9 = this;

      return React.createElement(
        React.Fragment,
        null,
        React.createElement(
          "div",
          { className: "post-footer" },
          React.createElement(InfoLikeComment, {
            nberComment: this.state.nberComment,
            nberLike: this.state.nberLike,
            handleClickToggle: this.handleClickToggle
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
            className: this.state.classTogglePostDetail ? "form-comment-list-input-container-global D-none_V-hidden_O-0" : "form-comment-list-input-container-global",
            style: {
              display: this.state.classTogglePostDetail ? "none" : "flex"
            }
          },
          React.createElement(InputForm, {
            postId: this.state.postId,
            imgProfile: this.state.imgProfile,
            handleAddComment: this.handleAddComment
          }),
          React.createElement(
            "div",
            { className: "container-global-comment-list" },
            this.state.listComments.length > 0 && this.state.listComments.sort(function (a, b) {
              return new Date(a.created_at).getTime() - new Date(b.created_at).getTime();
            }).map(function (comment) {
              return React.createElement(ListComments, {
                key: comment.id,
                comment: comment,
                handleEditComment: _this9.handleEditComment,
                handleDeleteComment: _this9.handleDeleteComment,
                handleLikeorUnlikeComment: _this9.handleLikeorUnlikeComment,
                isLikeComment: _this9.state.isLikeComment,
                nberLikeCommnet: _this9.state.nberLikeCommnet
              });
            })
          ),
          this.state.canRequest && this.state.nberComment > this.state.listComments.length && React.createElement(
            "div",
            {
              className: "voir-plus",
              onClick: this.handleGetCommentPaginator
            },
            "voir plus"
          )
        )
      );
    }
  }]);

  return AppLikeComment;
}(React.Component);