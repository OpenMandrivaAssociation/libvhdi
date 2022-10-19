%global sname	vhdi

%global	major 1
%global libname		%mklibname %{sname}
%global develname	%mklibname %{sname} -d
%global pyname		python-py%{sname}


%bcond_without	python
%bcond_without	libfuse
# unpackaged yet
%bcond_with		libbfio
%bcond_with		libcdata
%bcond_with		libcerror
%bcond_with		libcfile
%bcond_with		libclocale
%bcond_with		libcnotify
%bcond_with		libcpath
%bcond_with		libcsplit
%bcond_with		libcthreads
%bcond_with		libfcache
%bcond_with		libfdata
%bcond_with		libfguid
%bcond_with		libuna

Summary: 	Library and tools to access the Virtual Hard Disk (VHD) image format
Name:		lib%{sname}
Version:	20210425
Release:	1
License:	LGPLv3+ and GPLv3+
Group:		File tools
URL:		https://github.com/libyal/%{name}
Source0:	https://github.com/libyal/%{name}/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	pkgconfig(fuse)

%{?with_python:
BuildRequires:	pkgconfig(python3)
}

%description
libvhdi is a library to access the Virtual Hard Disk image format.

Read supported formats:

* Virtual Hard Disk version 1 (VHD)
* Virtual Hard Disk version 2 (VHDX)

Supported image types:

* Fixed-size hard disk image
* Dynamic-size (or sparse) hard disk image
* Differential (or differencing) hard disk image
* Note that an undo disk image (.vud) is also a differential image

#---------------------------------------------------------------------------

%package -n %{sname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{sname}
libvhdi is a library to access the Virtual Hard Disk image format.

Read supported formats:

* Virtual Hard Disk version 1 (VHD)
* Virtual Hard Disk version 2 (VHDX)

Supported image types:

* Fixed-size hard disk image
* Dynamic-size (or sparse) hard disk image
* Differential (or differencing) hard disk image
* Note that an undo disk image (.vud) is also a differential image

This package provides some useful tools.

%files -n %{sname}
%license COPYING COPYING.LESSER
%{_bindir}/%{sname}info
%{_bindir}/%{sname}mount
%{_mandir}/man1/%{sname}info.1.*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
The %libname package contains library for %{name}.

%files -n %{libname}
%{_libdir}/lib%{sname}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

%files -n %{develname}
%license COPYING COPYING.LESSER
%doc AUTHORS NEWS README
%{_includedir}/lib%{sname}/
%{_includedir}/lib%{sname}.h
%{_libdir}/lib%{sname}.so
%{_libdir}/pkgconfig/lib%{sname}.pc
%{_mandir}/man3/lib%{sname}.3.zst*

#---------------------------------------------------------------------------

%{?with_python:
%package -n %{pyname}
Summary:        Python binding for the %{name}
Group:          Development/Libraries

%description -n %{pyname}
Python3 bindings for %name.

%files -n %{pyname}
%license COPYING COPYING.LESSER
%{py_platsitedir}/py%{sname}.so
#%%{py_platsitedir}/py%{sname}-*-py%{py_ver}.egg-info
}

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-python2 \
	--enable-wide-character-type \
	%{?with_python:--enable-python3}%{!?with_python:--disable-python3} \
	%{?with_libbfio:--enable-libbfio}%{!?with_libbfio:--disable-libbfio} \
	%{?with_libcdata:--enable-libcdata}%{!?with_libcdata:--disable-libcdata} \
	%{?with_libcerror:--enable-libcerror}%{!?with_libcerror:--disable-libcerror} \
	%{?with_libcfile:--enable-libcfile}%{!?with_libcfile:--disable-libcfile} \
	%{?with_libclocale:--enable-libclocale}%{!?with_libclocale:--disable-libclocale} \
	%{?with_libcnotify:--enable-libcnotify}%{!?with_libcnotify:--disable-libcnotify} \
	%{?with_libcpath:--enable-libcpath}%{!?with_libcpath:--disable-libcpath} \
	%{?with_libcsplit:--enable-libcsplit}%{!?with_libcsplit:--disable-libcsplit} \
	%{?with_libcthreads:--enable-libcthreads}%{!?with_libcthreads:--disable-libcthreads} \
	%{?with_libfcache:--enable-libfcache}%{!?with_libfcache:--disable-libfcache} \
	%{?with_libfdata:--enable-libfdata}%{!?with_libfdata:--disable-libfdata} \
	%{?with_libfguid:--enable-libfguid}%{!?with_libfguid:--disable-libfguid} \
	%{?with_libfuse:--enable-libfuse}%{!?with_libfuse:--disable-libfuse} \
	%{?with_libuna:--enable-python3}%{!?with_libuna:--disable-libuna}
%make_build

%install
%make_install

