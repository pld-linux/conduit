#
Summary:	Synchronization for Gnome
Name:		conduit
Version:	0.3.3
Release:	1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://files.conduit-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	03737db54a5682c972a601b5c15e504a
URL:		http://www.conduit-project.org/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	evolution-python
#BuildRequires:	intltool
#BuildRequires:	libtool
BuildRequires:	python-dateutil
BuildRequires:	python-pygoocanvas
BuildRequires:	python-vobject
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package libs
Summary:	-
Summary(pl):	-
Group:		Libraries

%description libs


%package devel
Summary:	Header files for ... library
Summary(pl):	Pliki nag³ówkowe biblioteki ...
Group:		Development/Libraries
#Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for ... library.

%description devel -l pl
Ten pakiet zawiera pliki nag

%package static
Summary:	Static ... library
Summary(pl):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl
Statyczna biblioteka ....

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS  ChangeLog NEWS README  TODO
%attr(755,root,root) %{_bindir}/start_conduit
%dir %{_libdir}/conduit
%{_libdir}/conduit/dataproviders
%{_desktopdir}/conduit.desktop
%dir %{_datadir}/conduit
%{_datadir}/conduit/*.png
%{_datadir}/conduit/*.glade
%{_datadir}/dbus-1/services/*.service
%{_datadir}/gnome/autostart/*.desktop
%{_pixmapsdir}/*.png
%dir %{py_sitescriptdir}/conduit
%{py_sitescriptdir}/conduit/*.py[co]
%dir %{py_sitescriptdir}/conduit/datatypes
%{py_sitescriptdir}/conduit/datatypes/*.py[co]

#%files devel
%{_pkgconfigdir}/conduit.pc
