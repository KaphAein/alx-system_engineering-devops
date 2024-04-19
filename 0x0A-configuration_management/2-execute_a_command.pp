# File: kill_process.pp

exec { 'kill_killmenow_process':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}