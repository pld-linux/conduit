Summary:	Synchronization for GNOME
Summary(pl.UTF-8):	Synchronizacja dla GNOME
Name:		conduit
Version:	0.3.17
Release:	4
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/conduit/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	0c94b2b980e26ea71a470683bbd6a45f
URL:		http://www.conduit-project.org/
BuildRequires:	dbus-devel >= 0.93
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-dateutil
BuildRequires:	python-dbus
BuildRequires:	python-pygoocanvas >= 0.8.0
BuildRequires:	python-pygtk-devel >= 2:2.10
BuildRequires:	python-vobject
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
%pyrequires_eq	python-modules
Requires:	pydoc
Requires:	python-PyXML
Requires:	python-dateutil
Requires:	python-gdata
Requires:	python-gnome-desktop-evolution
Requires:	python-pygoocanvas >= 0.8.0
Requires:	python-pygtk-gtk >= 2:2.10
Requires:	python-vobject
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conduit is a synchronization solution for GNOME which allows the user
to take their emails, files, bookmarks, and any other type of personal
information and synchronize that data with another computer, an online
service, or even another electronic device.

Conduit manages the synchronization and conversion of data into other
formats. For example, conduit allows you to;
 - Synchronize your tomboy notes to a file on a remote computer
 - Synchronize your emails to your mobile phone
 - Synchronize your bookmarks to delicious, gmail, or even your own
   webserver

%description -l pl.UTF-8
Conduit to narzędzie do synchronizacji dla GNOME, pozwalające
użytkownikowi pobierać swoje listy elektroniczne, pliki, zakładki i
inne rodzaje informacji osobistych oraz synchronizować te dane z innym
komputerem, usługą online albo nawet innym urządzeniem elektronicznym.

Conduit zarządza synchronizacją i konwersją danych do innych formatów.
Pozwala na przykład:
 - synchronizować notatki tomboya z plikiem na zdalnym komputerze
 - synchronizować listy elektroniczne z telefonem komórkowym
 - synchronizować zakładki z delicious, gmailem albo nawet własnym
   serwerem WWW

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/hicolor/26x26

%py_postclean

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/conduit
%attr(755,root,root) %{_bindir}/conduit-client
%attr(755,root,root) %{_bindir}/conduit.real
%dir %{_libdir}/conduit
%{_libdir}/conduit/modules
%{_desktopdir}/conduit.desktop
%dir %{_datadir}/conduit
%{_datadir}/conduit/*.png
%{_datadir}/conduit/*.ui
%{_datadir}/dbus-1/services/*.service
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%dir %{py_sitescriptdir}/conduit
%{py_sitescriptdir}/conduit/*.py[co]
%dir %{py_sitescriptdir}/conduit/dataproviders
%{py_sitescriptdir}/conduit/dataproviders/*.py[co]
%dir %{py_sitescriptdir}/conduit/datatypes
%{py_sitescriptdir}/conduit/datatypes/*.py[co]
%dir %{py_sitescriptdir}/conduit/gtkui
%{py_sitescriptdir}/conduit/gtkui/*.py[co]
%dir %{py_sitescriptdir}/conduit/hildonui
%{py_sitescriptdir}/conduit/hildonui/*.py[co]
%dir %{py_sitescriptdir}/conduit/platform
%{py_sitescriptdir}/conduit/platform/*.py[co]
%dir %{py_sitescriptdir}/conduit/utils
%{py_sitescriptdir}/conduit/utils/*.py[co]

#%files devel
%{_pkgconfigdir}/conduit.pc
