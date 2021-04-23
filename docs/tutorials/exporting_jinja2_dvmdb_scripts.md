# FA-ZTP Tutorials: Exporting Jinja2 Configuration Script Output to Filesystem

[Back to README](../../README.md#table-of-contents)

[Back to Tutorials](TUTORIALS.md)

## Exporting Jinja2 Configuration Script Output to Filesystem

Rather than upload and execute rendered jinja2 FortiGate config scripts in FortiManager, it is possible to
simply export the rendered scripts to a file system as .conf files. 

We provide the **./ztp_steps/50.00_export-rendered-dvmdb-scripts-to-files.yml** playbook to accomplish this.

* It will read the rendered Fortigates
* It will rendered the Jinja2 DVMDB script templates like normal, but rather store them in YAML it processes them a bit more.
* It looks for distinct FortiGates and creates a folder structure under **{{role_path}}/files/tmp/exported_dvmdb_scripts/{{fortigate_name}}
* It creates a "source" folder to contain the many scripts that are generated.
* It then writes the scripts to these folders for each FortiGate.
* Then using the Ansible "assemble" module we can quickly concatenate these scripts into one 
  file under **{{ role_path }}/files/tmp/exported_dvmdb_scripts/{{fortigate_name}}/{{fortigate_name}}_AIO.conf
  
These "AIO.conf" files suitable for copy/paste directly into a FortiGate CLI for manual testing or deployment.

**This 'feature' does NOT account for any API-created objects in FortiManager such as address or service objects or policies**

It is assumed you know this solution well if you're using this feature. Use at your own risk.

[Back to Top](#table-of-contents)