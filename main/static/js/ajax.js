function voto_callback(data){
    $(".voto")[0].innerText = "Votos: " + data.cant;
}

function compra_callback(data) {
	if (!data.stock) {
		alert("Lo sentimos, ya no tenemos este juego... :'(");
	};
	if (data.stock && data.compra) {
		alert("comprado");
		$(".btn-comprar")[0].innerText = "Comprado";
		$('.btn-comprar').removeAttr('onclick');
	};
}