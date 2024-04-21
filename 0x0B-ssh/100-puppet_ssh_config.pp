# Client config file w/ puppet

file { '/home/ubuntu/.ssh':
  ensure => 'directory',
  mode   => '0700',
}

file { '/home/ubuntu/.ssh/config':
  ensure => 'present',
  mode   => '0600',
}

file_line { 'Declare identity file':
  path => '/home/ubuntu/.ssh/config',
  line => 'IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
  path => '/home/ubuntu/.ssh/config',
  line => 'PasswordAuthentication no',
}
