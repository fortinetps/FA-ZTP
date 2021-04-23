FortiGate Ansible ZTP (FA-ZTP)
===============================

The FortiGate Ansible Zero-Touch-Provisioning (FA-ZTP) Role is a toolset for deploying FortiGates
through the FortiManager API. It is designed to help shape organizational workflows by providing 
pre-configured examples of each step in the process, but it is also a great learning tool
for Ansible and the FortiGate ZTP process.

Every step is clearly defined in the Ansible Role Tasks and supporting playbooks, and any step can be 
changed to meet organizational workflow needs. 

There are also data models to help explain the actual
FortiGate configuration data entities themselves, and how the Ansible role restructures this data to perform the ZTP operations.

It is not as fully-featured as some of Fortinet's other Professional Services Solutions (such as FortiProvision),
but it can help "bridge the gap" for organizations with the desire and resources to develop their own solutions.

It goes without saying that everything that this role does can be accomplished with the FortiManager GUI, however,
we have had overwhelming feedback from our customers who want to use Ansible.

Requirements
------------

* A FortiManager instance (v6.4+ is preferred, v7.0 is not yet tested).
* At least one FortiGate (physical or VM, v6.4+ is preferred, v7.0 is not yet tested).
  * Used to verify FortiManager configs -- can easily wipe/reset to test.
* FortiSwitches and FortiAPs are supported when attached to a FortiGate configuration.
* An Ubuntu 18/20 LTS Desktop Workstation.
* Jetbrains PyCharm Community Edition 2021.1+

Dependencies
------------

See requirements.txt in the repo this role came with.

License
-------

BSD

Author Information
------------------

Luke Weighall - Github: @lweighall
Fortinet Core CSE DevOps, 2021. - Github: @ftntcorecse

