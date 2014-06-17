#
# spec file for package chrome-grayscale-aurorae-theme
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


%define tarname 119168-chrome-grayscale
Name:           chrome-grayscale-aurorae-theme
Version:        0.95
Release:        1
Summary:        Chrome Grayscale Aurorae Theme
License:        GPL-2.0+
Group:          System/GUI/KDE
Source0:        %{tarname}.tar.gz
Source1:        LICENSE
Url:            http://kde-look.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:	kde4-filesystem
Requires:       kwin


%description
Clone of Chrome's grayscale theme. 

http://kde-look.org/content/show.php/Chrome+Grayscale+Aurorae?content=119168


%prep
%setup -q -c
cp -a %{SOURCE1} COPYING


%build


%install
mkdir -p %{buildroot}%{_kde4_appsdir}/aurorae/themes
cp -R chrome-grayscale %{buildroot}%{_kde4_appsdir}/aurorae/themes


%files
%defattr(-,root,root)
%doc COPYING
%dir %{_kde4_sharedir}
%dir %{_kde4_appsdir}
%dir %{_kde4_appsdir}/aurorae
%dir %{_kde4_appsdir}/aurorae/themes
%{_kde4_appsdir}/aurorae/themes/chrome-grayscale/


%changelog
* Tue Jun 17 2014 kamaradalinux@gmail.com
- Initial draft