# grootec
 0  0:0   PREOP  +  EK1100 EtherCAT-Koppler (2A E-Bus)
 1  0:1   PREOP  +  EL1018 8K. Dig. Eingang 24V, 10�s
 2  0:2   PREOP  +  EL1114 4K. Dig. Eingang 24V, 10�s, Sensorversorgung
 3  0:3   PREOP  +  EL1114 4K. Dig. Eingang 24V, 10�s, Sensorversorgung
 4  0:4   PREOP  +  EL1008 8K. Dig. Eingang 24V, 3ms
 5  0:5   PREOP  +  EL3064 4K.Ana. Eingang 0-10V
 6  0:6   PREOP  +  EL2809 16K. Dig. Ausgang 24V, 0.5A
 7  0:7   PREOP  +  EL7031 1K. Schrittmotor-Endstufe (24V, 1.5A)
 8  0:8   PREOP  +  EK1110 EtherCAT-Verl�ngerung
 9  0:9   PREOP  +  Delta MS300 EtherCAT(CoE)
10  0:10  INIT   E  ASDA-A2-E
11  0:11  PREOP  +  Delta ASDA-A3-E EtherCAT(CoE) Drive Rev0
12  0:12  PREOP  +  Delta ASDA-A3-E EtherCAT(CoE) Drive Rev0
13  0:13  PREOP  +  Delta ASDA-A3-E EtherCAT(CoE) Drive Rev0
14  0:14  PREOP  +  Delta ASDA-A3-E EtherCAT(CoE) Drive Rev0



Note: Using POSIX realtime
Found file(REL): ./grootec.hal
Failed to execute SDO download: Input/output error
LCEC: slave 0.a-axis: Failed to execute SDO download (0x60fe:0x02, size 4, byte0=0, error -5, abort_code 06020000)
LCEC: failed to configure slave 0.a-axis sdo for enabling digital output ports 1-4
LCEC: failure in proc_init for slave 0.a-axis
LCEC: failure, clearing config
LCEC: exiting
LCEC: returning -EINVAL
lcec: rtapi_app_main: Invalid argument (-22)
./grootec.hal:9: waitpid failed /usr/bin/rtapi_app lcec
./grootec.hal:9: /usr/bin/rtapi_app exited without becoming ready
./grootec.hal:9: insmod for lcec failed, returned -1
Shutting down and cleaning up LinuxCNC...
Note: Using POSIX realtime
LinuxCNC terminated with an error.  You can find more information in the log:
    /home/groot/linuxcnc_debug.txt


