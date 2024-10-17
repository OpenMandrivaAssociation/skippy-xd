Summary:	A full screen pager for X11
Name:		skippy-xd
Version:	0.5.1
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0:	http://thegraveyard.org/files/%{name}-%{version}.tar.xz
Url:		https://thegraveyard.org/skippy.php
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xrender)

%description
A full screen pager for X11, not entirely unlike expocity and Apple's
Expose. It arranges snapshots of all windows on the current desktop,
allowing you to easily switch between applications. It doesn't require
a specific window manager, but requires NetWM compliance to work
( working with gnome, fluxbox, Metacity, KWin, IceWM, and others )

This version is using XRender, XComposite, XDamage and XFixes extensions.

%files
%doc skippy-xd.rc-default COPYING
%{_bindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
%make

%install
mkdir -p %{buildroot}/%{_bindir}/
cp %{name} %{buildroot}/%{_bindir}/

