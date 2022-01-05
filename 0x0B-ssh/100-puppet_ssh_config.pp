# Modifies config file
file_line {
    'Private key':
    ensure => present,
    path   => '~/.ssh/config',
    line   => '    IdentityFile ~/.ssh/school'
}
