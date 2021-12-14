#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-datetime
Version  : 4.3
Release  : 3
URL      : https://files.pythonhosted.org/packages/5e/93/8d5559da5ccf146f6a4204252ca85b48dd7bf55b32350801a9a9209408c3/DateTime-4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/5e/93/8d5559da5ccf146f6a4204252ca85b48dd7bf55b32350801a9a9209408c3/DateTime-4.3.tar.gz
Summary  : An feature extraction algorithm
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-datetime-license = %{version}-%{release}
Requires: pypi-datetime-python = %{version}-%{release}
Requires: pypi-datetime-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(pytz)
BuildRequires : pypi(zope.interface)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
====================
        
        Encapsulation of date/time values.
        
        
        Function Timezones()
        --------------------

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
%setup -q -n DateTime-4.3
cd %{_builddir}/DateTime-4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639063862
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
cp %{_builddir}/DateTime-4.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-datetime/a0b53f43aab58b46bf79ba756c50771c605ab4c5
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
