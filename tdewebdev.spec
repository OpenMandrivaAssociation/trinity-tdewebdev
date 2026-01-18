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


Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdesdk-devel >= %{tde_version}

BuildSystem:	  cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DDOC_INSTALL_DIR=%{tde_prefix}/share/doc
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DSYSCONF_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_QUANTA_CVSSERVICE=OFF
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

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
%{tde_prefix}/bin/quanta
%{tde_prefix}/%{_lib}/trinity/quantadebuggerdbgp.la
%{tde_prefix}/%{_lib}/trinity/quantadebuggerdbgp.so
%{tde_prefix}/%{_lib}/trinity/quantadebuggergubed.la
%{tde_prefix}/%{_lib}/trinity/quantadebuggergubed.so
%{tde_prefix}/share/applications/tde/quanta.desktop
%{tde_prefix}/share/apps/kafkapart
%{tde_prefix}/share/icons/hicolor/*/apps/quanta.png
%{tde_prefix}/share/mimelnk/application/x-webprj.desktop
%{tde_prefix}/share/services/quantadebuggerdbgp.desktop
%{tde_prefix}/share/services/quantadebuggergubed.desktop
%{tde_prefix}/share/services/quanta_preview_config.desktop
%{tde_prefix}/share/servicetypes/quantadebugger.desktop
%{tde_prefix}/share/doc/tde/HTML/en/quanta/
%{tde_prefix}/share/man/man1/quanta.1*

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
%{tde_prefix}/share/apps/quanta/

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
%{tde_prefix}/bin/kimagemapeditor
%{tde_prefix}/%{_lib}/trinity/libkimagemapeditor.la
%{tde_prefix}/%{_lib}/trinity/libkimagemapeditor.so
%{tde_prefix}/share/applications/tde/kimagemapeditor.desktop
%{tde_prefix}/share/apps/kimagemapeditor/
%{tde_prefix}/share/icons/hicolor/*/apps/kimagemapeditor.png
%{tde_prefix}/share/icons/locolor/*/apps/kimagemapeditor.png
%{tde_prefix}/share/services/kimagemapeditorpart.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kimagemapeditor/
%{tde_prefix}/share/man/man1/kimagemapeditor.1*

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
%{tde_prefix}/bin/klinkstatus
%{tde_prefix}/%{_lib}/trinity/libklinkstatuspart.la
%{tde_prefix}/%{_lib}/trinity/libklinkstatuspart.so
%{tde_prefix}/share/applications/tde/klinkstatus.desktop
%{tde_prefix}/share/apps/klinkstatus/
%{tde_prefix}/share/apps/klinkstatuspart/
%{tde_prefix}/share/config.kcfg/klinkstatus.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/klinkstatus.png
%{tde_prefix}/share/services/klinkstatus_part.desktop
%{tde_prefix}/share/doc/tde/HTML/en/klinkstatus/
%{tde_prefix}/share/man/man1/klinkstatus.1*

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
%{tde_prefix}/bin/kmdr-editor
%{tde_prefix}/bin/kmdr-executor
%{tde_prefix}/bin/kmdr-plugins
%{tde_prefix}/%{_lib}/libkommanderplugin.so.*
%{tde_prefix}/%{_lib}/libkommanderwidgets.la
%{tde_prefix}/%{_lib}/libkommanderwidget.so.*
%{tde_prefix}/%{_lib}/libkommanderwidgets.so.*
%{tde_prefix}/share/applications/tde/kmdr-editor.desktop
%{tde_prefix}/share/applnk/.hidden/kmdr-executor.desktop
%{tde_prefix}/share/apps/katepart/syntax/kommander.xml
%{tde_prefix}/share/doc/tde/HTML/en/kommander/
%{tde_prefix}/share/icons/crystalsvg/*/apps/kommander.png
%{tde_prefix}/share/icons/hicolor/*/apps/kommander.png
%{tde_prefix}/share/mimelnk/application/x-kommander.desktop
%{tde_prefix}/%{_lib}/trinity/libkommander_part.so
%{tde_prefix}/%{_lib}/trinity/libkommander_part.la
%{tde_prefix}/share/apps/kommander/
%{tde_prefix}/share/apps/kmdr-editor/
%{tde_prefix}/share/apps/katepart/syntax/kommander-new.xml
%{tde_prefix}/share/apps/tdevappwizard/
%{tde_prefix}/share/services/kommander_part.desktop
%{tde_prefix}/share/man/man1/extractkmdr.1*
%{tde_prefix}/share/man/man1/kmdr-editor.1*
%{tde_prefix}/share/man/man1/kmdr-executor.1*
%{tde_prefix}/share/man/man1/kmdr-plugins.1*
%{tde_prefix}/share/man/man1/kmdr2po.1*

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
%{tde_prefix}/%{_lib}/libkommanderplugin.la
%{tde_prefix}/%{_lib}/libkommanderplugin.so
%{tde_prefix}/%{_lib}/libkommanderwidget.la
%{tde_prefix}/%{_lib}/libkommanderwidget.so
%{tde_prefix}/%{_lib}/libkommanderwidgets.so
%{tde_prefix}/include/tde/kommander*
%{tde_prefix}/include/tde/specials.h

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
%{tde_prefix}/bin/tdefilereplace
%{tde_prefix}/%{_lib}/trinity/libtdefilereplacepart.la
%{tde_prefix}/%{_lib}/trinity/libtdefilereplacepart.so
%{tde_prefix}/share/applications/tde/tdefilereplace.desktop
%{tde_prefix}/share/apps/tdefilereplace/
%{tde_prefix}/share/apps/tdefilereplacepart/
%{tde_prefix}/share/doc/tde/HTML/en/tdefilereplace/
%{tde_prefix}/share/icons/hicolor/*/apps/tdefilereplace.png
%{tde_prefix}/share/services/tdefilereplacepart.desktop
%{tde_prefix}/share/man/man1/tdefilereplace.1*

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
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
## nothing handles the extraction of the sources provided in the 
## packaging directory
## package separately?  Why doesn't upstream include this? -- Rex
# install docs
# for i in css html javascript ; do
#    pushd $i
#    ./install.sh <<EOF
# %{buildroot}%{tde_prefix}/share/apps/quanta/doc
# EOF
#    popd
#    rm -rf $i
# done
# cp -a php php.docrc %{buildroot}%{tde_prefix}/share/apps/quanta/doc/

# Adds missing icons in 'hicolor' theme
%__mkdir_p %{buildroot}%{tde_prefix}/share/icons/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128}/apps/
pushd %{buildroot}%{tde_prefix}/share/icons
for i in {16,22,32,64,128}; do %__cp crystalsvg/"$i"x"$i"/apps/kommander.png  hicolor/"$i"x"$i"/apps/kommander.png  ;done
popd

# Unwanted icon
%__rm -f "%{buildroot}%{tde_prefix}/share/icons/crystalsvg/16x16/actions/bug.png"

