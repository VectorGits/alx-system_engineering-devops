# This Script kills an already running script

exec { 'kill killmenow':
	command => 'pkill -f killmenow',
	path    => ['/bin', '/usr/bin'],
}
