Name:		skippy-xd
Version:    0.5.0
Release:	7
License:	GPL
Group:		Graphical desktop/Other	
Summary:	A full screen pager for X11
Source0:    http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
Url:		http://thegraveyard.org/skippy.php
BuildRequires: pkgconfig(x11)

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
mkdir -p %{buildroot}/%{_bindir}/
cp %{name} %{buildroot}/%{_bindir}/

%files
%doc CHANGELOG skippy-xd.rc-default COPYING
%{_bindir}/*
