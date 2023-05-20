%global betaver rc1

# Not currently working
%global debug_package %{nil}


Summary: COPS security scanner
Name: cops
Version: 1.0.5
Release: 0.1%{?dist}

Source: http://ftp.twaren.net/BSD/OpenBSD/distfiles/cops-%{version}%{betaver}.tar.gz

BuildRequires: perl-interpreter
Requires: perl-interpreter

License: BSD

%description
COPS security scanner

BuildRequires: gcc
BuildRequires: perl-interpreter

BuildRequires: glibc-headers
BuildRequires: /usr/include/fcntl.h
BuildRequires: /usr/include/grp.h
BuildRequires: /usr/include/pwd.h
BuildRequires: /usr/include/pwdadj.h
BuildRequires: /usr/include/signal.h
BuildRequires: /usr/include/stdio.h
BuildRequires: /usr/include/string.h
BuildRequires: /usr/include/sys/audit.h
BuildRequires: /usr/include/sys/label.h
BuildRequires: /usr/include/sys/stat.h
BuildRequires: /usr/include/sys/types.h

%prep
# Because tarball is mislabeled
%setup -n cops-%{version}%{betaver}

%build
make
make install

#%%check

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 bin/* %{buildroot}%{_bindir}/

%files
#%%license COPYING
%doc README.*
%{_bindir}/*

%changelog
