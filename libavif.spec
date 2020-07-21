# Force out of source build
%undefine __cmake_in_source_build

%bcond_without aom

Name:       libavif
Version:    0.8.0
Release:    1%{?dist}
Summary:    Library for encoding and decoding .avif files

License:    BSD
URL:        https://github.com/AOMediaCodec/libavif
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Patches to fix avif-pixbuf-loader bugs in latest release
Patch0:     https://github.com/AOMediaCodec/libavif/commit/9759bc7346802faa8ec96bb38456d8b8170580aa.patch#/0001-Fix-a-crash-in-the-gdk-pixbuf-loader-when-error-is-NULL.patch
Patch1:     https://github.com/AOMediaCodec/libavif/commit/61ec9835d0a0110e48346cb98ed095e29be19077.patch#/0002-Fix-a-crash-in-the-gdk-pixbuf-loader-removed-unnecessary-asserts.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  nasm
%if %{with aom}
BuildRequires:  pkgconfig(aom)
%endif
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(rav1e)
BuildRequires:  pkgconfig(zlib)

%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

%package devel
Summary:        Development files for libavif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package holds the development files for libavif.

%package tools
Summary:        Tools to encode and decode AVIF files

%description tools
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the commandline tools to encode and decode AVIF files.

%package     -n avif-pixbuf-loader
Summary:        AVIF image loader for GTK+ applications
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
Requires:       gdk-pixbuf2

%description -n avif-pixbuf-loader
Avif-pixbuf-loader contains a plugin to load AVIF images in GTK+ applications.

%prep
%autosetup -p1

%build
%cmake  %{?with_aom:-DAVIF_CODEC_AOM=1} \
        -DAVIF_CODEC_DAV1D=1 \
        -DAVIF_CODEC_RAV1E=1 \
        -DAVIF_BUILD_APPS=1 \
        -DAVIF_BUILD_GDK_PIXBUF=1
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libavif.so.5*

%files devel
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/
%{_libdir}/pkgconfig/libavif.pc

%files tools
%doc CHANGELOG.md README.md
%{_bindir}/avifdec
%{_bindir}/avifenc

%files -n avif-pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-avif.so

%changelog
* Wed Aug 05 21:17:23 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-1
- Update to 0.8.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3

* Wed Apr 29 2020 Andreas Schneider <asn@redhat.com> - 0.7.2-1
- Update to version 0.7.2
  * https://github.com/AOMediaCodec/libavif/blob/master/CHANGELOG.md

* Wed Apr 29 2020 Andreas Schneider <asn@redhat.com> - 0.7.1-1
- Update to version 0.7.1

* Wed Mar 04 2020 Andreas Schneider <asn@redhat.com> - 0.5.7-1
- Update to version 0.5.7

* Wed Mar 04 2020 Andreas Schneider <asn@redhat.com> - 0.5.3-2
- Fix License

* Sun Feb 16 2020 Andreas Schneider <asn@redhat.com> - 0.5.3-1
- Initial version
