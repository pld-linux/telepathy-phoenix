Summary:	Telepathy Phoenix echo bot and tester
Summary(pl.UTF-8):	Telepathy Phoenix - echo-bot i program testujący
Name:		telepathy-phoenix
Version:	0.0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-phoenix/%{name}-%{version}.tar.gz
# Source0-md5:	5ecac1278371c7ce90ea2a62415b3aa1
Patch0:		%{name}-link.patch
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	farstream-devel
BuildRequires:	glib2-devel >= 1:2.30
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	telepathy-farstream-devel >= 0.1.0
BuildRequires:	telepathy-glib-devel >= 0.17.5
Requires:	glib2 >= 1:2.30
Requires:	telepathy-farstream >= 0.1.0
Requires:	telepathy-glib >= 0.17.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phoenix is a echo bot for the telepathy framework re-using the
standard Telepathy infrastructure. Mission control is used for the
account management, standard Telepathy clients are used for the echo
implementation.

%description -l pl.UTF-8
Phoenix to echo-bot dla szkieletu telepathy, wykorzystujący
standardową infrastrukturę Telepathy. Do zarządzania kontami
wykorzystywane jest Mission Control, a do implementacji echa posłużyli
standardowi klienci Telepathy.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# use own namespace
for f in phoenix phoenix-test; do
	mv $RPM_BUILD_ROOT%{_bindir}/${f} $RPM_BUILD_ROOT%{_bindir}/tp-${f}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/tp-phoenix
%attr(755,root,root) %{_bindir}/tp-phoenix-test
%attr(755,root,root) %{_libexecdir}/phoenix-approver
%attr(755,root,root) %{_libexecdir}/phoenix-authenticator
%attr(755,root,root) %{_libexecdir}/phoenix-echo-call
%attr(755,root,root) %{_libexecdir}/phoenix-echo-text
%{_datadir}/telepathy-phoenix
