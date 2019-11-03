#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-doSNOW
Version  : 1.0.18
Release  : 24
URL      : https://cran.r-project.org/src/contrib/doSNOW_1.0.18.tar.gz
Source0  : https://cran.r-project.org/src/contrib/doSNOW_1.0.18.tar.gz
Summary  : Foreach Parallel Adaptor for the 'snow' Package
Group    : Development/Tools
License  : GPL-2.0
Requires: R-foreach
Requires: R-iterators
Requires: R-snow
BuildRequires : R-foreach
BuildRequires : R-iterators
BuildRequires : R-snow
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
the snow package of Tierney, Rossini, Li, and Sevcikova.

%prep
%setup -q -c -n doSNOW

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571819349

%install
export SOURCE_DATE_EPOCH=1571819349
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doSNOW
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doSNOW
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library doSNOW
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc doSNOW || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/doSNOW/DESCRIPTION
/usr/lib64/R/library/doSNOW/INDEX
/usr/lib64/R/library/doSNOW/Meta/Rd.rds
/usr/lib64/R/library/doSNOW/Meta/features.rds
/usr/lib64/R/library/doSNOW/Meta/hsearch.rds
/usr/lib64/R/library/doSNOW/Meta/links.rds
/usr/lib64/R/library/doSNOW/Meta/nsInfo.rds
/usr/lib64/R/library/doSNOW/Meta/package.rds
/usr/lib64/R/library/doSNOW/NAMESPACE
/usr/lib64/R/library/doSNOW/NEWS
/usr/lib64/R/library/doSNOW/R/doSNOW
/usr/lib64/R/library/doSNOW/R/doSNOW.rdb
/usr/lib64/R/library/doSNOW/R/doSNOW.rdx
/usr/lib64/R/library/doSNOW/examples/boot.R
/usr/lib64/R/library/doSNOW/help/AnIndex
/usr/lib64/R/library/doSNOW/help/aliases.rds
/usr/lib64/R/library/doSNOW/help/doSNOW.rdb
/usr/lib64/R/library/doSNOW/help/doSNOW.rdx
/usr/lib64/R/library/doSNOW/help/paths.rds
/usr/lib64/R/library/doSNOW/html/00Index.html
/usr/lib64/R/library/doSNOW/html/R.css
/usr/lib64/R/library/doSNOW/tests/doRUnit.R
/usr/lib64/R/library/doSNOW/unitTests/options.R
