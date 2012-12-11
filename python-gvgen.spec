%define oname gvgen

Summary: Python class to generate dot files for further use with graphviz
Name: python-gvgen
Version: 0.9
Release: %mkrel 7
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


%changelog
* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 0.9-7mdv2011.0
+ Revision: 599396
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9-6mdv2010.0
+ Revision: 442147
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.9-5mdv2009.1
+ Revision: 323726
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.9-4mdv2009.0
+ Revision: 259622
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9-3mdv2009.0
+ Revision: 247426
- rebuild

* Fri Feb 29 2008 Jérôme Soyer <saispo@mandriva.org> 0.9-1mdv2008.1
+ Revision: 176737
- Add files...
- New release 0.9
- New release 0.7

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary & description

* Thu Nov 29 2007 Jérôme Soyer <saispo@mandriva.org> 0.6-1mdv2008.1
+ Revision: 113891
- import python-gvgen


