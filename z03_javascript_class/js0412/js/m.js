
$(function(){
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,62,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];

let htmlData="";
for (let i=0; i<no.length;i++){
    htmlData += "<tr id='"+no[i]+"'>"; 
    htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]"'></td>;
    htmlData += "<td>"+no[i]+"</td>";
    htmlData += "<td>"+name[i]+"</td>";
    htmlData += "<td>"+kor[i]+"</td>";
    htmlData += "<td>"+eng[i]+"</td>";
    htmlData += "<td>"+math[i]+"</td>";
    htmlData += "<td>"+total[i]+"</td>";
    htmlData += "<td>"+avg[i]+"</td>";
    htmlData += "<td>0</td>";
    htmlData += "<td><button class='delBtn'>삭제</button></td>";
    htmlData += "</tr>"



$("#body").html(htmlData);


$("#allChk").click(function(){
     if($(this).is("checked")==true){
        console.log("체크되었다.");
        $(".stuChk").each(function(){
            $(this).prop("checked",true);
        })
     }else{
        console.log("체크해제되었다.");
        $(".stuChk").each(function(){
            $(this).prop("checked",false);
        })
     }
});




//table 삭제버튼

$(".delBtn").click(function(){
    console.log("현재 선택된 class id: "+$(this).parent().parent().attr("id"));
    if(confirm("정말 삭제하시겠어요?")){
        $("#"+$(this).parent().parent().attr("id")).remove();
    }
});


$("#deleteBtn").click(function(){
    console.log("체크박스 개수: "+$(".stuChk").length);

    if($(".stuChk:checked").length<1){
        alert("삭제할 데이터를 체크해주셔야 가능합니다.");
        return false;
    }
    if(!confirm("정말삭제하시겠어요?")){
        return false; 
    }
    if($(this).is(":checked")==true){
        console.log("현재 선택된 class값: "+$(this).val());
        console.log("현재 선택된 id 값:" +$(this).parent().parent().attr("id"));
        $("#"+$(this).parent().parent().attr("id")).remove();
    }
});

