# We need to regenerate the HMAC values after the buildroot policies have
# mucked around with binaries.  This overrides the default which was in place
# at least from Red Hat Linux 9 through Fedora 11's development cycle.
%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	for length in 1 256 384 512 ; do \
		$RPM_BUILD_ROOT/%{_bindir}/sha${length}hmac -S > \\\
		$RPM_BUILD_ROOT/%{_libdir}/%{name}/sha${length}hmac.hmac \
	done \
	%{nil}

Name:		hmaccalc
Version:	0.9.14
Release:	11%{?dist}
Summary:	Tools for computing and checking HMAC values for files

Group:		System Environment/Base
License:	BSD
URL:		https://pagure.io/hmaccalc/
Source0:	https://releases.pagure.org/hmaccalc/hmaccalc-%{version}.tar.gz

BuildRequires:	nss-devel

%description
The hmaccalc package contains tools which can calculate HMAC (hash-based
message authentication code) values for files.  The names and interfaces are
meant to mimic the sha*sum tools provided by the coreutils package.

%prep
%setup -q

%build
%configure --enable-sum-directory=%{_libdir}/%{name}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%check
make check

%files
%defattr(-,root,root,-)
%license LICENSE
%doc README
%{_bindir}/sha1hmac
%{_bindir}/sha256hmac
%{_bindir}/sha384hmac
%{_bindir}/sha512hmac
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/sha1hmac.hmac
%{_libdir}/%{name}/sha256hmac.hmac
%{_libdir}/%{name}/sha384hmac.hmac
%{_libdir}/%{name}/sha512hmac.hmac
%{_mandir}/*/*

%changelog
* Tue Jan 17 2020 Nicolas Ontiveros <niontive@microsoft.com> - 0.9.14-11
- Initial CBL-Mariner import from Fedora 28.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.14-10
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 26 2017 Nalin Dahyabhai <nalin@redhat.com> - 0.9.14-6
- update locations to point to the new pagure.io hosting

* Wed Feb 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.9.14-5
- Add missing %%license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Nalin Dahyabhai <nalin@redhat.com>
- conditionalize that last change in case we end up having to use this .spec
  file on older releases
- resync with .spec file from Fedora master

* Thu Oct 29 2015 David Sommerseth <davids@redhat.com> - 0.9.14-3
- Remove prelink dependency, it is no longer available in newer Fedora releases

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 11 2014 Nalin Dahyabhai <nalin@redhat.com> - 0.9.14-1
- improve error reporting (part of #1162135)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Nalin Dahyabhai <nalin@redhat.com> - 0.9.13-2
- only BuildRequire: prelink on the arches on which we know it runs (currently
  %%{ix86}, x86_64, ppc, ppc64, s390, s390x), so that it can be built on the
  rest (#1061889)

* Mon Oct 14 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.9.13-1
- treat unexpected command-line arguments as an error to avoid setting
  incorrect expectations, and warn when a check file doesn't appear to
  contain anything for us to check (#1016706)

* Fri Aug  9 2013 Nalin Dahyabhai <nalin@redhat.com> - 0.9.12-7
- correct License: tag - it's closer to BSD (no advertising, 3 clause) than
  proper MIT (rcritten)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 15 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.12-1
- fix regression of #512275 -- we looked for prelink, but didn't record
  its location properly (#559458)

* Tue Sep  8 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.11-1
- error out when we previously skipped a check entry because the value to be
  checked is the wrong size
- fix estimation of the expected length for truncated values

* Thu Sep  3 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.10-1
- refuse to truncate output below half the size of the hash length, or 80
  bits, whichever is higher, in case we get used in a situation where
  not doing so would make us vulnerable to CVE-2009-0217, in which an
  attacker manages to convince a party doing verification to truncate
  both the just-computed value and the value to be checked before
  comparing them, as comparing just 1 bit would make detecting forgeries
  close to impossible

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.9-1
- look for prelink at compile-time, and if we find it try to invoke it
  using a full pathname before trying with $PATH (#512275)
- buildrequires: prelink so that it will be found at compile-time

* Tue Jun  9 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.8-1
- when checking, skip input lines which don't look like valid input lines

* Tue Jun  9 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.7-1
- add a binary (-b) mode when summing

* Wed Apr  8 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.6-1
- fix 'make check' by using binaries built with a different path for their
  own check files
- add a non-fips compile-time option, which we don't use

* Mon Mar 30 2009 Nalin Dahyabhai <nalin@redhat.com>
- handle '-' as indicating that stdin should be used for the input file

* Fri Mar 27 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.5-1
- add a -t option, for truncating HMAC outputs

* Wed Mar 25 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.4-1
- use a longer default key, when we use the default key

* Tue Mar 24 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.3-1
- fix the -k option
- move self-check files to %%{_libdir}/%%{name}

* Tue Mar 24 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.2-1
- provide a way to override the directory which will be searched for self-check
  values (part of #491719)

* Tue Mar 24 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9.1-1
- store self-check values in hex rather than in binary form (part of #491719)

* Tue Mar 24 2009 Nalin Dahyabhai <nalin@redhat.com> 0.9-2
- add URL to fedorahosted home page, and mention it in the man page as a means
  to report bugs and whatnot (part of #491719)
- correct the license tag: "X11" -> "MIT" (part of #491719)
- expand the acronym HMAC in the description (part of #491719)
- disable the sumfile prefix (part of #491719)

* Fri Mar 20 2009 Nalin Dahyabhai <nalin@redhat.com>
- initial .spec file
