var like = document.getElementsByClassName("favorite");
for (var i=0; i<=like.length; i++){

    like[i].addEventListener("click", function(){
        $(this).toggleClass("fas")
    });
}