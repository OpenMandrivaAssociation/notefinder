Summary:	Full-featured exteansible desktop note-taking application for Unix
Name:	  	notefinder
Version:	0.4
Release:	6
Epoch:		1
License:	BSD-Like and GPLv2+
Group:		Office
Source0: 	http://notefinder.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		https://code.google.com/p/notefinder/
Requires:	python-qt4 >= 4.4.0
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	desktop-file-utils
BuildArch:	noarch

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
%setup -qn %{name}

%build

%install
python setup.py install --root=%{buildroot}

desktop-file-install --vendor='' \
	--dir=%{buildroot}%{_datadir}/applications \
	--remove-key='Version' \
	--add-category='Qt;KDE' \
	%{buildroot}%{_datadir}/applications/*.desktop

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{python_sitelib}/*

