# Import libraries
import xarray as xr
import parflow as pf
import pandas as pd
import glob
import numpy as np
import argparse

# Set up argument parsing for command line arguments
parser = argparse.ArgumentParser(description="Aggregate NLDAS-3 CONUS2 forcing data.")

parser.add_argument('waterYear', type=int, help='Water year of hourly NLDAS data to aggregate.')
parser.add_argument('variable', type=str, help='Forcing variable to aggregate.')
parser.add_argument('function', type=str, help='Aggregation function.')

# Parse arguments
args = parser.parse_args()

#################
# Set file paths and variable names
#################
waterYear = args.waterYear
var = args.variable
agg_function = args.function

# Set directory paths
indir = '/hydrodata/forcing/processed_data/CONUS2/NLDAS3/WY'
outdir = '/hydrodata/forcing/processed_data/CONUS2/NLDAS3/daily/WY'

if waterYear % 4 == 0: 
    N_days = 366
else: 
    N_days = 365

#################
# Aggregate
#################

# Loop through each day
for d in range(N_days):

    istep_start = str(int(d*24+1)).rjust(6, '0')
    istep_end = str(int((d+1)*24)).rjust(6, '0')

    filepath = indir + str(waterYear) + '/NLDAS.' + var + '.' + istep_start + '_to_' + istep_end + '.pfb'
    
    # Open as x-array DataSet
    ds = xr.open_dataset(filepath, name='var')

    # Aggregate
    if agg_function == 'mean':
        ds_agg = ds.mean(dim='z')
    elif agg_function == 'sum':
        ds_agg = ds.sum(dim='z') * 3600
    elif agg_function == 'min':
        ds_agg = ds.min(dim='z')
    elif agg_function == 'max':
        ds_agg = ds.max(dim='z')

    ds_numpy = ds_agg['var'].to_numpy()

    # reset to minimum float values where calculated to -inf
    ds_numpy[ds_numpy < np.finfo(np.float64).min] = np.finfo(np.float64).min

    # Set daily file number, starting counting at 001
    filenum = str(d+1)
        
    while len(filenum) < 3: 
        filenum = '0' + filenum
                
    # Save as daily pfb files
    outpath = outdir + str(waterYear) + '/NLDAS.' + var + '.daily.' + agg_function + '.' + filenum + '.pfb'
    pf.write_pfb(outpath, ds_numpy, p=48, q=48, r=1, dist=False)
