# This script install flask and Werkzeug packages

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.0.1',
  provider => 'pip3',
}
