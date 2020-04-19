%global appname n98-magerun2

# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun2-module-getpagespeed
Version: 1.0.5
Release: 1%{?dist}
Summary: The n98-magerun2 module by GetPageSpeed

License: GPLv2+ and MIT and BSD
URL: https://github.com/GetPageSpeed/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
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
* Sun Apr 19 2020 Danila Vershinin <info@getpagespeed.com> 1.0.5-1
- release 1.0.5

* Sun Dec 29 2019 Danila Vershinin <info@getpagespeed.com> 1.0.4-2
- use non-local, proper location for modules now that n98-magerun2 supports it

* Fri Aug 30 2019 Danila Vershinin <info@getpagespeed.com> 1.0.4-1
- upstream version auto-updated to 1.0.4

* Fri May 11 2018 Danila Vershinin <info@getpagespeed.com> 1.0.3-3
- upstream version auto-updated to 1.0.3

* Fri May 11 2018 Danila Vershinin <info@getpagespeed.com> 1.0.0-2
- update to 1.0.0

