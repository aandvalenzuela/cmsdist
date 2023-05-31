### RPM external gcc-fixincludes 2.0
## NO_VERSION_SUFFIX
## REVISION 1001
## NOCOMPILER

%prep
%build
%install
%post
if [ -d ${RPM_INSTALL_PREFIX}/%{cmsplatf}/external/gcc ] ; then
  for dir in $(ls -d ${RPM_INSTALL_PREFIX}/%{cmsplatf}/external/gcc/* 2>/dev/null) ; do
    mkhdr=$(find ${dir} -path '*/install-tools/mkheaders' -type f 2>/dev/null)
    if [ "x$mkhdr" != "x" ] ;  then
      $mkhdr -v ${dir}
    fi
  done
fi
