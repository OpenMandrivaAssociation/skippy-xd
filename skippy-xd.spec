Name:		skippy-xd
Version: 0.5.0
Release:	%mkrel 6
License:	GPL
Group:		Graphical desktop/Other	
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	A full screen pager for X11
Source0:    http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
Url:		http://thegraveyard.org/skippy.php
BuildRequires: X11-devel >= 6.8

%description
A full screen pager for X11, not entirely unlike expocity and Apple's
Expose. It arranges snapshots of all windows on the current desktop,
allowing you to easily switch between applications. It doesn't require
a specific window manager, but requires NetWM compliance to work 
( working with gnome, fluxbox, Metacity, KWin, IceWM, and others )

This version is using XRender, XComposite, XDamage and XFixes extensions.

%prep
%setup -q 

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir/
cp %{name} $RPM_BUILD_ROOT/%_bindir/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG skippy-xd.rc-default COPYING
%_bindir/*



%changelog
* Sat Aug 06 2011 Götz Waschk <waschk@mandriva.org> 0.5.0-6mdv2012.0
+ Revision: 693429
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-5mdv2011.0
+ Revision: 260770
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-4mdv2009.0
+ Revision: 252545
- rebuild
- fix no-buildroot-tag
- kill extra spacing at top of description

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.5.0-2mdv2008.1
+ Revision: 127322
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import skippy-xd


* Mon May 09 2005 Frederic Crozat <fcrozat@mandriva.com> 0.5.0-2mdk 
- Fix buildrequires for x86-64

* Tue Jan 25 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5.0-1mdk 
- First mandrakelinux package, based on skippy package
