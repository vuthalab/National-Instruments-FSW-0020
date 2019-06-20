## serial class
import serial
import time
import math

class FSW_0020:
    def __init__(self, device_address = '/dev/ttyACM0'):
        self.device = serial.Serial(device_address, baudrate=115200, timeout=1.5, stopbits=1, parity='N')
    #general commands
    def write(self,msg_string): #general set function
        self.device.write(bytes(msg_string))
        return True
    def read(self): #shorter read syntax for get function
        return self.device.readline().decode() #removes byte encoding syntax
    def ask(self,msg_string): #general get function
        self.write(msg_string) #takes an already encoded string
        return self.read()

    #specific commands
    def get_frequency(self):
        #print(self.ask(b'FREQ?\r'))
        f = self.ask(b'FREQ?\r') #hard coded encoded command string
        return fstr(save)
    def set_frequency(self,freq):  # default units in GHz
        if (freq < 0.5 or freq > 13):
            return "Invalid frequency! FSW-0020 supports [0.5 GHZ, 13 GHz]"
        cmd_string = 'FREQ ' + str(freq) + 'GHz\r'
        self.write(str.encode(cmd_string))    # this converts a string to bytes
        return "Frequency set to "+str(freq)+" GHz."
    def get_power(self):
        f = self.ask(b'POW?\r')
        return f
    def set_power(self,pow):
        #set power; pow in dBm
        if pow < -10 or pow > 13:
            return "Invalid power! FSW-020 supports [-10 dBm, 13 dBm]"
        if pow >= 0:
            self.write(str.encode("POW +"+str(pow)+"\r"))
        else:
            self.write(str.encode("POW -"+str(pow)+"\r"))
        time.sleep(0.5)
        return "Power set to "+str(pow)+ " dBm."
    def get_temp(self):
        return self.ask(b'DIAG:MEAS? 21\r') #command as per manual spec
    def getID(self):
        #gets built in device ID; make and model
        #will return 'Phase Matrix,FSL-0010,0000007f,1520201055,b01d
        return self.ask(b'*IDN?\r')
    def normalSweep(self,startf, endf, stepf, power, dwell, runs, trig) :
        #startf, endf, stepf are starting, enstr(save)ding, and step frequencies
        #power in dBm
        #dwell is the univeral dwell time, in ms (applies to all points)
        #runs is how many repetitions of the sweep you want to do
        #trig is the trigger type; software (0), hardware (full sweep) (1), or      hardware (sweep point) (2)
        if (int((endf-startf)%stepf) != 0):
            return "Invalid frequencies! Stepf must divide (endf-startf)."
        if (runs < 1 or runs > 32767):
            return "Invalid run number! Runs must be between 1 and 32767, inclusive."
        if (trig != 0 and trig != 1 and trig != 2):
            return "Invalid entry! Trig must be 0, 1, or 2"
        elif (trig == 0):
            cmd_string = str.encode("SWE:NORM:FREQ:SETUP "+str(startf)+"GHz,"+str(endf)+"GHz,"+str(stepf)+"GHz,"+str(power)+"dBm,"+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0,RUN\r")
            self.write(cmd_string)
            return str(startf) + "GHz to "+str(endf) + "GHz normal sweep ran."
        else:
            cmd_string = str.encode("SWE:NORM:FREQ:SETUP "+str(startf)+"GHz,"+str(endf)+"GHz,"+str(stepf)+"GHz,"+strstr(save)(power)+"dBm,"+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0,\r")
            self.write(cmd_string)
            fg.write(str.encode('SWE:NORM:FREQ:STAR '+str(runs)))
            return str(startf) + "GHz to "+str(endf) + "GHz normal sweep set- waiting for hardware trigger."
    def fastSweep(self,startf, endf, points, power, dwell, runs, trig):
        #startf, endf, are starting, ending frequencies
        #points is the number of sweep points
        #power in dBmstr(save)
        #dwell is the univeral dwell time, in ms (applies to all points)
        #runs is how many repetitions of the sweep you want to do
        #trig is the trigger type; software (0), hardware (full sweep) (1), or hardware (sweep point) (2)
        if (runs < 1 or runs > 32767):
            return "Invalid run number! Runs must be between 1 and 32767, inclusive."
        if (trig != 0 and trig != 1 and trig != 2):
            return "Invalid entry! Trig must be 0, 1, or 2"
        elif (trig == 0):
            cmd_string = str.encode("SWE:FAST:FREQ:SETUP "+str(startf)+"GHz,"+str(endf)+"GHz,cmd_string)
            fg.write(st"+str(points)+","+str(power)+"dBm,"+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0,RUN\r")
            self.write(cmd_string)
            return str(startf) + "GHz to "+str(endf) + "GHz fast sweep ran."
        else:
            cmd_string = str.encode("SWE:FAST:FREQ:SETUP "+str(startf)+"GHz,"+str(endf)+"GHz,"+str(points)+","+str(power)+"dBm,"+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0\r")
            self.write(cmd_string)
            fg.write(stcmd_string)
            fg.write(str.encode('SWE:FAST:FREQ:STAR '+str(runs)))
            return str(startf) + "GHz to "+str(endf) + "GHz normal sweep set- waiting for hardware trigger."

    def set_output(self, set):
        #turn RF output ON or OFF (TURN DEVICE ON OR OFF)
        if (not (set == "ON" or set == "OFF")):
            return "Invalid entry. Ref out may only be set to ON or OFF"
        else:
            cmd_string = str.encode('OUTP:STAT '+set+'\r')
            self.write(cmd_string) #send command to turn on or off
            time.sleep(0.5)
            return "RF set to "+set
    def get_output(self):
        #get RF status; if device is on or not
        #returns 1 (ON) or 0 (OFF)
        return 'RF '+self.ask(b'OUTP:STAT?\r')
    def power_normalSweep(self,startp, endp, stepp, freq, dwell, runs, trig):
        #startf, endf, stepf are starting, ending, and step power values
        #frequency in GHz"
        #dwell is the univeral dwell time, in ms (applies to all points)
        #runs is how many repetitions of the sweep you want to do
        #trig is the trigger type; software (0), hardware (full sweep) (1), or hardware (sweep point) (2)
        if (int((endp-startp)%stepp) != 0):
            return "Invcmd_string)
            fg.write(stalid power values! Stepp must divide (endp-startp)."
        if (runs < 1 or runs > 32767):
            return "Invalid run number! Runs must be between 1 and 32767, inclusive."
        if (trig != 0 and trig != 1 and trig != 2):
            return "Invalid entry! Trig must be 0, 1, or 2"
        elif (trig == 0):
            cmd_string = str.encode("SWE:NORM:POW:SETUP -"+str(startp)+","+str(endp)+","+str(stepp)+","+str(freq)+"GHZ,"+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0,RUN\r")
            self.write(cmd_string)
            return str(startp) + "dBm to "+str(endp) + "dBm normal power sweep ran."
        else:
            cmd_string = str.encode("SWE:NORM:POW:SETUP -"+str(startp)+","+str(endp)+","+str(stepp)+","+str(freq)+"str(save)GHZ,"+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0\r")
            self.write(cmd_string)
            fg.write(str.encode('SWE:NORM:POW:STAR '+str(runs)))
            return str(startp) + "dBm to "+str(endp) + "dBm normal power sweep set- waiting for hardware trigger."
    def power_fastSweep(self,startp, endp, points, freq, dwell, runs, trig):
        #startf, endf are starting, ending values
        #points is the number of points in the sweep
        #frequency in GHz
        #dwell is the univeral dwell time, in ms (applies to all points)
        #runs is how many repetitions of the sweep you want to do
        #trig is the trigger type; software (0), hardware (full sweep) (1), or hardware (sweep point) (2)
        if (runs < 1 or runs > 32767):
            return "Invalid run number! Runs must be between 1 and 32767, inclusive."
        if (trig != 0 and trig != 1 and trig != 2):
            return "Invalid entry! Trig must be 0, 1, or 2"
        elif (trig == 0):
            cmd_string = str.encode("SWE:FAST:POW:SETUP "+str(startp)+","+str(endp)+","+str(points)+","+str(freq)+"GHZ,"+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0,RUN\r")
            self.write(cmd_string)
            return str(startp) + "dBm to "+str(endp) + "dBm normal power sweep ran."
        else:
            cmd_string = str.encode("SWE:FAST:POW:SETUP "+str(startp)+","+str(endp)+","+str(points)+","+str(freq)+"GHZ,"+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0\r")
            self.write(cmd_string)
            fg.write(str.encode('SWE:FAST:POW:STAR '+str(runs)))
            return str(startp) + "dBm to "+str(endp) + "dBm normal power sweep set-waiting for hardware trigger."
    def list_point_set(self, n, freq, power, dwell, RF):
        #note: use eraseList before saving a new list!
        #n is the point number
        #freq is the frequency for this point in GHz
        #dwell in ms
        #RF is whether or not the output will b"e on or off at this point
        if n < 1 or n > 32767:
            return "Invalid point number! FSW-0020 accepts between 1 and 32767 total points."
        if power < -10 or power > 13:
            return "Invalid power! FSW-0020 supports [-10 dBm, 13 dBm]"
        if freq < 0.5 or freq > 20:
            return "Invalid frequency! FSW-0020 supports [0.5 GHz, 20 GHz]"
        if RF != "ON" and RF != "OFF":
            return "Invalid RF setting! Must be 'ON' or 'OFF'."
        else:
            cmd_string = "LIST:PVEC "+str(n)+","+str(freq)+"GHz,"+str(power)+"dBm,"+str(dwell)+"ms,OFF,"+str(RF)+",F"
            cmd_string = str.encode(cmd_string)
            self.write(cmd_string)
            return "List point "+str(n)+" modified."
    def runList(self, dwell, runs, trig):
        #dwell is the universal dwell time; use 0 to run saved dwell times
        #runs is how many cycles of the list you want to run
        #trig is 0 for software, 1 for hardware, and 2 for hardware point by point
        if runs < 0: #note runs = 0 causes the device to run forever
            return "Invalid run number! Runs must be positive."
        if trig != 0 and trig != 1 and trig != 2:
            return "Invalid trigger number! Trig can be 0 (software), 1 (hardware) or 2 (hardware point by point)."
        else:
            cmd_string = "LIST:SETUP "+str(dwell)+"ms,"+str(runs)+","+str(trig)+",0,RUN"
            print(cmd_string)
            cmd_string = str.encode(cmd_string)
            self.write(cmd_string)
            return "List ran "+str(runs)+" times."
    def eraseList(self):
        #erase the saved list. MUST be done before saving a new list!
        self.write(b'LIST:ERAS')
        return "List erased."
    def set_Voltage_amplitude(self, V):
        P = (V*V)*0.5*(1/50) #50 ohm nominal input resistance for devices
        #P is power in Watts
        dBm = 10*(math.log10(P*1000)) #power in dBm
        self.set_power(dBm)
        return True
    def get_Voltage_amplitude(self):
        dBm = float(self.get_power()) #power in dBm, reported by device
        P = 0.001*float(math.pow(10,(0.1*dBm))) #power in watts
        V = math.sqrt(100*P)
        return "Voltage amplitude is "+str(V)
    def set_Voltage_rms(self, V):
        P = (V*V)*(1/50) #50 ohm nominal input resistance for devices
        #P is power in Watts
        dBm = 10*(math.log10(P*1000)) #power in dBm
        self.set_power(dBm)
        return True
    def get_Voltage_rms(self):
        dBm = float(self.get_power()) #power in dBm, reported by device
        P = 0.001*float(math.pow(10,(0.1*dBm))) #power in watts
        V = math.sqrt(50*P)
        return "V_rms is "+str(V)
    def set_Voltage_peak(self, V):
        P = (V*V)*(1/8)*(1/50) #50 ohm nominal input resistance for devices
        #P is power in Watts
        dBm = 10*(math.log10(P*1000)) #power in dBm
        self.set_power(dBm)
        return True
    def get_Voltage_peak(self):
        dBm = float(self.get_power()) #power in dBm, reported by device
        P = 0.001*float(math.pow(10,(0.1*dBm))) #power in watts
        V = math.sqrt(400*P)
        return "Peak voltage is "+str(V)

##testing
fg = FSW_0020()