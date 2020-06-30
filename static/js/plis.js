function crearFav(){
    console.log("Funcionando");
    var current = $(this);
    var type = current.data('type')
    var pk = current.data('id');
    var action = current.data('action');

    $.ajax({
        url : "/marcar/" + type + "/" + pk + "/" + action + "/",
        type :"GET",
        date : {'objecto' : pk },
        success : function(json){
            console.log(json)
        }
    });

    return false;
}
$(function(){
$('[data-action="marcador"]').click(crearFav);

});