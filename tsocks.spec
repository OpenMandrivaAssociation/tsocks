%define name tsocks
%define version 1.8
%define beta beta5
%define sub_release 2
%define	major 1
%define	libname_orig lib%{name}
%define	libname %mklibname %{name} %{major}
%define	libnamedev %mklibname %{name} %{major} -d

%if %{beta}
%define release 0.%{beta}.%{sub_release}
%else
%define release %{sub_release}
%endif

Summary: A transparent SOCKS proxying library
Name: %{name}
Version: %{version}
Release: %mkrel %{release}
Source0: http://ftp1.sourceforge.net/tsocks/%{name}-%{version}%{beta}.tar.bz2
License: GPL
Group: Networking/Other
Url: http://tsocks.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: %{libname} = %{version}

%description
tsocks' role is to allow these non SOCKS aware applications (e.g
telnet, ssh, ftp etc) to use SOCKS without any modification. It does
this by intercepting the calls that applications make to establish
network connections and negotating them through a SOCKS server as
necessary.

%package -n	%{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n	%{libname}
Library for %{name}


%prep
%setup -q

%build
%configure2_5x
%make
sed -i -e 's£/usr/lib/£%{_libdir}/£g' tsocks

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so*

