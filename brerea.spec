Name:           brerea
Version:        3.3.2
Release:        0%{?dist}
Summary:        BREReA - Background removal, registration and averaging

Group:          Education/Science
License:        GPLv2+
URL:            http://urchin.spbcas.ru
Source0:        %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires: gtk2-devel
BuildRequires: libglade2-devel
BuildRequires: gtkdatabox-devel >= 0.9.0
BuildRequires: autogen
BuildRequires: intltool
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig

Requires: gtk2
Requires: libglade2
Requires: gtkdatabox >= 0.9.0
Requires: gnuplot
Requires: perl

%description
BREReA - Software for background removal, registration and averaging of gene expression patterns.

%package devel
Summary:        BREReA development
Group:          Education/Science
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for BREReA - Software for background removal, registration and averaging of gene expression patterns.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

d=`pwd`
for f in qdata qdata-gui
	do
		cd $f
		autoreconf -f -i
		./configure --prefix=/usr --docdir=%{_docdir}/$f --libdir=%{_libdir}
		make DESTDIR=%{buildroot}
		make install DESTDIR=%{buildroot}
		cd $d
	done

#%find_lang qdata
#%find_lang qdata-gui

#cat qdata.lang qdata-gui.lang > brerea.lang

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/bgrem
%{_bindir}/brerea_waiter
%{_bindir}/dregpat
%{_bindir}/dsplextr
%{_bindir}/dwavex
%{_bindir}/gcpreg
%{_bindir}/gcpreg-extr
%{_bindir}/integrate
%{_bindir}/brerea
%{_bindir}/regpat
%{_bindir}/rgdata
%{_bindir}/splapp
%{_bindir}/splextr
%{_bindir}/wavex
%{_docdir}/qdata-gui
%{_docdir}/qdata
%{_libdir}/libafer.so
%{_libdir}/libafer.so.0
%{_libdir}/libafer.so.0.0.0
%{_libdir}/libfdk.a
%{_libdir}/libfdk.la
%{_libdir}/libfdk.so
%{_libdir}/libfdk.so.0
%{_libdir}/libfdk.so.0.0.0
%{_libdir}/libfrdwt.so
%{_libdir}/libfrdwt.so.0
%{_libdir}/libfrdwt.so.0.0.0
%{_libdir}/librct.so
%{_libdir}/librct.so.0
%{_libdir}/librct.so.0.0.0
%{_datadir}/applications/brerea.desktop
%{_datadir}/gcpreg-extr
%{_datadir}/brerea
%{_datadir}/pixmaps/brerea_icon.png

%files devel
%defattr(-,root,root,-)
%{_includedir}/qdata-afer
%{_includedir}/qdata-fdk
%{_includedir}/qdata-frdwt
%{_includedir}/qdata-rct
%{_libdir}/libafer.a
%{_libdir}/libafer.la
%{_libdir}/libfrdwt.a
%{_libdir}/libfrdwt.la
%{_libdir}/librct.a
%{_libdir}/librct.la

%changelog

* Mon May 30  2016 Konstantin Kozlov <kozlov_kn@spbstu.ru> - 3.3.2

- New version
