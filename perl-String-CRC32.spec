%include	/usr/lib/rpm/macros.perl
Summary:	String-CRC32 perl module
Summary(pl):	Modu³ perla String-CRC32
Name:		perl-String-CRC32
Version:	1.2
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/String-CRC32-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String-CRC32 - calculates CRC of 32 bit lenghts.

%description -l pl
String-CRC32 - oblicza CRC d³ugo¶ci 32 bitów.

%prep
%setup -q -n String-CRC32-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/String/CRC32.pm
%dir %{perl_sitearch}/auto/String/CRC32
%{perl_sitearch}/auto/String/CRC32/CRC32.bs
%attr(755,root,root) %{perl_sitearch}/auto/String/CRC32/CRC32.so
%{_mandir}/man3/*
