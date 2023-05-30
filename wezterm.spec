Name:           wezterm
Version:        0
Release:        8%{?dist}
Summary:        Wez's Terminal Emulator

License:        MIT
URL:            https://wezfurlong.org/wezterm/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc gcc-g++ make rustc, cargo, fontconfig-devel, openssl-devel, libxcb-devel, libxkbcommon-devel, libxkbcommon-x11-devel, wayland-devel, mesa-libEGL-devel, xcb-util-devel, xcb-util-keysyms-devel, xcb-util-image-devel, xcb-util-wm-devel

%description
wezterm is a terminal emulator with support for modern features
such as fonts with ligatures, hyperlinks, tabs and multiple
windows.


%prep
%autosetup
sed -i 's/# debug = 2/debug = 2/' Cargo.toml


%build
CARGO_REGISTRIES_CRATES_IO_PROTOCOL=sparse \
    cargo build --release --features distro-defaults -p wezterm-gui -p wezterm -p wezterm-mux-server -p strip-ansi-escapes


%install
mkdir -p %{buildroot}/usr/bin %{buildroot}/etc/profile.d
install -Dm755 assets/open-wezterm-here -t %{buildroot}/usr/bin
install -Dm755 target/release/wezterm -t %{buildroot}/usr/bin
install -Dm755 target/release/wezterm-mux-server -t %{buildroot}/usr/bin
install -Dm755 target/release/wezterm-gui -t %{buildroot}/usr/bin
install -Dm755 target/release/strip-ansi-escapes -t %{buildroot}/usr/bin
install -Dm644 assets/shell-integration/* -t %{buildroot}/etc/profile.d
install -Dm644 assets/shell-completion/zsh %{buildroot}/usr/share/zsh/site-functions/_wezterm
install -Dm644 assets/shell-completion/bash %{buildroot}/etc/bash_completion.d/wezterm
install -Dm644 assets/icon/terminal.png %{buildroot}/usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
install -Dm644 assets/wezterm.desktop %{buildroot}/usr/share/applications/org.wezfurlong.wezterm.desktop
install -Dm644 assets/wezterm.appdata.xml %{buildroot}/usr/share/metainfo/org.wezfurlong.wezterm.appdata.xml
install -Dm644 assets/wezterm-nautilus.py %{buildroot}/usr/share/nautilus-python/extensions/wezterm-nautilus.py


%files
%license LICENSE.md
%doc README.md
/usr/bin/open-wezterm-here
/usr/bin/wezterm
/usr/bin/wezterm-gui
/usr/bin/wezterm-mux-server
/usr/bin/strip-ansi-escapes
/usr/share/zsh/site-functions/_wezterm
/etc/bash_completion.d/wezterm
/usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
/usr/share/applications/org.wezfurlong.wezterm.desktop
/usr/share/metainfo/org.wezfurlong.wezterm.appdata.xml
/usr/share/nautilus-python/extensions/wezterm-nautilus.py*
/etc/profile.d/*


%changelog
* Tue May 30 2023 Tzuchieh Lin <zjlin@zjlin.org> 0-8
- merge upstream (c6f4ff362)

* Thu May 25 2023 Tzuchieh Lin <zjlin@zjlin.org> 0-7
- merge upstream (bb23d046)

* Sun May 21 2023 Tzuchieh Lin <zjlin@zjlin.org> 0-6
- merge upstream (2428282b)

* Sat May 20 2023 Tzuchieh Lin <zjlin@zjlin.org> 0-5
- merge upstream (4ae176dd)

* Tue May 16 2023 Tzuchieh Lin <zjlin@zjlin.org> 0-4
- merge upstream (76406e84)

* Sun May 14 2023 Tzuchieh Lin <zjlin@zjlin.org> 0-3
- merge upstream (bdb173f1)

* Fri May 12 2023 Tzuchieh Lin <zjlin@zjlin.org> 0-2
- fix: only build packaged bin (zjlin@zjlin.org)

* Fri May 12 2023 Tzuchieh Lin <zjlin@zjlin.org> 0-1
- new package built with tito

