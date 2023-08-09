const fileInput = document.getElementById("input-file");
const fileOutput = document.getElementById("output-file");
const fileBtn = document.getElementById("fileBtn");
const submitBtn = document.getElementById("submitBtn");
const body = document.querySelector('body');
const modal = document.querySelector('.modal');

/* 1. 수동으로 파일버튼 눌러서 업로드하는 경우 */
// 파일 업로드 시 제출 버튼 생성 함수
function handleFileUp(event) {
    const files = event.target.files;
    fileOutput.textContent = Array.from(files).map(file=> file.name).join("\n")
    changeBtn();
}
// 업로드 시 파일 업로드 => 제출 버튼으로 변경하는 함수
function changeBtn() {
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

/* 2. 모달(드래그) 통해 파일 업로드하는 경우 */
//파일 넣는 부분에 이벤트가 발생했을 때 
fileInput.onchange = function (e) {
    modal.classList.toggle('show');//모달창을 띄운다.
}

//body에 드래그하고 있을 때
body.addEventListener('dragover', function (e) {
    e.preventDefault();
    e.stopPropagation();

    modal.classList.add('show');//모달창을 띄운다. add가 아닌 toggle로 하면 모달창이 껏다 켜졌다 반복함.
});

//body에 드래그 드랍했을 때
body.addEventListener('drop', function (e) {
    e.preventDefault();
    e.stopPropagation();

    const files = e.dataTransfer.files; // 업로드한 파일 List
    handleFiles(files);                 // 업로드 파일이름 추출 함수 호출
    changeBtn();                        //버튼 글자 'Upload File'에서 'Submit'으로 바꾸기
});

// 업로드한 파일명 추출하는 함수
function handleFiles(files) {
    let filename;
    for (const file of files) {
        filename = file.name;
    }
    modal.classList.remove('show'); // 드롭 후 모달창 닫기
    fileOutput.textContent = filename;
    fileInput.files = files;
}