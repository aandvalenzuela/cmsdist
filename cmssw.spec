### RPM cms cmssw CMSSW_13_2_X_2023-05-31-1100

Requires: cmssw-tool-conf

%define runGlimpse      yes
%define saveDeps        yes
%define branch          master
%define gitcommit       %{realversion}
# build with debug symbols, and package them in a separate rpm
%define subpackageDebug yes

## INCLUDE cmssw-queue-override

%define source1         git://github.com/cms-sw/cmssw.git?protocol=https&obj=%{branch}/%{gitcommit}&module=%{cvssrc}&export=%{srctree}&output=/src.tar.gz

## SUBPACKAGE debug IF %subpackageDebug
## INCLUDE scram-project-build
