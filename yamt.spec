Summary:	Yet Another Mp3 Tool
Summary(pl):	Jeszcze Jedno Narzêdzie Mp3
Name:		yamt
Version:	0.5
Release:	2
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	http://sourceforge.net/download.php/yamt/%{name}-%{version}.tar.gz
Patch0:		yamt-pixmaps.patch
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
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-gnome
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Multimedia \
	install

gzip -9nf AUTHORS NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/yamt
%{_applnkdir}/Multimedia/yamt.desktop
%{_datadir}/pixmaps/*
%{_datadir}/gnome/help/yamt
