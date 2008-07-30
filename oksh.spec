Summary:	OpenBSDs ksh for Linux
Name:		oksh
Version:	0.3
Release:	%mkrel 3
License:	GPLv3+
Group:		Shells
URL:		http://www.delilinux.de/oksh/
Source0:	http://www.delilinux.de/oksh/%{name}-%{version}.tar.gz
BuildRequires:	pmake
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
OpenBSDs ksh for Linux

%prep

%setup -q

%build
pmake DEFS="%{optflags}" ksh

%check
pmake test

%install
rm -rf %{buildroot}

install -d %{buildroot}/bin
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 ksh %{buildroot}/bin/oksh
ln -s %{buildroot}/bin/oksh %{buildroot}%{_bindir}/oksh

install -m0644 ksh.1 %{buildroot}%{_mandir}/man1/oksh.1

%post
%{_datadir}/rpm-helper/add-shell %{name} $1 /bin/oksh

%postun
%{_datadir}/rpm-helper/del-shell %{name} $1 /bin/oksh

%files
%defattr(-,root,root)
%doc ChangeLog.oksh README.oksh
/bin/oksh
%{_bindir}/oksh
%{_mandir}/man1/oksh.1*

