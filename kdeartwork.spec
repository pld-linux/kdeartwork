
%define		_state		snapshots
%define		_ver		3.1.92
%define         _snap           031014

Summary:	K Desktop Environment - artwork
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(ko):	KDE��
Summary(pl):	K Desktop Environment - grafiki itp.
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplica��es KDE
Name:		kdeartwork
Version:	%{_ver}.%{_snap}
Release:        1
Epoch:		8
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:        http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	5487e01cd082c61aba2a71497eb9aec3
Patch0:		%{name}-screensavers.patch
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	kdebase-devel >= 9:%{version}
BuildRequires:	libxml2-progs
BuildRequires:	sed >= 4.0
Requires:	kdelibs = 9:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
This package contains various graphics and such for KDE.

%description -l es
kdeartwork possue temas, sonidos, wallpapers, e estilos adicionais a
KDE.

%description -l pl
Pakiet ten zawiera r�ne grafiki i tym podobne dla KDE.

%description -l pt_BR
kdeartwork cont�m temas, sons, pap�is de parede e estilos de janelas
adicionais para o KDE.

%package -n kde-decoration-cde
Summary:	KDE Window Decoration - CDE
Summary(pl):	Dekoracja okna dla KDE - CDE
Group:		X11/Amusements
Requires:	kdebase-desktop >= 9:%{version}
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
Requires:	kdebase-desktop >= 9:%{version}
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
Requires:	kdebase-desktop >= 9:%{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-icewm
Extensions for KDE "IceWM" decoration.

%description -n kde-decoration-icewm -l pl
Rozszerzenie dekoracji okna IceWM dla KDE.

%package -n kde-decoration-kde1
Summary:        KDE Window Decoration - KDE 1
Summary(pl):    Dekoracja okna dla KDE - KDE 1
Group:          X11/Amusements
Requires:	kdebase-desktop >= 9:%{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-kde1
KDE Window Decoration - KDE 1.

%description -n kde-decoration-kde1 -l pl
Dekoracja okna dla KDE - KDE 1.

%package -n kde-decoration-kstep
Summary:        KDE Window Decoration - Kstep
Summary(pl):    Dekoracja okna dla KDE - Kstep
Group:          X11/Amusements
Requires:	kdebase-desktop >= 9:%{version}
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
Requires:	kdebase-desktop >= 9:%{version}
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
Requires:	kdebase-desktop >= 9:%{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-plastik
KDE Window Decoration - Plastik.

%description -n kde-decoration-plastik -l pl
Dekoracja okna dla KDE - Plastik.

%package -n kde-decoration-riscos
Summary:        KDE Window Decoration - Risc OS
Summary(pl):    Dekoracja okna dla KDE - Risc OS
Requires:	kdebase-desktop >= 9:%{version}
Group:          X11/Amusements
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-riscos
KDE Window Decoration - Risc OS.

%description -n kde-decoration-riscos -l pl
Dekoracja okna dla KDE - Risc OS.

%package -n kde-decoration-system
Summary:        KDE Window Decoration - System
Summary(pl):    Dekoracja okna dla KDE - System
Group:          X11/Amusements
Requires:	kdebase-desktop >= 9:%{version}
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
Requires:	kdelibs >= 9:%{version}
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
Requires:	kdelibs >= 9:%{version}
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
Requires:	kdelibs >= 9:%{version}
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
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-icons-kdeclassic
KDE Icons Theme - kdeclassic.

%description -n kde-icons-kdeclassic -l pl
Motyw ikon dla KDE - kdeclassic.

%package -n kde-icons-slick
Summary:	KDE Icons Theme - slick
Summary(pl):	Motyw ikon dla KDE - slick
Group:		X11/Amusements
Requires:	kdelibs >= 9:%{version}
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
Requires:	kdebase-core >= 9:%{version}
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
Requires:	kdebase-core >= 9:%{version}
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
Requires:	kdebase-screensavers >= 9:%{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description screensavers
Screen savers for KDE.

%description screensavers -l pl
Wygaszacze ekranu dla KDE.

%package sounds
Summary:	KDE Sounds
Summary(pl):	D�wi�ki dla KDE
Group:		X11/Amusements
Requires:	kdebase-desktop >= 9:%{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description sounds
KDE Sounds.

%description sounds -l pl
D�wi�ki dla KDE.

%package wallpapers
Summary:	KDE Wallpapers
Summary(pl):	Tapety dla KDE
Group:		X11/Amusements
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description wallpapers
KDE Wallpapers.

%description wallpapers -l pl
Tapety dla KDE.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build

for f in `find . -name *.desktop` ; do
	sed -i 's/\[nb\]/\[no\]/g'  $f
done

%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

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

#%files -n kde-decoration-kde1
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kwin_kde1.la
#%attr(755,root,root) %{_libdir}/kde3/kwin_kde1.so
#%{_datadir}/apps/kwin/kde1*

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

#%files -n kde-decoration-system
#%defattr(644,root,root,755)
#%{_libdir}/kde3/kwin_system.la
#%attr(755,root,root) %{_libdir}/kde3/kwin_system.so
#%{_datadir}/apps/kwin/system*

%files -n kde-icons-Technical
%defattr(644,root,root,755)
%{_iconsdir}/Technical

%files -n kde-icons-ikons
%defattr(644,root,root,755)
%{_iconsdir}/ikons

%files -n kde-icons-kdeclassic
%defattr(644,root,root,755)
%{_iconsdir}/kdeclassic

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
%{_libdir}/kde3/plugins/styles/plastik.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/plastik.so
%{_datadir}/apps/kstyle/themes/plastik.themerc

%files kworldclock
%defattr(644,root,root,755)
%{_datadir}/apps/kworldclock/maps/[^d]*
%{_datadir}/apps/kworldclock/maps/depths/*

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kscreensaver/*
##%{_datadir}/config/*

%files sounds
%defattr(644,root,root,755)
%{_datadir}/sounds/*

%files wallpapers
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*
