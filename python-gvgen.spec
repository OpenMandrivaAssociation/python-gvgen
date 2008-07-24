%define oname gvgen

Summary: Python class to generate dot files for further use with graphviz
Name: python-gvgen
Version: 0.9
Release: %mkrel 3
URL: http://software.inl.fr/trac/trac.cgi/wiki/GvGen
Source0: http://software.inl.fr/releases/GvGen/%{oname}-%{version}.tar.bz2
Source1: user-guide.tex.lyx
License: GPL
Group: Development/Python
BuildRequires: python-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
GvGen is a python class to generate dot files for further use with graphviz:
    * Edge creation, naming and connection
    * Apply any graphviz property on the fly
    * Apply graphviz properties to a style

%prep
%setup -q -n %{oname}-%version -a 0

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

# (saispo) fix doc installation
mkdir -p %{buildroot}/%{_datadir}/doc/%{name}/
cp -f %{SOURCE1} %{buildroot}/%{_datadir}/doc/%{name}/user-guide.tex.lyx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%{py_puresitedir}/*
