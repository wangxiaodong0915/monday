MONDAY_PATH=/home/monday_uat/monday
MONDAY_LOG=/home/monday_uat/log
PYTHONPATH=$MONDAY_PATH/lib
export MONDAY_PATH
export MONDAY_LOG
export PYTHONPATH
PATH=$PATH:$MONDAY_PATHE/lib
export PATH

echo $PATH
echo $MONDAY_LOG
echo $MONDAY_PATH