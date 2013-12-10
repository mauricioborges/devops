#!/bin/env bash
# Script to run jython with wlst as a module
# set up WL_HOME, the root directory of your WebLogic installation
WL_HOME="/home/vagrant/Oracle/Middleware/wlserver_10.3"
JAVA_HOME="/usr/java/jdk1.7.0_45/"
WLST_OFFLINE_LOG=/tmp/wlstscripting.$$.log
WLST_CACHEDIR=~/.jythoncachedir
#FKUTILS="."
#JYTHON="/program/jython"

killed () {
   echo ""
   echo Cleaning up tempfile: $WLST_OFFLINE_LOG
   rm -rf $WLST_OFFLINE_LOG
   trap - 0
}


umask 027
touch $WLST_OFFLINE_LOG
chmod 777 $WLST_OFFLINE_LOG
if [ ! -d $WLST_CACHEDIR ] ; then
    mkdir -p $WLST_CACHEDIR
fi

trap killed 0 1 2 15
# set up common environment
. "${WL_HOME}/server/bin/setWLSEnv.sh" 2>&1 > /dev/null

#CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${FMWLAUNCH_CLASSPATH}${CLASSPATHSEP}${DERBY_CLASSPATH}${CLASSPATHSEP}${DERBY_TOOLS}${CLASSPATHSEP}${POINTBASE_CLASSPATH}${CLASSPATHSEP}${POINTBASE_TOOLS}:${FKUTILS}"
CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${FMWLAUNCH_CLASSPATH}${CLASSPATHSEP}${DERBY_CLASSPATH}${CLASSPATHSEP}${DERBY_TOOLS}${CLASSPATHSEP}${POINTBASE_CLASSPATH}${CLASSPATHSEP}${POINTBASE_TOOLS}"

#echo CLASSPATH=${CLASSPATH}

#JVM_ARGS="-classpath ${JYTHON}/jython.jar:${CLASSPATH}  -Dpython.path=${CLASSPATH}:${HOME} ${WLST_PROPERTIES} ${JVM_D64} ${MEM_ARGS} ${CONFIG_JVM_ARGS} -Dpython.cachedir=$WLST_CACHEDIR -Dwlst.offline.log=$WLST_OFFLINE_LOG -Dweblogic.management.confirmKeyfileCreation=true -Djava.security.egd=file:///dev/urandom"
JVM_ARGS="-classpath ${CLASSPATH}  -Dpython.path=${CLASSPATH}:${HOME} ${WLST_PROPERTIES} ${JVM_D64} ${MEM_ARGS} ${CONFIG_JVM_ARGS} -Dpython.cachedir=$WLST_CACHEDIR -Dwlst.offline.log=$WLST_OFFLINE_LOG -Dweblogic.management.confirmKeyfileCreation=true -Djava.security.egd=file:///dev/urandom"

"${JAVA_HOME}/bin/java" ${JVM_ARGS} org.python.util.jython "$@"
