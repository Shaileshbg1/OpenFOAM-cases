#!/bin/sh
# Source tutorial run functions
. $WM_PROJECT_DIR/bin/tools/CleanFunctions
. $WM_PROJECT_DIR/bin/tools/RunFunctions

# RUN changeDictionary TO DEFINE INITIAL CONDITIONS FOR EACH REGION 
for i in muscle gland tissue tumor
do
   runApplication -s $i changeDictionary -region $i
done

