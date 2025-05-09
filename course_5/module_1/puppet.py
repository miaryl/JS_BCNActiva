# what is Puppet?

'''
class sudo {
    package {'sudo':
             ensure => present,
    }
}
'''

# Puppet resources
  # Resources : the basic unit for modeling the configuration that we want to manage
'''
 ## introduction 
class sysctl {
    # make sure the directory exists, some distros don't have it
    file { '/etc/sysctl.d':
          ensure => directory,
    }
}

 ## about this code
class timezone {
    file {'/etc/timezone':
          ensure => file,
          content => "UTC\n",
          replace => true,
          }
}
'''

# Puppet clasees
'''
 ## introduction
class ntp {                                # network time protocol
    package {'mtp':
             ensure => latest,
    }
    file {'/etc/ntp.conf':
          source => 'puppet:///modules/ntp/ntp.conf'
          replace => true,
          }
    service {'ntp':
             enable => true,
             ensure => running,
             }
}
'''

# practice quiz
'''
what is the benefit of grouping resources into clasees when using Puppet? -> Providers can be specified.
what defines which provider will be used for a particular resource? -> Puppet assigns providers based on the resource type and data collected from the system.
inPuppet's file resource type, which attribute overwrites content that already exists? -> Replace
'''
