# $Id$
# Authority: dag

Summary: MPEG library for SDL
Name: smpeg
Version: 0.4.4
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://icculus.org/smpeg/
Source: ftp://sunsite.dk/pub/os/linux/loki/open-source/smpeg/smpeg-%{version}.tar.gz
Patch0: smpeg-0.4.4-gcc32.patch
Patch1: smpeg-0.4.4-fixes.patch
Patch2: smpeg-0.4.4-PIC.patch
Patch3: smpeg-0.4.4-gnu-stack.patch
Patch4: smpeg-0.4.4-m4.patch
Patch5: smpeg-0.4.4-gcc41.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, gtk+-devel, gcc-c++
BuildRequires: autoconf, automake, automake14

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. SMPEG has
completed the initial work to wed these two projects in order to 
create a general purpose MPEG video/audio player for the Linux OS. 


%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%setup
%patch0 -p0 -b .gcc32
%patch1 -p0 -b .fixes
%patch2 -p0 -b .PIC
%patch3 -p1 -b .gnu-stack
%patch4 -p1 -b .m4
%patch5 -p1 -b .gcc41


%build
%{__automake} -a || %{__automake}-1.4 -a
%{__autoconf}
%configure \
    --disable-opengl-player
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README TODO
%{_bindir}/plaympeg
%{_bindir}/gtv
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/smpeg-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4


%changelog
* Wed Jan 18 2006 Matthias Saou <http://freshrpms.net/> 0.4.4-1
- Include patch from Gentoo to fix compilation with gcc 4.1 (FC5).
- Also include nice PIC, gnu stack and m4 patches from Gentoo.

* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 0.4.4-0
- Initial package. (using DAR)

