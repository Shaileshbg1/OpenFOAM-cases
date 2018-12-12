# OpenFOAM-cases

This repository has different conjugate heat transfer cases simulated on OpenFOAM5 with the help of its many utilities and automation of these cases using python and pyFoam, with visualization on paraview.

The physical phenomenon that we are trying to understand and simulate is that of heat transfer inside a breast with malignant tissue (tumor). 

The cases published here are the rough works which I carried out in setting up conjugate heat transfer cases in OpenFOAM using its (and some user defined) utilities, and visualization with paraview. My work in any of the organizations is not published.

Learning objectives:
1) Basic templates for setting up conjugate heat transfer cases in OpenFOAM with multiple materials.
2) Defining material properties, boundary conditions and energy sources for each material.
3) Using multiple pre-processing (changeDictionary, setFields, mapFields, etc), mesh generation (blockMesh, snappyHexMesh), mesh manipulation (createPatch, createBaffles, checkMesh, etc) and postProcessing (postProcess) utilities.
4) Using user defined utilities like pyFoam (pyFoamPlotRunner, pyFoamFromTemplate) to manipulate OpenFOAM cases and control OpenFOAM runs.
5) Automation of OpenFoam cases using python and pyFoam (parsedParameterFile, BasicRunner.)
6) Basic changes to the solver (mostly querying information about meshes, boundary patches, boundary and internal field values etc) 
7) Basic field operations (defining different volume scalar/vector and tensor fields.)
8) Using python trace files to manipulate paraview visualization.
