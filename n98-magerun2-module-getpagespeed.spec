# License: MIT
# http://opensource.org/licenses/MIT

Name: n98-magerun2-module-getpagespeed
Version: 1.0.0
Release: 2%{?dist}
Summary: n98-magerun2 module by GetPageSpeed

License: GPLv2+ and MIT and BSD
URL: http://magerun.net/
Source0: https://github.com/GetPageSpeed/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: n98-magerun2

%description
Collection of useful commands for n98-magerun2.

%prep
%autosetup

%build
# Nothing to do


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}%{_usr}/local/share/n98-magerun2/modules/getpagespeed
%{__cp} -r src %{buildroot}%{_usr}/local/share/n98-magerun2/modules/getpagespeed/
%{__cp} -r n98-magerun2.yaml %{buildroot}%{_usr}/local/share/n98-magerun2/modules/getpagespeed/

%files
%defattr(644,root,root,755)
%{_usr}/local/share/n98-magerun2/modules/getpagespeed

%changelog
* Fri May 11 2018 Danila Vershinin <info@getpagespeed.com> 1.0.0-2
- update to 1.0.0

