# This script fixes the web server changing a line in a config file

include stdlib
exec {
    'fix line on wp-settings.php':
    onlyif  => 'test -e /var/www/html/wp-settings.php'
    command => "sed -i 's/phpp/php' /var/www/html/wp-settings.php",
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
