# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-Keepalive

Summary: Manage connections, with keep-alive
Name: perl-POE-Component-Client-Keepalive
Version: 0.0701
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-Keepalive/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCAPUTO/POE-Component-Client-Keepalive-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
POE::Component::Client::Keepalive creates and manages connections for
other components.  It maintains a cache of kept-alive connections for
quick reuse.  It is written specifically for clients that can benefit
from kept-alive connections, such as HTTP clients.  Using it for one-
shot connections would probably be silly.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/POE/Component/Client/Keepalive.pm
%{perl_vendorlib}/POE/Component/Connection/Keepalive.pm

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.0701-1
- Updated to release 0.0701.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
