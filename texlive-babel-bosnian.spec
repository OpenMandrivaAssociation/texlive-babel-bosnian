Name:		texlive-babel-bosnian
Version:	38174
Release:	2
Summary:	Babel contrib support for Bosnian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-bosnian
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bosnian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bosnian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bosnian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a language definition file that enables
support of Bosnian with babel.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-bosnian
%{_texmfdistdir}/tex/generic/babel-bosnian
%doc %{_texmfdistdir}/doc/generic/babel-bosnian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
