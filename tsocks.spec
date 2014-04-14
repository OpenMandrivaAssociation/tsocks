%define major           1
%define libname_orig    lib%{name}
%define libname         %mklibname %{name} %{major}
%define libnamedev      %mklibname %{name} %{major} -d
%define beta            beta5

Name:           tsocks
Version:        1.8
Release:        0.%{beta}.8
Summary:        A transparent SOCKS proxying library
License:        GPL
Group:          Networking/Other
URL:            http://tsocks.sourceforge.net/
Source0:        http://ftp1.sourceforge.net/tsocks/%{name}-%{version}%{beta}.tar.bz2
BuildRequires:  glibc-static-devel
Requires:       %{libname} = %{version}-%{release}

%description
tsocks' role is to allow these non SOCKS aware applications (e.g
telnet, ssh, ftp etc) to use SOCKS without any modification. It does
this by intercepting the calls that applications make to establish
network connections and negotating them through a SOCKS server as
necessary.

%package -n %{libname}
Summary:        Library for %{name}
Group:          System/Libraries

%description -n %{libname}
Library for %{name}.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__perl} -pi -e 's|/usr/lib|%{_libdir}|g' %{buildroot}%{_bindir}/tsocks


%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*

%files -n %{libname}
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/*.so*


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.8-0.beta5.7mdv2010.0
+ Revision: 445563
- rebuild

* Fri Mar 06 2009 Michael Scherer <misc@mandriva.org> 1.8-0.beta5.6mdv2009.1
+ Revision: 349607
- fix buildRequires
- rebuild
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill stupid perl -pi -e "s/\-lc//g" Makefile
    - BR glibc-devel
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + David Walluck <walluck@mandriva.org>
    - fix build
    - patch to disable -lc
    - fix build
    - sed the installed tsocks
    - remove -lc from Makefile
    - spec cleanup


* Sat Mar 11 2006 Pascal Terjan <pterjan@mandriva.com> 1.8-0.beta5.2mdk
- Fix running with lib64
- mkrel

* Mon Apr 11 2005 Olivier Blin <oblin@mandrakesoft.com> 1.8-0.beta5.1mdk
- initial Mandrakelinux release

