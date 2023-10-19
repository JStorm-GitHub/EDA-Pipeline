###############################################################################
# Created by write_sdc
# Tue May 16 21:23:53 2023
###############################################################################
current_design s386
###############################################################################
# Timing Constraints
###############################################################################
create_clock -name clk -period 1.0000 
set_clock_uncertainty 0.0500 clk
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {CK}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {CK}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {GND}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {GND}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {VDD}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {VDD}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v0}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v0}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v1}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v1}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v2}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v2}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v3}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v3}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v4}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v4}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v5}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v5}]
set_input_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v6}]
set_input_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v6}]
set_output_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v13_D_10}]
set_output_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v13_D_10}]
set_output_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v13_D_11}]
set_output_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v13_D_11}]
set_output_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v13_D_12}]
set_output_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v13_D_12}]
set_output_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v13_D_6}]
set_output_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v13_D_6}]
set_output_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v13_D_7}]
set_output_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v13_D_7}]
set_output_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v13_D_8}]
set_output_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v13_D_8}]
set_output_delay 0.1000 -clock [get_clocks {clk}] -min -add_delay [get_ports {v13_D_9}]
set_output_delay 0.2000 -clock [get_clocks {clk}] -max -add_delay [get_ports {v13_D_9}]
###############################################################################
# Environment
###############################################################################
###############################################################################
# Design Rules
###############################################################################
