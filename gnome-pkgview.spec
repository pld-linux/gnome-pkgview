Summary:	Displays the version of GNOME desktop components installed
Summary(pl):	Wy�wietlanie wersji zainstalowanych komponent�w �rodowiska GNOME
Name:		gnome-pkgview
Version:	1.0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.greatnorthern.demon.co.uk/packages/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	8cabf2cacc011caa4a1ee6c6b4dacdf4
Source1:	%{name}-pld.png
Patch0:		%{name}-pld.patch
URL:		http://www.greatnorthern.demon.co.uk/gnome-pkgview.html
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libxml2-devel >= 2.0.0
Requires(post):	GConf2
Requires:	gnome-desktop >= 2.4.0
Requires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Currently, there is no easy way of determining which version of GNOME
you are running. Its a common question on IRC and on mailing lists.
This makes the task of debugging and providing support more difficult
for those who try to help out. This little application provides a
couple of useful pieces of information.

%description -l pl
Aktualnie nie ma prostej metody, kt�ra pozwala�aby sprawdzi�, kt�ra
wersja GNOME jest aktualnie zainstalowana. Pytanie to jest powszechne
na IRC-u i listach dyskusyjnych. Sprawia to, �e proces odpluskwiania i
udzielania pomocy jest trudniejszy dla tych, kt�rzy pr�buj� pom�c. Ta
ma�a aplikacja udost�pnia kilka u�ytecznych informacji.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/pld.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
