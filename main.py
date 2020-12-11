from brukeropusreader import read_file
import glob
import os
import shutil
from pathlib import Path
from decimal import Decimal, ROUND_HALF_EVEN

# Find manually converted .dpt file to take X-Axis values from
dptTemplate = glob.glob("dpt_template/*.dpt")[0]

# Read through .dpt template line by line, extracting the X-Axis values
with open(dptTemplate, "r") as file:
  dptArray = file.readlines()
  xValues = list(map(lambda line: line[0: line.index(",")], dptArray))

# Store all /raw_data subdirectories and files in lists
subdirs = [x[0] for x in os.walk("raw_data")]
filesAndDirs = list(map(lambda dir: glob.glob(dir + "/*"), subdirs))
flatFilesAndDirs = [item for sublist in filesAndDirs for item in sublist]
files = list(filter(lambda filtered: os.path.isfile(filtered), flatFilesAndDirs))
dirs = list(filter(lambda filtered: os.path.isdir(filtered), flatFilesAndDirs))

# Remove /converted_data folder
try:
  shutil.rmtree("converted_data")
except:
  print("could not remove /converted_data, directory not does exist")

# Calculate files and directories that need to be created
targetDirs = list(map(lambda dir: dir.replace("raw_data/", "converted_data/"), dirs))
targetFiles = list(map(lambda file: file.replace("raw_data/", "converted_data/"), files))

# Create all target directories
for dir in targetDirs:
  try:
    Path(dir).mkdir(parents=True, exist_ok=True)
  except:
    print("Could not create directory: " + dir)

# Read binary OPUS files and extract ScSm data, lining up each value with it's
# corresponding X-Axis value, and save each row as an X-Axis,Y-Axis pair
for fileIndex, binaryFile in enumerate(files):
  opus_data = read_file(binaryFile)
  newFileName = targetFiles[fileIndex] + ".dpt"
  with open(newFileName, "w") as newFile:
    for index, yValue in enumerate(opus_data["ScSm"]):
      newFile.write(str(xValues[index]) + "," + str(Decimal(str(yValue)).quantize(Decimal('.00001'), rounding=ROUND_HALF_EVEN)) + "\n")
  print("Created file: " + newFileName)