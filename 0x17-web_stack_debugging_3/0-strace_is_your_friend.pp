# This script fixes the web server changing a line in a config file

include stdlib
file_line {
    'fix line on wp-settings.php':
    ensure => present,
    path   => '/var/www/html/wp-settings.php',
    line   => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
    match  => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
}
