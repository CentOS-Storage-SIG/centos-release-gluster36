Summary: GlusterFS 3.6 packages from the CentOS Storage SIG repository
Name: centos-release-gluster36
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-3.6.repo
Source1: COPYING

BuildArch: noarch

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

%description
yum configuration for GlusterFS 3.6 packages as delivered via the CentOS
Storage SIG.

%prep
cp %{SOURCE1} .

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.6.repo

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.6.repo
%license COPYING

%changelog
* Thu Nov 12 2015 Niels de Vos <ndevos@redhat.com> - 1.0-1
- Initial version based on centos-release-gluster37