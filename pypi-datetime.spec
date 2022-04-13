#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-datetime
Version  : 4.4
Release  : 13
URL      : https://files.pythonhosted.org/packages/ab/62/4a898c8e189ef390e11868349c87ef6cf3deb7677c1c1e03ce3a01be760f/DateTime-4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/ab/62/4a898c8e189ef390e11868349c87ef6cf3deb7677c1c1e03ce3a01be760f/DateTime-4.4.tar.gz
Summary  : An feature extraction algorithm
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-datetime-license = %{version}-%{release}
Requires: pypi-datetime-python = %{version}-%{release}
Requires: pypi-datetime-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(pytz)
BuildRequires : pypi(zope.interface)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://github.com/zopefoundation/DateTime/workflows/tests/badge.svg
:target: https://github.com/zopefoundation/DateTime/actions?query=workflow%3Atests
:alt: CI status

%package license
Summary: license components for the pypi-datetime package.
Group: Default

%description license
license components for the pypi-datetime package.


%package python
Summary: python components for the pypi-datetime package.
Group: Default
Requires: pypi-datetime-python3 = %{version}-%{release}

%description python
python components for the pypi-datetime package.


%package python3
Summary: python3 components for the pypi-datetime package.
Group: Default
Requires: python3-core
Provides: pypi(pypi_datetime)
Requires: pypi(pytz)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-datetime package.


%prep
%setup -q -n DateTime-4.4
cd %{_builddir}/DateTime-4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649866116
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-datetime
cp %{_builddir}/DateTime-4.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-datetime/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-datetime/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
