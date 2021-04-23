# FA-ZTP: Ansible ZTP Role Architecture

[Back to README](../../README.md#table-of-contents)

[Back to Architecture](ARCHITECTURE.md)


* [Understanding the Ansible ZTP Role Architecture](#understanding-the-ansible-ztp-role-architecture)
  * [Ansible Role Defaults](ansible_ztp.md#ansible-role-defaults)
  * [Ansible Role Variables](ansible_ztp.md#ansible-role-variables)
  * [Ansible Role Files](ansible_ztp.md#ansible-role-files) 
  * [Ansible Role Templates](ansible_ztp.md#ansible-role-templates) 
  * [Ansible Role Tasks](ansible_ztp.md#ansible-role-tasks)



## Understanding the Ansible ZTP Role Architecture

The official definition of an Ansible Role can be found here: 
https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html

We are using this definition as a **scaffold** to organize tasks in the order they need to be executed.

We are also using an Ansible role for the way it handles variables.

Here is a screenshot of the basic Ansible ZTP Folder Structure:

![](docs/images/ansible_ztp_role_dirs_1.png)

### Ansible Role Defaults

* Ansible Roles can have **default** variables
  * Defined under **/defaults/main.yml** or **/defaults/main/*.yml**. 
    * ![](docs/images/ztp_role_defaults_pic.png)
  * We use this feature to define things like 
    the target FortiManager ADOM or default device model string but it can be expanded for any usage.
  * ![Example Ansible ZTP Role Default Settings](roles/fortigate.ztp/defaults/main/fortimanager_settings.yml)
  
### Ansible Role Variables

* Ansible Roles have **vars** that can override the **defaults**.
    * These are defined under **/vars/main.yml** or **/vars/main/*.yml**.
      * ![](docs/images/ztp_role_vars_pic.png)
    * ![Example Ansible ZTP Role Base Variables](roles/fortigate.ztp/vars/main/base.yml)
    * We also use the **/vars/fortigates** directory as a target for any import, which allows for exceptions and manual changes.
    * ![Example Ansible ZTP Role FortiGate YAML File](roles/fortigate.ztp/vars/fortigates/TEST_FGT1.yaml)
    * We then render these **/var/fortigates/*.yaml** files to **/files/tmp/fortigates** to actually use them.
        * This is what allows for a VCS-based agile workflow. Exceptions and imports under **/vars/fortigates** with branches.
        * It also acts as a safety net, or "checkpoint", for configurations to be validated before rendered to **/files/tmp/fortigates**.
    * Most importantly, vars can be imported when Ansible Roles are executed in playbooks **outside** of the Ansible Role itself -- which is exactly how we sequence tasks.


### Ansible Role Files

* Ansible Roles have a **files** directory which can contain anything we want.
    * ![](docs/images/ztp_role_files_pic.png)
    * Temporary files such as rendered FortiGates and configuration scripts.
    * Python scripts to help import and transform Organizational Workflow Data.
    * Spreadsheets to import
    * "Support CSV" Files with serial numbers
  
### Ansible Role Templates

* Ansible Roles have a **templates** directory for Jinja2 templates.
    * ![](docs/images/ztp_role_templates_pic.png)
    * We can organize FortiGate CLI config templates here.
    * We also use Jinja2 templates within Ansible Tasks simply to organize data that makes it easy for Ansible Tasks to consume.
      * ![Normalized Interfaces Ansible ZTP Task uses Jinja2 Template](roles/fortigate.ztp/tasks/add/normalized_interface_device_mapping.yml)
      * ![Normalized Interfaces Jinja2 Template](roles/fortigate.ztp/templates/interfaces/normalized_interfaces.j2)
    * FortiManager has the CLI Template functionality, but since we're using Ansible already on principle, it is easier to 
    create scripts for each FortiGate individually with Jinja2 templates.
    * FortiGate configuration scripts are templated on a per-FortiGate basis (just like the Ansible ZTP YAML data model).
        * ![FortiGate Script Templates](roles/fortigate.ztp/templates/dvmdb_scripts)
    * We also use Jinja2 templates to generate complicated API data payloads like a Firewall Policy which can have
    many options expanded upon.
      * For example, we have to flatten the policy data structure for policy packages in the FortiGate YAML files even further
      * ![Flattening a FortiGate YAML Policy Package list to a list of policies](roles/fortigate.ztp/templates/policy_packages/map_policy_api_data.j2)
      * ![The Attribute Map for policies](roles/fortigate.ztp/vars/main/adom_policy_attribute_map.yml)
        * This is an example of how to expand the Organizational Workflow Data Model.
        * The keys in this file represent column names from the ADOM Policies sheet in the example spreadsheet.
        * The corresponding values to each key are the actual API keys that the FortiManager expects. This is an example of 
          how to translate "friendly" names to the "api" key names before making an API call.
        * ![The Ansible ZTP Role Task that Converts this Key Map and then Applies Policies](roles/fortigate.ztp/tasks/add/policy_package_rule_adom.yml)
  
### Ansible Role Tasks

* Last but not least, Ansible Roles have **tasks** which are simple playbooks that do all of the heavy lifting.
    * ![](docs/images/ztp_role_tasks_pic.png)
    * Ansible Role Tasks all operate with the same implicit variable set defined as by the **default** and **vars** sections above.
    * This means that these tasks can be written with a common data model in mind.
    * The most common variable here is **ztp_fortigates** which is the list of dictionaries that makes up the Organizational Data Model converted to the Ansible ZTP Data Model
    * This variable is usually read using the task: ![Read Rendered FortiGates](roles/fortigate.ztp/tasks/templates/read_rendered_fortigates.yml)
    * This Task is called in almost every operation, but for the sake of an example: ![Add Rendered FortiGates](ztp_steps/01.01_add-rendered-fortigates.yml)
    

[Back to Top](#table-of-contents)


