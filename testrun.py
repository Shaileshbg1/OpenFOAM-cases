#!/usr/bin/python

import os, subprocess, sys, mmap
import numpy as np
from os import path
from subprocess import *
from numpy import genfromtxt
from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory
from PyFoam.Basics.TemplateFile import TemplateFile

input_data = genfromtxt('input_file.csv', delimiter=',')
# print(input_data.shape[0])
for i in range(input_data.shape[0]):
    for y in np.arange(0.035, 0.055, 0.005):

        # clean
        subprocess.call(['./clean.sh'])
        print("Cleaning the case done")

        orig = SolutionDirectory(path.expandvars("$HOME/Niramai/Niramai_cases/with_subprocess"), archive=None,
                                 paraviewLink=False)

        # Muscle Meshing
        # run blockMesh
        work_muscle = SolutionDirectory(path.expandvars("$HOME/Niramai/Niramai_cases/with_subprocess/muscle"),
                                        archive=None,
                                        paraviewLink=False)
        os.chdir("muscle")
        subprocess.call('blockMesh > logblockMesh', shell=True, stdout=PIPE, stderr=PIPE)
        if 'End' in open('logblockMesh').read():
            print("Muscle blockMesh done")
        else:
            print('There is a problem with muscle blockMesh')
            print("Stopping execution")
            sys.exit()

        # run pyFoamFromTemplate
        bmName = path.join(work_muscle.systemDir(), "snappyHexMeshDict")
        template = TemplateFile(bmName + ".template", expressionDelimiter="$")
        template.writeToFile(bmName, {'mr': input_data[i, 4]})
        subprocess.call('pyFoamFromTemplate.py system/snappyHexMeshDict ', shell=True, stderr=PIPE,
                        stdout=PIPE)
        print("Setting template file for muscle done")

        # run snappyHexMesh
        subprocess.call('snappyHexMesh -overwrite > logsnappyHexMesh', shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logsnappyHexMesh').read():
            print("Muscle snappyHexMesh done")
        else:
            print('There is a problem with muscle snappyHexMesh')
            print("Stopping execution")
            sys.exit()

        # Tissue Meshing
        # run blockMesh
        work_tissue = SolutionDirectory(path.expandvars("$HOME/Niramai/Niramai_cases/with_subprocess/tissue"),
                                        archive=None,
                                        paraviewLink=False)
        os.chdir("..")
        os.chdir("tissue")
        subprocess.call('blockMesh > logblockMesh', shell=True, stdout=PIPE, stderr=PIPE)
        if 'End' in open('logblockMesh').read():
            print("Tissue blockMesh done")
        else:
            print('There is a problem with tissue blockMesh')
            print("Stopping execution")
            sys.exit()

        # run pyFoamFromTemplate
        bmName = path.join(work_tissue.systemDir(), "snappyHexMeshDict")
        template = TemplateFile(bmName + ".template", expressionDelimiter="$")
        template.writeToFile(bmName, {'sr': input_data[i, 6], 'gr': input_data[i, 5]})
        subprocess.call('pyFoamFromTemplate.py system/snappyHexMeshDict ', shell=True, stderr=PIPE,
                        stdout=PIPE)
        print("Setting template file for tissue done")

        # run snappyHexMesh
        subprocess.call('snappyHexMesh -overwrite > logsnappyHexMesh', shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logsnappyHexMesh').read():
            print("Tissue snappyHexMesh done")
        else:
            print('There is a problem with tissue snappyHexMesh')
            print("Stopping execution")
            sys.exit()

        # Tumor Meshing
        # run blockMesh
        os.chdir("..")
        os.chdir("tumor")
        work_tumor = SolutionDirectory(path.expandvars("$HOME/Niramai/Niramai_cases/with_subprocess/tumor"),
                                       archive=None,
                                       paraviewLink=False)
        subprocess.call('blockMesh > logblockMesh', shell=True, stdout=PIPE, stderr=PIPE)
        if 'End' in open('logblockMesh').read():
            print("Tumor blockMesh done")
        else:
            print('There is a problem with tumor blockMesh')
            print("Stopping execution")
            sys.exit()

        # run pyFoamFromTemplate
        bmName = path.join(work_tumor.systemDir(), "snappyHexMeshDict")
        template = TemplateFile(bmName + ".template", expressionDelimiter="$")
        template.writeToFile(bmName,
                             {'x': input_data[i, 0], 'y': y, 'z': input_data[i, 2],
                              'r': input_data[i, 3]})
        subprocess.call('pyFoamFromTemplate.py system/snappyHexMeshDict ', shell=True, stderr=PIPE,
                        stdout=PIPE)
        print("Setting template file for tumor done")

        # run snappyHexMesh
        subprocess.call('snappyHexMesh -overwrite > logsnappyHexMesh', shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logsnappyHexMesh').read():
            print("Tumor snappyHexMesh done")
        else:
            print('There is a problem with tumor snappyHexMesh')
            print("Stopping execution")
            sys.exit()

        # Gland Meshing
        # run blockMesh

        work_gland = SolutionDirectory(path.expandvars("$HOME/Niramai/Niramai_cases/with_subprocess/gland"),
                                       archive=None,
                                       paraviewLink=False)
        os.chdir("..")
        os.chdir("gland")
        subprocess.call('blockMesh > logblockMesh', shell=True, stdout=PIPE, stderr=PIPE)
        if 'End' in open('logblockMesh').read():
            print("Gland blockMesh done")
        else:
            print('There is a problem with gland blockMesh')
            print("Stopping execution")
            sys.exit()

        # run pyFoamFromTemplate
        bmName = path.join(work_gland.systemDir(), "snappyHexMeshDict")
        template = TemplateFile(bmName + ".template", expressionDelimiter="$")
        template.writeToFile(bmName,
                             {'x': input_data[i, 0], 'y': y, 'z': input_data[i, 2],
                              'r': input_data[i, 3],
                              'gr': input_data[i, 5], 'mr': input_data[i, 4]})
        subprocess.call('pyFoamFromTemplate.py system/snappyHexMeshDict ', shell=True, stderr=PIPE,
                        stdout=PIPE)
        print("Setting template file for gland done")

        # run snappyHexMesh
        subprocess.call('snappyHexMesh -overwrite > logsnappyHexMesh', shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logsnappyHexMesh').read():
            print("Gland snappyHexMesh done")
        else:
            print('There is a problem with gland snappyHexMesh')
            print("Stopping execution")
            sys.exit()

        print("Meshing all the four regions complete")

        # merge and stitch muscle mesh onto gland
        # run mergeMesh
        subprocess.call('mergeMeshes -overwrite . ../muscle/ > logMergeMuscleGland', shell=True, stderr=PIPE,
                        stdout=PIPE)
        if 'End' in open('logMergeMuscleGland').read():
            print("Merging of muscle to gland done")
        else:
            print('There was a problem while merging muscle to gland')
            print("Stopping execution")
            sys.exit()

        # run stitch mesh
        subprocess.call(
            'stitchMesh -partial -toleranceDict toleranceDict -overwrite muscle_ext muscle_int > logStitchMuscleGland',
            shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logStitchMuscleGland').read():
            print("Stitching of muscle to gland done")
        else:
            print('There was a problem while stitching muscle to gland')
            print("Stopping execution")
            sys.exit()


        # removing extra files
        # noinspection PyShadowingNames
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
        subprocess.call('mergeMeshes -overwrite . ../tissue/ > logMergeTissueGland', shell=True, stderr=PIPE,
                        stdout=PIPE)
        if 'End' in open('logMergeTissueGland').read():
            print("Merging of tissue to gland done")
        else:
            print('There was a problem while merging tissue to gland')
            print("Stopping execution")
            sys.exit()

        # run stitch mesh
        subprocess.call(
            'stitchMesh -partial -toleranceDict toleranceDict -overwrite gland_ext gland_int > logStitchTissueGland',
            shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logStitchTissueGland').read():
            print("Stitching of tissue to gland done")
        else:
            print('There was a problem while stitching tissue to gland')
            print("Stopping execution")
            sys.exit()
        # removing extra files
        os.chdir("0")
        bash_command('rm meshPhi')
        os.chdir("../constant/polyMesh")
        bash_command('rm *Zones')
        bash_command('rm meshModifiers')
        os.chdir("../..")

        # merge and stitch tumor mesh onto gland
        # run mergeMesh
        subprocess.call('mergeMeshes -overwrite . ../tumor/ > logMergeTumorGland', shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logMergeTumorGland').read():
            print("Merging of tumor to gland done")
        else:
            print('There was a problem while merging tumor to gland')
            print("Stopping execution")
            sys.exit()

        # run stitch mesh
        subprocess.call(
            'stitchMesh -partial -toleranceDict toleranceDict -overwrite tumor_ext tumor_int > logStitchTumorGland',
            shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logStitchTumorGland').read():
            print("Stitching of tumor to gland done")
        else:
            print('There was a problem while stitching tumor to gland')
            print("Stopping execution")
            sys.exit()
        # removing extra files

        os.chdir("0")
        bash_command('rm meshPhi')
        os.chdir("../constant/polyMesh")
        bash_command('rm *Zones')
        bash_command('rm meshModifiers')
        os.chdir("../..")

        # run checkMesh
        subprocess.call('checkMesh -constant -allGeometry -allTopology > logCheckMesh', shell=True, stderr=PIPE, stdout=PIPE)
        with open('logCheckMesh', 'rb', 0) as file:
            s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(b'Failed') != -1:
            print('Mesh checks failed')
            print("Stopping execution")
            sys.exit()
        else:
            print("Check mesh done")

        # define different cell zones using topoSetDict
        bmName = path.join(work_gland.systemDir(), "topoSetDict")
        template = TemplateFile(bmName + ".template", expressionDelimiter="$")
        template.writeToFile(bmName,
                             {'x': input_data[i, 0], 'y': y, 'z': input_data[i, 2],
                              'r': input_data[i, 3],
                              'sr': input_data[i, 6], 'gr': input_data[i, 5], 'mr': input_data[i, 4]})
        subprocess.call('pyFoamFromTemplate.py system/topoSetDict', shell=True, stderr=PIPE, stdout=PIPE)
        print("Setting different cellZones done")

        # run topoSet
        subprocess.call('topoSet > logtopoSet', shell=True, stderr=PIPE, stdout=PIPE)
        if 'End' in open('logtopoSet').read():
            print("Separating meshes by topoSet done")
        else:
            print('There was a problem while separating meshes by topoSet')
            print("Stopping execution")
            sys.exit()

        # splitMesh as per different cellZones
        subprocess.call('splitMeshRegions -cellZones -overwrite > logSplitMeshRegions', shell=True, stderr=PIPE,
                        stdout=PIPE)
        if 'End' in open('logSplitMeshRegions').read():
            print("Splitting meshes done")
        else:
            print('There was a problem while splitting meshes')
            print("Stopping execution")
            sys.exit()
        # counting the number of folders in system directory after split mesh
        folders = 0

        for _, dirnames, filenames in os.walk("system"):
            # ^ this idiom means "we won't be using this value"
            folders += len(dirnames)

        print("The number of folders after split mesh is: {:,} folders".format(folders))

        # stop execution if no of folders > 4

        if folders > 4:
            # noinspection PyPep8
            print("Unwanted domains formed, change tumor location and/or dimensions to within tolerance limits")
            print("Stopping execution")
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
        template.writeToFile(bmName, {'r': input_data[i, 3]})
        subprocess.call('pyFoamFromTemplate.py constant/tumor/fvOptions', shell=True, stderr=PIPE, stdout=PIPE)
        print("Setting metabolic heat generation rate of tumor done")

        # Running solver
        subprocess.call('pyFoamPlotRunner.py --hardcopy --progress chtMultiRegionSimpleFoam', shell=True, stderr=PIPE,
                        stdout=PIPE)
        if 'End' in open('PyFoamRunner.chtMultiRegionSimpleFoam.logfile').read():
            print("Solver run done")
        else:
            print('There was a problem while running the solver')
            print("Stopping execution")
            sys.exit()

        # plotting residuals
        subprocess.call('pyFoamRedoPlot.py --csv-files --pickle-file Gnuplotting.analyzed/pickledPlots', shell=True,
                        stderr=PIPE, stdout=PIPE)
        print("Plotting done")

        # post processing
        subprocess.call('paraFoam -touchAll', shell=True, stderr=PIPE, stdout=PIPE)
        print("Creating files for paraview post-processing done")

        subprocess.call('all.foam', shell=True, stderr=PIPE, stdout=PIPE)
        print("Created one combined file")
