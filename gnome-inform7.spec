Summary:	Inform 7 interactive fiction editor and compiler
Name:		gnome-inform7
Version:	5Z71
Release:	1
License:	GPL v2 + Closed-source Freely distributable compiler
Group:		Development
Source0:	http://dl.sourceforge.net/gnome-inform7/I7_%{version}_GNOME_Source.tar.gz
# Source0-md5:	cdb48f47b0e18bb7228401b9035b4d13
Source1:	http://www.inform-fiction.org/I7Downloads/I7_5U92_Linux_i386.tar.gz
# Source1-md5:	d6faac063eabb0d546baf444cafb0beb
Patch0:		%{name}-as-needed.patch
Patch1:		%{name}-fix.patch
URL:		http://inform7.com/
BuildRequires:	SDL_sound-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -a1
tar xzf inform7-5U92/inform7-compilers_5U92_i386.tar.gz
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
mv share/inform7/Compilers/ni src/ni/ni
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/gconf/schemas/gnome-inform7.schemas
%{_sysconfdir}/gtkterp.ini
%attr(755,root,root) %{_bindir}/gnome-inform7
%dir %{_libdir}/gnome-inform7
%attr(755,root,root) %{_libdir}/gnome-inform7/cBlorb
%attr(755,root,root) %{_libdir}/gnome-inform7/gtkterp-frotz
%attr(755,root,root) %{_libdir}/gnome-inform7/gtkterp-git
%attr(755,root,root) %{_libdir}/gnome-inform7/gtkterp-glulxe
%attr(755,root,root) %{_libdir}/gnome-inform7/inform-6.31-biplatform
%attr(755,root,root) %{_libdir}/gnome-inform7/ni
%{_desktopdir}/gnome-inform7.desktop
%{_datadir}/gnome-inform7
%{_pixmapsdir}/*.png
%{_pixmapsdir}/gnome-inform7
