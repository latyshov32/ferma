# ferma
ferma
http://zgo.narod.ru/publ/dht11_dht22_in_raspberry_pi_and_webiopi/1-1-0-51

print("Content-type: text/html")
print()
print("<h1>Hello world!</h1>")

ЖАВА СКРИПТ

npm install node-dht-sensor

var sensor = require("node-dht-sensor");
 
sensor.read(22, 4, function(err, temperature, humidity) {
  if (!err) {
    console.log(`temp: ${temperature}°C, humidity: ${humidity}%`);
  }
});
