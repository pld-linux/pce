Summary:	PCE - PC Emulator
Summary(pl.UTF-8):	Emulator PC
Name:		pce
Version:	0.1.7
Release:	1
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://www.hampa.ch/pce/download/%{name}-%{version}.tar.gz
# Source0-md5:	19d22748aaed7990bac4284dfcd61cab
URL:		http://www.hampa.ch/pce/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCE is an IBM PC hardware emulator. It emulates most of the hardware
of an IBM PC 5150. The emulation is complete enough to boot DOS and
run most DOS applications.

%description -l pl.UTF-8
PCE jest emulatorem komputera IBM PC. Emuluje większość sprzętu z IBM
PC 5150. Emulacja jest kompletna i pozwala uruchomić DOS i większość
aplikacji DOSowych.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS NEWS README pce.lsm
%attr(755,root,root) %{_bindir}/*
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/*
%{_mandir}/man?/*
%{_datadir}/%{name}
