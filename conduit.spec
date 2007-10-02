Summary:	Synchronization for GNOME
Summary(pl.UTF-8):	Synchronizacja dla GNOME
Name:		conduit
Version:	0.3.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://files.conduit-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	0cb7f2566d1221f01390a35fdfcc84b3
URL:		http://www.conduit-project.org/
BuildRequires:	dbus-devel >= 0.93
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-dateutil
BuildRequires:	python-pygoocanvas >= 0.8.0
BuildRequires:	python-pygtk-devel >= 2:2.10
BuildRequires:	python-vobject
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	pydoc
Requires:	python-PyXML
Requires:	python-dateutil
Requires:	python-evolution >= 0.0.3
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

%py_postclean

%find_lang %{name} --with-gnome

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
%{_libdir}/conduit/dataproviders
%{_desktopdir}/conduit.desktop
%dir %{_datadir}/conduit
%{_datadir}/conduit/*.png
%{_datadir}/conduit/*.glade
%{_datadir}/dbus-1/services/*.service
%{_datadir}/gnome/autostart/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%dir %{_omf_dest_dir}/conduit
%{_omf_dest_dir}/conduit/conduit-C.omf
%dir %{py_sitescriptdir}/conduit
%{py_sitescriptdir}/conduit/*.py[co]
%dir %{py_sitescriptdir}/conduit/datatypes
%{py_sitescriptdir}/conduit/datatypes/*.py[co]

#%files devel
%{_pkgconfigdir}/conduit.pc
