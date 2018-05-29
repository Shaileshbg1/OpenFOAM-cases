#!/bin/sh
cd ${0%/*} || exit 1    # Run from this directory

# Source tutorial clean functions
. $WM_PROJECT_DIR/bin/tools/CleanFunctions

cleanCase
cd muscle/
rm -rf log*
rm -rf constant/polyMesh

cd ../gland/
find /home/shailesh/Niramai/Niramai_cases/with_subprocess/gland/constant -maxdepth 1 -mindepth 1 -not -name cellToRegion -not -name regionProperties -not -name toleranceDict -not -name triSurface -not -name gland -not -name muscle -not -name tissue -not -name tumor -exec rm -R {} \;
find /home/shailesh/Niramai/Niramai_cases/with_subprocess/gland/system -maxdepth 1 -mindepth 1 -not -name blockMeshDict -not -name controlDict -not -name decomposeParDict -not -name fvSchemes -not -name fvSolution -not -name meshQualityDict -not -name snappyHexMeshDict -not -name snappyHexMeshDict.template -not -name topoSetDict -not -name topoSetDict.template -not -name gland -not -name tissue -not -name tumor -not -name muscle -not -name blockMeshDict.template -not -name surfaces -exec rm -R {} \;
rm -r 0/
mkdir 0/

find /home/shailesh/Niramai/Niramai_cases/with_subprocess/gland/ -maxdepth 1 -mindepth 1 -not -name T -not -name p -not -name 0 -not -name constant -not -name system -not -name changeDictionary.sh -not -name dataFile -exec rm -R {} \;
rm -rf constant/gland/polyMesh
rm -rf constant/muscle/polyMesh
rm -rf constant/tissue/polyMesh
rm -rf constant/tumor/polyMesh

cd ../tissue/
rm -rf log*
rm -rf constant/polyMesh

cd ../tumor/
rm -rf log*
rm -rf constant/polyMesh

#------------------------------------------------------------------------------
