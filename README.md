# Bruker OPUS to .DPT bulk file converter

Bulk file converter for Bruker OPUS Spectroscopy Software 

Convert many binary format OPUS files to .dpt (Data Point Table) file format

This script uses the [Bruker OPUS Reader](https://github.com/qedsoftware/brukeropusreader) package to convert binary OPUS files into python objects, and then creates .dpt files from the ScSm (Single channel spectrum of the sample) data.

How to use:

1. Create ```/dpt_template``` and ```/raw_data``` folders in the root folder of this project. (On the same level as main.py)
2. Manually convert one OPUS file e.g. (XXX.0001) to .dpt format and place it in the ```/dpt_template``` directory. (The X-Axis will be extracted from this template to be used as the X-Axis for all bulk-converted files)
3. Place your binary OPUS files in the ```/raw_data``` folder. You can create as many nested subdirectories as you'd like - this same folder structure will be copied and used for the converted files. (e.g. for a binary file placed in ```/raw_data/scan 1/full scan.0001```, the converted .dpt file will be generated and placed in ```/converted_data/scan 1/full scan.0001.dpt```)
4. Run ```python -m pip install -r requirements.txt``` to install dependencies
4. Run the bulk conversion script with the following command: ```python main.py```
