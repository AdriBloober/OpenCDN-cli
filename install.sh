#!/bin/bash

PYTHON="python3"
PIP="$PYTHON -m pip"

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

$PIP -V
if [ $? != 0 ]; then
  echo "Please check the $PYTHON and pip requirements and install $PYTHON and $PIP!"
  exit 1
fi

$PIP install --upgrade -r requirements.txt

INSTALL_DIR=/usr/local/bin/open_cdn_cli
rm -rf $INSTALL_DIR
mkdir $INSTALL_DIR
cp open_cdn_cli/* $INSTALL_DIR/
cp __main__.py $INSTALL_DIR/
chmod a+x $INSTALL_DIR/__main__.py
EXEC=/usr/local/bin/opencdn
echo "#!/bin/bash" > $EXEC
echo "PYTHONPATH=\$PYTHONPATH:/usr/local/bin $PYTHON $INSTALL_DIR/__main__.py \$@" >> $EXEC
chmod a+x /usr/local/bin/opencdn