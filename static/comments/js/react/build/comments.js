var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var App = function (_React$Component) {
  _inherits(App, _React$Component);

  function App(props) {
    _classCallCheck(this, App);

    var _this = _possibleConstructorReturn(this, (App.__proto__ || Object.getPrototypeOf(App)).call(this, props));

    _this.state = {
      postId: props.postId,
      classTogglePostDetail: props.classTogglePostDetail.toString() === "1",
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile,
      urlGetData: props.urlGetData,
      listComments: [],
      nberLike: props.nberLike,
      nberComment: props.nberComment
    };
    _this.handleAddComment = _this.handleAddComment.bind(_this);
    _this.handleEditComment = _this.handleEditComment.bind(_this);
    _this.handleDeleteComment = _this.handleDeleteComment.bind(_this);
    return _this;
  }
  // D-none_V-hidden_O-0


  _createClass(App, [{
    key: "handleClickToggle",
    value: function handleClickToggle() {
      var toggle = this.state.classTogglePostDetail;
      this.setState({ classTogglePostDetail: !toggle });
    }
  }, {
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this2 = this;

      fetch(this.state.urlGetData, { method: "GET" }).then(function (response) {
        return response.json();
      }).then(function (res) {
        return _this2.setState({ listComments: res.data });
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
      var _this3 = this;

      fetch(this.state.urlAddUpdateComment, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          Accept: "application/json",
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": this.state.csrfToken
        },
        body: JSON.stringify({
          message: action.payload.msg,
          id_post: action.payload.post_id,
          id_comment: null
        })
      }).then(function (res) {
        return res.json();
      }).then(function (res) {
        // console.log(res);
        var commentData = _this3.state.listComments.slice();
        commentData.push(res);
        _this3.setState({ listComments: commentData });
      }).then(function () {
        _this3.updateNberComment("ADD");
      });
    }
  }, {
    key: "handleEditComment",
    value: function handleEditComment(action) {
      var _this4 = this;

      fetch(this.state.urlAddUpdateComment, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          Accept: "application/json",
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": this.state.csrfToken
        },
        body: JSON.stringify({
          message: action.payload.msg,
          id_post: action.payload.post_id,
          id_comment: action.payload.comment_id
        })
      }).then(function () {
        var commentData1 = _this4.state.listComments.slice();
        commentData1.filter(function (comment) {
          if (comment.id === action.payload.comment_id) {
            comment.comment_message = action.payload.msg;
            _this4.setState({ listComments: commentData1 });
          }
        });
      });
    }
  }, {
    key: "handleDeleteComment",
    value: function handleDeleteComment(id) {
      var _this5 = this;

      var formData = new FormData();
      formData.append("id_comment", id);

      fetch("/comment/delete-comment/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": this.state.csrfToken
        },
        body: formData
      }).then(function () {
        window.confirm("Vous êtes sûr de vouloir supprimer") && _this5.componentDidMount();
      }).then(function () {
        _this5.updateNberComment("DELETE");
      });
    }
  }, {
    key: "render",
    value: function render() {
      var _this6 = this;

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
          React.createElement(
            "div",
            { className: "box-action-icon" },
            React.createElement(LikeFormButton, null),
            React.createElement(
              "button",
              {
                className: "action-icon box-comment btn-container-comment-toggle",
                id: "{{post.id}}",
                onClick: function onClick() {
                  return _this6.handleClickToggle();
                }
              },
              React.createElement("img", {
                src: "/static/home/svg/comment.svg",
                className: "icon-like-comment-share",
                id: "{{post.id}}"
              }),
              React.createElement(
                "span",
                { id: "{{post.id}}", className: "label-like-comment-share" },
                "Commenter"
              )
            ),
            React.createElement(
              "button",
              { className: "action-icon box-share" },
              React.createElement("img", {
                src: "/static/home/svg/share.svg",
                className: "icon-like-comment-share"
              }),
              React.createElement(
                "span",
                { className: "label-like-comment-share" },
                "Partager"
              )
            )
          )
        ),
        React.createElement(
          "div",
          {
            title: this.state.postId,
            className: this.state.classTogglePostDetail ? "form-comment-list-input-container-global D-none_V-hidden_O-0" : "form-comment-list-input-container-global",
            id: "form-comment-list-input-container-global" + this.state.postId,
            method: "post"
          },
          React.createElement(InputForm, {
            postId: this.state.postId,
            classTogglePostDetail: this.state.classTogglePostDetail,
            urlAddUpdateComment: this.state.urlAddUpdateComment,
            csrfToken: this.state.csrfToken,
            imgProfile: this.state.imgProfile,
            handleAddComment: this.handleAddComment
          }),
          React.createElement(
            "div",
            {
              className: "container-global-comment-list",
              id: "container-global-comment-list-" + this.state.postId
            },
            this.state.listComments.length > 0 && this.state.listComments.map(function (comment) {
              return React.createElement(ListComments, {
                key: comment.id,
                comment: comment,
                handleEditComment: _this6.handleEditComment,
                handleDeleteComment: _this6.handleDeleteComment
              });
            })
          )
        )
      );
    }
  }]);

  return App;
}(React.Component);

// export default index;

document.querySelectorAll(".root-comments").forEach(function (div) {
  var postId = div.dataset.postId;
  var classTogglePostDetail = div.dataset.classTogglePostDetail;
  var urlAddUpdateComment = div.dataset.urlAddUpdateComment;
  var csrfToken = div.dataset.csrfToken;
  var imgProfile = div.dataset.imgProfile;
  var urlGetData = div.dataset.urlGetData;
  var nberLike = div.dataset.nberLike;
  var nberComment = div.dataset.nberComment;

  var root = ReactDOM.createRoot(div);
  root.render(React.createElement(App, {
    postId: postId,
    classTogglePostDetail: classTogglePostDetail,
    urlAddUpdateComment: urlAddUpdateComment,
    csrfToken: csrfToken,
    imgProfile: imgProfile,
    urlGetData: urlGetData,
    nberLike: nberLike,
    nberComment: nberComment
  }));
});