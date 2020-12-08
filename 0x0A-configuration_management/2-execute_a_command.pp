# Kill a process
exec { 'pkill':
    command => 'pkill -f killmenow'
}
