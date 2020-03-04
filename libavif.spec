%bcond_with aom

Name:           libavif
Version:        0.5.7
Release:        1%{?dist}
Summary:        Library for encoding and decoding .avif files
License:        BSD
Group:          Development/Libraries/C and C++
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
    %{_builddir}/%{name}-%{version}
make %{?_smp_mflags}
popd

%install
pushd obj
make %{?_smp_mflags} DESTDIR=%{buildroot} install
popd

%ldconfig_scriptlets

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
* Wed Mar 04 2020 Andreas Schneider <asn@redhat.com> - 0.5.7-1
- Update to version 0.5.7

* Wed Mar 04 2020 Andreas Schneider <asn@redhat.com> - 0.5.3-2
- Fix License

* Sun Feb 16 2020 Andreas Schneider <asn@redhat.com> - 0.5.3-1
- Initial version
