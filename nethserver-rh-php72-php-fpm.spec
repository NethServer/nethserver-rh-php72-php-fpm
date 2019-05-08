Name: nethserver-rh-php72-php-fpm
Version: 1.0.0
Release: 1%{?dist}
Summary: NethServer rh-php72-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: rh-php72, rh-php72-php-fpm

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
* Wed May 08 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First release

* Tue Mar 20 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Nextcloud: upgrade to v13 & optimizations - NethServer/dev#5427

* Tue Apr 04 2017 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- First release
- Nextcloud 11 - NethServer/dev#5242

