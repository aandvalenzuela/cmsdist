### RPM external py3-docutils 0.17.1
## IMPORT build-with-pip3

%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*