#
# Conditional build:
%bcond_with i18n	# w/wo i18n subpackages
#
%define		_state		snapshots
%define		_ver		3.2.90
%define		_snap		040504
%define		_packager	adgor

%define		_minlibsevr	9:3.2.90.040503
%define		_minbaseevr	9:3.2.90.040503

Summary:	K Desktop Environment - artwork
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(ko):	KDE¿ë
Summary(pl):	K Desktop Environment - grafiki itp.
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeartwork
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		8
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-%{_snap}.tar.bz2
##%% Source0-md5:	d018b0630af479131314c06ab90a0f93
#Source1:        http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
##%% Source1-md5:	e1d979cdd225df242239885c364c0db5
Patch0:		%{name}-screensavers.patch
Patch1:		%{name}-xscreensaver-dir.patch
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	ed
BuildRequires:	kdebase-devel >= %{_minbaseevr}
BuildRequires:	libxml2-progs
BuildRequires:	unsermake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

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
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-cde
KDE Window Decoration - CDE.

%description -n kde-decoration-cde -l pl
Dekoracja okna dla KDE - CDE.

%package -n kde-decoration-glow
Summary:	KDE Window Decoration - Glow
Summary(pl):	Dekoracja okna dla KDE - Glow
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-glow
KDE Window Decoration - Glow.

%description -n kde-decoration-glow -l pl
Dekoracja okna dla KDE - Glow.

%package -n kde-decoration-icewm
Summary:	Extensions for KDE IceWM decoration
Summary(pl):	Rozszerzenie dekoracji okna "IceWM" dla KDE
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-icewm
Extensions for KDE "IceWM" decoration.

%description -n kde-decoration-icewm -l pl
Rozszerzenie dekoracji okna IceWM dla KDE.

%package -n kde-decoration-kde1
Summary:	KDE Window Decoration - KDE 1
Summary(pl):	Dekoracja okna dla KDE - KDE 1
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-kde1
KDE Window Decoration - KDE 1.

%description -n kde-decoration-kde1 -l pl
Dekoracja okna dla KDE - KDE 1.

%package -n kde-decoration-kstep
Summary:	KDE Window Decoration - Kstep
Summary(pl):	Dekoracja okna dla KDE - Kstep
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-kstep
KDE Window Decoration - Kstep.

%description -n kde-decoration-kstep -l pl
Dekoracja okna dla KDE - Kstep.

%package -n kde-decoration-openlook
Summary:	KDE Window Decoration - OpenLook
Summary(pl):	Dekoracja okna dla KDE - OpenLook
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-openlook
KDE Window Decoration - OpenLook.

%description -n kde-decoration-openlook -l pl
Dekoracja okna dla KDE - OpenLook.

%package -n kde-decoration-plastik
Summary:	KDE Window Decoration - Plastik
Summary(pl):	Dekoracja okna dla KDE - Plastik
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-plastik
KDE Window Decoration - Plastik.

%description -n kde-decoration-plastik -l pl
Dekoracja okna dla KDE - Plastik.

%package -n kde-decoration-riscos
Summary:	KDE Window Decoration - Risc OS
Summary(pl):	Dekoracja okna dla KDE - Risc OS
Requires:	kdebase-desktop >= %{_minbaseevr}
Group:		X11/Amusements
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-riscos
KDE Window Decoration - Risc OS.

%description -n kde-decoration-riscos -l pl
Dekoracja okna dla KDE - Risc OS.

%package -n kde-decoration-system
Summary:	KDE Window Decoration - System
Summary(pl):	Dekoracja okna dla KDE - System
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-system
KDE Window Decoration - System.

%description -n kde-decoration-system -l pl
Dekoracja okna dla KDE - System.

%package -n kde-icons-Locolor
Summary:	KDE Icons Theme - locolor
Summary(pl):	Motyw ikon dla KDE - locolor
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-icons-locolor
Obsoletes:	%{name}-locolor
Obsoletes:	%{name}-themes

%description -n kde-icons-Locolor
KDE Icons Theme - locolor.

%description -n kde-icons-Locolor -l pl
Motyw ikon dla KDE - locolor.

%package -n kde-icons-Technical
Summary:	KDE Icons Theme - Technical
Summary(pl):	Motyw ikon dla KDE - Technical
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-icons-Technical
KDE Icons Theme - Technical.

%description -n kde-icons-Technical -l pl
Motyw ikon dla KDE - Technical.

%package -n kde-icons-ikons
Summary:	KDE Icons Theme - ikons
Summary(pl):	Motyw ikon dla KDE - ikons
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-icons-ikons
KDE Icons Theme - ikons.

%description -n kde-icons-ikons -l pl
Motyw ikon dla KDE - ikons.

%package -n kde-icons-kdeclassic
Summary:	KDE Icons Theme - kdeclassic
Summary(pl):	Motyw ikon dla KDE - kdeclassic
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-icons-kdeclassic
KDE Icons Theme - kdeclassic.

%description -n kde-icons-kdeclassic -l pl
Motyw ikon dla KDE - kdeclassic.

%package -n kde-icons-kids
Summary:	KDE Icons Theme - kids
Summary(pl):	Motyw ikon dla KDE - kids
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}

%description -n kde-icons-kids
KDE Icons Theme - kids.

%description -n kde-icons-kids -l pl
Motyw ikon dla KDE - kids.

%package -n kde-icons-slick
Summary:	KDE Icons Theme - slick
Summary(pl):	Motyw ikon dla KDE - slick
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-icons-slick
KDE Icons Theme - slick.

%description -n kde-icons-slick -l pl
Motyw ikon dla KDE - slick.

%package -n kde-style-dotnet
Summary:	KDE Style - DotNet
Summary(pl):	Styl dla KDE - DotNet
Group:		X11/Amusements
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-style-dotnet
KDE Style - DotNet.

%description -n kde-style-dotnet -l pl
Styl dla KDE - DotNet.

%package -n kde-style-plastik
Summary:	KDE Style - Plastik
Summary(pl):	Styl dla KDE - Plastik
Group:		X11/Amusements
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-style-plastik
KDE Style - Plastik.

%description -n kde-style-plastik -l pl
Styl dla KDE - Plastik.

%package kworldclock
Summary:	Themes for kworldclock
Summary(pl):	Motywy dla kworldclock
Group:		X11/Amusements
Requires:	kdetoys-kworldclock >= %{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes-kworldclock

%description kworldclock
Themes for kworldclock.

%description kworldclock -l pl
Motywy dla kworldclock.

%package screensavers
Summary:	Screen savers for KDE
Summary(pl):	Wygaszacze ekranu dla KDE
Group:		X11/Amusements
Requires:	kdebase-screensavers >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description screensavers
Screen savers for KDE.

%description screensavers -l pl
Wygaszacze ekranu dla KDE.

%package sounds
Summary:	KDE Sounds
Summary(pl):	D¼wiêki dla KDE
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description sounds
KDE Sounds.

%description sounds -l pl
D¼wiêki dla KDE.

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl):	Tapety dla KDE
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description wallpapers
KDE Wallpapers.

%description wallpapers -l pl
Tapety dla KDE.

%package i18n
Summary:	Common internationalization and localization files for kdeartwork
Summary(pl):	Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdeartwork
Group:		X11/Applications
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdelibs-i18n  >= 9:%{version}

%description i18n
Internationalization and localization files for kdeartwork.

%description i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdeartwork.

%package -n kde-decoration-cde-i18n
Summary:	Internationalization and localization files for kde-decoration-cde
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-cde
Group:		X11/Applications
Requires:	kde-decoration-cde = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-desktop-i18n >= 9:%{version}

%description -n kde-decoration-cde-i18n
Internationalization and localization files for kde-decoration-cde.

%description -n kde-decoration-cde-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-cde.

%package -n kde-decoration-icewm-i18n
Summary:	Internationalization and localization files for kde-decoration-icewm
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-icewm
Group:		X11/Applications
Requires:	kde-decoration-icewm = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-desktop-i18n >= 9:%{version}

%description -n kde-decoration-icewm-i18n
Internationalization and localization files for kde-decoration-icewm.

%description -n kde-decoration-icewm-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-icewm.

%package -n kde-decoration-glow-i18n
Summary:	Internationalization and localization files for kde-decoration-glow
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-glow
Group:		X11/Applications
Requires:	kde-decoration-glow = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-desktop-i18n >= 9:%{version}

%description -n kde-decoration-glow-i18n
Internationalization and localization files for kde-decoration-glow.

%description -n kde-decoration-glow-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-glow.

%package -n kde-decoration-plastik-i18n
Summary:	Internationalization and localization files for kde-decoration-plastik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-decoration-plastik
Group:		X11/Applications
Requires:	kde-decoration-plastik = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-desktop-i18n >= 9:%{version}

%description -n kde-decoration-plastik-i18n
Internationalization and localization files for kde-decoration-plastik.

%description -n kde-decoration-plastik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-decoration-plastik.

%package -n kde-style-plastik-i18n
Summary:	Internationalization and localization files for kde-style-plastik
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kde-style-plastik
Group:		X11/Applications
Requires:	kde-style-plastik = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description -n kde-style-plastik-i18n
Internationalization and localization files for kde-style-plastik.

%description -n kde-style-plastik-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kde-style-plastik.

%package screensavers-i18n
Summary:	Internationalization and localization files for screensavers
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla screensavers
Group:		X11/Applications
Requires:	%{name}-screensavers = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-screensavers-i18n >= 9:%{version}

%description screensavers-i18n
Internationalization and localization files for screensavers.

%description screensavers-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla screensavers.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	XSCREENSAVER=/usr/%{_lib}/xscreensaver/flame \
	XSCREENSAVER_CONFIG=/etc/X11/xscreensaver \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Makefile installs these basing on XSCREENSAVER_DIR/* files -
# let's do it manually to avoid BR: xscreensaver{,-GL,-GLE}
install kscreensaver/kxsconfig/ScreenSavers/*.desktop $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver
rm -f $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver/pixmaps.desktop

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
# these don't exist in 3.2:
#rm -f debian/{kbouboule,kmatrix,kmorph3d,kpipes,kpyro,krock,kslidescreen}.kss.1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi

%find_lang desktop_kdeartwork		--with-kde
%find_lang kstyle_plastik_config	--with-kde
%find_lang kwin_cde_config		--with-kde
%find_lang kwin_glow_config		--with-kde
%find_lang kwin_icewm_config		--with-kde
%find_lang kwin_plastik_config		--with-kde

> screensavers.lang
%find_lang klock	--with-kde
cat klock.lang >> screensavers.lang
%find_lang kpartsaver	--with-kde
cat kpartsaver.lang >> screensavers.lang
%find_lang kxsconfig	--with-kde
cat kxsconfig.lang >> screensavers.lang

%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with i18n}
%files i18n -f desktop_kdeartwork.lang
%files -n kde-decoration-cde-i18n -f kwin_cde_config.lang
%files -n kde-decoration-icewm-i18n -f kwin_icewm_config.lang
%files -n kde-decoration-glow-i18n -f kwin_glow_config.lang
%files -n kde-decoration-plastik-i18n -f kwin_plastik_config.lang
%files -n kde-style-plastik-i18n -f kstyle_plastik_config.lang
%files screensavers-i18n -f screensavers.lang
%endif

%files -n kde-decoration-cde
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_cde.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_cde.so
%{_libdir}/kde3/kwin_cde_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_cde_config.so
%{_datadir}/apps/kwin/cde.desktop

%files -n kde-decoration-icewm
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_icewm.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_icewm.so
%{_libdir}/kde3/kwin_icewm_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_icewm_config.so
%{_datadir}/apps/kwin/icewm-themes
%{_datadir}/apps/kwin/icewm.desktop

%files -n kde-decoration-glow
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_glow.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_glow.so
%{_libdir}/kde3/kwin_glow_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_glow_config.so
%{_datadir}/apps/kwin/glow-themes
%{_datadir}/apps/kwin/glow.desktop

%files -n kde-decoration-kde1
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_kde1.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_kde1.so
%{_datadir}/apps/kwin/kde1*

%files -n kde-decoration-kstep
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_kstep.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_kstep.so
%{_datadir}/apps/kwin/kstep*

%files -n kde-decoration-openlook
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_openlook.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_openlook.so
%{_datadir}/apps/kwin/openlook.desktop

%files -n kde-decoration-plastik
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_plastik.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_plastik.so
%{_libdir}/kde3/kwin_plastik_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_plastik_config.so
%{_datadir}/apps/kwin/plastik.desktop

#%files -n kde-decoration-riscos
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kwin_riscos.la
#%attr(755,root,root) %{_libdir}/kde3/kwin_riscos.so
#%{_datadir}/apps/kwin/riscos*

%files -n kde-decoration-system
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_system.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_system.so
%{_datadir}/apps/kwin/system.desktop

%files -n kde-icons-Technical
%defattr(644,root,root,755)
%{_iconsdir}/Technical

%files -n kde-icons-ikons
%defattr(644,root,root,755)
%{_iconsdir}/ikons

%files -n kde-icons-kdeclassic
%defattr(644,root,root,755)
%{_iconsdir}/kdeclassic

%files -n kde-icons-kids
%defattr(644,root,root,755)
%{_iconsdir}/kids

%files -n kde-icons-Locolor
%defattr(644,root,root,755)
%{_iconsdir}/Locolor

%files -n kde-icons-slick
%defattr(644,root,root,755)
%{_iconsdir}/slick

%files -n kde-style-dotnet
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/dotnet.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/dotnet.so
%{_datadir}/apps/kstyle/themes/dotnet*

%files -n kde-style-plastik
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_plastik_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_plastik_config.so
%{_libdir}/kde3/plugins/styles/plastik.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/plastik.so
%{_datadir}/apps/kstyle/themes/plastik.themerc

%files kworldclock
%defattr(644,root,root,755)
%{_datadir}/apps/kworldclock/maps/[!d]*
%{_datadir}/apps/kworldclock/maps/depths/*

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%{_datadir}/apps/kscreensaver/K*.desktop
%{_datadir}/apps/kscreensaver/kpartsaver.desktop
%{_datadir}/apps/kscreensaver/*.png
%{_mandir}/man1/*.kss.1*

# KDE xscreensaver wrappers (should R: xscreensaver?)
%attr(755,root,root) %{_bindir}/kxsconfig
%attr(755,root,root) %{_bindir}/kxsrun
# extrusion.desktop is for xscreensaver-GLE, the rest for xscreensaver{,-GL}
%{_datadir}/apps/kscreensaver/[!Kk]*.desktop
%{_datadir}/apps/kscreensaver/k[!p]*.desktop
%{_datadir}/config/*rc
%{_mandir}/man1/kxsconfig.1*
%{_mandir}/man1/kxsrun.1*

%files sounds
%defattr(644,root,root,755)
%{_datadir}/sounds/*

%files wallpapers
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*
