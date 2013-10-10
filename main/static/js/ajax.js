function voto_callback(data){
    $(".voto")[0].innerText = "Votos: " + data.cant;
}

function compra_callback(data) {
	if (!data.stock) {
		alert("Producto sin stock");
	};
	if (!data.compra) {
		alert("Producto comprado");
	};
	if (data.stock && data.compra) {
		$(".btn-comprar")[0].innerText = "Comprado";
	};
}