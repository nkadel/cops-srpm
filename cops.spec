Summary: COPS security scanner
Name: cops
Version: 1.0.4
Release: 0.1%{?dist}


Source: http://ftp.twaren.net/BSD/OpenBSD/distfiles/cops.1.04.tar.gz

BuildRequires: perl-interpreter
Requires: perl-interpreter

License: GPLv3+

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
%setup -n cops_104

%build
# Does not work
#make

#%%{make_build}

#%%check

%install
# does not work yet
#make install

%files
#%%license COPYING
%doc README.*

%changelog
