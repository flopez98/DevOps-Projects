add-content -path c:\users\2LoudMusic\.ssh\config -value @'

Host ${hostname}
  HostName ${hostname}
  User ${user}
  IdentityFile ${identityfile}
'@