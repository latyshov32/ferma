import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.132.23'  # Change this to your Raspberry Pi IP address
host_port = 8000


class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
           <html lang="ru">
           <head>
           <meta charset="utf-8"/>
           <title>СИТИ-ФЕРМА №2</title>
           </head>
           <body>
           <center><script type="text/javascript">
           document.write(Date());
           </script>
           </center>
           </body>
           <body bgcolor="D8BFD8">
           <body style="width:960px; margin: 20px auto;">
           <center><h1>Сити-ферма №2<br>
           Разработчик: Алексей Латышов</h1>
           <p><strong>УПРАВЛЕНИЕ:</strong></p>
           <p>Свет 1: <a href="/led1/on"><font color="green"><strong><button>СТАРТ</button></strong></font></a><a href="/led1/off"><font color="red"><strong><button>СТОП</button></strong></font></a></p>
           <p>Свет 2: <a href="/led2/on"><font color="green"><strong><button>СТАРТ</button></strong></font></a><a href="/led2/off"><font color="red"><strong><button>СТОП</button></strong></font></a></p>
           <p>Насос: <a href="/led3/on"><font color="green"><strong><button>СТАРТ</button></strong></font></a><a href="/led3/off"><font color="red"><strong><button>СТОП</button></strong></font></a></p>
           <p>Авто: <a href="/led-all/on"><font color="green"><strong><button>СТАРТ</button></strong></font></a><a href="/led-all/off"><font color="red"><strong><button>СТОП</button></strong></font></a></p>
           <p><strong>Статус:</strong></p>
           <div id="led-status"></div>
           <script>
               document.getElementById("led-status").innerHTML="{}";
           </script>
           </body>
           </html>
        '''
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        if self.path=='/':
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(21, GPIO.OUT)
            GPIO.setup(20, GPIO.OUT)
            GPIO.setup(26, GPIO.OUT)
            
        elif self.path=='/led1/on':
            GPIO.output(21, GPIO.LOW)
            status='LED1 is ON'
        elif self.path=='/led1/off':
            GPIO.output(21, GPIO.HIGH)
            status='LED1 is OFF'

        elif self.path=='/led2/on':
            GPIO.output(20, GPIO.LOW)
            status='LED2 is ON'
        elif self.path=='/led2/off':
            GPIO.output(20, GPIO.HIGH)
            status='LED2 is OFF'

        elif self.path=='/led3/on':
            GPIO.output(26, GPIO.LOW)
            status='LED3 is ON'
        elif self.path=='/led3/off':
            GPIO.output(26, GPIO.HIGH)
            status='LED3 is OFF'
            
        elif self.path=='/led-all/on':
            GPIO.output(21, GPIO.LOW)
            GPIO.output(20, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
            status='All LEDs are ON'
        
        elif self.path=='/led-all/off':
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH) 
            GPIO.output(26, GPIO.HIGH)
            status='All LEDs are OFF'
            
            
        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()

