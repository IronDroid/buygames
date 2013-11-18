$(document).on("ready", inicio);
function inicio () {
	$(".content_comment h5").timeago();
	$('#mycarousel').jcarousel({
		scroll: 2,
		animation: 'slow',
		wrap: 'circular'
	});
};

$(function(){
	var popup = new function () {
		var $self      = $('#pago'),
		$overlay = $self.find('.overlay'),
		$panel   = $self.find('.panel');

		this.hide = function () {
			$overlay.addClass('fadeOut');
			$panel.addClass('bounceOutUp');

            setTimeout(function () {
                $self.removeClass('show');
                $overlay.removeClass('fadeOut').removeClass('fadeIn');
                $panel.removeClass('bounceOutUp').removeClass('bounceInDown');
            }, 1010);

            return false;
        };

        this.show = function () {
            $self.addClass('show');
            $overlay.addClass('fadeIn');
            $panel.addClass('bounceInDown');
        };

        // botones para cerrar
        // $overlay.click(this.hide);
        $('#cerrar').click(this.hide);
    }();
});

$(function(){
    var popup = new function () {
        var $self      = $('#stock'),
        $overlay = $self.find('.overlay'),
        $panel   = $self.find('.panel');

        this.hide = function () {
            $overlay.addClass('fadeOut');
            $panel.addClass('bounceOutUp');

            setTimeout(function () {
                $self.removeClass('show');
                $overlay.removeClass('fadeOut').removeClass('fadeIn');
                $panel.removeClass('bounceOutUp').removeClass('bounceInDown');
            }, 1010);

            return false;
        };

        this.show = function () {
            $self.addClass('show');
            $overlay.addClass('fadeIn');
            $panel.addClass('bounceInDown');
        };

        // botones para cerrar
        // $overlay.click(this.hide);
        $('#cerrar_stock').click(this.hide);
    }();
});

$(function(){
    var popup = new function () {
        var $self      = $('#notcard'),
        $overlay = $self.find('.overlay'),
        $panel   = $self.find('.panel');

        this.hide = function () {
            $overlay.addClass('fadeOut');
            $panel.addClass('bounceOutUp');

            setTimeout(function () {
                $self.removeClass('show');
                $overlay.removeClass('fadeOut').removeClass('fadeIn');
                $panel.removeClass('bounceOutUp').removeClass('bounceInDown');
            }, 1010);

            return false;
        };

        this.show = function () {
            $self.addClass('show');
            $overlay.addClass('fadeIn');
            $panel.addClass('bounceInDown');
        };

        // botones para cerrar
        // $overlay.click(this.hide);
        $('#cerrar_card').click(this.hide);
    }();
});