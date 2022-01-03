# Install a package with a puppet manifest
package {
  'puppet-lint':
  ensure  => installed,
  version => '2.5.0',
  hold    => true,
  source  => 'https://rubygems.org/'
}
