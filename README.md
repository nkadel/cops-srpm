cops-srpm
=========

Wrapper for SRPM building tools for copos_104. COPS is quite old
security auditing sofware written by Dan Farmer. The last updates were
in 2012, but some folks still use it.

Building COPS
===============

Ideally, install "mock" and use that to build for both RHEL and up,
through 9 and Fedora 38. Run these commands at the top directory.

* make getsrc # Get source tarvalls for all SRPMs

* make cfgs # Create local .cfg configs for "mock".
* * centos-stream+epel-8-x86_64.cfg # Used for some Makefiles
* * centos-stream+epel-9-x86_64.cfg # Used for some Makefiles
* * fedora-38-x86_64.cfg # Used for some Makefiles

* make repos # Creates local local yum repositories in $PWD/ansiblerepo
* * gitrepo/el/8
* * gitrepo/el/9
* * gitrepo/fedora/38

* make # Make all distinct versions using "mock"

Building a compoenent, without "mock" and in the local working system,
can also be done for testing.

* make build

Installing COPS
=================

The relevant yum repository is built locally in ansiblereepo. To enable the repository, use this:

* make repo

Then install the .repo file in /etc/yum.repos.d/ as directed. This
requires root privileges, which is why it's not automated.

COPS RPM Build Security
=======================

There is a significant security risk with enabling yum repositories
for locally built components. Generating GPG signed packages and
ensuring that the compneents are in this build location are securely
and safely built is not addressed in this test setup.

		Nico Kadel-Garcia <nkadel@gmail.com>
