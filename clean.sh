#!/bin/sh
cd ${0%/*} || exit 1    # Run from this directory

# Source tutorial clean functions
. $WM_PROJECT_DIR/bin/tools/CleanFunctions
<muscle>
cleanCase
rm -rf log*
rm -rf constant/polyMesh

find <path_to_directory>/constant -maxdepth 1 -mindepth 1 -not -name cellToRegion -not -name regionProperties -not -name toleranceDict -not -name triSurface -not -name gland -not -name muscle -not -name tissue -exec rm -R {} \;
find <path_to_directory>/system -maxdepth 1 -mindepth 1 -not -name blockMeshDict -not -name controlDict -not -name decomposeParDict -not -name fvSchemes -not -name fvSolution -not -name meshQualityDict -not -name snappyHexMeshDict -not -name snappyHexMeshDict.template -not -name topoSetDict -not -name topoSetDict.template -not -name gland -not -name tissue -not -name muscle -not -name blockMeshDict.template -exec rm -R {} \;
rm -r 0/
mkdir 0/

find <path_to_gland_directory> -maxdepth 1 -mindepth 1 -not -name T -not -name p -not -name 0 -not -name constant -not -name system -not -name changeDictionary.sh -exec rm -R {} \;
rm -rf constant/gland/polyMesh
rm -rf constant/muscle/polyMesh
rm -rf constant/tissue/polyMesh

<tissue>
rm -rf log*
rm -rf constant/polyMesh

#------------------------------------------------------------------------------
