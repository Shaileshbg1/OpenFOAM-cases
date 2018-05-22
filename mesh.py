#!/usr/bin/python

import os
from os import path
import subprocess
from subprocess import *
import csv
import sys

from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory
from PyFoam.Basics.TemplateFile import TemplateFile

# clean
subprocess.call(['./clean.sh'])
print("Cleaning the case done")

orig = SolutionDirectory(path.expandvars("$HOME/Niramai/Niramai_cases/with_subprocess"), archive=None, paraviewLink=False)

'''


filename = "input.csv"  # csv file name
fields = []  # initializing the titles and rows list
rows = []

with open(filename, 'r') as inputfile:  # reading csv file
    csvreader = csv.reader(inputfile)  # creating a csv reader object
    fields = next(csvreader)  # extracting field names through first row
    for row in csvreader:  # extracting each data row one by one
        x = row[0]
        y = row[1]
        z = row[2]
        r = row[3]

    #print("Total number of rows: ", csvreader.line_num)

    #print("Field names are: " + ','.join(field for field in fields))  # printing field names
'''

# Muscle Meshing
# run blockMesh
os.chdir("muscle")
cmd = 'blockMesh -noFunctionObjects > logBlockMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Muscle blockMesh done")

# run snappyHexMesh
cmd = 'snappyHexMesh -overwrite -noFunctionObjects > logSnappyHexMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Muscle snappyHexMesh done")

os.chdir("..")

# Tissue Meshing
# run blockMesh
os.chdir("tissue")
cmd = 'blockMesh -noFunctionObjects > logBlockMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Tissue blockMesh done")

# run snappyHexMesh
cmd = 'snappyHexMesh -overwrite -noFunctionObjects > logSnappyHexMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Tissue snappyHexMesh done")

os.chdir("..")

# Tumor Meshing
# run blockMesh
os.chdir("tumor")
work_tumor = SolutionDirectory(path.expandvars("$HOME/Niramai/Niramai_cases/with_subprocess/tumor"), archive=None,
                               paraviewLink=False)
cmd = 'blockMesh -noFunctionObjects > logBlockMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Tumor blockMesh done")

# run pyFoamFromTemplate
bmName = path.join(work_tumor.systemDir(), "snappyHexMeshDict")
template = TemplateFile(bmName + ".template", expressionDelimiter="$")
template.writeToFile(bmName, {'x': 0, 'y': 0.049, 'z': 0, 'r': 0.01})
cmd = 'pyFoamFromTemplate.py system/snappyHexMeshDict'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Setting template file for tumor done")

# run snappyHexMesh
cmd = 'snappyHexMesh -overwrite -noFunctionObjects > logSnappyHexMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Tumor snappyHexMesh done")

os.chdir("..")

# Gland Meshing
# run blockMesh

work_gland = SolutionDirectory(path.expandvars("$HOME/Niramai/Niramai_cases/with_subprocess/gland"), archive=None,
                               paraviewLink=False)
os.chdir("gland")
cmd = 'blockMesh -noFunctionObjects > logBlockMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Gland blockMesh done")

# run pyFoamFromTemplate
bmName = path.join(work_gland.systemDir(), "snappyHexMeshDict")
template = TemplateFile(bmName + ".template", expressionDelimiter="$")
template.writeToFile(bmName, {'x': 0, 'y': 0.049, 'z': 0, 'r': 0.01})
cmd = 'pyFoamFromTemplate.py system/snappyHexMeshDict'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Setting template file for gland done")

# run snappyHexMesh
cmd = 'snappyHexMesh -overwrite -noFunctionObjects > logSnappyHexMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Gland snappyHexMesh done")

print("Meshing all the four regions complete")

# merge and stitch muscle mesh onto gland
# run mergeMesh
cmd = 'mergeMeshes -overwrite -noFunctionObjects . ../muscle/ > logMergeMuscleGland'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Merging of muscle and gland meshes done")

# run stitch mesh
cmd = 'stitchMesh -partial -toleranceDict toleranceDict -overwrite -noFunctionObjects muscle_ext muscle_int > logStitchMuscleGland'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Stitching of muscle and gland meshes done")


# removing extra files

def bash_command(cmd):
    subprocess.Popen(cmd, shell=True, executable='/bin/bash')


os.chdir("0")
bash_command('rm meshPhi')
os.chdir("../constant/polyMesh")
bash_command('rm *Zones')
bash_command('rm meshModifiers')
os.chdir("../..")

# merge and stitch tissue mesh onto gland
# run mergeMesh
cmd = 'mergeMeshes -overwrite -noFunctionObjects . ../tissue/ > logMergeTissueGland'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Merging of tissue and gland meshes done")

# run stitch mesh
cmd = 'stitchMesh -partial -toleranceDict toleranceDict -overwrite -noFunctionObjects gland_ext gland_int > logStitchTissueGland'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Stitching of tissue and gland meshes done")

# removing extra files

os.chdir("0")
bash_command('rm meshPhi')
os.chdir("../constant/polyMesh")
bash_command('rm *Zones')
bash_command('rm meshModifiers')
os.chdir("../..")

# merge and stitch tumor mesh onto gland
# run mergeMesh
cmd = 'mergeMeshes -overwrite -noFunctionObjects . ../tumor/ > logMergeTumorGland'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Merging of tumor and gland meshes done")

# run stitch mesh
cmd = 'stitchMesh -partial -toleranceDict toleranceDict -overwrite -noFunctionObjects tumor_ext tumor_int > logStitchTumorGland'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Stitching of tumor and gland meshes done")

# removing extra files

os.chdir("0")
bash_command('rm meshPhi')
os.chdir("../constant/polyMesh")
bash_command('rm *Zones')
bash_command('rm meshModifiers')
os.chdir("../..")

# run checkMesh
cmd = 'checkMesh > logCheckMesh'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("checkMesh done")

# define different cell zones using topoSetDict
bmName = path.join(work_gland.systemDir(), "topoSetDict")
template = TemplateFile(bmName + ".template", expressionDelimiter="$")
template.writeToFile(bmName, {'x': 0, 'y': 0.049, 'z': 0, 'r': 0.01})
cmd = 'pyFoamFromTemplate.py system/topoSetDict'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Setting different cellZones done")

# run topoSet
cmd = 'topoSet -noFunctionObjects > logtopoSet'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Setting of cellZones by topoSet done")

# splitMesh as per different cellZones
cmd = 'splitMeshRegions -cellZones -overwrite -noFunctionObjects > logSplitMeshRegions'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("splitMesh done")

# counting the number of folders in system directory after split mesh
folders = 0

for _, dirnames, filenames in os.walk("system"):
    # ^ this idiom means "we won't be using this value"
    folders += len(dirnames)

print("{:,} folders".format(folders))

# stop execution if no of folders > 4

if folders > 4:
    print("There are unwanted domains formed, change tumor location and/or dimensions to within tolerance limits - stopping execution")
    sys.exit()

# setting initial conditions for each region in 0
bash_command('tee 0/gland/T 0/muscle/T 0/tissue/T 0/tumor/T < T >/dev/null')
bash_command('tee 0/gland/p 0/muscle/p 0/tissue/p 0/tumor/p < p >/dev/null')
print("Copying initial conditions done")

# run changeDictionary to define initial conditions for each region
subprocess.call(['./changeDictionary.sh'])

print("setting initial conditions for each region done")

# setting metabolic heat generation rate of tumor

metabolic_path = os.path.abspath(os.path.dirname(__file__))
bmName = os.path.join(metabolic_path, "constant/tumor/fvOptions")
template = TemplateFile(bmName + ".template", expressionDelimiter="$")
template.writeToFile(bmName, {'r': 0.01})
cmd = 'pyFoamFromTemplate.py constant/tumor/fvOptions'
pipefile = open('output', 'w')
retcode = call(cmd, shell=True, stdout=pipefile)
pipefile.close()
os.remove('output')
print("Setting metabolic heat generation rate of tumor done")
