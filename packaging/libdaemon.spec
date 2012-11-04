Name:           libdaemon
Version:        0.14
Release:        0
License:        LGPL-2.1+
Summary:        Lightweight C library That Eases the Writing of UNIX Daemons
Url:            http://0pointer.de/lennart/projects/libdaemon/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  doxygen
BuildRequires:  pkg-config

%description
libdaemon is a lightweight C library that eases the writing of UNIX
daemons.


%package devel
License:        GPL-2.0+
Summary:        Lightweight C library That Eases the Writing of UNIX Daemons
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libdaemon = %{version}

%description devel
libdaemon is a lightweight C library that eases the writing of UNIX
daemons.

%prep
%setup -q

%build
%configure \
        --disable-static --with-pic \
        --disable-lynx
make %{?_smp_mflags}

%install
%make_install
# We don't care about the HTML README
rm %{buildroot}%{_datadir}/doc/libdaemon/{README.html,style.css}

%post -n libdaemon0 -p /sbin/ldconfig

%postun -n libdaemon0 -p /sbin/ldconfig

%files -n libdaemon
%defattr (-,root,root)
%doc LICENSE 
%{_libdir}/libdaemon.so.0*

%files devel
%defattr (-,root,root)
%{_libdir}/libdaemon.so
%{_libdir}/pkgconfig/libdaemon.pc
%dir %{_includedir}/libdaemon
%{_includedir}/libdaemon/*.h

%changelog
