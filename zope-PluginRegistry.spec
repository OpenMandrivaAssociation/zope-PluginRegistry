%define product		PluginRegistry
%define realVersion     1.1.1
%define release         1

%define version %(echo %{realVersion} | sed -e 's/-/./g')

%define zope_minver	2.7
%define plone_minver	2.0

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	PluginRegistry is a tool for Product developers to enable a pluggable architecture
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://www.zope.org/Products/PluginRegistry/PluginRegistry-%{version}/PluginRegistry-%{version}.tar.bz2
URL:		http://www.zope.org/Products/PluginRegistry
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	plone >= %{plone_minver}

Provides:	plone-Faq == %{version}
Obsoletes:	zope-Faq


%description
PluginRegistry is a tool for Product developers to enable a pluggable architecture.

%prep
%setup -c

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{product}-%{version} %{buildroot}%{software_home}/Products/%{product}


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(0644, root, root, 0755)
%{software_home}/Products/*

