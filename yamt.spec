Summary:	Yet Another Mp3 Tool
Summary(pl):	Jeszcze Jedno Narzêdzie Mp3
Name:		yamt
Version:	0.5
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/yamt/%{name}-%{version}.tar.gz
# Source0-md5:	22beb30f6762ede1641e89c978636dcd
Patch0:		%{name}-pixmaps.patch
Patch1:		%{name}-ac_fix.patch
Patch2:		%{name}-va_arg_fix.patch
URL:		http://yamt.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAMT is Yet Another Mp3 Tool which helps you to organize your mp3s.

%description -l pl
YAMT jest Jeszcze Jednym Narzêdziem Mp3, które pomo¿e porz±dkowaæ
twoje pliki mp3.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Multimedia

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/yamt
%{_applnkdir}/Multimedia/yamt.desktop
%{_pixmapsdir}/*
