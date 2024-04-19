exec { 'kill killmenow':
	command => 'pkill -f killmenow',
	path    => ['/bin', '/usr/bin'],
}