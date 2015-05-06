Summary:	Library for performing comman tasks related to PAR recovery sets
Summary(pl.UTF-8):	Library for performing comman tasks related to PAR recovery sets
Name:		libpar2
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/parchive/%{name}-%{version}.tar.gz
# Source0-md5:	94c6df4e38efe08056ecde2a04e0be91
URL:		http://parchive.sourceforge.net/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libsigc++-devel
BuildRequires:  libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibPar2 allows for the generation, modification, verification, and
repair of PAR v1.0 and PAR v2.0(PAR2) recovery sets. It contains the
basic functions needed for working with these sets and is the basis
for GUI applications such as GPar2.

%description -l pl.UTF-8

%package devel
Summary:	Header files for libpar2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpar2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpar2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpar2.

%package static
Summary:	Static libpar2 library
Summary(pl.UTF-8):	Statyczna biblioteka libpar2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpar2 library.

%description static -l pl.UTF-8
Statyczna biblioteka libpar2.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/libpar2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README ROADMAP
%attr(755,root,root) %{_libdir}/libpar2.so.0
%attr(755,root,root) %{_libdir}/libpar2.so.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpar2.so
%{_includedir}/libpar2

%files static
%defattr(644,root,root,755)
%{_libdir}/libpar2.a
