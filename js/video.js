(function() {
    var canvas = document.getElementById('canvas'),
	context = canvas.getContext('2d'),
	video = document.getElementById('video');

    navigator.getMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
    navigator.getMedia({
	video: true,
	audio: false
    }, function(stream) {
	video.src = vendorURl.createObjectURL(stream);
	video.play();
    } function(error) {
	//Error occured!
    }
    });
	
})();
