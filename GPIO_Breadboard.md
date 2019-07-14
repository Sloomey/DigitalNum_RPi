# How the breadboard and GPIO pins are set up.
## I am using a Raspberry Pi 3 Model B+
![The Breadboard I will be using as an example.](https://images-na.ssl-images-amazon.com/images/I/51kAyh7busL._AC_SY400_.jpg)
The breadboard I will be using as an example.
### The materials needed:
* 14 LEDs
* 14 220 ohm 5% resistors 
* 16 male to female jumper wires 
* Rasberry Pi (Recommended: Raspberry Pi 3 Model B+)

### LED Locations (Put the anode where the number is, not the cathode):
* e 30
* f 30
* b 28 
* i 28
* b 26
* i 26
* e 24
* f 24
* b 22
* i 22
* b 20 
* i 20
* e 18
* f 18

**Resistors will be connected one right from the cathode to ground.**
**Jumper Wires will be one underneath the resistor.**

### Jumper wire GPIO Locations (in BOARD numbering system):
You might have to change the code based on the location of your jumper wires.
* GROUND 1: 6
* GROUND 2: 9 
* Rest are Power Wires:
* 7
* 11
* 12
* 13
* 15
* 16
* 18 
* 21
* 22 
* 24
* 26 
* 29 
* 31 
* 32


