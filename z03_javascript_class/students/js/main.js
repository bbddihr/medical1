//1.ajx stu_score.json 10개 데이터를 출력하시오.
//2.학생입력>학생추가 프로그램을 구성하시오
//3.학생수정>학생성적수정이 가능하게 구서하시오
//4.학생삭제>선택된 학생이 삭제되도록 구성하시오.

$(function(){
    $.ajax({
        url:"json/stu_score.json",
        data:"",
        type:"get",
        dataType:"json",
        success:function(data){
            alert("데이터 가져오기 성공")
            console.log(data);
            s_count=data.length;
            let htmlData="";
            for (let i=0; i<10;i++){
                htmlData += "<tr id='"+data[i].no+"'>";
                htmlData +="<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                htmlData +="<td>"+data[i].no+"</td>";
                htmlData +="<td>"+data[i].name+"</td>";
                htmlData +="<td>"+data[i].kor+"</td>";
                htmlData +="<td>"+data[i].eng+"</td>";
                htmlData +="<td>"+data[i].math+"</td>";
                htmlData +="<td>"+data[i].total+"</td>";
                htmlData +="<td>"+data[i].avg+"</td>";
                htmlData +="<td>"+data[i].rank+"</td>";
                htmlData +="<td><button class='delBtn'>삭제</button></td>";
                htmlData +="</tr>";
            
        }
        $("#body").html(htmlData);
    },
    error:function(){alert('error');}
    });

    $("#searchBtn").click(function(){
        if($("#s_word").val().length<1){
            alert("검색할 학생이름을 입력하셔야 가능합니다.");
            return false;
        }
        let s_word=$("#s_word").val();
        console.log("검색어: "+s_word);
    });
    $.ajax({
        url:"json/stu_score.json", // ./, /
        data:"",
        type:"get",
        dataType:"json",
        success:function(data){
            //alert("데이터 가져오기 성공");
            console.log(data);
            s_count = data.length;
            let htmlData = "";
            for (let i=0;i<10;i++){
                // 홍길동.indexOf('홍')
                if(data[i].name.indexOf(s_word) != -1){
                    htmlData += "<tr id='"+data[i].no+"'>";
                    htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
                    htmlData += "<td>"+data[i].no+"</td>";
                    htmlData += "<td>"+data[i].name+"</td>";
                    htmlData += "<td>"+data[i].kor+"</td>";
                    htmlData += "<td>"+data[i].eng+"</td>";
                    htmlData += "<td>"+data[i].math+"</td>";
                    htmlData += "<td>"+data[i].total+"</td>";
                    htmlData += "<td>"+data[i].avg+"</td>";
                    htmlData += "<td>"+data[i].rank+"</td>";
                    htmlData += "<td><button class='delBtn'>삭제</button></td>";
                    htmlData += "</tr>";
                }//if
            }//for
            // html소스를 tbody 추가
            $("#body").html(htmlData);
        },
        error:function(){ alert("에러"); }
    });//ajax
});

    $("#writeBtn").click(function(){
        if($(".stuChk:checked"),length>=1){
            alert("학생입력을 위해 체크를 해제해주세요")
            $(".stuChk").each(function(){
                $(this).prop("checked",false);
            });
            return false;
        }
        $(".p_all").css("display","block");
        $(".p_main h2").text("학생성적입력");
        $("#name").prop("readonly",false);
    });
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
        $("#id").val("");
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    });
    $("#confirmBtn").on("click",function(){
        if($("#id").val()==""){
            console.log("이름:  "+$("#name").val());
            if($("#name").val().length<2){
                alert("다시입력해주세요.");
                $("#name").focus();
                return false;
            }
            console.log("번호:  "+s_count);
            let i_name=$("#name").val();
            let i_kor=Number($("#kor").val());
            let i_eng=Number($("#eng").val());
            let i_math=Number($("#math").val());
            let i_total =i_kor+i_eng+i_math;
            let i_avg = (i_total/3).toFixed(2);
            

            let htmlData="";
            htmlData += "<tr id='"+i_no+"'>";
            htmlData +="<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
            htmlData +="<td>"+i_no+"</td>";
            htmlData +="<td>"+i_name+"</td>";
            htmlData +="<td>"+i_kor+"</td>";
            htmlData +="<td>"+i_eng+"</td>";
            htmlData +="<td>"+i_math+"</td>";
            htmlData +="<td>"+i_total+"</td>";
            htmlData +="<td>"+i_avg+"</td>";
            htmlData +="<td>0</td>";
            htmlData +="<td><button class='delBtn'>삭제</button></td>";
            htmlData +="</tr>";
        
            $("#body").append(htmlData);
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");
        }else{
            o_no=$("#id").val();
            o_name=$("#name").val();
            o_kor=Number($("#kor").val());
            o_eng=Number($("#eng").val());
            o_math=Number($("#math").val());
            let o_total = o_kor+o_eng+o_math;
            let o_avg = o_total/3;

            console.log("id:  "+o_no);
            console.log("kor:  "+o_kor);
            console.log("eng:  "+o_eng);
            console.log("math:  "+o_math);
            
            let htmlData="";
            htmlData += "<tr id='"+o_no+"'>";
            htmlData +="<td><input type='checkbox' name='stu' class='stuChk' value='"+o_no+"'></td>";
            htmlData +="<td>"+o_no+"</td>";
            htmlData +="<td>"+o_name+"</td>";
            htmlData +="<td>"+o_kor+"</td>";
            htmlData +="<td>"+o_eng+"</td>";
            htmlData +="<td>"+o_math+"</td>";
            htmlData +="<td>"+o_total+"</td>";
            htmlData +="<td>"+o_avg+"</td>";
            htmlData +="<td>"+0+"</td>";
            htmlData +="<td><button class='delBtn'>삭제</button></td>";
            htmlData +="</tr>";

            $("#"+o_no).html(htmlData);
            $("#id").val("");
            $("#name").val("");
            $("#kor").val("");
            $("#eng").val("");
            $("#math").val("");
            $(".p_all").css("display","none");
            

        }
        });
        $("#allChk").click(function(){
            if($(this).is(":checked")==true){
                $(".stuChk").each(function(){
                    $(this).prop("checked",true);
                    
                })
            }
        })

    });
        

