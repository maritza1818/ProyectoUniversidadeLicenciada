#!/xampp/perl/bin/perl.exe
use strict;
use warnings;
use CGI;
use Text::CSV;

# Crear objeto CGI
my $cgi = CGI->new;

# Imprimir encabezado HTTP
print $cgi->header('text/html;charset=UTF-8');

# Imprimir encabezado HTML
print $cgi->start_html('Resultados de la Búsqueda');
print $cgi->h1('Resultados de la Búsqueda');

# Obtener parámetros del formulario HTML
my $nombre_universidad = $cgi->param('nombre_universidad') || '';
my $departamento_local = $cgi->param('departamento_local') || '';

# Ruta al archivo CSV
my $csv_file = 'C:/xampp/htdocs/Programas de Universidades.csv';

# Crear objeto Text::CSV
my $csv = Text::CSV->new({ binary => 1, auto_diag => 1 });

# Abrir el archivo CSV
open my $fh, '<:encoding(utf8)', $csv_file or die "No se puede abrir el archivo '$csv_file': $!";

# Ignorar la primera línea (encabezados)
$csv->getline($fh);

# Imprimir tabla HTML
print "<table border='1'>";
print "<tr><th>Nombre Universidad</th><th>Periodo Licenciamiento</th><th>Departamento Local</th><th>Denominación Programa</th></tr>";

# Procesar las líneas restantes del archivo CSV
while (my $row = $csv->getline($fh)) {
    my ($nombre, $periodo, $departamento, $denominacion) = @$row;

    # Verificar si coincide con los parámetros de búsqueda
    if ($nombre =~ /$nombre_universidad/i && $departamento =~ /$departamento_local/i) {
        print "<tr><td>$nombre</td><td>$periodo</td><td>$departamento</td><td>$denominacion</td></tr>";
    }
}

# Cerrar el archivo CSV
close $fh;

# Cerrar tabla HTML y HTML
print "</table>";
print $cgi->end_html;
