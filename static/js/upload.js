/**
 * Created by Administrator on 2017/4/3.
 */
$("input[name='submit']").click(function () {
    if(
         $("input[name='up_file']").val() &&
         $("input[name='file_discribe']").val()
    ){
    }else {
           alert("请选择文件")
    }
})