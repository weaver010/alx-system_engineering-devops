# Script that fix the limits for user holberton
exec { 'userlimit':
  command  => "sed -i 's/holberton hard nofile 4/holberton hard nofile 65536/g' /etc/security/limits.conf",
  provider => shell,
}

-> exec { 'userlimit2':
  command  => "sed -i 's/holberton soft nofile 5/holberton soft nofile 65536/g' /etc/security/limits.conf",
  provider => shell,
}

-> exec { 'restart':
  command  => 'sysctl -p',
  provider => shell,
}
