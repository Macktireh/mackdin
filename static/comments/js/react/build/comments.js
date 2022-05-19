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
      classTogglePostDetail: props.classTogglePostDetail,
      urlAddUpdateComment: props.urlAddUpdateComment,
      csrfToken: props.csrfToken,
      imgProfile: props.imgProfile,
      urlGetData: props.urlGetData,
      listComments: []
    };
    return _this;
  }

  _createClass(App, [{
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
    key: "render",
    value: function render() {
      return React.createElement(
        "form",
        {
          title: this.state.postId,
          className: "form-comment-list-input-container-global",
          id: "form-comment-list-input-container-global{{post.id}}",
          method: "post"
        },
        React.createElement(InputForm, {
          postId: this.state.postId,
          classTogglePostDetail: this.state.classTogglePostDetail,
          urlAddUpdateComment: this.state.urlAddUpdateComment,
          csrfToken: this.state.csrfToken,
          imgProfile: this.state.imgProfile
        }),
        React.createElement(
          "div",
          {
            className: "container-global-comment-list",
            id: "container-global-comment-list-" + this.state.postId
          },
          this.state.listComments.length > 0 && this.state.listComments.map(function (comment) {
            return React.createElement(ListComments, { key: comment.id, comment: comment });
          })
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

  var root = ReactDOM.createRoot(div);
  root.render(React.createElement(App, {
    postId: postId,
    classTogglePostDetail: classTogglePostDetail,
    urlAddUpdateComment: urlAddUpdateComment,
    csrfToken: csrfToken,
    imgProfile: imgProfile,
    urlGetData: urlGetData
  }));
});