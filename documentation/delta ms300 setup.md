# Delta MS300 Parameter File

Spindle: Jianken JGL110/4.2R24-30 (800Hz, 4 poles)
VFD: Delta MS300 High Speed Series

## Chapter 0 Drive Parameters
### 0-20: Source of Master Frequency Command 
    8 - Communication Card

### 0-21: Source of Operation Command (AUTO) 
    5- Communication Card


## Chapter 1 Basic Parameters

Note Jianken JGL110 has a totally linear V/F curve, hence no mid points are needed.

### 1-00: Max operation Frequency of motor 1 
    800 

### 1-01: Output frequency of motor 1 
    800 

### 1-02: Output Voltage of motor 1 
    380 

### 1-07: Min output frequency of motor 1 
    10 (could be 0?) - 10 = 300 rpm

### 1-09: Start-up frequency  
    10

### 1-09: Output frequency upper limit
    800

### 1-10: Output frequency lower limit
    10 

### 1-12: Accel. time motor 1
    100 (should be equal to 10s)

### 1-13: Decel. time motor 1
    100 (should be equal to 10s)

### 1-45: Time unit for acceleration/ deceleration
    1 (Changed) Unit 0.1s


## Chapter 2 Digital Input / Output Parameters

Review at Machine!

### 2-13: Multi-function output 1 (RY1) - Relay
    1 : Indication during RUN (connect to relay to switch on Chiller)

## Chapter 3 Analog Input / Output Parameters
*Not in use*

## Chapter 4 Multi-stage Speed Parameters
*Not in use*

## Chapter 5 Motor Parameters

### 5-01: Full-load Current of Induction Motor 1 (A)
    7.5 (rated current according to Jianken)

### 5-02: Rated Power of Induction Motor 1 (kW)
    4.2

### 5-03: Rated Speed of Induction Motor 1 (rpm)
    24000

### 5-04: Pole Number of Induction Motor 1
    4 (default)

## Chapter 6 Protection Parameters  (1)

Check against default values

### 6-03: Over-current stall prevention during acceleration
    150 (Jianken typical)

### 6-04: Over-current stall prevention during operation
    150 (Jianken typical)


## Chapter 7 Special Parameters  

Check current secctings - DC Brake is 07-00 - 07-04

## Chapter 9 Communication Parameters
*Not in use, does not relate to EtherCAT*

## Chapter 11 Communication Parameters
*Not in use*

## Chapter 13 Macro / User Define Macro
*Not in use*

## Chapter 14 Protection Parameters (2)
*Not in use*