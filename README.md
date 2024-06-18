# # LinuxCNC Config for groot EtherCAT Edition
Repository for all things related to the linuxCNC and EtherCAT based control system of my CNC router groot2.0. You're welcome to fork, however, push requests will not be considered as the main purpose of this repo is version control and backup for myself.

_Status_: This is a work in progress, expect substantial changes over time. In other words: For the love of all that is holy: Don't try this at home. It couldn't possibly be more broken and machine specific.

## About the machine
* CNC router made from aluminum profile and plate based on a design by fraseserbruch.de
* Workspace XYZ approx. 650/1200/230 mm
* Key components
    * ATC spindle Jianken JGL110 (4.2 kW, BT30) driven by VFD Delta MS300 with CMM-EC02 EtherCAT Interface
    * All drives Delta A3 Series (Driver Delta ASDA-A3 0421 and Motors EMCA0604 series (A2)) in CSP mode
    * Drive for A axis Delta A2 series 750W
    * Control based on linuxCNC 2.9.2 
    * IO based on EtherCAT with Etherlab Master and linuxcnc-ethercat: https://github.com/linuxcnc-ethercat/linuxcnc-ethercat
    * ATC Setup using a carousel style tool change based on probe_basic and carousel.comp (currently disabled)
    * tool lenght sensor and 3D wireless touch probe
    * xhc-whb04b-6 wireless 4 axis pendant
    * Further features: Status lights, control console for start/stop and feed and spindle override
    * Custom EtherCAT Slaves for Siemens HMI panel, see https://github.com/GuiHue/EtherCAT-CNC-HMI

## About the config
* LinuxCNC 2.9 pre (following master)
* Debian 12 Bookworm with Preempt-rt kernel 
* GUI: QtPyVCP based Probe_basic (python3) 

## Useful Links 
* General LinuxCNC items:
    * Physical override using poti https://forum.linuxcnc.org/24-hal-components/36336-physical-feed-override-knob?start=0
    * Run/Step buttons https://forum.linuxcnc.org/47-hal-examples/13201-run-step-hold-resume-buttons?start=0
    


## Useful Hints
