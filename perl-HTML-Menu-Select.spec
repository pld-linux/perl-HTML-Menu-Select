# TODO
# - Apache::Util::escape_html can't be used as it uses the xs symbol from apache module libperl.so
#   see apache1-mod_perl.spec.
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Menu-Select
Summary:	HTML::Menu::Select - Create HTML for select menus to simplify your templates
Summary(pl.UTF-8):	HTML::Menu::Select - tworzenie HTML-a dla list wyboru w celu uproszczenia szablonów
Name:		perl-HTML-Menu-Select
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7f465d6959e3ff0a647bd939c3ec7b96
URL:		http://search.cpan.org/dist/HTML-Menu-Select/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
#BuildRequires:	perl(Apache::Util)
BuildRequires:	perl-CGI-Simple
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This modules creates HTML for form select items.

This module allows you to quickly prototype a page, allowing the CGI
to completely generate the HTML, while allowing you at a later stage
to easily change how much HTML it generates.

%description -l pl.UTF-8
Ten moduł tworzy HTML dla elementów listy wyboru w formularzu.

Pozwala szybko stworzyć prototyp strony, generowanej w całości przez
CGI, a jednocześnie pozwala na późniejszym etapie zadecydować, jak
dużo HTML-a będzie generowane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# see note at start of spec
mv t/escapeHTML-Apache-Util.{t,invalid}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/HTML/Menu
%{perl_vendorlib}/HTML/Menu/Select.pm
%{_mandir}/man3/*
