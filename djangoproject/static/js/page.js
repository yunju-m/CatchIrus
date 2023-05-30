// 새로고침없이 페이지 url 수정
// 해당 내용이 같이 변하지 않는 문제 수정필요
const pageBtn = document.querySelectorAll(".page-item");
$(document).ready(function(){
    $(".page-item").click(clickPage);
});
function clickPage(event){
    event.preventDefault();
    // history.pushState(null, null, event.target.href);
    console.log("나 실행함!");
    let data = {"page": event.target.innerText};
    $.ajax({
        headers: { "X-CSRFToken": '{{csrf_token}}' },
        url: `/file/?page=${event.target.innerText}`,
        type: "POST",
        dataType: "json",
        data: data,
        success:function(data){
            console.log(data);
            
        },
        error: function(){
            alert('Error 발생했습니다.');
        }
    });
};