# Creates a manifest that kills a process named killmenow
exec {
  'killing':
  command => 'pkill -f killmenow',
  provider => shell,
}
