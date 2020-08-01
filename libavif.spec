%bcond_with aom

Name:           libavif
Version:        0.7.3
Release:        3%{?dist}
Summary:        Library for encoding and decoding .avif files
License:        BSD
Url:            https://github.com/AOMediaCodec/libavif

Source0:        https://github.com/AOMediaCodec/libavif/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  nasm
BuildRequires:  pkgconfig(dav1d)
%if %{with aom}
BuildRequires:  pkgconfig(aom)
%endif
BuildRequires:  pkgconfig(rav1e)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

%package devel
Requires:       %{name} = %{version}-%{release}
Summary:        Development files for libavif

%description devel
This package holds the development files for libavif.

%package tools
Summary:        Tools for libavif

%description tools
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the commandline tools for libavif.

%prep
%autosetup -p1

%build
mkdir -p obj
pushd obj
%cmake \
    -DAVIF_CODEC_RAV1E:BOOL=ON \
    -DAVIF_CODEC_DAV1D:BOOL=ON \
    %if %{with aom}
    -DAVIF_CODEC_AOM:BOOL=ON \
    %endif
    -DAVIF_BUILD_APPS:BOOL=ON \
    -DAVIF_BUILD_EXAMPLES:BOOL=ON \
    ..
%make_build
popd

%install
%make_install -C obj

%files
%license LICENSE
%{_libdir}/libavif.so.*

%files devel
%license LICENSE
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/
%{_libdir}/pkgconfig/libavif.pc

%files tools
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/avifdec
%{_bindir}/avifenc

%changelog
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
