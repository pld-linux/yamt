Summary:	Yet Another Mp3 Tool
Summary(pl):	Jeszcze Jedno Narzêdzie Mp3
Name:		yamt
Version:	0.5
Release:	3
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://download.sourceforge.net/pub/sourceforge/yamt/%{name}-%{version}.tar.gz
Patch0:		%{name}-pixmaps.patch
URL:		http://yamt.sourceforge.net/
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
YAMT is Yet Another Mp3 Tool which helps you to organize your mp3s.

%description -l pl
YAMT jest Jeszcze Jednym Narzêdziem Mp3, które pomo¿e porz±dkowaæ
twoje pliki mp3.

%prep
%setup -q
%patch0 -p1

%build
automake
gettextize --copy --force
%configure \
	--enable-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Multimedia

gzip -9nf AUTHORS NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/yamt
%{_applnkdir}/Multimedia/yamt.desktop
%{_pixmapsdir}/*
%{_datadir}/gnome/help/yamt
