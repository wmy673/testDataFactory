from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class MockRequestHandler(BaseHTTPRequestHandler):
    """
    简单的 Mock HTTP 请求处理器，用于模拟接口响应。
    """

    def do_GET(self):
        """
        处理 GET 请求，返回固定的 JSON 响应。
        """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = '{"message": "This is a mock GET response"}'
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        """
        处理 POST 请求，返回固定的 JSON 响应。
        """
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = '{"message": "This is a mock POST response"}'
        self.wfile.write(response.encode('utf-8'))

def start_mock_server(host: str = 'localhost', port: int = 8000):
    """
    启动 Mock HTTP 服务器。

    :param host: 监听地址
    :param port: 监听端口
    :return: HTTPServer 实例
    """
    server = HTTPServer((host, port), MockRequestHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print(f"Mock 服务器已启动，地址: http://{host}:{port}")
    return server

# 示例用法
if __name__ == "__main__":
    server = start_mock_server(host='localhost', port=8000)
    try:
        input("按回车键停止 Mock 服务器...\n")
    finally:
        server.shutdown()
        print("Mock 服务器已停止")
