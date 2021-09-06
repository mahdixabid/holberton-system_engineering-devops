#creating a file using puppet.
file {'/tmp/holberton':
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}