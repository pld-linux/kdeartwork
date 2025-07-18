# TODO:
# - Splitting kde-emoticons subpkg
#
# Conditional build:
%bcond_with	arts			# build with aRts support

%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

Summary:	K Desktop Environment - artwork
Summary(es.UTF-8):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(ko.UTF-8):	KDE용
Summary(pl.UTF-8):	K Desktop Environment - grafiki itp.
Summary(pt_BR.UTF-8):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeartwork
Version:	3.5.10
Release:	2
Epoch:		8
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	6e6f089dc0f1dabb0f138641600d0b59
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-screensavers.patch
Patch2:		%{name}-xscreensaver-dir.patch
Patch3:		kde-ac260-lt.patch
Patch4:		kde-am.patch
Patch5:		am-install.patch
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	ed
BuildRequires:	kdebase-devel >= %{_minbaseevr}
BuildRequires:	libxml2-progs
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains various graphics and such for KDE.

%description -l es.UTF-8
kdeartwork possue temas, sonidos, wallpapers, e estilos adicionais a
KDE.

%description -l pl.UTF-8
Pakiet ten zawiera różne grafiki i tym podobne dla KDE.

%description -l pt_BR.UTF-8
kdeartwork contém temas, sons, papéis de parede e estilos de janelas
adicionais para o KDE.

%package -n kde-decoration-cde
Summary:	KDE Window Decoration - CDE
Summary(pl.UTF-8):	Dekoracja okna dla KDE - CDE
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-cde
KDE Window Decoration - CDE.

%description -n kde-decoration-cde -l pl.UTF-8
Dekoracja okna dla KDE - CDE.

%package -n kde-decoration-glow
Summary:	KDE Window Decoration - Glow
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Glow
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-glow
KDE Window Decoration - Glow.

%description -n kde-decoration-glow -l pl.UTF-8
Dekoracja okna dla KDE - Glow.

%package -n kde-decoration-icewm
Summary:	Extensions for KDE IceWM decoration
Summary(pl.UTF-8):	Rozszerzenie dekoracji okna "IceWM" dla KDE
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-icewm
Extensions for KDE "IceWM" decoration.

%description -n kde-decoration-icewm -l pl.UTF-8
Rozszerzenie dekoracji okna IceWM dla KDE.

%package -n kde-decoration-kde1
Summary:	KDE Window Decoration - KDE 1
Summary(pl.UTF-8):	Dekoracja okna dla KDE - KDE 1
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-kde1
KDE Window Decoration - KDE 1.

%description -n kde-decoration-kde1 -l pl.UTF-8
Dekoracja okna dla KDE - KDE 1.

%package -n kde-decoration-kstep
Summary:	KDE Window Decoration - Kstep
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Kstep
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-kstep
KDE Window Decoration - Kstep.

%description -n kde-decoration-kstep -l pl.UTF-8
Dekoracja okna dla KDE - Kstep.

%package -n kde-decoration-openlook
Summary:	KDE Window Decoration - OpenLook
Summary(pl.UTF-8):	Dekoracja okna dla KDE - OpenLook
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-openlook
KDE Window Decoration - OpenLook.

%description -n kde-decoration-openlook -l pl.UTF-8
Dekoracja okna dla KDE - OpenLook.

%package -n kde-decoration-riscos
Summary:	KDE Window Decoration - Risc OS
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Risc OS
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-riscos
KDE Window Decoration - Risc OS.

%description -n kde-decoration-riscos -l pl.UTF-8
Dekoracja okna dla KDE - Risc OS.

%package -n kde-decoration-system
Summary:	KDE Window Decoration - System
Summary(pl.UTF-8):	Dekoracja okna dla KDE - System
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-system
KDE Window Decoration - System.

%description -n kde-decoration-system -l pl.UTF-8
Dekoracja okna dla KDE - System.

%package -n kde-decoration-smoothblend
Summary:	KDE Window Decoration - Smoothblend
Summary(pl.UTF-8):	Dekoracja okna dla KDE - Smoothblend
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-decoration-smoothblend
KDE Window Decoration - Smoothblend.

%description -n kde-decoration-smoothblend -l pl.UTF-8
Dekoracja okna dla KDE - Smoothblend.


%package -n kde-emoticons
Summary:	KDE emoticons themes
Summary(pl.UTF-8):	Motywy emotikon dla KDE
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-icons-locolor
Obsoletes:	kdeartwork-locolor
Obsoletes:	kdeartwork-themes

%description -n kde-emoticons
KDE emoticons themes.

%description -n kde-emoticons -l pl.UTF-8
Motywy emotikon dla KDE.

%package -n kde-icons-Locolor
Summary:	KDE Icons Theme - locolor
Summary(pl.UTF-8):	Motyw ikon dla KDE - locolor
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-icons-locolor
Obsoletes:	kdeartwork-locolor
Obsoletes:	kdeartwork-themes

%description -n kde-icons-Locolor
KDE Icons Theme - locolor.

%description -n kde-icons-Locolor -l pl.UTF-8
Motyw ikon dla KDE - locolor.

%package -n kde-icons-hicolor
Summary:	KDE Icons Theme - hicolor
Summary(pl.UTF-8):	Motyw ikon dla KDE - hicolor
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}

%description -n kde-icons-hicolor
KDE Icons Theme - hicolor.

%description -n kde-icons-hicolor -l pl.UTF-8
Motyw ikon dla KDE - hicolor.

%package -n kde-icons-Technical
Summary:	KDE Icons Theme - Technical
Summary(pl.UTF-8):	Motyw ikon dla KDE - Technical
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-Technical
KDE Icons Theme - Technical.

%description -n kde-icons-Technical -l pl.UTF-8
Motyw ikon dla KDE - Technical.

%package -n kde-icons-ikons
Summary:	KDE Icons Theme - ikons
Summary(pl.UTF-8):	Motyw ikon dla KDE - ikons
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-ikons
KDE Icons Theme - ikons.

%description -n kde-icons-ikons -l pl.UTF-8
Motyw ikon dla KDE - ikons.

%package -n kde-icons-kdeclassic
Summary:	KDE Icons Theme - kdeclassic
Summary(pl.UTF-8):	Motyw ikon dla KDE - kdeclassic
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-kdeclassic
KDE Icons Theme - kdeclassic.

%description -n kde-icons-kdeclassic -l pl.UTF-8
Motyw ikon dla KDE - kdeclassic.

%package -n kde-icons-kids
Summary:	KDE Icons Theme - kids
Summary(pl.UTF-8):	Motyw ikon dla KDE - kids
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}

%description -n kde-icons-kids
KDE Icons Theme - kids.

%description -n kde-icons-kids -l pl.UTF-8
Motyw ikon dla KDE - kids.

%package -n kde-icons-slick
Summary:	KDE Icons Theme - slick
Summary(pl.UTF-8):	Motyw ikon dla KDE - slick
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-icons-slick
KDE Icons Theme - slick.

%description -n kde-icons-slick -l pl.UTF-8
Motyw ikon dla KDE - slick.

%package -n kde-style-dotnet
Summary:	KDE Style - DotNet
Summary(pl.UTF-8):	Styl dla KDE - DotNet
Group:		X11/Amusements
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-style-dotnet
KDE Style - DotNet.

%description -n kde-style-dotnet -l pl.UTF-8
Styl dla KDE - DotNet.

%package -n kde-style-phase
Summary:	KDE Style - Phase
Summary(pl.UTF-8):	Styl dla KDE - Phase
Group:		X11/Amusements
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description -n kde-style-phase
KDE Style - Phase.

%description -n kde-style-phase -l pl.UTF-8
Styl dla KDE - Phase.

%package kworldclock
Summary:	Themes for kworldclock
Summary(pl.UTF-8):	Motywy dla kworldclock
Group:		X11/Amusements
Requires:	kdetoys-kworldclock >= %{version}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes-kworldclock

%description kworldclock
Themes for kworldclock.

%description kworldclock -l pl.UTF-8
Motywy dla kworldclock.

%package screensavers
Summary:	Screen savers for KDE
Summary(pl.UTF-8):	Wygaszacze ekranu dla KDE
Group:		X11/Amusements
Requires:	kdebase-screensavers >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description screensavers
Screen savers for KDE.

%description screensavers -l pl.UTF-8
Wygaszacze ekranu dla KDE.

%package sounds
Summary:	KDE Sounds
Summary(pl.UTF-8):	Dźwięki dla KDE
Group:		X11/Amusements
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description sounds
KDE Sounds.

%description sounds -l pl.UTF-8
Dźwięki dla KDE.

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl.UTF-8):	Tapety dla KDE
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdeartwork
Obsoletes:	kdeartwork-themes

%description wallpapers
KDE Wallpapers.

%description wallpapers -l pl.UTF-8
Tapety dla KDE.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
	XSCREENSAVER=/usr/%{_lib}/xscreensaver/flame \
	XSCREENSAVER_CONFIG=/usr/share/xscreensaver \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
	--with%{!?with_arts:out}-arts \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir}

%{__make}
rm -f makeinstall.stamp

%install
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT \
		kde_htmldir=%{_kdedocdir}

	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	# Makefile installs these basing on XSCREENSAVER_DIR/* files -
	# let's do it manually to avoid BR: xscreensaver{,-GL,-GLE}
	install kscreensaver/kxsconfig/ScreenSavers/*.desktop $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver
	rm -f $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver/pixmaps.desktop

	rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
	rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*/*/*.la
	touch installed.stamp
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-cde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_cde.so
%attr(755,root,root) %{_libdir}/kde3/kwin_cde_config.so
%{_datadir}/apps/kwin/cde.desktop

%files -n kde-decoration-icewm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_icewm.so
%attr(755,root,root) %{_libdir}/kde3/kwin_icewm_config.so
%{_datadir}/apps/kwin/icewm-themes
%{_datadir}/apps/kwin/icewm.desktop

%files -n kde-decoration-glow
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_glow.so
%attr(755,root,root) %{_libdir}/kde3/kwin_glow_config.so
%{_datadir}/apps/kwin/glow-themes
%{_datadir}/apps/kwin/glow.desktop

%files -n kde-decoration-kde1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_kde1.so
%{_datadir}/apps/kwin/kde1*

%files -n kde-decoration-kstep
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_kstep.so
%{_datadir}/apps/kwin/kstep*

%files -n kde-decoration-openlook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_openlook.so
%{_datadir}/apps/kwin/openlook.desktop

%files -n kde-decoration-riscos
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_riscos.so
%{_datadir}/apps/kwin/riscos*

%files -n kde-decoration-system
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_system.so
%{_datadir}/apps/kwin/system.desktop

%files -n kde-decoration-smoothblend
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin*_smoothblend*.so
%{_datadir}/apps/kwin/smoothblend.desktop

%files -n kde-emoticons
%defattr(644,root,root,755)
%{_datadir}/emoticons

%files -n kde-icons-Locolor
%defattr(644,root,root,755)
%{_iconsdir}/Locolor

#%files -n kde-icons-hicolor
#%defattr(644,root,root,755)
#%{_iconsdir}/hicolor

%files -n kde-icons-ikons
%defattr(644,root,root,755)
%{_iconsdir}/ikons

%files -n kde-icons-kdeclassic
%defattr(644,root,root,755)
%{_iconsdir}/kdeclassic

%files -n kde-icons-kids
%defattr(644,root,root,755)
%{_iconsdir}/kids

%files -n kde-icons-slick
%defattr(644,root,root,755)
%{_iconsdir}/slick

%files -n kde-style-dotnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/dotnet.so
%{_datadir}/apps/kstyle/themes/dotnet*

%files -n kde-style-phase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kstyle_phase_config.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/phasestyle.so
%{_datadir}/apps/kstyle/themes/phase.themerc

%files kworldclock
%defattr(644,root,root,755)
%{_datadir}/apps/kworldclock/maps/[!d]*
#%{_datadir}/apps/kworldclock/maps/depths/*

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*.kss
%{_datadir}/apps/kfiresaver
%{_datadir}/apps/kscreensaver/*.png

# KDE xscreensaver wrappers (should R: xscreensaver?)
%attr(755,root,root) %{_bindir}/kxsconfig
%attr(755,root,root) %{_bindir}/kxsrun
# extrusion.desktop is for xscreensaver-GLE, the rest for xscreensaver{,-GL}
%{_datadir}/apps/kscreensaver/*.desktop
#%{_datadir}/config/*rc

%files sounds
%defattr(644,root,root,755)
%{_datadir}/sounds/*

%files wallpapers
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*
