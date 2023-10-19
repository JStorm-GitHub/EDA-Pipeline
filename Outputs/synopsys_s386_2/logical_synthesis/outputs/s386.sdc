###################################################################

# Created by write_sdc on Tue May 16 20:38:28 2023

###################################################################
set sdc_version 2.0

set_units -time ns -resistance MOhm -capacitance fF -voltage V -current uA
set_max_area 0
set_load -pin_load 0.3 [get_ports v13_D_10]
set_load -pin_load 0.3 [get_ports v13_D_11]
set_load -pin_load 0.3 [get_ports v13_D_12]
set_load -pin_load 0.3 [get_ports v13_D_6]
set_load -pin_load 0.3 [get_ports v13_D_7]
set_load -pin_load 0.3 [get_ports v13_D_8]
set_load -pin_load 0.3 [get_ports v13_D_9]
create_clock [get_ports CK]  -name ideal_clock1  -period 2  -waveform {0 1}
set_clock_latency 0.4  [get_clocks ideal_clock1]
set_clock_uncertainty 0.05  [get_clocks ideal_clock1]
set_clock_transition -max -rise 0.1 [get_clocks ideal_clock1]
set_clock_transition -max -fall 0.1 [get_clocks ideal_clock1]
set_clock_transition -min -rise 0.1 [get_clocks ideal_clock1]
set_clock_transition -min -fall 0.1 [get_clocks ideal_clock1]
set_input_delay -clock ideal_clock1  0.1  [get_ports GND]
set_input_delay -clock ideal_clock1  0.1  [get_ports VDD]
set_input_delay -clock ideal_clock1  0.1  [get_ports v0]
set_input_delay -clock ideal_clock1  0.1  [get_ports v1]
set_input_delay -clock ideal_clock1  0.1  [get_ports v2]
set_input_delay -clock ideal_clock1  0.1  [get_ports v3]
set_input_delay -clock ideal_clock1  0.1  [get_ports v4]
set_input_delay -clock ideal_clock1  0.1  [get_ports v5]
set_input_delay -clock ideal_clock1  0.1  [get_ports v6]
set_output_delay -clock ideal_clock1  0.1  [get_ports v13_D_10]
set_output_delay -clock ideal_clock1  0.1  [get_ports v13_D_11]
set_output_delay -clock ideal_clock1  0.1  [get_ports v13_D_12]
set_output_delay -clock ideal_clock1  0.1  [get_ports v13_D_6]
set_output_delay -clock ideal_clock1  0.1  [get_ports v13_D_7]
set_output_delay -clock ideal_clock1  0.1  [get_ports v13_D_8]
set_output_delay -clock ideal_clock1  0.1  [get_ports v13_D_9]
