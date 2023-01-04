# Workaround for incompatible build system
%global debug_package %{nil}

Summary:	OpenBSDs ksh for Linux
Name:		oksh
Version:	7.2
Release:	1
License:	GPLv3+
Group:		Shells
URL:		https://github.com/ibara/oksh
Source0:	https://github.com/ibara/oksh/archive/refs/tags/oksh-%{version}.tar.gz

%description
OpenBSDs ksh for Linux

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
%configure

%build
%make_build

%install
%make_install

%post
%{_datadir}/rpm-helper/add-shell %{name} $1 /bin/oksh

%postun
%{_datadir}/rpm-helper/del-shell %{name} $1 /bin/oksh

%files
%defattr(-,root,root)
%{_bindir}/oksh
%{_mandir}/man1/oksh.1*
