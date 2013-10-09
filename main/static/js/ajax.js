function voto_callback(data){
    $(".voto")[0].innerText = "Votos: " + data.cant;
}

function compra_callback(data) {
	$(".btn-comprar")[0].innerText = "Comprado";
}