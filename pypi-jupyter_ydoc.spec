#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_ydoc
Version  : 0.3.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/06/cb/a38b4a227b407c17483964537765ab5b99734960ac8293c922c3a8b55b9c/jupyter_ydoc-0.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/06/cb/a38b4a227b407c17483964537765ab5b99734960ac8293c922c3a8b55b9c/jupyter_ydoc-0.3.1.tar.gz
Summary  : Document structures for collaborative editing using Ypy
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_ydoc-license = %{version}-%{release}
Requires: pypi-jupyter_ydoc-python = %{version}-%{release}
Requires: pypi-jupyter_ydoc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_nodejs_version)
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build Status](https://github.com/jupyter-server/jupyter_ydoc/workflows/Tests/badge.svg)](https://github.com/jupyter-server/jupyter_ydoc/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/jupyter-ydoc)](https://pypi.org/project/jupyter-ydoc/)
[![npm (scoped)](https://img.shields.io/npm/v/@jupyter/ydoc)](https://www.npmjs.com/package/@jupyter/ydoc)

%package license
Summary: license components for the pypi-jupyter_ydoc package.
Group: Default

%description license
license components for the pypi-jupyter_ydoc package.


%package python
Summary: python components for the pypi-jupyter_ydoc package.
Group: Default
Requires: pypi-jupyter_ydoc-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_ydoc package.


%package python3
Summary: python3 components for the pypi-jupyter_ydoc package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_ydoc)
Requires: pypi(y_py)

%description python3
python3 components for the pypi-jupyter_ydoc package.


%prep
%setup -q -n jupyter_ydoc-0.3.1
cd %{_builddir}/jupyter_ydoc-0.3.1
pushd ..
cp -a jupyter_ydoc-0.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675740717
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_ydoc
cp %{_builddir}/jupyter_ydoc-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyter_ydoc/81d09a310cae56af32801b16ed77aca87475f9da || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_ydoc/81d09a310cae56af32801b16ed77aca87475f9da

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
