var like = document.getElementsByClassName("fav");
for (var i=0; i<=like.length; i++){
    console.log(like[i]);
}
var like = document.getElementsByClassName("favorite");
for (var i=0; i<=like.length; i++){

    like[i].addEventListener("click", function(){
        $(this).toggleClass("fas")
    });
}