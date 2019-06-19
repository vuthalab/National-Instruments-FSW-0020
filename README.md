# National-Instruments-FSW-0020
Python class for the NI Quicksyn FSW-0020 Synthesizer

Find the data sheet and programming manual for this device under Manuals and Datasheets on the Google Drive, or on their website.
Features

This device may be controlled with Python through its USB interface.

It produces signals with frequency between 500 MHz and 2 GHz with 0.001 Hz precision and a 1 ms switching time. It also allows for output power control between -10 dBm and +13 dBm with 0.1 dBm nominal precision, at any allowed frequency.

It can sweep power and frequencies within these limits at any specified rate and resolution, with dwell between 5 us 4294 s. Sweeps may be initiated with a software or hardware trigger, or run point-by-point with repeated hardware triggering.

Features we haven’t yet tested include AM, FM , pulse modulation, and the clock reference input and output.
Hardware
Main ports connected for our testing. Note the banana cables and BNC connecting to the port box.
Ports, Power, and Cooling

The main ports on this device are an SPI connector (white, 20 pins), a USB port, and an SMA connector (labelled RF out). We use the SPI connector for the power supply, ground pins, and a hardware trigger pin. Each pin is soldered to a plug and connected to a port box. There, a BNC cable connects to the signal wire, and two Banana connectors meet the ground and power wires.

Use the port box to connect and disconnect any cables, and avoid disconnecting the SPI plug to prevent damage. Also, when unplugging, be sure to turn the output off, then unplug/turn off the power supply, then finally unplug the USB and BNC output cable. This order prevents voltage reflection, which could damage the output.
Power supply for the device, in operation.

This device requires +12 V for power. It nominally consumes a maximum of 24 W when initially powered on, and 20 W during normal operation. We observe this device consume about 15 W and operate as expected.

Other ports include AM, FM, pulse generation, and reference input and output; each of which we haven’t yet tested. These are labelled as expected.

Our testing suggest trigger signals should be +3.3 V, less than 1 A, and less than 2 seconds long.

The attached heat sink should prevent the device from reaching its maximum operating temperature of 55°C. If using the synthesizer for more than about 30 minutes, a spare computer fan should help prevent overheating.
Building the SPI Connector

To build a new SPI/power connector, use a DF1B-20DS-2.5RC housing connector and DF1B-2022 SC pins, both available from DigiKey. Be sure to buy at least two of the connectors and forty of the pins, as they are somewhat hard to work with..

The pin numbers are a follows: {Power (+12 V): Pins 3 and 4; Ground: Pins 8,10,19 and 20; and Hardware Trigger (0V, 3.3V): Pin 17}. Pin number locations are listed on the connector you will need to buy, or can be found in the data sheet.

To assemble a plug, push all the pins in as far as possible, and place the bend in their “U” shape towards the middle of the connector. Only then push the relevant wire ends in (use soft wire; really push them down) and solder. Ideally, the plastic should melt a little bit and seal the pins in place. Do not crimp the pins or wrap the wires around them, as the wires will break and the pins will eventually fall out.
Software

Find the programming manual for this device under Manuals and Data Sheets on the Google Drive, listed as “Quicksyn FSW-0020 Programming Manual”. We use the SCPI commands, found at the last page.

Our Python class for this device may be found under googledrive/samarium_control/widgets/objects and is titled “fsw_0020_synthesizer.py”.
Setup

To use this code, connect the synthesizer via USB, power it on, and type “find /dev/ttyACM*” into Terminal. It should appear here when plugged out and in. Fill out this address as the “device_address” parameter in the init function.
Main Commands and Testing

Run the code to initialize the synthesizer as “fg”. To run commands, type “print(fg.<command>)” to see a list of available commands (as all commands return an information string). These commands and parameters match the features described here and are well documented within the code.

Many commands are get or set commands- get/set frequency, get/set power, get ID (returning the make and serial number) or get temp (returning the temperature in degrees Celsius). To turn the output on or off, use set_output; to know if the device is on or off, use get_output.

We also included code for frequency and power sweeps; where you may choose a range of frequencies at a specified power, or vice versa. For each, you choose starting and ending values, and either a step value (“normal sweep”), or the number of points you would like to hit between your starting and ending values (“fast sweep”). (Note that your step value must divide your range; you will receive an error message otherwise, and no sweep will run). As the rest of the parameters suggest, you may choose a dwell time applied to each point (in ms), the number of runs, and a trigger (“0” for software; running immediately, “1” for a full sweep with one hardware trigger, and “2” for one point per hardware trigger).
