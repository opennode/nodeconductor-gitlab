Name: nodeconductor-gitlab
Summary: GitLab plugin for NodeConductor
Group: Development/Libraries
Version: 0.1.0
Release: 1.el7
License: MIT
Url: http://nodeconductor.com
Source0: %{name}-%{version}.tar.gz

Requires: nodeconductor > 0.102.2
Requires: python-gitlab >= 0.9

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
GitLab plugin for NodeConductor.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Mon Jul 18 2016 Dmitri Tsumak <dmitri@opennodecloud.com> - 0.1.0-1.el7
- Initial version of the package
