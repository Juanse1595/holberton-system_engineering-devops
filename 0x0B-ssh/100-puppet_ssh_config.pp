# Modifies config file
file_line {
    'Private key':
    ensure => present,
    path   => '~/.ssh/config',
    line   => '    IdentityFile ~/.ssh/school'
}

file_line {
    'No password':
    ensure => present,
    path   => '~/.ssh/config',
    line   => '    BatchMode yes'
}
