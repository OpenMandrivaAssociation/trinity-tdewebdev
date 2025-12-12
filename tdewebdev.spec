%bcond clang 1
%bcond tdefilereplace 0

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tdewebdev
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Summary:	Web development applications
Group:		Applications/Editors
Version:	%{tde_version}
Release:	%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdesdk-devel >= %{tde_version}

BuildSystem:	  cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DFORCE_DEBUGGER -DWITH_DEBUGGER"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DBIN_INSTALL_DIR="%{tde_bindir}"
BuildOption:    -DDOC_INSTALL_DIR="%{tde_docdir}"
BuildOption:    -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}"
BuildOption:    -DLIB_INSTALL_DIR="%{tde_libdir}"
BuildOption:    -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig"
BuildOption:    -DSYSCONF_INSTALL_DIR="%{_sysconfdir}/trinity"
BuildOption:    -DSHARE_INSTALL_PREFIX="%{tde_datadir}"
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_QUANTA_CVSSERVICE=OFF
BuildOption:    -DBUILD_ALL=ON

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

# XSLT support
BuildRequires:  pkgconfig(libxslt)

# PERL support
BuildRequires:	perl

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)

# ICU support
BuildRequires:  pkgconfig(icu-i18n)

# Readline support
BuildRequires:	readline-devel

Obsoletes:	trinity-kdewebdev-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdewebdev-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdewebdev < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdewebdev = %{?epoch:%{epoch}:}%{version}-%{release}

Requires: trinity-quanta = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-quanta-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kimagemapeditor = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klinkstatus = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kommander = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Web development applications, including:
* kimagemapeditor: HTML image map editor
* klinkstatus: link checker
* kommander: visual dialog building tool
* quanta+: web development

%files
%defattr(-,root,root,-)

##########

%package -n trinity-quanta
Summary:	web development environment for TDE [Trinity]
Group:		Applications/Development
Requires:	trinity-tdefilereplace
Requires:	trinity-klinkstatus = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kommander = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-quanta-data = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:	trinity-kimagemapeditor = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	tidy

%description -n trinity-quanta
Quanta Plus is a web development environment for working with HTML
and associated languages. It strives to be neutral and transparent
to all markup languages, while supporting popular web-based scripting
languages, CSS and other emerging W3C recommendations.

Quanta Plus supports many external components, debuggers and other tools
for web development, several of which are shipped with the TDE web
development module.

Quanta Plus is not in any way affiliated with any commercial versions
of Quanta. The primary coders from the original team left the GPL'd
version to produce a commercial product.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-quanta
%defattr(-,root,root,-)
%{tde_bindir}/quanta
%{tde_tdelibdir}/quantadebuggerdbgp.la
%{tde_tdelibdir}/quantadebuggerdbgp.so
%{tde_tdelibdir}/quantadebuggergubed.la
%{tde_tdelibdir}/quantadebuggergubed.so
%{tde_tdeappdir}/quanta.desktop
%{tde_datadir}/apps/kafkapart
%{tde_datadir}/icons/hicolor/*/apps/quanta.png
%{tde_datadir}/mimelnk/application/x-webprj.desktop
%{tde_datadir}/services/quantadebuggerdbgp.desktop
%{tde_datadir}/services/quantadebuggergubed.desktop
%{tde_datadir}/services/quanta_preview_config.desktop
%{tde_datadir}/servicetypes/quantadebugger.desktop
%{tde_tdedocdir}/HTML/en/quanta/
%{tde_mandir}/man1/quanta.1*

##########

%package -n trinity-quanta-data
Summary:	data files for Quanta Plus web development environment [Trinity]
Group:		Applications/Development

%description -n trinity-quanta-data
This package contains architecture-independent data files for Quanta
Plus, a web development environment for working with HTML and associated
languages.

See the quanta package for further information.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-quanta-data
%defattr(-,root,root,-)
%{tde_datadir}/apps/quanta/

##########

%package -n trinity-kimagemapeditor
Summary:	HTML image map editor for TDE
Group:		Applications/Development

%description -n trinity-kimagemapeditor
KImageMapEditor is a tool that allows you to edit image maps in HTML
files. As well as providing a standalone application, KImageMapEditor
makes itself available as a KPart for embedding into larger applications.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-kimagemapeditor
%defattr(-,root,root,-)
%{tde_bindir}/kimagemapeditor
%{tde_tdelibdir}/libkimagemapeditor.la
%{tde_tdelibdir}/libkimagemapeditor.so
%{tde_tdeappdir}/kimagemapeditor.desktop
%{tde_datadir}/apps/kimagemapeditor/
%{tde_datadir}/icons/hicolor/*/apps/kimagemapeditor.png
%{tde_datadir}/icons/locolor/*/apps/kimagemapeditor.png
%{tde_datadir}/services/kimagemapeditorpart.desktop
%{tde_tdedocdir}/HTML/en/kimagemapeditor/
%{tde_mandir}/man1/kimagemapeditor.1*

##########

%package -n trinity-klinkstatus
Summary:	web link validity checker for TDE
Group:		Applications/Development

%description -n trinity-klinkstatus
KLinkStatus is TDE's web link validity checker. It allows you to
search internal and external links throughout your web site. Simply
point it to a single page and choose the depth to search.

You can also check local files, or files over ftp:, fish: or any other
KIO protocols. For performance, links can be checked simultaneously.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-klinkstatus
%defattr(-,root,root,-)
%{tde_bindir}/klinkstatus
%{tde_tdelibdir}/libklinkstatuspart.la
%{tde_tdelibdir}/libklinkstatuspart.so
%{tde_tdeappdir}/klinkstatus.desktop
%{tde_datadir}/apps/klinkstatus/
%{tde_datadir}/apps/klinkstatuspart/
%{tde_datadir}/config.kcfg/klinkstatus.kcfg
%{tde_datadir}/icons/hicolor/*/apps/klinkstatus.png
%{tde_datadir}/services/klinkstatus_part.desktop
%{tde_tdedocdir}/HTML/en/klinkstatus/
%{tde_mandir}/man1/klinkstatus.1*

##########

%package -n trinity-kommander
Summary:	visual dialog builder and executor tool [Trinity]
Group:		Applications/Development
Requires:	gettext

%description -n trinity-kommander
Kommander is a visual dialog building tool whose primary objective is
to create as much functionality as possible without using any scripting
language.

More specifically, Kommander is a set of tools that allow you to create
dynamic GUI dialogs that generate, based on their state, a piece of
text. The piece of text can be a command line to a program, any piece
of code, business documents that contain a lot of repetitious or
templated text and so on.

The resulting generated text can then be executed as a command line
program (hence the name "Kommander"), written to a file, passed to a
script for extended processing, and literally anything else you can
think of. And you aren't required to write a single line of code!

As well as building dialogs, Kommander may be expanded to create full
mainwindow applications.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-kommander
%defattr(-,root,root,-)
%{tde_bindir}/kmdr-editor
%{tde_bindir}/kmdr-executor
%{tde_bindir}/kmdr-plugins
%{tde_libdir}/libkommanderplugin.so.*
%{tde_libdir}/libkommanderwidgets.la
%{tde_libdir}/libkommanderwidget.so.*
%{tde_libdir}/libkommanderwidgets.so.*
%{tde_tdeappdir}/kmdr-editor.desktop
%{tde_datadir}/applnk/.hidden/kmdr-executor.desktop
%{tde_datadir}/apps/katepart/syntax/kommander.xml
%{tde_tdedocdir}/HTML/en/kommander/
%{tde_datadir}/icons/crystalsvg/*/apps/kommander.png
%{tde_datadir}/icons/hicolor/*/apps/kommander.png
%{tde_datadir}/mimelnk/application/x-kommander.desktop
%{tde_tdelibdir}/libkommander_part.so
%{tde_tdelibdir}/libkommander_part.la
%{tde_datadir}/apps/kommander/
%{tde_datadir}/apps/kmdr-editor/
%{tde_datadir}/apps/katepart/syntax/kommander-new.xml
%{tde_datadir}/apps/tdevappwizard/
%{tde_datadir}/services/kommander_part.desktop
%{tde_mandir}/man1/extractkmdr.1*
%{tde_mandir}/man1/kmdr-editor.1*
%{tde_mandir}/man1/kmdr-executor.1*
%{tde_mandir}/man1/kmdr-plugins.1*
%{tde_mandir}/man1/kmdr2po.1*

##########

%package -n trinity-kommander-devel
Summary:	development files for Kommander [Trinity]
Group:		Development/Libraries
Requires:	trinity-kommander = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kommander-devel
This package contains the headers and other development files for
building plugins or otherwise extending Kommander.

Kommander is a visual dialog building tool whose primary objective is
to create as much functionality as possible without using any scripting
language.

See the kommander package for further information.

This package is part of TDE, as a component of the TDE web development module.

%files -n trinity-kommander-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkommanderplugin.la
%{tde_libdir}/libkommanderplugin.so
%{tde_libdir}/libkommanderwidget.la
%{tde_libdir}/libkommanderwidget.so
%{tde_libdir}/libkommanderwidgets.so
%{tde_tdeincludedir}/kommander*
%{tde_tdeincludedir}/specials.h

##########

%if %{with tdefilereplace}

%package -n trinity-tdefilereplace
Summary:	Batch search-and-replace component for TDE
Group:		Applications/Utilities

Obsoletes:	trinity-kfilereplace < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kfilereplace = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdefilereplace
TDEFileReplace is an embedded component for TDE that acts as a batch
search-and-replace tool. It allows you to replace one expression with
another in many files at once.

Note that at the moment TDEFileReplace does not come as a standalone
application.

This package is part of Trinity, as a component of the TDE utilities module.

%files -n trinity-tdefilereplace
%defattr(-,root,root,-)
%{tde_bindir}/tdefilereplace
%{tde_tdelibdir}/libtdefilereplacepart.la
%{tde_tdelibdir}/libtdefilereplacepart.so
%{tde_tdeappdir}/tdefilereplace.desktop
%{tde_datadir}/apps/tdefilereplace/
%{tde_datadir}/apps/tdefilereplacepart/
%{tde_tdedocdir}/HTML/en/tdefilereplace/
%{tde_datadir}/icons/hicolor/*/apps/tdefilereplace.png
%{tde_datadir}/services/tdefilereplacepart.desktop
%{tde_mandir}/man1/tdefilereplace.1*

%endif

##########

%package devel
Group: Development/Libraries
Summary:	Header files and documentation for %{name} 

Obsoletes:	trinity-kdewebdev-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdewebdev-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:	trinity-tdelibs-devel >= %{tde_version}
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kommander-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%files devel


%prep -a
%if %{without kxsldbg}
%__rm -rf kxsldbg/ doc/kxsldbg/ doc/xsldbg/
%endif


%conf -p
unset QTDIR QTLIB QTINC
export PATH="%{tde_bindir}:${PATH}"


%install -a
## nothing handles the extraction of the sources provided in the 
## packaging directory
## package separately?  Why doesn't upstream include this? -- Rex
# install docs
# for i in css html javascript ; do
#    pushd $i
#    ./install.sh <<EOF
# %{buildroot}%{tde_datadir}/apps/quanta/doc
# EOF
#    popd
#    rm -rf $i
# done
# cp -a php php.docrc %{buildroot}%{tde_datadir}/apps/quanta/doc/

# Adds missing icons in 'hicolor' theme
%__mkdir_p %{buildroot}%{tde_datadir}/icons/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128}/apps/
pushd %{buildroot}%{tde_datadir}/icons
for i in {16,22,32,64,128}; do %__cp crystalsvg/"$i"x"$i"/apps/kommander.png  hicolor/"$i"x"$i"/apps/kommander.png  ;done
popd

# Unwanted icon
%__rm -f "%{buildroot}%{tde_datadir}/icons/crystalsvg/16x16/actions/bug.png"

