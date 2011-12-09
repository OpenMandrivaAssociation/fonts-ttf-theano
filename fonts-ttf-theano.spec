%define pkgname theano

Summary:	Theano Classical Fonts
Name:		fonts-ttf-theano
Version:	2.0
Release:	%mkrel 1
License:	OFL
Group:		System/Fonts/True type
URL:		http://www.thessalonica.org.ru/en/fonts.html
Source0:	http://www.thessalonica.org.ru/downloads/%{pkgname}-%{version}.ttf.zip
BuildRequires:	freetype-tools
BuildRequires:	dos2unix
BuildArch:	noarch

%description
Theano is a common name for some fonts designed from historic samples. Most
of these fonts were initially intended as Greek-only faces, but currently
Theano fonts contain a standard set of Latin, Greek and Cyrillic characters
(including the full polytonic set for Greek) and some additional characters.
These fonts can be useful for classicists or medievalists.

%prep
%setup -q -c -n %{pkgname}-%{version}
dos2unix OFL-FAQ.txt

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/theano

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/theano
ttmkfdir %{buildroot}%{_xfontdir}/TTF/theano -o %{buildroot}%{_xfontdir}/TTF/theano/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/theano/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/theano \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-theano:pri=50

%files
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt
%dir %{_xfontdir}/TTF/theano
%{_xfontdir}/TTF/theano/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/theano/fonts.dir
%{_xfontdir}/TTF/theano/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-theano:pri=50
