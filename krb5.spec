Summary:	Kerberos network authentication syste
Name:		krb5
Version:	1.12.1
Release:	3
License:	MIT
Group:		Networking
Source0:	http://web.mit.edu/kerberos/dist/krb5/1.12/%{name}-%{version}-signed.tar
# Source0-md5:	524b1067b619cb5bf780759b6884c3f5
Patch0:		%{name}-LDFLAGS.patch
BuildRequires:	libcom_err-devel
BuildRequires:	openldap-devel
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kerberos is a network authentication protocol. It is designed to
provide strong authentication for client/server applications by using
secret-key cryptography. A free implementation of this protocol is
available from the Massachusetts Institute of Technology.

%package libs
Summary:	Kerberos libraries
Group:		Libraries

%description libs
Kerberos libraries.

%package devel
Summary:	Header files for Kerberos libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for Kerberos
libraries.

%prep
%setup -qc
tar -xf %{name}-%{version}.tar.gz
mv %{name}-%{version}/src/* .

%{__sed} -i "/KRB5ROOT=/s/\/local//" util/ac_check_krb5.m4

%build
%configure \
	--disable-rpath		\
	--enable-dns-for-realm	\
	--with-ldap		\
	--with-system-et	\
	--without-tcl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
# TODO: split server, client and add systemd services
%attr(755,root,root) %{_bindir}/gss-client
%attr(755,root,root) %{_bindir}/k5srvutil
%attr(755,root,root) %{_bindir}/kadmin
%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/ksu
%attr(755,root,root) %{_bindir}/kswitch
%attr(755,root,root) %{_bindir}/ktutil
%attr(755,root,root) %{_bindir}/kvno
%attr(755,root,root) %{_bindir}/sclient
%attr(755,root,root) %{_bindir}/sim_client
%attr(755,root,root) %{_bindir}/uuclient
%attr(755,root,root) %{_sbindir}/gss-server
%attr(755,root,root) %{_sbindir}/kadmin.local
%attr(755,root,root) %{_sbindir}/kadmind
%attr(755,root,root) %{_sbindir}/kdb5_ldap_util
%attr(755,root,root) %{_sbindir}/kdb5_util
%attr(755,root,root) %{_sbindir}/kprop
%attr(755,root,root) %{_sbindir}/kpropd
%attr(755,root,root) %{_sbindir}/kproplog
%attr(755,root,root) %{_sbindir}/krb5-send-pr
%attr(755,root,root) %{_sbindir}/krb5kdc
%attr(755,root,root) %{_sbindir}/sim_server
%attr(755,root,root) %{_sbindir}/sserver
%attr(755,root,root) %{_sbindir}/uuserver

%dir %{_libdir}/krb5
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/db2.so
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/kldap.so
%attr(755,root,root) %{_libdir}/krb5/plugins/preauth/otp.so
%attr(755,root,root) %{_libdir}/krb5/plugins/preauth/pkinit.so

%{_mandir}/man1/k5srvutil.1*
%{_mandir}/man1/kadmin.1*
%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/krb5-config.1*
%{_mandir}/man1/krb5-send-pr.1*
%{_mandir}/man1/ksu.1*
%{_mandir}/man1/kswitch.1*
%{_mandir}/man1/ktutil.1*
%{_mandir}/man1/kvno.1*
%{_mandir}/man1/sclient.1*
%{_mandir}/man5/.k5identity.5
%{_mandir}/man5/.k5login.5
%{_mandir}/man5/k5identity.5*
%{_mandir}/man5/k5login.5*
%{_mandir}/man5/kadm5.acl.5*
%{_mandir}/man5/kdc.conf.5*
%{_mandir}/man5/krb5.conf.5*
%{_mandir}/man8/kadmin.local.8
%{_mandir}/man8/kadmind.8*
%{_mandir}/man8/kdb5_ldap_util.8*
%{_mandir}/man8/kdb5_util.8*
%{_mandir}/man8/kprop.8*
%{_mandir}/man8/kpropd.8*
%{_mandir}/man8/kproplog.8*
%{_mandir}/man8/krb5kdc.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgssapi_krb5.so.2
%attr(755,root,root) %ghost %{_libdir}/libgssrpc.so.4
%attr(755,root,root) %ghost %{_libdir}/libk5crypto.so.3
%attr(755,root,root) %ghost %{_libdir}/libkadm5clnt_mit.so.9
%attr(755,root,root) %ghost %{_libdir}/libkadm5srv_mit.so.9
%attr(755,root,root) %ghost %{_libdir}/libkdb5.so.7
%attr(755,root,root) %ghost %{_libdir}/libkdb_ldap.so.1
%attr(755,root,root) %ghost %{_libdir}/libkrad.so.0
%attr(755,root,root) %ghost %{_libdir}/libkrb5.so.3
%attr(755,root,root) %ghost %{_libdir}/libkrb5support.so.0
%attr(755,root,root) %ghost %{_libdir}/libverto.so.0
%attr(755,root,root) %{_libdir}/libgssapi_krb5.so.*.*
%attr(755,root,root) %{_libdir}/libgssrpc.so.*.*
%attr(755,root,root) %{_libdir}/libk5crypto.so.*.*
%attr(755,root,root) %{_libdir}/libkadm5clnt_mit.so.*.*
%attr(755,root,root) %{_libdir}/libkadm5srv_mit.so.*.*
%attr(755,root,root) %{_libdir}/libkdb5.so.*.*
%attr(755,root,root) %{_libdir}/libkdb_ldap.so.*.*
%attr(755,root,root) %{_libdir}/libkrad.so.*.*
%attr(755,root,root) %{_libdir}/libkrb5.so.*.*
%attr(755,root,root) %{_libdir}/libkrb5support.so.*.*
%attr(755,root,root) %{_libdir}/libverto.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krb5-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/gssapi
%{_includedir}/gssrpc
%{_includedir}/kadm5
%{_includedir}/krb5
%{_pkgconfigdir}/*.pc
