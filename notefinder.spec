Summary:	Full-featured exteansible desktop note-taking application for Unix
Name:	  	notefinder
Version:	2.5
Release:	%mkrel 2
License:	BSD-Like and GPLv2+
Group:		Office
Source0: 	http://notefinder.googlecode.com/files/%name-%version.tar.gz
URL:		http://code.google.com/p/notefinder/
Requires:	python-qt4 >= 4.4.0
%py_requires -d
BuildRequires:	python-setuptools
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
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
./install.sh %buildroot%_prefix

# install plugins
for i in plugins/*
do
	cd $i
	python setup.py install --root=%{buildroot} --prefix=%_prefix
	cd -
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/%{name}
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{python_sitelib}/*
