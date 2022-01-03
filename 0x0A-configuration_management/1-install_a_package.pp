# Install a package with a puppet manifest
package {
  'puppet-lint':
  ensure => '2.5.0',
  name   => 'puppet-lint',
  source => 'https://rubygems.org/',
}
