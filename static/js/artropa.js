(function ($){
         $("#cate").click(function(){
                var $this = $("#categor");
                if ($this.hasClass("ropita")){
                    $this.removeClass();
                    $this.addClass("ropashow");
                } else if ($this.hasClass("ropashow")){
                    $this.removeClass();
                    $this.addClass("ropita");
                }
            
            });
            $("#public").click(function(){
                var $this = $("#publico");
                if ($this.hasClass("ropita")){
                    $this.removeClass();
                    $this.addClass("ropashow");
                } else if ($this.hasClass("ropashow")){
                    $this.removeClass();
                    $this.addClass("ropita");
                }
            
            });
        $("#ropajs").click(function(){
            $("#accesorio").removeClass("ropashow");
            $("#cartera").removeClass("ropashow");
            $("#zapato").removeClass("ropashow");
            $(".bag").removeClass("active");
            $(".shoe").removeClass("active");
            $(".accesory").removeClass("active");
            $("#zapato").addClass("ropita");
            $("#cartera").addClass("ropita");
            $("#accesorio").addClass("ropita");
            $(".clothe").addClass("active");
            $("#ropa").removeClass("ropita");
            $("#ropa").addClass("ropashow");
        });
        $("#zapasjs").click(function(){
            $(".clothe").removeClass("active");
            $(".accesory").removeClass("active");
            $(".bag").removeClass("active");
            $("#ropa").removeClass("ropashow");
            $("#accesorio").removeClass("ropashow");
            $("#cartera").removeClass("ropashow");
            $("#ropa").addClass("ropita");
            $("#cartera").addClass("ropita");
            $("#accesorio").addClass("ropita");
            $(".shoe").addClass("active");
            $("#zapato").removeClass("ropita");
            $("#zapato").addClass("ropashow");
        });
        $("#carterajs").click(function(){
            $(".clothe").removeClass("active");
            $(".accesory").removeClass("active");
            $(".shoe").removeClass("active");
            $("#ropa").removeClass("ropashow");
            $("#zapato").removeClass("ropashow");
            $("#accesorio").removeClass("ropashow");
            $("#zapato").addClass("ropita");
            $("#ropa").addClass("ropita");
            $("#cartera").addClass("ropita");
            $(".bag").addClass("active");
            $("#accesorio").addClass("ropita");
            $("#cartera").removeClass("ropita");
            $("#cartera").addClass("ropashow");
        });
        $("#accjs").click(function(){
            $(".clothe").removeClass("active");
            $(".shoe").removeClass("active");
            $(".bag").removeClass("active");
            $("#ropa").removeClass("ropashow");
            $("#zapato").removeClass("ropashow");
            $("#cartera").removeClass("ropashow");
            $("#cartera").addClass("ropita");
            $("#zapato").addClass("ropita");
            $("#ropa").addClass("ropita");
            $(".accesory").addClass("active");
            $("#accesorio").removeClass("ropita");
            $("#accesorio").addClass("ropashow");
        });
        $("#form-cat").click(function(){
            $(".category").toogle();
        });

})(jQuery);