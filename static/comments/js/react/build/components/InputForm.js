var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var InputForm = function (_React$Component) {
  _inherits(InputForm, _React$Component);

  function InputForm(props) {
    _classCallCheck(this, InputForm);

    var _this = _possibleConstructorReturn(this, (InputForm.__proto__ || Object.getPrototypeOf(InputForm)).call(this, props));

    _this.state = {
      msg: ""
    };
    return _this;
  }

  _createClass(InputForm, [{
    key: "handleSubmit",
    value: function handleSubmit(e) {
      e.preventDefault();
      this.props.handleAddComment({
        payload: {
          post_id: this.props.postId,
          msg: this.state.msg
        }
      });
    }
  }, {
    key: "render",
    value: function render() {
      var _this2 = this;

      return React.createElement(
        "form",
        {
          onSubmit: function onSubmit(e) {
            _this2.handleSubmit(e);
            _this2.setState({ msg: "" });
          }
        },
        React.createElement(
          "div",
          { className: "form-comment-container-input" },
          React.createElement(
            "div",
            { className: "form-content-comment" },
            React.createElement("img", { src: this.props.imgProfile }),
            React.createElement("textarea", {
              className: "input_message_comment_id",
              autoComplete: "off",
              placeholder: "Ajouter un commentaire...",
              required: true,
              value: this.state.msg,
              onChange: function onChange(e) {
                return _this2.setState({ msg: e.target.value });
              }
            })
          ),
          React.createElement(
            "button",
            {
              className: "btn-send-comment",
              type: "submit",
              disabled: this.state.msg === ""
            },
            React.createElement("img", { src: "/static/home/svg/send.svg" })
          )
        )
      );
    }
  }]);

  return InputForm;
}(React.Component);