var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var LikeFormButton = function (_React$Component) {
  _inherits(LikeFormButton, _React$Component);

  function LikeFormButton(props) {
    _classCallCheck(this, LikeFormButton);

    var _this = _possibleConstructorReturn(this, (LikeFormButton.__proto__ || Object.getPrototypeOf(LikeFormButton)).call(this, props));

    _this.state = {
      postId: props.postId,
      classTogglePostDetail: props.classTogglePostDetail,
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile,
      handleAddComment: props.handleAddComment,
      msg: ""
    };
    return _this;
  }

  _createClass(LikeFormButton, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "form",
        { className: "like-form" },
        React.createElement("input", { type: "hidden", name: "post_id", value: "{{post.id}}" }),
        React.createElement(
          "button",
          { type: "submit", className: "like-btn{{post.id}}" },
          React.createElement("img", {
            id: "like-img{{post.id}}",
            className: "icon-like-comment-share",
            src: "/static/home/svg/unlike.svg"
          }),
          React.createElement(
            "span",
            { className: "like-text{{post.id}} label-like-comment-share" },
            "J'aime"
          )
        )
      );
    }
  }]);

  return LikeFormButton;
}(React.Component);