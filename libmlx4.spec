#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmlx4
Version  : 1.0.6
Release  : 2
URL      : https://www.openfabrics.org/downloads/mlx4/libmlx4-1.0.6.tar.gz
Source0  : https://www.openfabrics.org/downloads/mlx4/libmlx4-1.0.6.tar.gz
Summary  : Mellanox ConnectX InfiniBand HCA Userspace Driver
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
BuildRequires : libibverbs-dev

%description
libmlx4 provides a device-specific userspace driver for Mellanox
ConnectX HCAs for use with the libibverbs library.

%package dev
Summary: dev components for the libmlx4 package.
Group: Development
Provides: libmlx4-devel

%description dev
dev components for the libmlx4 package.


%prep
%setup -q -n libmlx4-1.0.6

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/*.so
