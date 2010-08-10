### RPM external alpgen 213
## BUILDIF case $(uname):$(uname -m) in Linux:i*86 ) true ;; Linux:x86_64 ) true ;;  Linux:ppc64 ) false ;; Darwin:* ) false ;; * ) false ;; esac 

%define realversion %(echo %v | cut -d- -f1 )
Source: http://mlm.home.cern.ch/mlm/alpgen/V2.1/v%{realversion}.tgz
Source1: config.sub-amd64
Patch0: alpgen-212
Patch1: alpgen-212-gfortran
 
%prep
%setup -c -n alpgen-%v
%patch0 -p1 
case %gccver in
  4.*)
%patch1 -p0
  ;;
esac

%build
cd 2Qphwork; make gen; cd ..
cd 2Qwork; make gen; cd ..
cd 4Qwork; make gen; cd ..
cd hjetwork; make gen; cd ..
cd Njetwork; make gen; cd ..
cd QQhwork; make gen; cd ..
cd topwork; make gen; cd ..
cd vbjetwork; make gen; cd ..
cd wcjetwork; make gen; cd ..
cd wphjetwork; make gen; cd ..
cd wphqqwork; make gen; cd ..
cd wqqwork; make gen; cd ..
cd zqqwork; make gen; cd ..

cd phjetwork; make gen; 
export USRF=120_180bin
make gen -f cmsMakefile
export USRF=180_240bin
make gen -f cmsMakefile
export USRF=20_60bin
make gen -f cmsMakefile
export USRF=240_300bin
make gen -f cmsMakefile
export USRF=300_7000bin
make gen -f cmsMakefile
export USRF=60_120bin
make gen -f cmsMakefile
cd ..

cd wjetwork; make gen; 
export USRF=0ptw100
make gen -f cmsMakefile
export USRF=100ptw300
make gen -f cmsMakefile
export USRF=300ptw800
make gen -f cmsMakefile
export USRF=800ptw1600
make gen -f cmsMakefile
export USRF=1600ptw3200
make gen -f cmsMakefile
export USRF=3200ptw5000
make gen -f cmsMakefile
export USRF=VBFHiggsTo2Tau
make gen -f cmsMakefile
export USRF=2j_vbf_inv
make gen -f cmsMakefile
export USRF=3j_vbf_inv
make gen -f cmsMakefile
cd ..

cd zjetwork; make gen; 
export USRF=0ptz100
make gen -f cmsMakefile
export USRF=100ptz300
make gen -f cmsMakefile
export USRF=300ptz800
make gen -f cmsMakefile
export USRF=800ptz1600
make gen -f cmsMakefile
export USRF=1600ptz3200
make gen -f cmsMakefile
export USRF=3200ptz5000
make gen -f cmsMakefile
export USRF=VBFHiggsTo2Tau
make gen -f cmsMakefile
export USRF=2j_vbf_inv
make gen -f cmsMakefile
export USRF=3j_vbf_inv
make gen -f cmsMakefile
cd ..

cd Njetwork; make gen; 
export USRF=100_160
make gen -f cmsMakefile
export USRF=100_180
make gen -f cmsMakefile
export USRF=140_180
make gen -f cmsMakefile
export USRF=140_5600
make gen -f cmsMakefile
export USRF=160_200
make gen -f cmsMakefile
export USRF=180_250
make gen -f cmsMakefile
export USRF=180_5600
make gen -f cmsMakefile
export USRF=200_250
make gen -f cmsMakefile
export USRF=20_100
make gen -f cmsMakefile
export USRF=20_80
make gen -f cmsMakefile
export USRF=250_400
make gen -f cmsMakefile
export USRF=400_5600
make gen -f cmsMakefile
export USRF=80_140
make gen -f cmsMakefile
cd ..

%install
mkdir -p %{i}/bin
mkdir -p %{i}/alplib
cp zjetwork/zjet_*gen %{i}/bin/
cp wjetwork/wjet_*gen %{i}/bin/
cp phjetwork/phjet_*gen %{i}/bin/
cp Njetwork/Njet_*gen %{i}/bin/

cp 2Qphwork/2Qphgen %{i}/bin/
cp 2Qwork/2Qgen %{i}/bin/
cp 4Qwork/4Qgen %{i}/bin/

cp hjetwork/hjetgen %{i}/bin/
cp Njetwork/Njetgen %{i}/bin/
cp phjetwork/phjetgen %{i}/bin/

cp QQhwork/QQhgen %{i}/bin/
cp topwork/topgen %{i}/bin/
cp vbjetwork/vbjetgen %{i}/bin/

cp wcjetwork/wcjetgen %{i}/bin/
cp wjetwork/wjetgen %{i}/bin/
cp wphjetwork/wphjetgen %{i}/bin/
cp wphqqwork/wphqqgen %{i}/bin/
cp wqqwork/wqqgen %{i}/bin/

cp zjetwork/zjetgen %{i}/bin/
cp zqqwork/zqqgen %{i}/bin/

cp -R alplib/* %{i}/alplib/
