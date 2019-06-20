# National-Instruments-FSW-0020
Python class for the NI Quicksyn FSW-0020 Synthesizer

<!-- wp:paragraph {"align":"left"} -->
<p style="text-align:left">Find the data sheet and programming manual for this device under <a href="https://drive.google.com/drive/folders/0BxtBYCHo7PyzfmxFel8zcER1aFRNY3lrRi05bElpUFRLeFNkNzhnSUNIS0NndmxhUlFWM0E">Manuals and Datasheets</a> on the Google Drive, or on their <a href="http://ni-microwavecomponents.com/quicksyn-full#documentation">website</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Features</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This device may be controlled with Python through its USB interface.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It produces signals with frequency between 500 MHz and 2 GHz with 0.001 Hz precision and a 1 ms switching time. It also allows for output power control between -10 dBm and +13 dBm with 0.1 dBm nominal precision, at any allowed frequency. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It can sweep power and frequencies within these limits at any specified rate and resolution, with dwell between 5 us 4294 s. Sweeps may be initiated with a software or hardware trigger, or run point-by-point with repeated hardware triggering.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Features we haven't yet tested include AM, FM , pulse modulation, and the clock reference input and output.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Hardware</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4>Ports, Power, and Cooling</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The main ports on this device are an SPI connector (white, 20 pins), a USB port, and an SMA connector (labelled RF out). We use the SPI connector for the power supply, ground pins, and a hardware trigger pin. Each pin is soldered to a plug and connected to a port box. There, a BNC cable connects to the signal wire, and two Banana connectors meet the ground and power wires. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Use the port box to connect and disconnect any cables, and avoid disconnecting the SPI plug to prevent damage. Also, when unplugging, be sure to turn the output off, then unplug/turn off the power supply, then finally unplug the USB and BNC output cable. This order prevents voltage reflection, which could damage the output.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This device requires +12 V for power. It nominally consumes a maximum of 24 W when initially powered on, and 20 W during normal operation. We observe this device consume about 15 W and operate as expected.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Other ports include AM, FM, pulse generation, and reference input and output; each of which we haven't yet tested. These are labelled as expected.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our testing suggest trigger signals should be +3.3 V, less than 1 A, and less than 2 seconds long. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The attached heat sink should prevent the device from reaching its maximum operating temperature of 55<strong>°</strong>C. If using the synthesizer for more than about 30 minutes, a spare computer fan should help prevent overheating.  </p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>Building the SPI Connector</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To build a new SPI/power connector, use a DF1B-20DS-2.5RC housing connector and DF1B-2022 SC pins, both available from DigiKey. Be sure to buy at least two of the connectors and forty of the pins, as they are somewhat hard to work with..</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The pin numbers are a follows: {Power (+12 V): Pins 3 and 4; Ground: Pins 8,10,19 and 20; and Hardware Trigger (0V, 3.3V): Pin 17}. Pin number locations are listed on the connector you will need to buy, or can be found in the data sheet.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To assemble a plug, push all the pins in as far as possible, and place the bend in their "U" shape towards the middle of the connector. Only then push the relevant wire ends in (use soft wire; really push them down) and solder. Ideally, the plastic should melt a little bit and seal the pins in place. Do not crimp the pins or wrap the wires around them, as the wires will break and the pins will eventually fall out.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Software</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Find the programming manual for this device under Manuals and Data Sheets on the Google Drive, listed as "Quicksyn FSW-0020 Programming Manual". We use the SCPI commands, found at the last page.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our Python class for this device may be found under <a href="https://drive.google.com/drive/folders/1dJO_H5MnHgHPdGbpeVIjRQA95KoP7WjN">googledrive/samarium_control/widgets/objects</a> and is titled "fsw_0020_synthesizer.py". </p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>Setup</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To use this code, connect the synthesizer via USB, power it on, and type "find /dev/ttyACM*" into Terminal. It should appear here when plugged out and in. Fill out this address as the "device_address" parameter in the init function.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>Main Commands and Testing</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Run the code to initialize the synthesizer as "fg". To run commands, type "print(fg.&lt;command&gt;)" to see a list of available commands (as all commands return an information string). These commands and parameters match the features described here and are well documented within the code.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Many commands are get or set commands- get/set frequency, get/set power, get ID (returning the make and serial number) or get temp (returning the temperature in degrees Celsius). To turn the output on or off, use set_output; to know if the device is on or off, use get_output. </p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>Sweeps</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We also included code for frequency and power sweeps; where you may choose a range of frequencies at a specified power, or vice versa. For each, you choose starting and ending values, and either a step value ("normal sweep"), or the number of points you would like to hit between your starting and ending values ("fast sweep"). (Note that your step value must divide your range; you will receive an error message otherwise, and no sweep will run). As the rest of the parameters suggest, you may choose a dwell time applied to each point (in ms), the number of runs, and a trigger ("0" for software; running immediately, "1" for a full sweep with one hardware trigger, and "2" for one point per hardware trigger).</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>List Mode</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To use list mode, set each point of the list individually using the "list_point_setup" command. You may overwrite points and modify points in any order, specifying a frequency, power and dwell time for each. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Lists require a separate "run list" command. Note that specifying a dwell time other than zero for this run command will apply a universal dwell time to the points the the list. Also, use the erase list command to clear any saved sweeps before setting a new one.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>Voltage Convenience Functions</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We included functions which allow a user to choose peak-to-peak voltage, RMS voltage, or the voltage amplitude. These make use of the 50 ohm nominal resistance provided by measurement devices, or experiment controls, and adjust the power accordingly.</p>
<!-- /wp:paragraph -->
