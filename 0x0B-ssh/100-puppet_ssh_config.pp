# Modifies config file
file_line {
    'Private key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school'
}

file_line {
    'No password':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '    BatchMode yes'
}
