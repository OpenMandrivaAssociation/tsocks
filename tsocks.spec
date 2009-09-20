%define major           1
%define libname_orig    lib%{name}
%define libname         %mklibname %{name} %{major}
%define libnamedev      %mklibname %{name} %{major} -d
%define beta            beta5

Name:           tsocks
Version:        1.8
Release:        %mkrel 0.%{beta}.7
Summary:        A transparent SOCKS proxying library
License:        GPL
Group:          Networking/Other
URL:            http://tsocks.sourceforge.net/
Source0:        http://ftp1.sourceforge.net/tsocks/%{name}-%{version}%{beta}.tar.bz2
BuildRequires:  glibc-static-devel
Requires:       %{libname} = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*

%files -n %{libname}
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/*.so*
