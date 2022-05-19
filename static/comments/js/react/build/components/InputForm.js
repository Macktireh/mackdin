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
      postId: props.postId,
      classTogglePostDetail: props.classTogglePostDetail,
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile
    };
    return _this;
  }

  _createClass(InputForm, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        { className: "form-comment-container-input" },
        React.createElement(
          "div",
          { className: "form-content-comment" },
          React.createElement("img", { src: this.state.imgProfile }),
          React.createElement("input", {
            type: "text",
            name: "message",
            id: "input_message_comment-" + this.state.postId,
            className: "input_message_comment_id",
            autoComplete: "off",
            placeholder: "Ajouter un commentaire...",
            required: true
          }),
          React.createElement("input", {
            type: "hidden",
            name: "post_id_comment",
            id: "input_hidden_post_comment-" + this.state.postId,
            value: this.state.postId
          }),
          React.createElement("input", {
            type: "hidden",
            name: "post_id_comment2",
            id: "input_hidden_post_comment2-" + this.state.postId,
            value: ""
          })
        ),
        React.createElement(
          "button",
          {
            className: "btn-send-comment",
            type: "submit",
            name: "submit_c_form",
            title: this.state.postId
          },
          React.createElement("img", { src: "/static/home/svg/send.svg" })
        )
      );
    }
  }]);

  return InputForm;
}(React.Component);