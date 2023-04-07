import socketio

io = socketio.Client()


@io.on("connect")
def connect():
    io.emit("req_pos", {"dummy": "msg"})


@io.on("player_pos")
def player_pos(message):
    io.emit("ret_pos", {"red": [0, 0]})


io.connect("http://192.168.178.147:5000")
io.wait()
