Name:           Automation
Version:        1.0
Release:        0
Summary:        Sample app
Group:          Applications/Multimedia
Prefix:         %{_prefix}
BuildRoot:      %{_tmppath}/%{name}-root

%description
Automation details

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/*

%changelog

In this file, under % prep section you may noticed the macro “%setup -q -n %{name}-%{version}”. This macro executes the following command in the background.

cd /usr/src/redhat/BUILD
rm -rf icecast
gzip -dc /usr/src/redhat/SOURCES/icecast-2.3.3.tar.gz | tar -xvvf -
if [ $? -ne 0 ]; then
  exit $?
fi
cd icecast
cd /usr/src/redhat/BUILD/icecast
chown -R root.root .
chmod -R a+rX,g-w,o-w .