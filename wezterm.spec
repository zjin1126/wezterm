Name:           wezterm
Version:        0.0.0
Release:        0%{?dist}
Summary:        Wez's Terminal Emulator.

License:        MIT
URL:            https://wezfurlong.org/wezterm/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  rustc, cargo, fontconfig-devel, openssl-devel, libxcb-devel, libxkbcommon-devel, libxkbcommon-x11-devel, wayland-devel, mesa-libEGL-devel, xcb-util-devel, xcb-util-keysyms-devel, xcb-util-image-devel, xcb-util-wm-devel
#Requires:       

%description
wezterm is a terminal emulator with support for modern features
such as fonts with ligatures, hyperlinks, tabs and multiple
windows.


%prep
%autosetup


%build
CARGO_REGISTRIES_CRATES_IO_PROTOCOL=sparse cargo build --all --release


%install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
