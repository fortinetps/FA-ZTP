# FA-ZTP Steps

[Back to README](../../README.md#table-of-contents)

[Back to Reference](REFERENCE.md)

## 00.01_import-spreadsheet.yml

* Passes var **spreadsheet_path** which tells the role where to look for the import data.
* Generates FortiGate YAML files under **{{ role_path }}/vars/fortigates/**
* Uses Python script at **{{ role_path}}/files/python/consume_branch_spreadsheet.py** to parse the spreadsheet to YAML files.
  * Python script also does the conversion from the Organizational Workflow Data Model (spreadsheet) to the Ansible
    ZTP Role Data Model (FortiGate YAML files).
    
[Back to Top](#fa-ztp-steps)

## 00.10_render-fortigate-templates.yml

* Converges Ansible ZTP Role Defaults with the FortiGate YAML files under 
  **{{ role_path }}/vars/fortigates/**
* Uses Jinja2 template **{{ role_path }}/templates/fortigates/spreadsheet_fgt_merge.j2**
    
    
[Back to Top](#fa-ztp-steps)

## 00.11_validate-rendered-fortigate-templates.yml

* Reads rendered FortiGates.
* Validates rendered FortiGates using Python Schema
* Python Schema @ **{{ role_path }}/files/python/ansible_ztp_role_data_model/fortigate_schema.py**
    
[Back to Top](#fa-ztp-steps)

## 00.15_render-dvmdb-scripts.yml

* Reads rendered FortiGates.
* For each FortiGate it renders each of the Jinja2 templates @ **{{ role_path }}/templates/dvmdb_scripts/**
* Each rendered script is stored in memory until all of them are rendered.
* After all rendering is done the scripts are stored as a list of dictionaries, converted to YAML, 
  and written @ **{{ role_path }}/files/tmp/dvmdb_scripts/rendered_dvmdb_scripts.yml**.
* If you want to export these as actual files -- edit the task **templates/render_dvmdb_scripts.yml**
    
[Back to Top](#fa-ztp-steps)

## 00.20_read-rendered-fortigates.yml

* Reads the rendered FortiGates.
* Used by many, many other playbooks on this list.
    
[Back to Top](#fa-ztp-steps)

## 00.21_read-rendered-policies-as-flattened.yml

* Reads the rendered Policies as a flattened list of dictionaries.
* These dictionaries contain the policy, as well as the policy package name, if its global or adom, etc.
* This "flattened" list of dictionaries is the easist to process in Ansible
* Like **00.20_read-rendered-fortigates.yml** this file is used often by other playbooks on this list.
    
[Back to Top](#fa-ztp-steps)

## 00.28_ensure-adom-in-fmg.yml

* Reads the rendered FortiGates.
* Reads the Target ADOMs for FortiGates, and Global Policy Packages.
* Ensures the ADOMs actually exist.
* Will cause an error if ADOMs do not exist and will tell you what's wrong.
    
[Back to Top](#fa-ztp-steps)

## 00.29_ensure-policy-packages.yml

* Reads the rendered FortiGates.
* For each distinct Policy Package Name, it adds them to FortiManager if they don't already exist
    
[Back to Top](#fa-ztp-steps)

## 00.30_ensure-service-groups.yml

* Reads the rendered FortiGates.
* For each distinct service object and service group, it adds them to FortiManager if they don't already exist
    
[Back to Top](#fa-ztp-steps)

## 00.31_ensure-address-groups.yml

* Reads the rendered FortiGates.
* For each distinct address object and address group, it adds them to FortiManager if they don't already exist
    
[Back to Top](#fa-ztp-steps)

## 00.32_ensure-device-groups.yml

* Reads the rendered FortiGates.
* For each distinct FortiGate device group, it adds them to FortiManager if they don't already exist
    
[Back to Top](#fa-ztp-steps)

## 00.33_ensure-security-profiles.yml

* Reads the rendered FortiGates.
* For each distinct security profile of any type (AV/AppControl/IPS/etc), if the name of that profile
  does not exist it will create it in FortiManager.
* We do not provide the means to define these security profiles specific details in this role. 
  That is something that would have to be customized.
* It is recommended if you use security profiles in firewall policies, that the security profiles be pre-configured.
    
[Back to Top](#fa-ztp-steps)


## 01.01_add-rendered-fortigates.yml

* Reads the rendered FortiGates.
* Adds the rendered FortiGates to the target FortiManager ADOM.
    
[Back to Top](#fa-ztp-steps)

## 01.02_add-fortigates-to-device-groups.yml

* Reads the rendered FortiGates.
* Adds the FortiGates to their specific device groups.
    
[Back to Top](#fa-ztp-steps)

## 01.03_process-rendered-dvmdb-scripts.yml

* Reads the rendered FortiGates.
* Reads the rendered DVMDB config scripts.
* Uploads the rendered DVMDB config scripts.
* Executes the rendered DVMDB config scripts -- keeps track of the FortiManager Task ID.
* Queries the FortiManager Task IDs until they are done.
* If all script executions were successful, the DVMDB config scripts are deleted.
  * If not successful -- they are left on FortiManager for inspection.
    
[Back to Top](#fa-ztp-steps)

## 01.04_map-interfaces-by-device.yml

* Reads the rendered FortiGates.
* Uses Jinja2 to render a list of "normalized interfaces" to assign in FortiManager.
* Adds any "normalized interfaces" that are not defined in FortiManager yet.
* Adds the "normalized interface dynamic mappings" that are generated via Jinja2 template.
    
[Back to Top](#fa-ztp-steps)

## 01.05_map-sdwan-zones-by-device.yml

* Reads the rendered FortiGates.
* Uses Jinja2 to render a list of SDWAN "normalized interfaces" to assign in FortiManager.
* Adds any SDWAN "normalized interfaces" that are not defined in FortiManager yet.
* Adds the SDWAN "normalized interface dynamic mappings" that are generated via Jinja2 template.
    
[Back to Top](#fa-ztp-steps)

## 01.08_add-wan-address-objects.yml

* Reads the rendered FortiGates.
* Adds Address Objects for WAN interfaces
* Adds address object dynamic mappings for WAN interfaces that are not DHCP.
    
[Back to Top](#fa-ztp-steps)

## 01.09_add-vlan-address-objects.yml

* Reads the rendered FortiGates.
* Adds Address Objects for VLAN Interfaces
* Adds dynamic mappings from each FortiGate to Address Objects
    
[Back to Top](#fa-ztp-steps)

## 01.10_add-adom-policy-package-rules.yml

* Reads the flattened list of firewall policies, from rendered FortiGates.
* For non-global policies it attempts to add them to the proper policy package.
* If a policy by the same name already exists it is skipped.
    
[Back to Top](#fa-ztp-steps)

## 01.12_assign-policy-packages.yml

* Reads rendered FortiGates.
* Assigns ADOM Policy Packages to FortiGates.
    
[Back to Top](#fa-ztp-steps)

## 01.14_assign-system-templates.yml

* Reads rendered FortiGates.
* Assigns system templates ("Provisioning Templates" in GUI speak) to FortiGates.
    
[Back to Top](#fa-ztp-steps)

## 02.10_install-fgt-settings.yml

* Reads rendered FortiGates.
* Tells FortiManager to commit all device setting changes to the FortiGates configuration.
    
[Back to Top](#fa-ztp-steps)

## 02.11_install-fgt-policy-packages.yml

* Reads rendered FortiGates.
* Tells FortiManager to commit all policy packages to the FortiGates configuration.
    
[Back to Top](#fa-ztp-steps)

## 800.12_unassign-policy-packages.yml

* Reads rendered FortiGates.
* Unassigns policy pacakges
    
[Back to Top](#fa-ztp-steps)

## 800.13_unassign-system-templates.yml

* Reads rendered FortiGates.
* Unassigns system templates.
    
[Back to Top](#fa-ztp-steps)

## 900.00.debug-role-device-inventory.yml

* Reads rendered FortiGates.
* Prints the rendered FortiGates to screen/terminal. 
    
[Back to Top](#fa-ztp-steps)

## 900.04_debug-ansible-facts.yml

* Reads rendered FortiGates.
* Prints the ansible facts to screen/terminal.
    
[Back to Top](#fa-ztp-steps)

## 900.05_get-fmgr-policy-packages.yml

* Reads rendered FortiGates.
* Gets all policy packages from the role-default ADOM in FortiManager -- referenced in the rendered FortiGates.
    
[Back to Top](#fa-ztp-steps)

## 900.06_get-fmgr-policy-package-rules.yml

* Reads rendered FortiGates.
* Gets the policy
    
[Back to Top](#fa-ztp-steps)

## 900.11_debug-rendered-dvmdb-scripts.yml

* Reads rendered FortiGates.
* Reads rendered DVMDB scripts.
* Uploads DVMDB scripts to FortiManager and leaves them there for inspection.
    
[Back to Top](#fa-ztp-steps)

## 900.12_DEBUG-get-policy-security-profiles.yml

* Reads rendered FortiGates.
* Tests the Jinja2 template **{{ role_path }}/templates/policy_packages/get_security_profiles.j2**
* Prints output to screen.
    
[Back to Top](#fa-ztp-steps)

## 999.80_DELETE-dvmdb-script.yml

* Reads rendered FortiGates.
* Deletes any DVMDB scripts from FortiManager that were added by the role.
    
[Back to Top](#fa-ztp-steps)

## 999.90_DELETE-rendered-fortigates.yml

* Reads rendered FortiGates.
* Deletes rendered FortiGates from target FortiManager.
    
[Back to Top](#fa-ztp-steps)

## 999.99_RESET-role-to-default.yml

* Deletes the contents of the folders:
  * {{ role_path }}/files/tmp
  * {{ role_path }}/vars/fortigates
  
Removes all imported FortiGates and deleting all rendered tmp files.
    
[Back to Top](#fa-ztp-steps)

## 999.100_DEV-ONLY-Remove-and-Reset-Everything.yml

* Reads the rendered FortiGates.
* Attempts to delete the rendered FortiGates from the target FortiManager.
* Attempts to delete the rendered DVMDB scripts from the target Fortimanager.
* Runs the playbook **999.99_RESET-role-to-default.yml** after deleting its content from the target Fortimanager.

    
[Back to Top](#fa-ztp-steps)
