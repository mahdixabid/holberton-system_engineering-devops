# killing process using puppet
exec { "kill_process":
    command => 'pkill killmenow',
}