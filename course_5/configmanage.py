# what are domain speficic languages(DSL)?
  # domain-specific language(DSL) : a programming language that's more limited in scope
'''
if $facts ['is_virtual'] {
    package {'smartmontools':
             ensure => purged,
             }
} else {
    package {'smartmontools':
             ensure => installed,
             }
}

About this code
This code block is a Puppet manifest, which is a configuration file used to manage systems using the Puppet automation framework.

The code you provided is an if statement. 
An if statement is a conditional statement that executes a block of code if a certain condition is met. 
In this case, the condition is whether the is_virtual fact is set to true. 
The is_virtual fact is a built-in fact that Puppet uses to determine if the node is a virtual machine.

If the is_virtual fact is set to true,
then the code in the if statement block will be executed.
This code will purge the smartmontools package. The smartmontools package is a software package that provides tools for monitoring and managing hard drives. 
Purging the smartmontools package on a virtual machine is typically done to improve performance.

If the is_virtual fact is set to false, then the code in the else statement block will be executed. 
This code will install the smartmontools package.

In this code block, the value of the is_virtual fact is true, 
so the code in the if statement block will be executed. 
This means that the smartmontools package will be purged.

what is a fact in Puppet? -> A variable representing characteristics of a system

'''
# the driving principles of connfiguration management
'''
file { '/etc/issue':
      mode => '0644',
      content => "Internal system \l \n",
      }

About this code
This resource ensures that the /etc/issue file has a set of permissions and a specific line in it.
Fulfilling this requirement is an idempotent operation. 
If the file already exists and has the desired content,
then Puppet will understand that no action has to be taken. 
If the file doesn't exist, then puppet will create it. '
'If the contents or permissions don't match,
Puppet will fix them. No matter how many times the agent applies the rule, 
the end result is that this file will have the requested contents and permissions. 

'''