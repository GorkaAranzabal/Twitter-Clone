const tweetSound = new Audio("static/tweet.wav");

document.querySelector("form").addEventListener("submit", () => {
  tweetSound.play();
});
