const fileInput = document.getElementById("input-file");
const fileOutput = document.getElementById("output-file");
const fileBtn = document.getElementById("fileBtn");
const submitBtn = document.getElementById("submitBtn");
const body = document.querySelector('body');
const modal = document.querySelector('.modal');
const modal_post = document.getElementById("modal_post");
let file; // 추가: 선택된 파일을 저장할 변수

// 파일 선택 요소와 드래그 앤 드롭 이벤트를 처리하는 함수
function handleFileSelection(event) {
    const files = event.target.files || event.dataTransfer.files;

    // 이미 선택된 파일이 있다면 기존 파일을 덮어쓰기
    if (files.length > 0) {
        file = files[0]; // 첫 번째 파일만 사용
        fileOutput.textContent = file.name;
        submitBtn.setAttribute("type", "submit");
        fileBtn.setAttribute("hidden", "hidden");
    }
}

// 파일 입력 요소 이벤트 리스너 등록
fileInput.addEventListener('change', handleFileSelection);

// 드래그 앤 드롭 이벤트 처리
function handleDropEvent(e) {
    e.preventDefault();
    const files = e.dataTransfer.files;

    // 이미 선택된 파일이 있다면 기존 파일을 덮어쓰기
    if (files.length > 0) {
        file = files[0]; // 첫 번째 파일만 사용
        fileOutput.textContent = file.name;
        
        submitBtn.setAttribute("type", "submit");
        fileBtn.setAttribute("hidden", "hidden");
        console.log(file);
    }
    //modal_post.setAttribute("method","POST");
    modal.classList.remove('show'); // 드롭 후 모달창 닫기
    // 이후의 파일 업로드 과정은 아래의 코드와 동일
    
    //////////// 여기부터 파이썬에서 하는 일 같다고 추측 중
    // // 서버로 파일 전송
    // const formData = new FormData();
    // formData.append("input-file", file);
    // console.log("ddd");

    // fetch('/modalfile', {

    //     method: 'POST',
    //     body: formData,
    //     headers: {
    //         'X-CSRFToken': getCookie('csrftoken'), // Django CSRF 토큰을 헤더에 포함
    //     },
    // })
    // .then(response => response.text())
    // .then(data => {
    // })
    // .catch(error => {
    //     console.error('Error:', error);
    // });
}

// body에 드래그 앤 드롭 이벤트 리스너 등록
body.addEventListener('dragover', function (e) {
    e.preventDefault();
    modal.classList.add('show'); // 모달창을 띄웁니다.
});

body.addEventListener('drop', handleDropEvent);

// modal에 드래그 앤 드롭 이벤트 리스너 등록
modal.addEventListener('dragover', function (e) {
    e.preventDefault();
});

modal.addEventListener('drop', handleDropEvent);

// 파일 선택 버튼을 클릭했을 때 이벤트 처리
function handleBtnClick(event){
    event.preventDefault();
    fileInput.click(); // 파일 선택 창을 열기 위해 input[type="file"] 클릭 이벤트 발생
}

fileBtn.addEventListener("click", handleBtnClick);

