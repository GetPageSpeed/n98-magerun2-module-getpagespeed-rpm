%global appname n98-magerun2

# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun2-module-getpagespeed
Version: 1.0.12
Release: 1%{?dist}
Summary: The n98-magerun2 module by GetPageSpeed

License: GPLv2+ and MIT and BSD
URL: https://github.com/GetPageSpeed/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

# This is where /usr/share/n98-magerun2/modules was added as modules location
Requires: n98-magerun2 >= 3.2.0

%description
Collection of useful commands for n98-magerun2.


%prep
%autosetup


%build
# Nothing to do


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}%{_datadir}/%{appname}/modules/getpagespeed
%{__cp} -r src %{buildroot}%{_datadir}/%{appname}/modules/getpagespeed/
%{__cp} -r n98-magerun2.yaml %{buildroot}%{_datadir}/%{appname}/modules/getpagespeed/


%files
%defattr(644,root,root,755)
%{_datadir}/%{appname}/modules/getpagespeed


%changelog
* Wed May 03 2023 Danila Vershinin <info@getpagespeed.com> 1.0.12-1
- release 1.0.12

* Tue Dec 29 2020 Danila Vershinin <info@getpagespeed.com> 1.0.11-1
- release 1.0.11

* Sun Oct 04 2020 Danila Vershinin <info@getpagespeed.com> 1.0.10-1
- release 1.0.10

* Sat Oct 03 2020 Danila Vershinin <info@getpagespeed.com> 1.0.9-1
- release 1.0.9

* Sun Apr 26 2020 Danila Vershinin <info@getpagespeed.com> 1.0.8-1
- release 1.0.8

* Sun Apr 19 2020 Danila Vershinin <info@getpagespeed.com> 1.0.6-1
- released 1.0.6

* Sun Dec 29 2019 Danila Vershinin <info@getpagespeed.com> 1.0.4-2
- use non-local, proper location for modules now that n98-magerun2 supports it

* Fri Aug 30 2019 Danila Vershinin <info@getpagespeed.com> 1.0.4-1
- upstream version auto-updated to 1.0.4

* Fri May 11 2018 Danila Vershinin <info@getpagespeed.com> 1.0.3-3
- upstream version auto-updated to 1.0.3

* Fri May 11 2018 Danila Vershinin <info@getpagespeed.com> 1.0.0-2
- update to 1.0.0

