# _______________________________________________________________________________________________________________________
# Author:       W Eaton, Princeton Uni. 2022
# Contact:      weaton@princeton.edu
# Last edit:    4th Feb 2022
# Notes:
#   Script to isolate gravity from the no_gravitation and cowling/self-gravitation simulations:
# ______________________________________________________________________________________________________________________
import numpy as np
from create_stn_list import gen_stn_list

# SPECIFY PARAMS:
path_no_grav  = "./test1/no_gravitation/specfemx/raw"
label_no_grav = "nograv_noatt.yspec"

path_grav = "./test1/self_gravitation/specfemx/conv"

path_out = "./test1/pure_gravity/yspec/self_grav/conv"

channels = "ZTPG"

stns = gen_stn_list(18)

for stn in stns:
    # Load no-gravity data - note not loading grav column as erroneous for obvious reasons:
    ng_data = np.loadtxt(fname=f"{path_no_grav}/conv_{stn}.Y5.MX")

    # Load gravity data
    g_data = np.loadtxt(fname=f"{path_grav}/{label_grav}.{stn}", usecols=usecols[grav_type])

    # Check time is correct
    assert (ng_data[:,0] == g_data[:,0]).all()

    for i in range(len(channels)):
        chl = channels[i]

        if chl == "G":
            grav = g_data[:, i + 1]
        else:
            grav = g_data[:, i+1] - ng_data[:, i+1]


        out_fname = f"{path_out}/{label_out}.{stn}.D{chl}"
        np.savetxt(fname=out_fname, X=np.transpose(np.array([ng_data[:,0], grav])), fmt="%f" )

        print(f"Saved {out_fname}")



