$("#btn-obtener").click(function () {
    var searched=$("#id_search").val();
    $.get("https://imdb-api.com/en/API/SearchMovie/k_29bfmsvl/"+searched,
    function(data){
        console.log(data);
        $("#table_body").empty();
        $.each(data.results,function(i, item){
            var fila = "<tr><td>"+parseInt(i+1)+
                        "</td><td>"+item.title+
                        "</td><td><img src='"+item.image+" width='100' height='200''>"+
                        "</td><td>"+item.description+
                        "</td><td>Null</td></tr>";
            $("#table_body").append(fila);
        
        });
    });

});
//   cierre del click 