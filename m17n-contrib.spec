Name:     m17n-contrib
Summary:  Contributed multilingualization datafiles for m17n-lib
Version:  1.1.10
Release:  3%{?dist}
Group:    System Environment/Libraries
License:  LGPLv2+
URL:      http://www.m17n.org/m17n-lib/index.html
Source0:  http://www.m17n.org/m17n-lib-download/m17n-contrib-%{version}.tar.gz
Source1:  mai-inscript.mim
Patch0:	  bug433416-bn-probhat.patch
Patch1:	  as-inscript-keysummary-440201.patch
Patch2:   ml-inscript-keysummary-435259.patch
Patch3:   kn-inscript-ZWNJ-440007.patch
Patch4:   or-inscript-ZWJ-ZWNJ-466748.patch
Patch5:   pa-jhelum-numeric-503478.patch
Patch6:   kn-kgp-halantha-ayogavaaha.patch
Patch7:   te-inscript-ZWJ-451203.patch
BuildArch: noarch
BuildRequires: m17n-db-devel >= 1.5.2-3
Requires: m17n-db >= 1.4.0
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package contains contributed multilingualization (m17n) datafiles
for the m17n-lib project.

# mk_pkg <name> <lang-code> <icons?1:0>
%define mk_pkg() \
%package %1\
Summary:    Contributed input maps for %(echo %1 | sed -e "s/\\(.*\\)/\\u\\1/")\
Group:      System Environment/Libraries\
# for %{_datadir}/m17n\
Requires:   m17n-contrib\
Obsoletes:  m17n-db-%1 < 1.4.0.1\
Obsoletes:  ibus-m17n-%1 < 0.1.1.20081013-3\
\
%description %1\
This package provides contributed multilingualization (m17n) input maps\
for %(echo %1 | sed -e "s/\\(.*\\)/\\u\\1/").\
\
%files %1\
%defattr(-,root,root,-)\
%{_datadir}/m17n/%2-*.mim\
%if %3\
%{_datadir}/m17n/icons/%2-*.png\
%else\
%{nil}\
%endif

%define mk_pkg_uses_db() \
%package %1\
Summary:    Contributed input maps for %(echo %1 | sed -e "s/\\(.*\\)/\\u\\1/")\
Group:      System Environment/Libraries\
# for %{_datadir}/m17n\
Requires:   m17n-contrib\
Requires:   m17n-db-%1 >= 1.4.0 \
Obsoletes:  ibus-m17n-%1 < 0.1.1.20081013-3\
\
%description %1\
This package provides contributed multilingualization (m17n) input maps\
for %(echo %1 | sed -e "s/\\(.*\\)/\\u\\1/").\
\
%files %1\
%defattr(-,root,root,-)\
%{_datadir}/m17n/%2-*.mim\
%if %3\
%{_datadir}/m17n/icons/%2-*.png\
%else\
%{nil}\
%endif

%mk_pkg_uses_db assamese as 1
%mk_pkg_uses_db bengali bn 1
%mk_pkg czech cs 1
%mk_pkg esperanto eo 1
%mk_pkg_uses_db gujarati gu 1
%mk_pkg_uses_db hindi hi 1
%mk_pkg_uses_db kannada kn 1
%mk_pkg kashmiri ks 0
%mk_pkg maithili mai 0
%mk_pkg_uses_db malayalam ml 1
%mk_pkg marathi mr 1
%mk_pkg nepali ne 1
%mk_pkg_uses_db oriya or 1
%mk_pkg pashto ps 1
%mk_pkg_uses_db punjabi pa 1
%mk_pkg_uses_db russian ru 0
%mk_pkg sindhi sd 1
%mk_pkg_uses_db sinhala si 0
%mk_pkg tai tai 0
%mk_pkg_uses_db tamil ta 1
%mk_pkg_uses_db telugu te 1
%mk_pkg urdu ur 1
%mk_pkg_uses_db vietnamese vi 1
%mk_pkg_uses_db chinese zh 1


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p0

%build
%configure
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -c -p"
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/m17n/

rm -rf $RPM_BUILD_ROOT/%{_bindir}

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_datadir}/m17n/scripts

%changelog
* Tue Jan 19 2010 Parag Nemade <pnemade AT redhat.com> -1.1.10-3
- Resolves: rh#556750: Add patch te-inscript-ZWJ-451203.patch

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1.10-2.1
- Rebuilt for RHEL 6 

* Mon Aug 17 2009 Parag Nemade <pnemade@redhat.com> -1.1.10-2
- Add patch kn-kgp-halantha-ayogavaaha.patch

* Wed Jul 29 2009 Parag Nemade <pnemade@redhat.com> -1.1.10-1
- update to new upstream release 1.1.10 
- Resolves: rh#513920: [pa_IN]Jhelum layout conflict with shortcut key in lokalize
- revert pa-jhelum-numeric-503478.patch to its original version.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-7
- update patch pa-jhelum-numeric-503478.patch

* Tue Jun 02 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-6
- Resolves: rh#503478-[pa_IN][Jhelum] layout need update for Gurmukhi Numeric

* Wed May 06 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-5
- Resolves: rh#485152- Kashmiri (Arabic-persian) language keyboard layout 

* Wed Apr 08 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-4
- Resolves: rh#494810-[indic][m17n-db][m17n-contrib] ibus .engine files no longer needed for new ibus

* Mon Apr 06 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-3
- Fix broken deps for maithili subpackage.

* Fri Apr 03 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-2
- Resolves: rh#491794 [mai_IN] Removing @maithili-support removes m17n-db-hindi package
- Resolves: rh#493793 [mai_IN] No default keymap for language

* Tue Mar 03 2009 Parag Nemade <pnemade@redhat.com> -1.1.9-1
- Update to new upstream release 1.1.9

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 05 2008 Parag Nemade <pnemade@redhat.com> -1.1.8-2.fc10
- Resolves: Bug 466748-[or_IN] Needed ZWJ & ZWNJ for Oriya Inscript keymap

* Tue Oct 21 2008 Parag Nemade <pnemade@redhat.com> -1.1.8-1.fc10
- Update to new upstream release 1.1.8

* Mon Oct 20 2008 Jens Petersen <petersen@redhat.com> - 1.1.7-5.fc10
- add obsoletes for ibus-m17n subpackages

* Wed Oct 15 2008 Parag Nemade <pnemade@redhat.com> - 1.5.2-4
- create .engine files for ibus-m17n with m17n-gen-ibus-engine (#466410)

* Thu Sep 04 2008 Parag Nemade <pnemade@redhat.com> -1.1.7-3
- Resolves: rh# Bug 458264-Required Inscript map for Sindhi language

* Fri Jul 04 2008 Parag Nemade <pnemade@redhat.com> -1.1.7-2
- Resolves: rh#453910: [kn_IN]Include latest kn- kgp.mim againist the latest build

* Thu Jul 03 2008 Parag Nemade <pnemade@redhat.com> -1.1.7-1
- Update to new upstream release 1.1.7

* Wed May 21 2008 Parag Nemade <pnemade@redhat.com> -1.1.6-4
- Resolves: rh#447682,rh#447683

* Wed Apr 02 2008 Parag Nemade <pnemade@redhat.com> -1.1.6-3.fc9
- Resolves: rh#440201,rh#435259,rh#440007

* Thu Feb 28 2008 Parag Nemade <pnemade@redhat.com> -1.1.6-2.fc9
- Resolves: rh#433416

* Thu Feb 07 2008 Parag Nemade <pnemade@redhat.com> -1.1.6-1.fc9
- Update to new upstream release 1.1.6
- Resolves: rh#431169

* Thu Jan 24 2008 Parag Nemade <pnemade@redhat.com> -1.1.5-2
- Resolves:rh#430054

* Mon Dec 31 2007 Parag Nemade <pnemade@redhat.com> -1.1.5-1.fc9
- Update to new upstream release 1.1.5

* Fri Dec 28 2007 Parag Nemade <pnemade@redhat.com> -1.1.4-1.fc9
- Update to new upstream release 1.1.4

* Tue Dec 18 2007 Parag Nemade <pnemade@redhat.com> -1.1.3-4.fc9
- Resolves: rh#404081, rh#419691

* Mon Aug 13 2007 Parag Nemade <pnemade@redhat.com>
- update License tag

* Wed Jul 25 2007 Parag Nemade <pnemade@redhat.com> - 1.1.3-3
- Added m17n-contrib as Requires for mk_pkg() macro generating packages.
- Added m17b-contrib and m17n-db-lang as Requires
  for mk_pkg_uses_db() macro generating packages.

* Wed Jul 25 2007 Parag Nemade <pnemade@redhat.com> - 1.1.3-2
- Import to cvs
- bump release

* Tue Jul 24 2007 Parag Nemade <pnemade@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Tue Jul 24 2007 Parag Nemade <pnemade@redhat.com>
- Bump release

* Mon Jul 23 2007 Parag Nemade <pnemade@redhat.com>
- SPEC cleanup
- make tbl2mim.awk executable
- bump release

* Mon Jul 23 2007 Parag Nemade <pnemade@redhat.com>
- updated SPEC according to suggestions from Jens Petersen in #249006

* Fri Jul 20 2007 Parag Nemade <pnemade@redhat.com> - 1.1.2-1
- Initial package for Fedora Review.
