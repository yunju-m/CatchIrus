// 새로고침없이 페이지 url 수정
// 해당 내용이 같이 변하지 않는 문제 수정필요
const pageBtn = document.querySelectorAll(".page-item");
function clickPage(event){
    console.log(event);
    event.preventDefault();
    // history.pushState(null, null, event.target.href);
    console.log("나 실햄함!");
    $.ajax({
        url: "{% url 'file' %}",
        type: "GET",
        data: event.target.innerText,
        success:function(data){
            console.log(data);
        },
        error: function(){
            alert('응애??? 왜 너가 여기서나와?');
        }
    });
};

pageBtn[0].addEventListener("click", clickPage);
pageBtn[1].addEventListener("click", clickPage);
pageBtn[2].addEventListener("click", clickPage);
pageBtn[3].addEventListener("click", clickPage);