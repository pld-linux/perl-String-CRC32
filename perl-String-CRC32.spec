#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	String
%define		pnam	CRC32
Summary:	String::CRC32 - Perl interface to CRC32 generation
Summary(pl.UTF-8):	String::CRC32 - perlowy interfejs do generowania CRC32
Name:		perl-String-CRC32
Version:	1.7
Release:	8
License:	Public Domain
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	795a7c23fae9d24e485d4de08a58ef03
URL:		http://search.cpan.org/dist/String-CRC32/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::CRC32 module calculates CRC of 32 bit lenghts.

%description -l pl.UTF-8
Moduł String::CRC32 oblicza CRC długości 32 bitów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%doc README.md
%{perl_vendorarch}/String/CRC32.pm
%dir %{perl_vendorarch}/auto/String/CRC32
%attr(755,root,root) %{perl_vendorarch}/auto/String/CRC32/CRC32.so
%{_mandir}/man3/*
