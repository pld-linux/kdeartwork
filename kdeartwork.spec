
%define		_state		stable
%define		_ver		3.1

Summary:	K Desktop Environment - artwork
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(ko):	KDE¿ë
Summary(pl):	K Desktop Environment - grafiki itp.
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeartwork
Version:	%{_ver}
Release:	3
Epoch:		7
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	kdebase-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs
Requires:	kdelibs = %{version}
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdeartwork-locolor
Obsoletes:	kdeartwork-kworldclock

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_htmldir	/usr/share/doc/kde/HTML

%description
This package contains various graphics and such for KDE.

%description -l es
kdeartwork possue temas, sonidos, wallpapers, e estilos adicionais a
KDE.

%description -l pl
Pakiet ten zawiera ró¿ne grafiki i tym podobne dla KDE.

%description -l pt_BR
kdeartwork contém temas, sons, papéis de parede e estilos de janelas
adicionais para o KDE.

%package -n kde-decoration-cde
Summary:	KDE Window Decoration - CDE
Summary(pl):	Dekoracja okna dla KDE - CDE
Group:		X11/Amusements

%description -n kde-decoration-cde
KDE Window Decoration - CDE

%description -n kde-decoration-cde -l pl
Dekoracja okna dla KDE - CDE

%package -n kde-decoration-icewm
Summary:	Extensions for KDE IceWM decoration
Summary(pl):	Rozszerzenie dekoracji okna "IceWM" dla KDE
Group:		X11/Amusements

%description -n kde-decoration-icewm
Extensions for KDE "IceWM" decoration

%description -n kde-decoration-icewm -l pl
Rozszerzenie dekoracji okna IceWM dla KDE

%package -n kde-decoration-glow
Summary:	KDE Window Decoration - Glow
Summary(pl):	Dekoracja okna dla KDE - Glow
Group:		X11/Amusements

%description -n kde-decoration-glow
KDE Window Decoration - Glow

%description -n kde-decoration-glow -l pl
Dekoracja okna dla KDE - Glow

%package -n kde-decoration-openlook
Summary:	KDE Window Decoration - OpenLook
Summary(pl):	Dekoracja okna dla KDE - OpenLook
Group:		X11/Amusements

%description -n kde-decoration-openlook
KDE Window Decoration - OpenLook

%description -n kde-decoration-openlook -l pl
Dekoracja okna dla KDE - OpenLook

%package -n kde-icons-Technical
Summary:	KDE Icons Theme - Technical
Summary(pl):	Motyw ikon dla KDE - Crystal
Group:		X11/Amusements

%description -n kde-icons-Technical
KDE Icons Theme - Technical

%description -n kde-icons-Technical -l pl
Motyw ikon dla KDE - Technical

%package -n kde-icons-ikons
Summary:	KDE Icons Theme - ikons
Summary(pl):	Motyw ikon dla KDE - ikons
Group:		X11/Amusements

%description -n kde-icons-ikons
KDE Icons Theme - ikons

%description -n kde-icons-ikons -l pl
Motyw ikon dla KDE - ikons

%package -n kde-icons-kdeclassic
Summary:	KDE Icons Theme - kdeclassic
Summary(pl):	Motyw ikon dla KDE - kdeclassic
Group:		X11/Amusements

%description -n kde-icons-kdeclassic
KDE Icons Theme - kdeclassic.

%description -n kde-icons-kdeclassic -l pl
Motyw ikon dla KDE - kdeclassic.

%package -n kde-icons-Locolor
Summary:	KDE Icons Theme - locolor
Summary(pl):	Motyw ikon dla KDE - locolor
Group:		X11/Amusements

%description -n kde-icons-Locolor
KDE Icons Theme - locolor.

%description -n kde-icons-Locolor -l pl
Motyw ikon dla KDE - locolor.

%package -n kde-icons-slick
Summary:	KDE Icons Theme - slick
Summary(pl):	Motyw ikon dla KDE - slick
Group:		X11/Amusements

%description -n kde-icons-slick
KDE Icons Theme - slick

%description -n kde-icons-slick -l pl
Motyw ikon dla KDE - slick

%package -n kde-style-dotnet
Summary:	KDE Style - DotNet
Summary(pl):	Styl dla KDE - DotNet
Group:		X11/Amusements

%description -n kde-style-dotnet
KDE Style - DotNet

%description -n kde-style-dotnet -l pl
Styl dla KDE - DotNet

%package kworldclock
Summary:	Themes for kworldclock
Summary(pl):	Motywy dla kworldclock
Group:		X11/Amusements
Requires:	kdetoys-kworldclock

%description kworldclock
Themes for kworldclock.

%description kworldclock -l pl
Motywy dla kworldclock.

%package screensavers
Summary:	Screen savers for KDE
Summary(pl):	Wygaszacze ekranu dla KDE
Group:		X11/Amusements
Requires:	kdebase-screensavers

%description screensavers
Screen savers for KDE.

%description screensavers -l pl
Wygaszacze ekranu dla KDE.

%package sounds
Summary:	KDE Sounds
Summary(pl):	D¼wiêki dla KDE
Group:		X11/Amusements

%description sounds
KDE Sounds

%description sounds -l pl
D¬wiêki dla KDE

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl):	Tapety dla KDE
Group:		X11/Amusements

%description wallpapers
KDE Wallpapers

%description wallpapers -l pl
Tapety dla KDE

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/.hidden
mv $ALD/{System/ScreenSavers,.hidden}

#mv $RPM_BUILD_ROOT%{_pixmapsdir}/{L,l}ocolor
# Conflict with kdeaddons-kicker: (not verified yet)
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/ktimemon.png
# Conflict with kdebase:
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/bell.png
# Conflict with kdegames-kspaceduel: (not verifiet yet)
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/kspaceduel.png
# Conflict with kdegames-lskat:
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/lskat.png
# Conflict with kdenetwork-ksirc:
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/ksirc.png
# Conflict with kdesdk:
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/mimetypes/gettext.png
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/kbabel.png
# Conflicts with kdetoys-kteatime:
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/16x16/apps/kteatime.png
# Conflict with kdetoys-ktux:
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/ktux.png
# Conflict with koffice-kspread: (not verified yet)
#rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/kspreadcalc.png

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

#%find_lang kdeartwork --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-cde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_cde*
%{_datadir}/apps/kwin/cde*

%files -n kde-decoration-icewm
%defattr(644,root,root,755)
%{_datadir}/apps/kwin/icewm-themes/*

%files -n kde-decoration-glow
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_glow*
%{_datadir}/apps/kwin/glow*

%files -n kde-decoration-openlook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin_openlook*
%{_datadir}/apps/kwin/openlook*

%files -n kde-icons-Technical
%defattr(644,root,root,755)
%{_pixmapsdir}/Technical

%files -n kde-icons-ikons
%defattr(644,root,root,755)
%{_pixmapsdir}/ikons

%files -n kde-icons-kdeclassic
%defattr(644,root,root,755)
%{_pixmapsdir}/kdeclassic

%files -n kde-icons-Locolor
%defattr(644,root,root,755)
%{_pixmapsdir}/Locolor

%files -n kde-icons-slick
%defattr(644,root,root,755)
%{_pixmapsdir}/slick

%files -n kde-style-dotnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/dotnet*
%{_datadir}/apps/kstyle/themes/dotnet*

%files kworldclock
%defattr(644,root,root,755)
%{_datadir}/apps/kworldclock/maps/[^d]*
%{_datadir}/apps/kworldclock/maps/depths/*

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kscreensaver
#{_datadir}/config/*
%{_applnkdir}/.hidden/ScreenSavers/*

%files sounds
%defattr(644,root,root,755)
%{_datadir}/sounds/*

%files wallpapers
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*
