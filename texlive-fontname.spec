# revision 24661
# category Package
# catalog-ctan /info/fontname
# catalog-date 2010-10-25 08:39:19 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-fontname
Version:	20101025
Release:	2
Summary:	Scheme for naming fonts in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/fontname
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontname.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontname.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The scheme for assigning names is described (in the
documentation part of the package), and map files giving the
relation between foundry name and 'TeX-name' are also provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/fontname/adobe.map
%{_texmfdistdir}/fonts/map/fontname/apple.map
%{_texmfdistdir}/fonts/map/fontname/bitstrea.map
%{_texmfdistdir}/fonts/map/fontname/dtc.map
%{_texmfdistdir}/fonts/map/fontname/itc.map
%{_texmfdistdir}/fonts/map/fontname/linot-cd.map
%{_texmfdistdir}/fonts/map/fontname/linotype-cd.map
%{_texmfdistdir}/fonts/map/fontname/linotype.map
%{_texmfdistdir}/fonts/map/fontname/monotype.map
%{_texmfdistdir}/fonts/map/fontname/skey1250.map
%{_texmfdistdir}/fonts/map/fontname/skey1555.map
%{_texmfdistdir}/fonts/map/fontname/softkey-1250.map
%{_texmfdistdir}/fonts/map/fontname/softkey-1555.map
%{_texmfdistdir}/fonts/map/fontname/softkey.map
%{_texmfdistdir}/fonts/map/fontname/special.map
%{_texmfdistdir}/fonts/map/fontname/supplier.map
%{_texmfdistdir}/fonts/map/fontname/texfonts.map
%{_texmfdistdir}/fonts/map/fontname/typeface.map
%{_texmfdistdir}/fonts/map/fontname/urw.map
%{_texmfdistdir}/fonts/map/fontname/variant.map
%{_texmfdistdir}/fonts/map/fontname/weight.map
%{_texmfdistdir}/fonts/map/fontname/width.map
%{_texmfdistdir}/fonts/map/fontname/yandy.map
%doc %{_texmfdistdir}/doc/fonts/fontname/8a.html
%doc %{_texmfdistdir}/doc/fonts/fontname/8r.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Adobe-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Apple-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Bitstream-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/fontname/DTC-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Encodings.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Filenames-for-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Font-legalities.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Font-name-lists.html
%doc %{_texmfdistdir}/doc/fonts/fontname/History.html
%doc %{_texmfdistdir}/doc/fonts/fontname/ITC-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Introduction.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Linotype-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Long-names.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Long-naming-scheme.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Makefile
%doc %{_texmfdistdir}/doc/fonts/fontname/Monotype-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Name-mapping-file.html
%doc %{_texmfdistdir}/doc/fonts/fontname/References.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Standard-PostScript-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Suppliers.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Typefaces.html
%doc %{_texmfdistdir}/doc/fonts/fontname/URW-fonts.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Variants.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Weights.html
%doc %{_texmfdistdir}/doc/fonts/fontname/Widths.html
%doc %{_texmfdistdir}/doc/fonts/fontname/bitstrea.aka
%doc %{_texmfdistdir}/doc/fonts/fontname/cork.html
%doc %{_texmfdistdir}/doc/fonts/fontname/dvips.html
%doc %{_texmfdistdir}/doc/fonts/fontname/fontname.aux
%doc %{_texmfdistdir}/doc/fonts/fontname/fontname.cp
%doc %{_texmfdistdir}/doc/fonts/fontname/fontname.html
%doc %{_texmfdistdir}/doc/fonts/fontname/fontname.pdf
%doc %{_texmfdistdir}/doc/fonts/fontname/fontname.texi
%doc %{_texmfdistdir}/doc/fonts/fontname/fontname.toc
%doc %{_texmfdistdir}/doc/fonts/fontname/index.html
%doc %{_texmfdistdir}/doc/fonts/fontname/texmext.html
%doc %{_texmfdistdir}/doc/fonts/fontname/texmital.html
%doc %{_texmfdistdir}/doc/fonts/fontname/texmsym.html
%doc %{_texmfdistdir}/doc/fonts/fontname/texnansi.html
%doc %{_texmfdistdir}/doc/fonts/fontname/texnansx.html
%doc %{_texmfdistdir}/doc/fonts/fontname/xl2.html
%doc %{_texmfdistdir}/doc/fonts/fontname/xt2.html
%doc %{_infodir}/fontname.info*

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdir}/doc/info/*.info %{buildroot}%{_infodir}
