# OpenFOAM-cases

This repository has different conjugate heat transfer cases simulated on OpenFOAM5 with the help of its many utilities and automation of these cases using python and pyFoam, with visualization on paraview.

The physical phenomenon that we are trying to understand and simulate is that of heat transfer inside a breast with malignant tissue (tumor). 

The cases published here are the rough works which I carried out in setting up conjugate heat transfer cases in OpenFOAM using its (and some user defined) utilities, and visualization with paraview. My work in any of the organizations is not published.

The master branch uses topoSet to set up different regions in the breast, uses PyFOAM template file to automate setting up the tumor position. Has anisotropic thermal conductivity set throughout the breast.

There are six different branches each simulating a slightly different case, some description of each branch:
1) basicBashScript: This has the first basic complete set up of the case, with four different regions, each having its own material properties and sources. Run script runs the whole case including setting up files for postprocessing, clean script works on 'find' statement so the directory structure has to be changed. This does not have any pyFoam utilities used.

2) dense_breast_5mm_tissue: This case has pyfoam utilities utilized for checking the residuals, having a case summary, etc.

3) fatty_breast_12mm_tissue: Same set up as dense breast structure but the tissue region's dimensions have been changed, and hence changes to snappyHexMeshDict.

4) snappy_with_stls: Defining different regions using stls in snappyHexMesh.

5) on_server: Dense breast case modified to be utilizable on a server set up (like using pyFoamRunner.py instead of pyFoamPlotRunner.py)

6) no_tumor: Case set up with only three regions.

Learning objectives:
1) Basic templates for setting up conjugate heat transfer cases in OpenFOAM with multiple materials.
2) Defining material properties, boundary conditions and energy sources for each material.
3) Using multiple pre-processing (changeDictionary, setFields, mapFields, etc), mesh generation (blockMesh, snappyHexMesh), mesh manipulation (createPatch, createBaffles, checkMesh, etc) and postProcessing (postProcess) utilities.
4) Using user defined utilities like pyFoam (pyFoamPlotRunner, pyFoamFromTemplate) to manipulate OpenFOAM cases and control OpenFOAM runs.
5) Setting anisotropic thermal conductivity, using topoSet to define different regions, using setFields to set different regional properties. 

