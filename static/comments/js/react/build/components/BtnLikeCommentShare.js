var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var BtnLikeCommentShare = function (_React$Component) {
  _inherits(BtnLikeCommentShare, _React$Component);

  function BtnLikeCommentShare(props) {
    _classCallCheck(this, BtnLikeCommentShare);

    var _this = _possibleConstructorReturn(this, (BtnLikeCommentShare.__proto__ || Object.getPrototypeOf(BtnLikeCommentShare)).call(this, props));

    _this.state = {};
    return _this;
  }

  _createClass(BtnLikeCommentShare, [{
    key: "render",
    value: function render() {
      var _this2 = this;

      return React.createElement(
        "div",
        { className: "box-action-icon" },
        React.createElement(
          "button",
          { onClick: function onClick() {
              return _this2.props.handleLikeorUnlike();
            } },
          React.createElement("img", {
            src: this.props.isLike ? "/static/home/svg/like.svg" : "/static/home/svg/unlike.svg"
          }),
          React.createElement(
            "span",
            { style: { color: this.props.isLike ? "#1abc9c" : "#f1f1f1" } },
            this.props.lang === "fr" ? "J'aime" : "Like"
          )
        ),
        React.createElement(
          "button",
          { onClick: function onClick() {
              return _this2.props.handleClickToggle();
            } },
          React.createElement("img", { src: "/static/home/svg/comment.svg" }),
          React.createElement(
            "span",
            null,
            this.props.lang === "fr" ? "Commenter" : "Comment"
          )
        ),
        React.createElement(
          "button",
          null,
          React.createElement("img", { src: "/static/home/svg/share.svg" }),
          React.createElement(
            "span",
            null,
            this.props.lang === "fr" ? "Partager" : "Share"
          )
        )
      );
    }
  }]);

  return BtnLikeCommentShare;
}(React.Component);