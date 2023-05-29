const fileInput = document.getElementById("input-file");
const fileOutput = document.getElementById("output-file");
const fileBtn = document.getElementById("fileBtn");
const submitBtn = document.getElementById("submitBtn");

// 파일 업로드 시 제출 버튼 생성 함수
function handleFileUp(event) {
    const files = event.target.files;
    fileOutput.textContent = Array.from(files).map(file=> file.name).join("\n")
    fileBtn.setAttribute("hidden", "hidden");
    submitBtn.setAttribute("type", "submit");
}

// 업로드 버튼 마우스 올려놓을 경우
function handleBtnEnter(){
    fileBtn.style.backgroundColor = "#183e84";
    submitBtn.style.backgroundColor = "#183e84";
}

// 업로드 버튼 마우스 떠날 경우
function handleBtnLeave(){
    fileBtn.style.backgroundColor = "cornflowerblue";
    submitBtn.style.backgroundColor = "cornflowerblue";
}

fileBtn.addEventListener("mouseenter", handleBtnEnter);
fileBtn.addEventListener("mouseleave", handleBtnLeave);
submitBtn.addEventListener("mouseenter", handleBtnEnter);
submitBtn.addEventListener("mouseleave", handleBtnLeave);

fileInput.addEventListener("input", handleFileUp);