# Useful for upstrem git repos with tags
%global betaver %{nil}
#%%global betaver rc1

# Not currently working
%global debug_package %{nil}


Summary: Computer Oracle and Password System
Name: cops
Version: 1.0.4
Release: 0.1%{?dist}

# Old, locked source, switch to git repo ASAP
Source: http://ftp.twaren.net/BSD/OpenBSD/distfiles/cops.1.04.tar.gz
Patch1: cops_104.rhel8.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: perl-interpreter
Requires: perl-interpreter

License: BSD

%description
The package, which will henceforth be referred to as COPS (Computer
Oracle and Password System), can be broken down into three key parts.
The first is the actual set of programs that attempt to automate
security checks that are often performed manually (or perhaps with self-
written short shell scripts or programs) by a systems administrator.
The second part is the documentation, which details how to set up,
operate, and interpret the results of the programs. 

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
%autosetup  -n cops_104 -p1

%build
./reconfig
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
* Sat May 20 2023 Nico Kadel-Garcia - 1.0.4-0.1
- Set up initial SRPM
