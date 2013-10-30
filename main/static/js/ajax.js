function voto_callback(data){
    $(".voto")[0].innerText = "Votos: " + data.cant;
}

function compra_callback(data) {
	if (!data.stock) {
		popup_show_stock(data.mensaje);
	};
	if (data.stock && data.compra) {
		popup_show(data.mensaje);
		$(".btn-comprar")[0].innerText = "Comprado";
		$('.btn-comprar').removeAttr('onclick');
	};
}
function popup_show_stock(data){
	var pago = $('#stock');
	var overlay = pago.find(".overlay");
	var panel = pago.find(".panel");

	pago.addClass("show");
	overlay.addClass("fadeIn");
	panel.addClass("bounceInDown");
}
function popup_show(data){
	var pago = $('#pago');
	var overlay = pago.find(".overlay");
	var panel = pago.find(".panel");

	pago.addClass("show");
	overlay.addClass("fadeIn");
	panel.addClass("bounceInDown");
}