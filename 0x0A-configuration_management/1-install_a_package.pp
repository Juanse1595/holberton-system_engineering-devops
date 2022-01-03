# Install a package with a puppet manifest
package {
  'puppet-lint':
  ensure => '2.5.0',
  source => 'https://rubygems.org/'
}
