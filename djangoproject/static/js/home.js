const fileInput = document.getElementById("input-file");
const fileOutput = document.getElementById("output-file");
const fileBtn = document.getElementById("fileBtn");
const submitBtn = document.getElementById("submitBtn");
const body = document.querySelector('body');
const modal = document.querySelector('.modal');
//let file = document.getElementById("input-file")

function handleFileUp(event) {
    const files = event.target.files;
    fileOutput.textContent = Array.from(files).map(file=> file.name).join("\n")
    fileBtn.setAttribute("hidden", "hidden");
    submitBtn.setAttribute("type", "submit");
}

function handleBtnEnter(){
    fileBtn.style.backgroundColor = "#183e84";
    submitBtn.style.backgroundColor = "#183e84";
}

function handleBtnLeave(){
    fileBtn.style.backgroundColor = "cornflowerblue";
    submitBtn.style.backgroundColor = "cornflowerblue";
}

fileBtn.addEventListener("mouseenter", handleBtnEnter);
fileBtn.addEventListener("mouseleave", handleBtnLeave);
submitBtn.addEventListener("mouseenter", handleBtnEnter);
submitBtn.addEventListener("mouseleave", handleBtnLeave);

fileInput.addEventListener("input", handleFileUp);

// //파일 넣는 부분에 이벤트가 발생했을 때 
// file.onchange = function (e) {
//     modal.classList.toggle('show');//모달창을 띄운다.
// }

// //body에 드래그하고 있을 때
// body.addEventListener('dragover', function (e) {
//     e.preventDefault();
//     console.log('dragover');
//     modal.classList.add('show');//모달창을 띄운다. add가 아닌 toggle로 하면 모달창이 껏다 켜졌다 반복함.
// });

// //body에 드래그 드랍했을 때
// body.addEventListener('drop', function (e) {
//     e.preventDefault();
//     console.log('drop');
//     //버튼 글자 'Upload File'에서 'Submit'으로 바꾸기
// });


// //modal에 클릭 이벤트가 발생했을 때
// modal.addEventListener('click', (event) => {
//     if (event.target === modal) {//클릭이 모달창 위면
//         modal.classList.toggle('show');//모달창을 띄우고

//         if (!modal.classList.contains('show')) {
//             body.style.overflow = 'auto';
//         }
//     }
// });