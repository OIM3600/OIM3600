function greet(name) {
  // alert("hello, " + name);
  const heading = document.querySelector("h1");
  heading.innerText = "hello, " + name;
}

const btn = document.querySelector("button");

btn.addEventListener("click", function (event) {
  const nameInput = document.querySelector("#name-input").value;
  greet(nameInput);
  event.preventDefault();
});
