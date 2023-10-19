export PLATFORM               = sky130hd

export DESIGN_NAME            = s386
export DESIGN_NICKNAME        = s386

export VERILOG_FILES = $(sort $(wildcard ./designs/src/$(DESIGN_NICKNAME)/*.v))
                       
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

export SDC_FILE      = $(mkfile_dir)/*.sdc





export CORE_UTILIZATION = 60
export CORE_MARGIN = 5
export PLACE_DENSITY_LB_ADDON = 0.20
