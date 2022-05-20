var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Option = function (_React$Component) {
  _inherits(Option, _React$Component);

  function Option(props) {
    _classCallCheck(this, Option);

    var _this = _possibleConstructorReturn(this, (Option.__proto__ || Object.getPrototypeOf(Option)).call(this, props));

    _this.state = {
      comment: props.comment,
      toggle: false
    };
    return _this;
  }

  _createClass(Option, [{
    key: "handleClickToggle",
    value: function handleClickToggle() {
      var toggle = this.state.toggle;
      this.setState({ toggle: !toggle });
    }
  }, {
    key: "render",
    value: function render() {
      var _this2 = this;

      return React.createElement(
        React.Fragment,
        null,
        React.createElement(
          "div",
          {
            className: "comment-options-btn",
            onClick: function onClick() {
              return _this2.handleClickToggle();
            }
          },
          React.createElement("span", { id: "btn-point" }),
          React.createElement("span", { id: "btn-point" }),
          React.createElement("span", { id: "btn-point" })
        ),
        React.createElement(
          "div",
          {
            className: this.state.toggle ? "comment-options-actions-container" : "comment-options-actions-container display-none"
          },
          React.createElement(
            "ul",
            null,
            React.createElement(
              "div",
              {
                className: "comment-options-item comment-options-item-edit",
                onClick: function onClick() {
                  _this2.props.handleIsEditingComment();
                  _this2.handleClickToggle();
                }
              },
              React.createElement("img", {
                src: "/static/home/svg/edit.svg",
                className: "comment-options-item-img"
              }),
              React.createElement(
                "span",
                { className: "btn-edit-comment comment-options-item-span" },
                "Modifier"
              )
            ),
            React.createElement(
              "div",
              {
                className: "comment-options-item comment-options-item-delete",
                onClick: function onClick() {
                  _this2.props.handleDeleteComment(_this2.state.comment.id);
                  _this2.handleClickToggle();
                }
              },
              React.createElement("img", {
                src: "/static/home/svg/delete.svg",
                className: "comment-options-item-img"
              }),
              React.createElement(
                "span",
                { className: "btn-del-comment comment-options-item-span" },
                "Supprimer"
              )
            )
          )
        )
      );
    }
  }]);

  return Option;
}(React.Component);