%define	git 0

Summary:	QT-based multitab terminal emulator
Name:		qterminal
Version:	0.7.0
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	1
Source0:	https://github.com/lxde/qterminal/releases/download/%{version}/qterminal-%{version}.tar.xz
%endif
License:	GPLv2
Group:		Terminals
Url:		https://github.com/lxde/qterminal
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(qtermwidget5)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(lxqt)

%description
Qt based multitab terminal emulator.

%prep
%if %git
%setup -qn %{name}
%else
%setup -q
%endif
%apply_patches

%build
%cmake_qt5 -G Ninja

%ninja -C build

%install
%ninja_install -C build

%files
%doc AUTHORS NEWS README
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
