

#include <ArduinoJson.h>
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "sironialfondo";
const char* password = "MartinFierro2013";

//Your Domain name with URL path or IP address with path
const char* serverName = "http://192.168.0.121:8000/";
const char* serverNameLogin = "http://192.168.0.121:8000/login/";
const char* serverNameApi = "http://192.168.0.121:8000/api/";
// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 5 seconds (5000)
unsigned long timerDelay = 10000;
int pin_door = 22;
int pin_entry = 23;
int pin_exit = 21;
bool sensor_entry = false;
bool sensor_exit = false;
bool past_sensor_entry = false;
bool past_sensor_exit = false;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
  
  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
  pinMode(pin_entry,INPUT);
  pinMode(pin_exit,INPUT);
  pinMode(pin_door,OUTPUT);
  sensor_entry= digitalRead(pin_entry);
  past_sensor_entry = sensor_entry;
  sensor_exit= digitalRead(pin_exit);
  past_sensor_exit = sensor_entry;
}

void loop() {
  if (millis() - lastTime<= timerDelay){
    digitalWrite(pin_door,true);
  }else{
    digitalWrite(pin_door,false);
  }
  //Send an HTTP POST request every 10 minutes
  sensor_entry= digitalRead(pin_entry);
  sensor_exit= digitalRead(pin_exit);
  
  bool add_entry = false;
  bool add_exit = false;
  if (sensor_entry != past_sensor_entry){
    
    past_sensor_entry = sensor_entry;
    if (sensor_entry){
      Serial.println("nuevo ingreso");
      add_entry = true;
    }
  }
  if (add_entry) {
    //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      if (addEntry() == HTTP_CODE_OK){
        lastTime = millis();
      }
    }
    else {
      Serial.println("WiFi Disconnected");
    }
  }
  if (sensor_exit != past_sensor_exit){
   
    past_sensor_exit = sensor_exit;
    if (sensor_exit){
      add_exit = true;
      Serial.println("nuevo egreso");
    }
  }
  if (add_exit) {
    
    //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      if (addExit() == HTTP_CODE_OK){
        lastTime = millis();
      }
    }
    else {
      Serial.println("WiFi Disconnected");
    }
  }
}
String getToken(){
  String token;
  WiFiClient client;
  HTTPClient http;

  // Your Domain name with URL path or IP address with path
  http.begin(client, serverNameLogin);

  // Specify content-type header
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  // Data to send with HTTP POST
  String httpRequestData = "username=admin&password=admin";           
  // Send HTTP POST request
  int httpResponseCode = http.POST(httpRequestData);
 
  Serial.print("HTTP Response code: ");
  Serial.println(httpResponseCode);
  // file found at server
  if(httpResponseCode == HTTP_CODE_OK) {
      
      String payload = http.getString();
      
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, payload);
      JsonObject root = doc.as<JsonObject>();
      String json = root[String("token")];
      token = json;
      Serial.println("token obtained" + token);
  }else{
    Serial.println("error obtaining token");
  }
  // Free resources
  http.end();
  return token;
}
int addExit(){
  WiFiClient client;
  HTTPClient http;

  // Specify content-type header
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  
  // Data to send with HTTP POST
  String httpRequestData = "";           

  // file found at server
  String token = getToken();
  
  
  String atr = "token "+ token;
  String entries = "exits/";
  http.begin(client, serverNameApi + entries);
  
  http.addHeader("Authorization", atr);
  int httpResponseCode = http.POST(httpRequestData);
  
  
  String payload = http.getString();
  Serial.println(payload);
  
  // Free resources
  http.end();
  return httpResponseCode;
}

int addEntry(){
  WiFiClient client;
  HTTPClient http;

  // Specify content-type header
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  
  // Data to send with HTTP POST
  String httpRequestData = "";           

  // file found at server
  String token = getToken();
  String atr = "token "+ token;
  String entries = "entries/";
  http.begin(client, serverNameApi + entries);
  
  http.addHeader("Authorization", atr);
  int httpResponseCode = http.POST(httpRequestData);
  
  
  String payload = http.getString();
  Serial.println(payload);
  
  // Free resources
  http.end();
  return httpResponseCode;
}
