%global tl_name fontname
%global tl_revision 75544

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Scheme for naming fonts in TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/fontname
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontname.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontname.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The scheme for assigning names is described (in the documentation part
of the package), and map files giving the relation between foundry name
and 'TeX-name' are also provided.

