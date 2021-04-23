# FA-ZTP Tutorials: Debugging the Ansible ZTP Role

[Back to README](../../README.md#table-of-contents)

[Back to Tutorials](TUTORIALS.md)

## Using the Debug_Ansible_ZTP.yml Playbook

Just as the name of the file implies this is a tool for debugging the entire Ansible ZTP Role.

When opened you will notice it contains the same "- import_playbook: " statements as the **Ansible_ZTP_AIO.yml** playbook.
Except most of them are commented out.

You can use this playbook to comment/uncomment any ztp_step playbook that is required to debug whatever you want to debug.

For example, use this configuration to debug the import of the spreadsheet and rendering/validation of that data. 
We were recently making changes to the python schema for the Ansible ZTP Data Model, which
is why this debug playbook is in this configuration.

```python

- import_playbook: ./ztp_steps/00.01_import-spreadsheet.yml
- import_playbook: ./ztp_steps/00.10_render-fortigate-templates.yml
- import_playbook: ./ztp_steps/00.11_validate-rendered-fortigate-templates.yml
#- import_playbook: ./ztp_steps/00.15_render-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/00.28_ensure-adom-in-fmg.yml
#- import_playbook: ./ztp_steps/00.29_ensure-policy-packages.yml
#- import_playbook: ./ztp_steps/00.30_ensure-service-groups.yml
#- import_playbook: ./ztp_steps/00.31_ensure-address-groups.yml
#- import_playbook: ./ztp_steps/00.32_ensure-device-groups.yml
#- import_playbook: ./ztp_steps/00.33_ensure-security-profiles.yml
#- import_playbook: ./ztp_steps/00.34_ensure-system-templates.yml
#- import_playbook: ./ztp_steps/01.01_add-rendered-fortigates.yml
#- import_playbook: ./ztp_steps/01.02_add-fortigates-to-device-groups.yml
#- import_playbook: ./ztp_steps/01.03_process-rendered-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/01.04_map-interfaces-by-device.yml
#- import_playbook: ./ztp_steps/01.05_map-sdwan-zones-by-device.yml

#- import_playbook: ./ztp_steps/01.08_add-wan-address-objects.yml
#- import_playbook: ./ztp_steps/01.09_add-vlan-address-objects.yml
#- import_playbook: ./ztp_steps/01.10_add-adom-policy-package-rules.yml
#- import_playbook: ./ztp_steps/01.12_assign-policy-packages.yml
#- import_playbook: ./ztp_steps/01.14_assign-system-templates.yml
#- import_playbook: ./ztp_steps/02.10_install-fgt-settings.yml
#- import_playbook: ./ztp_steps/02.11_install-fgt-policy-packages.yml


#- import_playbook: ./ztp_steps/900.11_debug-rendered-dvmdb-scripts.yml

```

... but what about other scenarios?


## Debugging DVMDB Jinja2 Script Templates

Let's say you make some changes to the Jinja2 templates for the DVMDB scripts. 

You could debug them using this configuration:

```python

- import_playbook: ./ztp_steps/00.01_import-spreadsheet.yml
- import_playbook: ./ztp_steps/00.10_render-fortigate-templates.yml
- import_playbook: ./ztp_steps/00.11_validate-rendered-fortigate-templates.yml
- import_playbook: ./ztp_steps/00.15_render-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/00.28_ensure-adom-in-fmg.yml
#- import_playbook: ./ztp_steps/00.29_ensure-policy-packages.yml
#- import_playbook: ./ztp_steps/00.30_ensure-service-groups.yml
#- import_playbook: ./ztp_steps/00.31_ensure-address-groups.yml
#- import_playbook: ./ztp_steps/00.32_ensure-device-groups.yml
#- import_playbook: ./ztp_steps/00.33_ensure-security-profiles.yml
#- import_playbook: ./ztp_steps/00.34_ensure-system-templates.yml
#- import_playbook: ./ztp_steps/01.01_add-rendered-fortigates.yml
#- import_playbook: ./ztp_steps/01.02_add-fortigates-to-device-groups.yml
#- import_playbook: ./ztp_steps/01.03_process-rendered-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/01.04_map-interfaces-by-device.yml
#- import_playbook: ./ztp_steps/01.05_map-sdwan-zones-by-device.yml

#- import_playbook: ./ztp_steps/01.08_add-wan-address-objects.yml
#- import_playbook: ./ztp_steps/01.09_add-vlan-address-objects.yml
#- import_playbook: ./ztp_steps/01.10_add-adom-policy-package-rules.yml
#- import_playbook: ./ztp_steps/01.12_assign-policy-packages.yml
#- import_playbook: ./ztp_steps/01.14_assign-system-templates.yml
#- import_playbook: ./ztp_steps/02.10_install-fgt-settings.yml
#- import_playbook: ./ztp_steps/02.11_install-fgt-policy-packages.yml

- import_playbook: ./ztp_steps/900.11_debug-rendered-dvmdb-scripts.yml

```

This will import/render/validate the FortiGates, and then render the DVMDB scripts and upload them to FortiManager for you to inspect.

Or you can do it without re-importing FortiGate data:

```python

#- import_playbook: ./ztp_steps/00.01_import-spreadsheet.yml
#- import_playbook: ./ztp_steps/00.10_render-fortigate-templates.yml
#- import_playbook: ./ztp_steps/00.11_validate-rendered-fortigate-templates.yml
- import_playbook: ./ztp_steps/00.15_render-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/00.28_ensure-adom-in-fmg.yml
#- import_playbook: ./ztp_steps/00.29_ensure-policy-packages.yml
#- import_playbook: ./ztp_steps/00.30_ensure-service-groups.yml
#- import_playbook: ./ztp_steps/00.31_ensure-address-groups.yml
#- import_playbook: ./ztp_steps/00.32_ensure-device-groups.yml
#- import_playbook: ./ztp_steps/00.33_ensure-security-profiles.yml
#- import_playbook: ./ztp_steps/00.34_ensure-system-templates.yml
#- import_playbook: ./ztp_steps/01.01_add-rendered-fortigates.yml
#- import_playbook: ./ztp_steps/01.02_add-fortigates-to-device-groups.yml
#- import_playbook: ./ztp_steps/01.03_process-rendered-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/01.04_map-interfaces-by-device.yml
#- import_playbook: ./ztp_steps/01.05_map-sdwan-zones-by-device.yml

#- import_playbook: ./ztp_steps/01.08_add-wan-address-objects.yml
#- import_playbook: ./ztp_steps/01.09_add-vlan-address-objects.yml
#- import_playbook: ./ztp_steps/01.10_add-adom-policy-package-rules.yml
#- import_playbook: ./ztp_steps/01.12_assign-policy-packages.yml
#- import_playbook: ./ztp_steps/01.14_assign-system-templates.yml
#- import_playbook: ./ztp_steps/02.10_install-fgt-settings.yml
#- import_playbook: ./ztp_steps/02.11_install-fgt-policy-packages.yml

- import_playbook: ./ztp_steps/900.11_debug-rendered-dvmdb-scripts.yml

```

[Back to Top](#fa-ztp-tutorials-debugging-the-ansible-ztp-role)

## Debugging Service and Address Objects

```python

- import_playbook: ./ztp_steps/00.01_import-spreadsheet.yml
- import_playbook: ./ztp_steps/00.10_render-fortigate-templates.yml
- import_playbook: ./ztp_steps/00.11_validate-rendered-fortigate-templates.yml
#- import_playbook: ./ztp_steps/00.15_render-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/00.28_ensure-adom-in-fmg.yml
#- import_playbook: ./ztp_steps/00.29_ensure-policy-packages.yml
- import_playbook: ./ztp_steps/00.30_ensure-service-groups.yml
- import_playbook: ./ztp_steps/00.31_ensure-address-groups.yml
#- import_playbook: ./ztp_steps/00.32_ensure-device-groups.yml
#- import_playbook: ./ztp_steps/00.33_ensure-security-profiles.yml
#- import_playbook: ./ztp_steps/00.34_ensure-system-templates.yml
#- import_playbook: ./ztp_steps/01.01_add-rendered-fortigates.yml
#- import_playbook: ./ztp_steps/01.02_add-fortigates-to-device-groups.yml
#- import_playbook: ./ztp_steps/01.03_process-rendered-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/01.04_map-interfaces-by-device.yml
#- import_playbook: ./ztp_steps/01.05_map-sdwan-zones-by-device.yml

#- import_playbook: ./ztp_steps/01.08_add-wan-address-objects.yml
#- import_playbook: ./ztp_steps/01.09_add-vlan-address-objects.yml
#- import_playbook: ./ztp_steps/01.10_add-adom-policy-package-rules.yml
#- import_playbook: ./ztp_steps/01.12_assign-policy-packages.yml
#- import_playbook: ./ztp_steps/01.14_assign-system-templates.yml
#- import_playbook: ./ztp_steps/02.10_install-fgt-settings.yml
#- import_playbook: ./ztp_steps/02.11_install-fgt-policy-packages.yml

#- import_playbook: ./ztp_steps/900.11_debug-rendered-dvmdb-scripts.yml
```

[Back to Top](#fa-ztp-tutorials-debugging-the-ansible-ztp-role)


## Debugging Policies

```python

- import_playbook: ./ztp_steps/00.01_import-spreadsheet.yml
- import_playbook: ./ztp_steps/00.10_render-fortigate-templates.yml
- import_playbook: ./ztp_steps/00.11_validate-rendered-fortigate-templates.yml
#- import_playbook: ./ztp_steps/00.15_render-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/00.28_ensure-adom-in-fmg.yml
- import_playbook: ./ztp_steps/00.29_ensure-policy-packages.yml
- import_playbook: ./ztp_steps/00.30_ensure-service-groups.yml
- import_playbook: ./ztp_steps/00.31_ensure-address-groups.yml
#- import_playbook: ./ztp_steps/00.32_ensure-device-groups.yml
- import_playbook: ./ztp_steps/00.33_ensure-security-profiles.yml
#- import_playbook: ./ztp_steps/00.34_ensure-system-templates.yml
- import_playbook: ./ztp_steps/01.01_add-rendered-fortigates.yml
- import_playbook: ./ztp_steps/01.02_add-fortigates-to-device-groups.yml
- import_playbook: ./ztp_steps/01.03_process-rendered-dvmdb-scripts.yml
- import_playbook: ./ztp_steps/01.04_map-interfaces-by-device.yml
- import_playbook: ./ztp_steps/01.05_map-sdwan-zones-by-device.yml
- import_playbook: ./ztp_steps/01.08_add-wan-address-objects.yml
- import_playbook: ./ztp_steps/01.09_add-vlan-address-objects.yml
- import_playbook: ./ztp_steps/01.10_add-adom-policy-package-rules.yml
#- import_playbook: ./ztp_steps/01.12_assign-policy-packages.yml
#- import_playbook: ./ztp_steps/01.14_assign-system-templates.yml
#- import_playbook: ./ztp_steps/02.10_install-fgt-settings.yml
#- import_playbook: ./ztp_steps/02.11_install-fgt-policy-packages.yml

#- import_playbook: ./ztp_steps/900.11_debug-rendered-dvmdb-scripts.yml

```

As you can see we have to actually add the FortiGates, so we can run scripts on them and create interfaces. 
So we can then dynamically map those interfaces and create them.
So we can create policies with them.

But what if you've already added all of that data and are just now changing the policies?

```python

- import_playbook: ./ztp_steps/00.01_import-spreadsheet.yml
- import_playbook: ./ztp_steps/00.10_render-fortigate-templates.yml
- import_playbook: ./ztp_steps/00.11_validate-rendered-fortigate-templates.yml
#- import_playbook: ./ztp_steps/00.15_render-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/00.28_ensure-adom-in-fmg.yml
#- import_playbook: ./ztp_steps/00.29_ensure-policy-packages.yml
#- import_playbook: ./ztp_steps/00.30_ensure-service-groups.yml
#- import_playbook: ./ztp_steps/00.31_ensure-address-groups.yml
#- import_playbook: ./ztp_steps/00.32_ensure-device-groups.yml
#- import_playbook: ./ztp_steps/00.33_ensure-security-profiles.yml
#- import_playbook: ./ztp_steps/00.34_ensure-system-templates.yml
#- import_playbook: ./ztp_steps/01.01_add-rendered-fortigates.yml
#- import_playbook: ./ztp_steps/01.02_add-fortigates-to-device-groups.yml
#- import_playbook: ./ztp_steps/01.03_process-rendered-dvmdb-scripts.yml
#- import_playbook: ./ztp_steps/01.04_map-interfaces-by-device.yml
#- import_playbook: ./ztp_steps/01.05_map-sdwan-zones-by-device.yml
#- import_playbook: ./ztp_steps/01.08_add-wan-address-objects.yml
#- import_playbook: ./ztp_steps/01.09_add-vlan-address-objects.yml
- import_playbook: ./ztp_steps/01.10_add-adom-policy-package-rules.yml
#- import_playbook: ./ztp_steps/01.12_assign-policy-packages.yml
#- import_playbook: ./ztp_steps/01.14_assign-system-templates.yml
#- import_playbook: ./ztp_steps/02.10_install-fgt-settings.yml
#- import_playbook: ./ztp_steps/02.11_install-fgt-policy-packages.yml

#- import_playbook: ./ztp_steps/900.11_debug-rendered-dvmdb-scripts.yml

```



[Back to Top](#fa-ztp-tutorials-debugging-the-ansible-ztp-role)