function signOut() {
            location.href = ('index.html')
        }
    function showSomething(id) {
		document.getElementById(id).style.display = 'block';
    }
    function hideSomething(id) {
		document.getElementById(id).style.display = 'none';
    }
    var socket = io.connect('http://0.0.0.0:80/test');
    socket.on('message', function(data) {
    console.log(data);
    if(data == "connected") {
        showSomething('shipstarted');
    }
    });