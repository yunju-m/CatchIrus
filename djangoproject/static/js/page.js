const pageBtn = document.querySelectorAll(".page-item");
const pagelink = document.querySelectorAll(".page-link");
const usertable = document.getElementsByClassName("table-group-divider")[0];

$(document).ready(function(){
    $(".page-item").click(userDataHandler);
});

function clickPage(event){
    const urlParams = new URL(event.target.href).searchParams;
    const clickpage = urlParams.get('page');

    // 클릭한 페이지 번호 활성화
    for (let p = 1; p < pageBtn.length-1; p++){
        if(p == clickpage){
            pageBtn[p].className = "page-item active";
            if (p == 1){
                pagelink[0].setAttribute("href", `?page=${p}`);
                pageBtn[0].className = "page-item disabled";
                pagelink[pageBtn.length-1].setAttribute("href", `?page=${p+1}`);
                pageBtn[pageBtn.length-1].className = "page-item";
            } else if (p == pageBtn.length-2){
                pagelink[pageBtn.length-1].setAttribute("href", `?page=${p}`);
                pageBtn[pageBtn.length-1].className = "page-item disabled";
                pagelink[0].setAttribute("href", `?page=${p-1}`);
                pageBtn[0].className = "page-item";
            } 
            else{
                pagelink[0].setAttribute("href", `?page=${p-1}`);
                pageBtn[0].className = "page-item";
                pagelink[pageBtn.length-1].setAttribute("href", `?page=${p+1}`);
            }
        } else{
            pageBtn[p].className = "page-item";
        }
    }
}
function userDataHandler(event){
    event.preventDefault();
    // history.pushState(null, null, event.target.href);
    const urlParams = new URL(event.target.href).searchParams;
    const clickpage = urlParams.get('page');
    let data = {"page": clickpage};

    // 클릭한 page 번호를 파라미터로 url POST 
    $.ajax({
        headers: { "X-CSRFToken": '{{csrf_token}}' },
        url: `/file/?page=${clickpage}`,
        type: "POST",
        dataType: "json",
        data: data,
        success:function(data){
            console.log(data);
            userJson = JSON.stringify(data);
            resultuser = JSON.parse(userJson);
            usermodel = JSON.parse(resultuser.usermodel);
            userpage = data.userpage;
            
            // 기존의 테이블 정보 삭제
            tablesize = usertable.rows.length;
            for(let i = 0; i <= tablesize; i++){
                usertable.deleteRow(-1);
            }

            let startpage = 10*data.userpage-10;   // 시작 페이지번호
            let endpage = 10*data.userpage;     // 끝 페이지번호
            let start = 0;          // 페이지 시작 판단 변수
            // usermodel 데이터에서 filename, date 추출
            $.each(usermodel, function(key, value){
                // console.log("key: " + key);
                // console.log(value);
                const newRow = usertable.insertRow();
                let cnt = 0;
                
                $.each(value.fields, function(key, value){
                    // page의 시작 조절
                    start = start + 1
                    if (startpage > start || startpage > endpage){
                        return false;
                    }
                    if (cnt == 0){  // 번호 저장
                        startpage = startpage + 1;
                        // 최대 10개의 내용만 출력되게 조절
                        if(startpage > endpage){
                            return false;
                        } else{
                            let newCell = newRow.insertCell(cnt);
                            newCell.innerText = startpage;
                        }
                    }
                    else{   // 사용자, 제목, 날짜 순서로 저장
                        let newCell = newRow.insertCell(cnt);
                        newCell.innerText = `${value}`;
                    }
                    cnt = cnt + 1;
                })
            })
        },
        error: function(){
            alert('Error 발생했습니다.');
        }
    });
    // page버튼 이벤트 기능
    clickPage(event);
};