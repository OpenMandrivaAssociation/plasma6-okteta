%define git 20241028
%define gitbranch work/kossebau/kf6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A simple HEX editor for KDE
Name:		plasma6-okteta
Version:	0.26.60
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/okteta/-/archive/%{gitbranch}/okteta-%{gitbranchd}.tar.bz2#/okteta-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/%{name}/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake(qca-qt6)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	pkgconfig(shared-mime-info)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Okteta is a simple editor for the raw data of files. This type of program
is also called hex editor or binary editor.

%files -f all.lang
%{_datadir}/applications/org.kde.okteta.desktop
%{_datadir}/okteta
%{_bindir}/okteta
%{_bindir}/struct2osd
%{_datadir}/knsrcfiles/okteta-structures.knsrc
%{_datadir}/metainfo/org.kde.okteta.appdata.xml
%{_datadir}/config.kcfg/structureviewpreferences.kcfg
%{_datadir}/mime/packages/okteta.xml
%{_iconsdir}/*/*/apps/okteta.png
%{_qtdir}/plugins/kf6/parts/oktetapart.so
%{_datadir}/qlogging-categories6/okteta.categories

#----------------------------------------------------------------------------

%define kasten4controllers_major 0
%define libkasten4controllers %mklibname Kasten5Controllers

%package -n %{libkasten4controllers}
Summary:	Okteta shared library
Group:		System/Libraries

%description -n %{libkasten4controllers}
Okteta shared library.

%files -n %{libkasten4controllers}
%{_libdir}/libKasten5Controllers.so.%{kasten4controllers_major}*

#----------------------------------------------------------------------------

%define kasten4core_major 0
%define libkasten4core %mklibname Kasten5Core

%package -n %{libkasten4core}
Summary:	Okteta shared library
Group:		System/Libraries

%description -n %{libkasten4core}
Okteta shared library.

%files -n %{libkasten4core}
%{_libdir}/libKasten5Core.so.%{kasten4core_major}*

#----------------------------------------------------------------------------

%define kasten4gui_major 0
%define libkasten4gui %mklibname Kasten5Gui

%package -n %{libkasten4gui}
Summary:	Okteta shared library
Group:		System/Libraries

%description -n %{libkasten4gui}
Okteta shared library.

%files -n %{libkasten4gui}
%{_libdir}/libKasten5Gui.so.%{kasten4gui_major}*

#----------------------------------------------------------------------------

%define kasten4okteta2controllers_major 0
%define libkasten4okteta2controllers %mklibname Kasten5Okteta3Controllers

%package -n %{libkasten4okteta2controllers}
Summary:	Okteta shared library
Group:		System/Libraries

%description -n %{libkasten4okteta2controllers}
Okteta shared library.

%files -n %{libkasten4okteta2controllers}
%{_libdir}/libKasten5Okteta3Controllers.so.%{kasten4okteta2controllers_major}*

#----------------------------------------------------------------------------

%define kasten4okteta2core_major 0
%define libkasten4okteta2core %mklibname Kasten5Okteta3Core

%package -n %{libkasten4okteta2core}
Summary:	Okteta shared library
Group:		System/Libraries

%description -n %{libkasten4okteta2core}
Okteta shared library.

%files -n %{libkasten4okteta2core}
%{_libdir}/libKasten5Okteta3Core.so.%{kasten4okteta2core_major}*

#----------------------------------------------------------------------------

%define kasten4okteta2gui_major 0
%define libkasten4okteta2gui %mklibname Kasten5Okteta3Gui

%package -n %{libkasten4okteta2gui}
Summary:	Okteta shared library
Group:		System/Libraries

%description -n %{libkasten4okteta2gui}
Okteta shared library.

%files -n %{libkasten4okteta2gui}
%{_libdir}/libKasten5Okteta3Gui.so.%{kasten4okteta2gui_major}*

#----------------------------------------------------------------------------

%define okteta3core_major 0
%define libokteta3core %mklibname Okteta4Core

%package -n %{libokteta3core}
Summary:	Okteta shared library
Group:		System/Libraries

%description -n %{libokteta3core}
Okteta shared library.

%files -n %{libokteta3core}
%{_libdir}/libOkteta4Core.so.%{okteta3core_major}*

#----------------------------------------------------------------------------

%define okteta3gui_major 0
%define libokteta3gui %mklibname Okteta4Gui

%package -n %{libokteta3gui}
Summary:	Okteta shared library
Group:		System/Libraries
Obsoletes:	%{mklibname okteta1gui 0} < 1:4.10.0
Obsoletes:	%{mklibname okteta1gui 1} < 1:14.12.0
Obsoletes:	%{mklibname okteta2gui 2} < 3:0.26.2

%description -n %{libokteta3gui}
Okteta shared library.

%files -n %{libokteta3gui}
%{_libdir}/libOkteta4Gui.so.%{okteta3gui_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Okteta
Group:		Development/KDE and Qt
Requires:	%{libkasten4controllers} = %{EVRD}
Requires:	%{libkasten4core} = %{EVRD}
Requires:	%{libkasten4gui} = %{EVRD}
Requires:	%{libkasten4okteta2controllers} = %{EVRD}
Requires:	%{libkasten4okteta2core} = %{EVRD}
Requires:	%{libkasten4okteta2gui} = %{EVRD}
Requires:	%{libokteta3core} = %{EVRD}
Requires:	%{libokteta3gui} = %{EVRD}

%description devel
This package includes the header files you will need to compile
applications that use Okteta libraries.

%files devel
%{_includedir}/*
%{_libdir}/libKasten5Controllers.so
%{_libdir}/libKasten5Core.so
%{_libdir}/libKasten5Gui.so
%{_libdir}/libKasten5Okteta3Controllers.so
%{_libdir}/libKasten5Okteta3Core.so
%{_libdir}/libKasten5Okteta3Gui.so
%{_libdir}/libOkteta4Core.so
%{_libdir}/libOkteta4Gui.so
%{_libdir}/qt6/plugins/designer/okteta4widgets.so
%{_libdir}/cmake/Okteta3Kasten5Gui
%{_libdir}/cmake/Okteta3Kasten5Core
%{_libdir}/cmake/Okteta3Kasten5Controllers
%{_libdir}/cmake/Okteta4Gui
%{_libdir}/cmake/Okteta4Core
%{_libdir}/cmake/Kasten5Gui
%{_libdir}/cmake/Kasten5Core
%{_libdir}/cmake/Kasten5Controllers
%{_libdir}/pkgconfig/Okteta4Core.pc
%{_libdir}/pkgconfig/Okteta4Gui.pc
%{_libdir}/qt6/mkspecs/modules/qt_Okteta4Core.pri
%{_libdir}/qt6/mkspecs/modules/qt_Okteta4Gui.pri

#----------------------------------------------------------------------------

%install -a
%find_lang libkasten
%find_lang liboktetacore
%find_lang liboktetagui
%find_lang liboktetakasten
%find_lang okteta --with-html
%find_lang oktetapart
cat *.lang | sort -u >all.lang
