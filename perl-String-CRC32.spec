#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	CRC32
Summary:	String::CRC32 perl module
Summary(pl):	Modu� perla String::CRC32
Name:		perl-String-CRC32
Version:	1.2
Release:	7
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94b13443eac7241a323a876da95ac1c0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::CRC32 - calculates CRC of 32 bit lenghts.

%description -l pl
String::CRC32 - oblicza CRC d�ugo�ci 32 bit�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/String/CRC32.pm
%dir %{perl_vendorarch}/auto/String/CRC32
%{perl_vendorarch}/auto/String/CRC32/CRC32.bs
%attr(755,root,root) %{perl_vendorarch}/auto/String/CRC32/CRC32.so
%{_mandir}/man3/*
