Summary:	K Desktop Environment - artwork
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary:	KDE¿ë
Summary(pl):	K Desktop Environment - grafiki itp.
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplicações KDE
Name:		kdeartwork
Version:	3.0.3
Release:	7
Epoch:		7
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-fix-icon-in-about-dialogbox2.patch
Patch1:		%{name}-fix-icon-in-about-dialogbox3.patch
Patch2:		%{name}-fix-icon-in-about-dialogbox.patch
Patch3:		%{name}-fix-mem-leak.patch
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
%define		_prefix		/usr/X11R6
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

%package screensavers
Summary:	Screen savers for KDE
Summary(pl):	Wygaszacze ekranu dla KDE
Group:		X11/Amusements

%description screensavers
Screen savers for KDE.

%description screensavers -l pl
Wygaszacze ekranu dla KDE.

%package themes
Summary:	Themes for KDE
Summary(pl):	Motywy dla KDE
Group:		X11/Amusements
Requires:	kdebase-screensavers

%description themes
Themes for KDE.

%description themes -l pl
Motywy dla KDE.

%package themes-kworldclock
Summary:	Themes for kworldclock
Summary(pl):	Motywy dla kworldclock
Group:		X11/Amusements
Requires:	kdetoys-kworldclock

%description themes-kworldclock
Themes for kworldclock.

%description themes-kworldclock -l pl
Motywy dla kworldclock.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_pixmapsdir}/{L,l}ocolor
# Conflict with kdeaddons-kicker:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/ktimemon.png
# Conflict with kdebase:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/bell.png
# Conflict with kdegames-kspaceduel:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/kspaceduel.png
# Conflict with kdegames-lskat:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/lskat.png
# Conflict with kdenetwork-ksirc:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/ksirc.png
# Conflict with kdesdk:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/mimetypes/gettext.png
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/kbabel.png
# Conflicts with kdetoys-kteatime:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/16x16/apps/kteatime.png
# Conflict with kdetoys-ktux:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/ktux.png
# Conflict with koffice-kspread:
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/locolor/{16x16,32x32}/apps/kspreadcalc.png

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang kdeartwork --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdeartwork.lang
%defattr(644,root,root,755)
%{_pixmapsdir}/Technical
%{_pixmapsdir}/ikons
%{_pixmapsdir}/slick
%{_pixmapsdir}/locolor/index.desktop
%{_pixmapsdir}/locolor/*/*/*.png
%{_datadir}/wallpapers/*
%{_datadir}/config/*

%files screensavers
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxs*
%attr(755,root,root) %{_bindir}/*.kss
%{_datadir}/apps/kscreensaver
%{_applnkdir}/System/ScreenSavers

%files themes
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_*.??
%{_libdir}/kde3/plugins/styles/*
%{_datadir}/apps/kstyle/themes/*
%{_datadir}/apps/kthememgr/Themes/*
%{_datadir}/apps/kwin/icewm-themes/*
%{_datadir}/apps/kwin/*.desktop
%{_datadir}/sounds/*

%files themes-kworldclock
%defattr(644,root,root,755)
%{_datadir}/apps/kworldclock/maps/[^d]*
%{_datadir}/apps/kworldclock/maps/depths/*
