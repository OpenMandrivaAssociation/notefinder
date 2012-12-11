Summary:	Full-featured exteansible desktop note-taking application for Unix
Name:	  	notefinder
Version:	0.4
Release:	%mkrel 4
Epoch:		1
License:	BSD-Like and GPLv2+
Group:		Office
Source0: 	http://notefinder.googlecode.com/files/%name-%version.tar.gz
URL:		http://code.google.com/p/notefinder/
Requires:	python-qt4 >= 4.4.0
%py_requires -d
BuildRequires:	python-setuptools
BuildRequires:	desktop-file-utils
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
NoteFinder is full-featured extensible desktop note-taking application. 

Features: 
* Adding, viewing, editing, removing entries
* Importing local and remote files as notes
* Wiki markup support
* Tabbed interface
* Assigning tags
* Smooth and smart search
* Finding related notes
* Service menu for Konqueror
* Ability to assign tags automatically
* Can be extended with Python plugins

%prep
%setup -qn %name

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=%{buildroot}

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--remove-key='Version' \
	--add-category='Qt;KDE' \
	%buildroot%_datadir/applications/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{python_sitelib}/*


%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1:0.4-4mdv2011.0
+ Revision: 593921
- rebuild for py2.7

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1:0.4-3mdv2010.1
+ Revision: 440343
- rebuild

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1:0.4-2mdv2009.1
+ Revision: 318561
- rebuild for new python

* Sat Dec 06 2008 Funda Wang <fwang@mandriva.org> 1:0.4-1mdv2009.1
+ Revision: 310957
- update to new version 0.4

* Thu Dec 04 2008 Funda Wang <fwang@mandriva.org> 1:0.3.7-1mdv2009.1
+ Revision: 309874
- new version 0.3.7

* Wed Oct 22 2008 Funda Wang <fwang@mandriva.org> 1:0.2-1mdv2009.1
+ Revision: 296467
- New version 0.2

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 1:0.1.8-1mdv2009.1
+ Revision: 291787
- New version series 0.1.8

* Sat Aug 02 2008 Funda Wang <fwang@mandriva.org> 3.1.5-1mdv2009.0
+ Revision: 260982
- New version 3.1.5

* Sat Aug 02 2008 Funda Wang <fwang@mandriva.org> 3.1-1mdv2009.0
+ Revision: 260527
- New version 3.1

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 3.0.9-1mdv2009.0
+ Revision: 259565
- New version 3.0.9

* Thu Jul 31 2008 Funda Wang <fwang@mandriva.org> 3.0.8-1mdv2009.0
+ Revision: 257389
- New version 3.0.8

* Fri Jul 11 2008 Funda Wang <fwang@mandriva.org> 2.9-1mdv2009.0
+ Revision: 233805
- New version 2.9

* Thu Jul 10 2008 Funda Wang <fwang@mandriva.org> 2.8-1mdv2009.0
+ Revision: 233244
- New version 2.8

* Tue Jul 08 2008 Funda Wang <fwang@mandriva.org> 2.6-1mdv2009.0
+ Revision: 232672
- update to new version 2.6

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 2.5-2mdv2009.0
+ Revision: 231965
- BR python-devel
- BR python
- BR setuptools
- install plugins also

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 2.5-1mdv2009.0
+ Revision: 231941
- import notefinder


