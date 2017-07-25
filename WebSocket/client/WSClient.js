var socket = 0;

function connect() {
	if (socket != 0 && socket.readyState != 1) return;

	socket = new WebSocket('ws://localhost:9999');
	socket.onopen = fuction() {
		socketOpened();
	};

	socket.onerror = function(error) {
		console.log('socket error');
		console.log(error);
		printMessage('connection error');
	};
	socket.onmessage = function(event) {
		handleMessage(event.data);
	};
	socket.onclose = function () {
		socketClosed();
	}
}

// // Connection opened
// socket.addEventListener('open', function (event) {
//     socket.send('Hello Server!');
// });

// // Listen for messages
// socket.addEventListener('message', function (event) {
//     console.log('Message from server', event.data);
// });