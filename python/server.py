from wsgiref.simple_server import make_server
# 导入simple_server模块

# 定义一个application，遵循wsgi协议；



def app(env, start_response):  # 服务器接收到的客户端请求都会存储在env中，再传入到app进行处理，处理后再返回
    start_response("200 ok", [("Content-Type", "text/html")])
    return [b'''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>22222</h1>
</body>
</html>
''']  # swgi协议规定必须返回bety


# 实例化一个服务器设置ip为本机，端口为5000，执行程序为上面的app
server = make_server("", 5000, app)
print('服务器运行中 地址 http://127.0.0.1:5000')
# 开启一个服务器，默认0.5秒轮询，接收客户端请求
server.serve_forever()