#include "DCMotor.h"
#include <Arduino.h>

 DCMotor::DCMotor(int pinL,int pinR):pinL(pinL),pinR(pinR)
 {
  pinMode(this->pinL, OUTPUT);
  pinMode(this->pinR, OUTPUT);
 }
  
  void DCMotor::RotateLeft(){
    digitalWrite(pinL, HIGH);
    digitalWrite(pinR, LOW);
  }
  void DCMotor::RotateRight(){
    digitalWrite(pinL, LOW);
    digitalWrite(pinR, HIGH);

  }
  void DCMotor::Stop(){
    digitalWrite(pinL, LOW);
    digitalWrite(pinR, LOW);
    

  }