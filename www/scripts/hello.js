const input = document.querySelector("#name-input");
const heading = document.querySelector("h1");

function greet() {
    const name = input.value;
    console.log(name);
    // window.alert("Hello, " + name);
    const message = `Welcome to my website, ${name}!`;
    heading.innerText = message;
    const speech = new SpeechSynthesisUtterance(message);
    window.speechSynthesis.speak(speech);
    event.preventDefault();
}
const form = document.querySelector("form");
form.addEventListener("submit", () => {
    greet();
});

input.addEventListener("keyup", () => {
    heading.innerText = `Hello, ${input.value}`;
});