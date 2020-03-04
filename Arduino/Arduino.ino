#include <Servo.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <RFID.h>

Servo Servomoteur;  
RFID ModuleRFID(10,9);
LiquidCrystal_I2C lcd(0x3F,20,4);
String NomPrenom;
int UID[5];


void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(2, INPUT);
  Servomoteur.attach(4); 
  Servomoteur.write(5);
  SPI.begin();
  ModuleRFID.init();    
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Passez votre tag");
  }

void loop()
{
  if (ModuleRFID.isCard()) {  
    if (ModuleRFID.readCardSerial()) {
      for(int i=0;i<=4;i++)
      {
      UID[i]=ModuleRFID.serNum[i];
      
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      delay(50);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      
      Serial.print(UID[i],HEX);
      }
      Serial.println("");
      }          
      ModuleRFID.halt();
      
      delay(1500);

      if(Serial.available()){
        NomPrenom=Serial.readString();
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Acces Autorise");
        lcd.setCursor(0,1);
        lcd.print(NomPrenom);
        digitalWrite(5, HIGH);
        Servomoteur.write(50); 
        while (digitalRead(2) == LOW) {
        // Do nothing
        }
        digitalWrite(5, LOW);
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Passez votre tag");
        Servomoteur.write(5);
      }
      else 
      {
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Acces Refuse");
        lcd.setCursor(0,1);
        lcd.print("Carte Inconnue");
        digitalWrite(6, HIGH);
        delay(3000);
        digitalWrite(6, LOW);
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Passez votre tag");
        Servomoteur.write(5); 
        }  }
       delay(10);
       }
       
       
       
