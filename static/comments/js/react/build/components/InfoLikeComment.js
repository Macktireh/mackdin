var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var InfoLikeComment = function (_React$Component) {
  _inherits(InfoLikeComment, _React$Component);

  function InfoLikeComment(props) {
    _classCallCheck(this, InfoLikeComment);

    var _this = _possibleConstructorReturn(this, (InfoLikeComment.__proto__ || Object.getPrototypeOf(InfoLikeComment)).call(this, props));

    _this.state = {};
    return _this;
  }

  _createClass(InfoLikeComment, [{
    key: "render",
    value: function render() {
      var _this2 = this;

      return React.createElement(
        "div",
        { className: "count-likes-comments" },
        React.createElement(
          "div",
          null,
          React.createElement(
            "span",
            null,
            this.props.nberLike > 1 ? this.props.nberLike + " Likes" : this.props.nberLike + " Like"
          )
        ),
        React.createElement(
          "div",
          { className: "comments-count-post" },
          React.createElement(
            "span",
            { id: "comments-num", onClick: function onClick() {
                return _this2.props.handleClickToggle();
              } },
            this.props.nberComment > 1 ? this.props.nberComment + (this.props.lang === "fr" ? " commentaires" : " comments") : this.props.nberComment + (this.props.lang === "fr" ? " commentaire" : " comment")
          )
        )
      );
    }
  }]);

  return InfoLikeComment;
}(React.Component);