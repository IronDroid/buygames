$(document).on("ready", inicio);
function inicio () {
	$(".content_comment h5").timeago();
	$('#mycarousel').jcarousel({
		scroll: 2,
		animation: 'slow',
		wrap: 'circular'
	});
};