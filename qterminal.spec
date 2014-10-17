%define	git 20141017

Summary:	QT-based multitab terminal emulator
Name:		qterminal
Version:	0.4.1
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	1
Source0:	%{name}-%{name}-master.tar.gz
%endif
License:	GPLv2
Group:		Terminals
Url:		https://gitorious.org/qterminal
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist
BuildRequires:	cmake(qtermwidget5)
BuildRequires:	cmake(Qt5LinguistTools)

%description
Qt based multitab terminal emulator. 

%prep
%if %git
%setup -qn %{name}
%else
%setup -qn %{name}-%{name}
%endif
%apply_patches

%build
%cmake \
	-DUSE_QT5:BOOL=ON \
	-DUSE_SYSTEM_QXT:BOOL=OFF
# FIXME stop turning system Qxt off once it works with Qt5

%install
%makeinstall_std -C build
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}_drop.desktop

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_drop.desktop
%{_datadir}/pixmaps/%{name}.png
%lang(cs) %{_datadir}/%{name}/translations/%{name}_cs.qm
%lang(de) %{_datadir}/%{name}/translations/%{name}_de.qm
%lang(es) %{_datadir}/%{name}/translations/%{name}_es.qm
%lang(et) %{_datadir}/%{name}/translations/%{name}_et.qm
%lang(it) %{_datadir}/%{name}/translations/%{name}_it.qm
%lang(ru) %{_datadir}/%{name}/translations/%{name}_ru.qm
