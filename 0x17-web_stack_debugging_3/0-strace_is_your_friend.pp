# This script fixes the web server changing a line in a config file

exec {'fix':
      command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
      path    => '/bin/',
}
