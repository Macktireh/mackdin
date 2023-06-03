const aside = document.querySelector(".container-aside-1");
const lang = document.getElementById("language_code").value;
const options = {
  method: "GET",
  headers: {
    "X-RapidAPI-Host": "free-news.p.rapidapi.com",
    "X-RapidAPI-Key": "7dd7c1ff69msh8d88e46f019579fp1a47cdjsn9fc979eccfb3",
  },
};

fetch(
  `https://free-news.p.rapidapi.com/v1/search?q=Microsoft&lang=${lang}&page_size=10`,
  options
)
  .then((response) => response.json())
  .then((response) => response.articles)
  .then((data) => {
    // console.log(data)
    data.forEach((article) => {
      aside.innerHTML += `
      <a href="${article.link}" target="_blank">
        <li class="box-actu">
          <p>${article.title}</p>
          <small>il y a ${timeSince(article.published_date)}</small>
        </li>
      </a>
      `;
    });
  })
  .catch();

var timeSince = function (date) {
  if (typeof date !== "object") {
    date = new Date(date);
  }

  var seconds = Math.floor((new Date() - date) / 1000);
  var intervalType;

  var interval = Math.floor(seconds / 31536000);
  if (interval >= 1) {
    intervalType = "année";
  } else {
    interval = Math.floor(seconds / 2592000);
    if (interval >= 1) {
      intervalType = "mois";
    } else {
      interval = Math.floor(seconds / 86400);
      if (interval >= 1) {
        intervalType = "jour";
      } else {
        interval = Math.floor(seconds / 3600);
        if (interval >= 1) {
          intervalType = "heure";
        } else {
          interval = Math.floor(seconds / 60);
          if (interval >= 1) {
            intervalType = "minute";
          } else {
            interval = seconds;
            intervalType = "seconde";
          }
        }
      }
    }
  }

  if (interval > 1 || interval === 0) {
    intervalType += "s";
  }

  return interval + " " + intervalType;
};
