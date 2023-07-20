const fileInput = document.getElementById("input-file");
const fileOutput = document.getElementById("output-file");
const fileBtn = document.getElementById("fileBtn");
const submitBtn = document.getElementById("submitBtn");
const body = document.querySelector('body');
const modal = document.querySelector('.modal');
let file = document.getElementById("input-file")

// 파일 입력 요소와 드래그 앤 드랍 이벤트를 처리하는 함수
function handleFileSelection(event) {
    const files = event.target.files || event.dataTransfer.files;
    fileOutput.textContent = Array.from(files).map(file => file.name).join("\n");
    fileBtn.setAttribute("hidden", "hidden");
    submitBtn.setAttribute("type", "submit");
}

// 파일 입력 요소 이벤트 리스너 등록
fileInput.addEventListener('input', handleFileSelection);

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

//파일 넣는 부분에 이벤트가 발생했을 때 
file.onchange = function (e) {
    modal.classList.toggle('show');//모달창을 띄운다.
}

//body에 드래그하고 있을 때
body.addEventListener('dragover', function (e) {
    e.preventDefault();
    console.log('dragoverrrr');
    modal.classList.add('show');//모달창을 띄운다. add가 아닌 toggle로 하면 모달창이 껏다 켜졌다 반복함.
});

//body에 드래그 드랍했을 때
body.addEventListener('drop', function (e) {
    e.preventDefault();
    console.log('bodydrop');
    //버튼 글자 'Upload File'에서 'Submit'으로 바꾸기
    handleFileSelection(e);
});

//modal에 드래그 드랍했을 때
modal.addEventListener('drop', function (e) {
    console.log('modaldrop');
    //버튼 글자 'Upload File'에서 'Submit'으로 바꾸기
    // handleFileSelection(e);
});


//modal에 클릭 이벤트가 발생했을 때
modal.addEventListener('click', (event) => {
    
    if (event.target === modal) {//클릭이 모달창 위면
        modal.classList.toggle('show');//모달창을 띄우고

        if (!modal.classList.contains('show')) {
            body.style.overflow = 'auto';
        }
    }
});