Summary:	K Desktop Environment - artwork
#Summary(pl):	K Desktop Environment - artwork
Name:		kdeartwork
Version:	3.0.3
Release:	3
Epoch:		7
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	XFree86-devel
BuildRequires:	OpenGL-devel
BuildRequires:	kdelibs-devel
BuildRequires:	kdebase-devel
BuildRequires:	libxml2-progs
Requires:	kdelibs = %{version}
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
This package contains various graphics, sounds, themes and such for
KDE.

%description -l pl
Ten pakiet zawiera ró¿ne grafiki, d¼wiêki, tematy i tym podobne dla
KDE.

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
Summary(pl):	Tematy dla KDE
Group:		X11/Amusements

%description themes
Themes for KDE.

%description themes -l pl
Tematy dla KDE.

%package themes-kworldclock
Summary:	Themes for kworldclock
Summary(pl):	Tematy dla kworldclock
Group:		X11/Amusements

%description themes-kworldclock
Themes for kworldclock.

%description themes-kworldclock -l pl
Tematy dla kworldclock.

%prep
%setup -q

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
# Conflicts with kdebase:
rm $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps/locolor/{16x16,32x32}/apps/bell.png

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang kdeartwork --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kdeartwork.lang
%defattr(644,root,root,755)
%{_pixmapsdir}/*
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
%{_datadir}/apps/kworldclock/*
