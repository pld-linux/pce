Summary:	PCE - PC Emulator
Summary(pl):	Emulator PC
Name:		pce
Version:	0.1.5
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.hampa.ch/pce/%{name}-%{version}.tar.gz
# Source0-md5:	e5060e734031a8690e7cb404034452d1
Patch0:		%{name}-DESTDIR.patch
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

%description -l pl
PCE jest emulatorem komputera IBM PC. Emuluje wiêkszo¶æ sprzêtu z IBM
PC 5150. Emulacja jest kompletna i pozwala uruchomiæ DOS i wiêkszo¶æ
aplikacji DOSowych.

%prep
%setup -q
%patch0 -p1

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
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/*
%{_mandir}/man?/*
%{_datadir}/%{name}
