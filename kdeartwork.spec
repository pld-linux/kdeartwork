
%define		_state		stable
%define		_ver		3.1.4

Summary:	K Desktop Environment - artwork
Summary(es):	K Desktop Environment - Plugins e Scripts para aplicativos KDE
Summary(ko):	KDE��
Summary(pl):	K Desktop Environment - grafiki itp.
Summary(pt_BR):	K Desktop Environment - Plugins e Scripts para aplica��es KDE
Name:		kdeartwork
Version:	%{_ver}
Release:	1
Epoch:		7
License:	LGPL
Vendor:		The KDE Team
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	042e42ade90a8d137edea88eb7d3e11d
# generated from kde-i18n
Source1:	ftp://blysk.ds.pg.gda.pl/linux/kde-i18n-package/%{version}/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	2a083985bbe4074dedffed88b4217d94
Patch0:		%{name}-screensavers.patch
Patch1:		%{name}-ac_am.patch
URL:		http://www.kde.org/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	ed
BuildRequires:	kdebase-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs
Requires:	kdelibs = 8:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

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
Requires:	kdebase >= %{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-cde
KDE Window Decoration - CDE.

%description -n kde-decoration-cde -l pl
Dekoracja okna dla KDE - CDE.

%package -n kde-decoration-icewm-ext
Summary:	Extensions for KDE IceWM decoration
Summary(pl):	Rozszerzenie dekoracji okna "IceWM" dla KDE
Group:		X11/Amusements
Requires:	kde-decoration-icewm >= %{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-icewm-ext
Extensions for KDE "IceWM" decoration.

%description -n kde-decoration-icewm-ext -l pl
Rozszerzenie dekoracji okna IceWM dla KDE.

%package -n kde-decoration-glow
Summary:	KDE Window Decoration - Glow
Summary(pl):	Dekoracja okna dla KDE - Glow
Group:		X11/Amusements
Requires:	kdebase >= %{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-glow
KDE Window Decoration - Glow.

%description -n kde-decoration-glow -l pl
Dekoracja okna dla KDE - Glow.

%package -n kde-decoration-openlook
Summary:	KDE Window Decoration - OpenLook
Summary(pl):	Dekoracja okna dla KDE - OpenLook
Group:		X11/Amusements
Requires:	kdebase >= %{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-decoration-openlook
KDE Window Decoration - OpenLook.

%description -n kde-decoration-openlook -l pl
Dekoracja okna dla KDE - OpenLook.

%package -n kde-icons-Technical
Summary:	KDE Icons Theme - Technical
Summary(pl):	Motyw ikon dla KDE - Technical
Group:		X11/Amusements
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
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-icons-kdeclassic
KDE Icons Theme - kdeclassic.

%description -n kde-icons-kdeclassic -l pl
Motyw ikon dla KDE - kdeclassic.

%package -n kde-icons-Locolor
Summary:	KDE Icons Theme - locolor
Summary(pl):	Motyw ikon dla KDE - locolor
Group:		X11/Amusements
Obsoletes:	%{name}
Obsoletes:	%{name}-icons-locolor
Obsoletes:	%{name}-locolor
Obsoletes:	%{name}-themes

%description -n kde-icons-Locolor
KDE Icons Theme - locolor.

%description -n kde-icons-Locolor -l pl
Motyw ikon dla KDE - locolor.

%package -n kde-icons-slick
Summary:	KDE Icons Theme - slick
Summary(pl):	Motyw ikon dla KDE - slick
Group:		X11/Amusements
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
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description -n kde-style-dotnet
KDE Style - DotNet.

%description -n kde-style-dotnet -l pl
Styl dla KDE - DotNet.

%package kworldclock
Summary:	Themes for kworldclock
Summary(pl):	Motywy dla kworldclock
Group:		X11/Amusements
Requires:	kdetoys-kworldclock
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
Requires:	kdebase-screensavers
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
# Holds %{_datadir}/wallpapers
Requires:	kdebase >= %{version}
Obsoletes:	%{name}
Obsoletes:	%{name}-themes

%description wallpapers
KDE Wallpapers.

%description wallpapers -l pl
Tapety dla KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"

for plik in `find . -name \*.desktop -o -name \*rc | xargs grep -l '\[nb\]'` ; do
	echo -e ',s/\[nb\]=/[no]=/\n,w' | ed $plik
done

%{__make} -f admin/Makefile.common cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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

for i in `find $RPM_BUILD_ROOT%{_applnkdir} -type f`; do
	if grep '^Icon=.[^.]*$' $i >/dev/null; then
		echo -e ',s/\(^Icon=.*$\)/\\1.png/\n,w' | ed $i
	fi
done

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang	klock			--with-kde
%find_lang	kpartsaver		--with-kde
cat klock.lang kpartsaver.lang > screensavers.lang
%find_lang	kwin_cde_config		--with-kde
%find_lang	kwin_glow_config	--with-kde

# does not build
#%find_lang	kxsconfig		--with-kde

# probably obsolete
#%find_lang	kless			--with-kde
#%find_lang	klpq			--with-kde
#%find_lang	ksysctrl		--with-kde

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-cde -f kwin_cde_config.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_cde*.la
%attr(755,root,root) %{_libdir}/kde3/kwin_cde*.so
%{_datadir}/apps/kwin/cde*

%files -n kde-decoration-icewm-ext
%defattr(644,root,root,755)
%{_datadir}/apps/kwin/icewm-themes/*

%files -n kde-decoration-glow -f kwin_glow_config.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_glow*.la
%attr(755,root,root) %{_libdir}/kde3/kwin_glow*.so
%{_datadir}/apps/kwin/glow*

%files -n kde-decoration-openlook
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_openlook.la
%attr(755,root,root) %{_libdir}/kde3/kwin_openlook.so
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
%{_libdir}/kde3/plugins/styles/dotnet.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/dotnet.so
%{_datadir}/apps/kstyle/themes/dotnet*

%files kworldclock
%defattr(644,root,root,755)
%{_datadir}/apps/kworldclock/maps/[^d]*
%{_datadir}/apps/kworldclock/maps/depths/*

%files screensavers -f screensavers.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kscreensaver/*
#%{_datadir}/config/*
%{_mandir}/man1/*.kss.*

%files sounds
%defattr(644,root,root,755)
%{_datadir}/sounds/*

%files wallpapers
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*
