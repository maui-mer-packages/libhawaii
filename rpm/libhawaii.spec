# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       libhawaii

# >> macros
# << macros

Summary:    Libraries for the Hawaii desktop environment
Version:    0.2.90
Release:    1
Group:      System/Libraries
License:    LGPLv2.1+
URL:        https://github.com/mauios/libhawaii.git
Source0:    libhawaii-%{version}.tar.xz
Source100:  libhawaii.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-default
BuildRequires:  qtconfiguration-devel

%description
Provides libraries for the Hawaii desktop environment.

%package devel
Summary:    Development files for Hawaii
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop plugins |
for Hawaii.


%package import-core
Summary:    Hawaii.Shell.Core plugin for QML
Group:      Development/System
Requires:   %{name} = %{version}-%{release}
Requires:   libhawaiishell = %{version}-%{release}

%description import-core
This package provides the Hawaii.Shell.Core plugin.

%package import-applications
Summary:    Hawaii.Shell.Applications plugin for QML
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description import-applications
This package provides the Hawaii.Shell.Applications plugin.

%package -n libhawaiishell
Summary:    Hawaii Shell library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libhawaiishell
Library for Hawaii Shell and its applications.

%package -n libhawaiishell-devel
Summary:    Development files for Hawaii Shell
Group:      Development/System
Requires:   %{name} = %{version}-%{release}
Requires:   libhawaii-devel = %{version}-%{release}
Requires:   qtconfiguration-devel

%description -n libhawaiishell-devel
This package contains the files necessary to develop applications |
that interact with Hawaii Shell.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libhawaiishell -p /sbin/ldconfig

%postun -n libhawaiishell -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.LIB README.md
%{_libdir}/libhawaii.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/hawaii/Hawaii/
%{_includedir}/hawaii/hawaii/
%{_libdir}/cmake/Hawaii/*.cmake
%{_libdir}/libhawaii.so
# >> files devel
# << files devel

%files import-core
%defattr(-,root,root,-)
%{_libdir}/hawaii/qml/Hawaii/Shell/Core/
# >> files import-core
# << files import-core

%files import-applications
%defattr(-,root,root,-)
%{_libdir}/hawaii/qml/Hawaii/Shell/Applications/
# >> files import-applications
# << files import-applications

%files -n libhawaiishell
%defattr(-,root,root,-)
%{_libdir}/libhawaiishell.so.*
# >> files -n libhawaiishell
# << files -n libhawaiishell

%files -n libhawaiishell-devel
%defattr(-,root,root,-)
%{_includedir}/hawaii/HawaiiShell/
%{_includedir}/hawaii/hawaiishell/
%{_libdir}/cmake/HawaiiShell/*.cmake
%{_libdir}/libhawaiishell.so
# >> files -n libhawaiishell-devel
# << files -n libhawaiishell-devel
