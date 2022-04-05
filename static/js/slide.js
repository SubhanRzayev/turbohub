$(".ig-box > div").on('click','img',function(){
  var src = $(this).attr("src");
  $(".ig-view > img").attr("src", src);
});



var c1 = $(".c1").attr("src");
var c2 = $(".c2").attr("src");
var c3 = $(".c3").attr("src");
var c4 = $(".c4").attr("src");
var arr = [c1,c2,c3,c4];
var n = 0;

$(".right").on('click',function(){
  $(".ig-view > img").attr("src",arr[n]);
  n += 1;
  if(n==4){
    n=0;
  }
});


$(".left").on('click',function(){
  $(".ig-view > img").attr("src",arr[n]);
  n -= 1;
  if(n==0){
    n=0;
  }
});







