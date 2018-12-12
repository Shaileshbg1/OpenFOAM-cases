#!/bin/sh
cd ${0%/*} || exit 1    # Run from this directory

# Source tutorial clean functions
. $WM_PROJECT_DIR/bin/tools/CleanFunctions

cleanCase
<muscle_directory>
rm -rf log*
rm -rf constant/polyMesh

<gland_directory>
find <path_to_gland_directory>/constant -maxdepth 1 -mindepth 1 -not -name cellToRegion -not -name regionProperties -not -name toleranceDict -not -name triSurface -not -name gland -not -name muscle -not -name tissue -not -name tumor -exec rm -R {} \;
find <path_to_gland_directory>system -maxdepth 1 -mindepth 1 -not -name blockMeshDict -not -name controlDict -not -name decomposeParDict -not -name fvSchemes -not -name fvSolution -not -name meshQualityDict -not -name snappyHexMeshDict -not -name snappyHexMeshDict.template -not -name topoSetDict -not -name topoSetDict.template -not -name gland -not -name tissue -not -name tumor -not -name muscle -not -name blockMeshDict.template -not -name surfaces -not -name setFieldsDict -exec rm -R {} \;
rm -r 0/
mkdir 0/

find <path_to_gland_directory> -maxdepth 1 -mindepth 1 -not -name T -not -name p -not -name 0 -not -name constant -not -name system -not -name changeDictionary.sh -exec rm -R {} \;
rm -rf constant/gland/polyMesh
rm -rf constant/muscle/polyMesh
rm -rf constant/tissue/polyMesh
rm -rf constant/tumor/polyMesh

<tissue directory>
rm -rf log*
rm -rf constant/polyMesh

<tumor_directory>
rm -rf log*
rm -rf constant/polyMesh

#------------------------------------------------------------------------------
