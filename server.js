// 引入http模块
const http = require('http')
// 创建web服务器实例
const server = http.createServer()
server.on('request', function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.write("你好啊")
    res.end();
})

server.listen(80, function () {
    console.log('服务器运行中 地址 http://127.0.0.1:80');
})