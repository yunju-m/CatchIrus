const fileInput = document.getElementById("input-file");
const fileOutput = document.getElementById("output-file");
const fileBtn = document.getElementById("fileBtn");
const submitBtn = document.getElementById("submitBtn");

fileInput.addEventListener('input', (event) =>{
    const files = event.target.files;
    fileOutput.textContent = Array.from(files).map(file=> file.name).join("\n")
    fileBtn.setAttribute("hidden", "hidden");
    submitBtn.setAttribute("type", "submit");
})

function handleBtnEnter(){
    fileBtn.style.backgroundColor = "#183e84";
    submitBtn.style.backgroundColor = "#183e84";
}

function handleBtnLeave(){
    fileBtn.style.backgroundColor = "cornflowerblue";
    submitBtn.style.backgroundColor = "cornflowerblue";
}

function handleBtnClick(event){
    // 새로고침 방지
    event.preventDefault();
    console.log(window.location.href);
    window.location.href = '/file';
}

fileBtn.addEventListener("mouseenter", handleBtnEnter);
fileBtn.addEventListener("mouseleave", handleBtnLeave);
submitBtn.addEventListener("mouseenter", handleBtnEnter);
submitBtn.addEventListener("mouseleave", handleBtnLeave);