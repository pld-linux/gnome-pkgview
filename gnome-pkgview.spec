Summary:	Displays the version of GNOME desktop components installed
Summary(pl):	Wy¶wietlanie wersji zainstalowanych komponentów ¶rodowiska GNOME
Name:		gnome-pkgview
Version:	1.0.6
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.greatnorthern.demon.co.uk/packages/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9b5e07077f06b72acb4568fc13f6d715
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.greatnorthern.demon.co.uk/gnome-pkgview.html
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	perl-XML-Parser
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
Aktualnie nie ma prostej metody, która pozwala³aby sprawdziæ, która
wersja GNOME jest aktualnie zainstalowana. Pytanie to jest powszechne
na IRC-u i listach dyskusyjnych. Sprawia to, ¿e proces odpluskwiania i
udzielania pomocy jest trudniejszy dla tych, którzy próbuj± pomóc. Ta
ma³a aplikacja udostêpnia kilka u¿ytecznych informacji.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv po/{no,nb}.po

%build
intltoolize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
