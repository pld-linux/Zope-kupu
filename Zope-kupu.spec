%define 	zope_subname	kupu
Summary:	Kupu is a 'document-centric' open source client-side editor for web browsers
Summary(pl):	Kupu jest edytorem klienckim pracuj±cym z popularnymi przegl±darkami WWW
Name:		Zope-%{zope_subname}
Version:	1.3.1
Release:	1
License:	Kupu
Group:		Development/Tools
Source0:	http://kupu.oscom.org/midcom-serveattachmentguid-f40122579e491f7a7417987bef0c49ee/kupu-%{version}.tar.gz
# Source0-md5:	992cff3ccc2dc42a3e7c19344cf52dc4
Patch0:		%{name}-python_ver.patch
URL:		http://kupu.oscom.org/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-FileSystemSite >= 1.3
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kupu is a 'document-centric' open source client-side editor 
for Mozilla, Netscape and Internet Explorer.
This version kupu is only for Zope.

%description -l pl
Kupu jest edytorem klienckim pracuj±cym z popularnymi 
przegl±darkami WWW (Mozilla, Netscape and Internet Explorer).
Wersja dla Zope.

%prep
%setup -q -n %{zope_subname}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af {Extensions,apache-lenya,cnf,common,default,form,i18n,multi} \
    {plone,python,roundup,silva,tests,tools,widgeteer,zope2,zope3,*.zcml} \
    {*.py,*.kupu,*.gif,*.xsl,refresh.txt,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}


%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc doc/*
%{_datadir}/%{name}
