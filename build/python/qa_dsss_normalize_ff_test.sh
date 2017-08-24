#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/build/python:$PATH
export DYLD_LIBRARY_PATH=/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/build/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=/Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/build/swig:$PYTHONPATH
/opt/local/bin/python2.7 /Users/victorguipont/Developpement-informatique/GNU-radio/gr-lpwan/python/qa_dsss_normalize_ff.py 
