%define gstapi	0.10

Summary:	Evas generic loaders
Name:		evas_generic_loaders
Version:	1.7.7
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://trac.enlightenment.org/e/wiki/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(eina) >= 1.7.0
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(poppler)

%description
These are additional "generic" loaders for Evas that are stand-alone
executables that evas may run from its generic loader module. This
means that if they crash, the application loading the image does not
crash also. In addition the licensing of these binaries will not
affect the license of any application that uses Evas as this uses a
completely generic execution system that allows anything to be plugged
in as a loader.

This package is part of the Enlightenment DR17 desktop shell.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_libdir}/evas/utils

