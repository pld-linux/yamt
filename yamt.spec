Summary:	Yet Another Mp3 Tool
Summary(pl):	Jeszcze Jedno Narzêdzie Mp3
Name:		yamt
Version:	0.4
Release:	1
Copyright:	GPL
Group:		X11/Aplications
Group(pl):	X11/Aplikacje
Source:		%{name}-%{version}.tar.gz
Patch0:		yamt-Makefile.patch
URL:		http://yamt.sourceforge.net/
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	gnome-libs
Requires:	ORBit
BuildPrereq:	gnome-libs-devel
BuildPrereq:	ORBit-devel

%define		_prefix		/usr/X11R6

%description
YAMT is Yet Another Mp3 Tool which helps you to organize your mp3s.

%description -l pl
YAMT jest Jeszcze Jednym Narzêdziem Mp3, które pomo¿e porz±dkowaæ twoje
pliki mp3.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="$RPM_OPT_FLAGS"
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="-s"
./configure \
    --prefix=$RPM_BUILD_ROOT%{_prefix} \
    --enable-gnome
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

make install

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/yamt || :

gzip -9nf AUTHORS COPYING NEWS README TODO

%find_lang yamt

%clean
rm -rf $RPM_BUILD_ROOT

%files -f yamt.lang
%defattr(644,root,root,755)
%doc {AUTHORS,COPYING,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/yamt
%{_datadir}/applnk/Applications/yamt.desktop
%{_datadir}/pixmaps/yamt/yamt-logo.png
%{_datadir}/gnome/help/yamt
