Name: nethserver-rh-php72-php-fpm
Version: 1.0.1
Release: 1%{?dist}
Summary: NethServer rh-php72-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: rh-php72, rh-php72-php-fpm
Requires: rh-php72-php-bcmath, rh-php72-php-gd, sclo-php72-php-imap
Requires: rh-php72-php-ldap, rh-php72-php-enchant, rh-php72-php-mbstring
Requires: rh-php72-php-pdo, sclo-php72-php-tidy, rh-php72-php-mysqlnd
Requires: rh-php72-php-soap, rh-php72-php-pgsql
Requires: rh-php72-php-pecl-apcu, rh-php72-php-intl
Requires: rh-php72-php-opcache

%description
Basic support for PHP 7.2 using SCL

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Wed Dec 11 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-1
- Change PHP-FPM version in Web server app - NethServer/dev#5912

* Wed May 08 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First release

* Tue Mar 20 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Nextcloud: upgrade to v13 & optimizations - NethServer/dev#5427

* Tue Apr 04 2017 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- First release
- Nextcloud 11 - NethServer/dev#5242
