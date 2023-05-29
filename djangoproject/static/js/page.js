// 새로고침없이 페이지 url 수정
// 해당 내용이 같이 변하지 않는 문제 수정필요
const pageBtn = document.getElementsByClassName("page-link");
function clickPage(event){
    console.log(event.target.href);
    event.preventDefault();
    history.pushState(null, null, event.target.href);
    console.log("나 실햄함!");

}
pageBtn[0].addEventListener("click", clickPage);
pageBtn[1].addEventListener("click", clickPage);
pageBtn[2].addEventListener("click", clickPage);
pageBtn[3].addEventListener("click", clickPage);