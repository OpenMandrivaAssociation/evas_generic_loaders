%define gstapi 1.0

Summary:	Evas generic loaders
Name:		evas_generic_loaders
Version:	1.13.2
Release:	4
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		https://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/%{name}/%{name}-%{version}.tar.xz
Patch0:		evas_generic_loaders-1.11.2-include-raw.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(efl)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(zlib)

%description
These are additional "generic" loaders for Evas that are stand-alone
executables that evas may run from its generic loader module. This
means that if they crash, the application loading the image does not
crash also. In addition the licensing of these binaries will not
affect the license of any application that uses Evas as this uses a
completely generic execution system that allows anything to be plugged
in as a loader.

%files
%doc AUTHORS COPYING README
%{_libdir}/evas/utils

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure
%make

%install
%makeinstall_std
