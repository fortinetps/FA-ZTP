from schema import Schema, And, Use, Or, Optional, SchemaError


def get_schema():
    schema = Schema(
        [{
            'address_groups': [
                {
                    'name': And(str),
                    'adom': And(str),
                    'subnets': Or(str, list)
                }
            ],
            'bgp_community_lists': [
                {
                    'action': And(str),
                    'fortigate_name': And(str),
                    'match': And(str),
                    'name': And(str),
                }
            ],
            'bgp_neighbor_groups': [
                {
                    'advertisement_interval': And(int),
                    'comments': Or(str, None),
                    'connect_timer': And(int),
                    'fortigate_name': And(str),
                    'link_failover': And(str, Or('enable', 'disable')),
                    'neighbor_group_name': And(str),
                    'prefix': And(str),
                    'remote_as': And(int),
                    'route_map_in': Or(str, None),
                    'route_map_out': Or(str, None),
                    'route_map_out_preferable': Or(str, None),
                }
            ],
            'bgp_neighbors': [
                {
                    'advertisement_interval': And(int),
                    'comments': Or(str, None),
                    'connect_timer': And(int),
                    'fortigate_name': And(str),
                    'link_failover': And(str, Or('enable', 'disable')),
                    'local_as': And(int),
                    'local_interface': And(str),
                    'neighbor_ip': And(str),
                    'remote_as': And(int),
                    'route_map_in': Or(str, None),
                    'route_map_out': Or(str, None),
                    'route_map_out_preferable': Or(str, None),
                }
            ],
            'bgp_route_maps': [
                {
                    'fortigate_name': And(str),
                    'match_community_list': Or(str, None),
                    'name':  And(str),
                    'set_community': Or(str, None),
                    'set_route_tag': Or(int, None)
                }
            ],
            'fap_profiles': [
                {
                    'fortiap_platform': And(str),
                    'location_name': And(str),
                    'profile_name': And(str),
                    'radio_1_band': And(str),
                    'radio_1_channel_width': And(str),
                    'radio_1_channels': Or(str, list),
                    'radio_1_mode': And(str),
                    'radio_2_band': And(str),
                    'radio_2_channel_width': And(str),
                    'radio_2_channels': Or(str, list),
                    'radio_2_mode': And(str),
                }
            ],
            'fap_ssids': [
                {
                    'authentication': Or(str, None),
                    'bridge_vlan': Or(int, None),
                    'broadcast_ssid': And(str, Or('enable', 'disable')),
                    'passphrase': Or(str, None),
                    'security_mode': And(str),
                    'ssid': And(str),
                    'traffic_mode': And(str),
                    'tunnel_ipv4_gateway': Or(str, None),
                    'upstream_fortigate_name': And(str)
                }
            ],
            'fgt_address_object_prefix': Or(str, None),
            'fgt_admin_user': And(str),
            'fgt_device_model': And(str),
            'fgt_faz_target_ip': Or(str, None),
            'fgt_fortiswitch_trunk_interfaces': Or(list, None),
            'fgt_mgmt_ip': Or(str, None),
            'fgt_mgmt_port': Or(str, None),
            'fgt_mgmt_vrf': Or(int, None),
            'fgt_lan_vlan_map': [
                {
                    'allow_access': Or(list, None),
                    'bgp_network': Or(str, None),
                    'device_detection': And(str, Or('enable', 'disable')),
                    'dhcp_server': Or(str, None),
                    'fortigate_name': And(str),
                    'ipv4_gateway': And(str),
                    'ipv4_subnet': And(str),
                    'ipv6_gateway': Or(str, None),
                    'ipv6_subnet': Or(str, None),
                    'network_alias': And(str),
                    'physical_interface': And(str),
                    'role': And(str),
                    'vlan_id': And(int),
                    'zone': Or(str, None)
                }
            ],
            'fgt_latitude': And(float),
            'fgt_local_bgp_as': Or(int, None),
            'fgt_location_name': And(str),
            'fgt_longitude': And(float),
            'fgt_name': And(str),
            'fgt_sn': And(str),
            'fgt_static_routes': [
                {
                    'fortigate_name': And(str),
                    'destination': And(str),
                    'gateway': Or(str, None),
                    'interface': And(str),
                    'distance': Or(int, None),
                    'comment': Or(str, None)
                }
            ],
            'fgt_street_address': And(str),
            'fgt_vdom': And(str),
            'fgt_wan1_dl_speed_kbps': Or(int, None),
            'fgt_wan1_ip': Or(str, None),
            'fgt_wan1_port': Or(str, None),
            'fgt_wan1_ul_speed_kbps': Or(int, None),
            'fgt_wan2_dl_speed_kbps': Or(int, None),
            'fgt_wan2_ip': Or(str, None),
            'fgt_wan2_port': Or(str, None),
            'fgt_wan2_ul_speed_kbps': Or(int, None),
            'fgt_wan3_dl_speed_kbps': Or(int, None),
            'fgt_wan3_ip': Or(str, None),
            'fgt_wan3_port': Or(str, None),
            'fgt_wan3_ul_speed_kbps': Or(int, None),
            'fmgr_mgmt_mode': And(str),
            'fmgr_object_description_string': And(str),
            'fmgr_target_adom': And(str),
            'fmgr_target_adom_mr': And(int),
            'fmgr_target_adom_ver': And(float),
            'fmgr_target_device_group': Or(str, None),
            'fortiaps': [
                {
                    'fap_profile': And(str),
                    'fortiap_name': And(str),
                    'fortiap_platform': And(str),
                    'fortiap_serial_number': And(str),
                    'upstream_fortigate_name': And(str),
                }
            ],
            'fortiswitches': [
                {
                    'fortiswitch_name': And(str),
                    'fortiswitch_platform': And(str),
                    'fortiswitch_serial_number': And(str),
                    'upstream_fortigate_name': And(str),
                    'ports': [
                        {
                            'allowed_vlans': Or(list, None),
                            'description': Or(str, None),
                            'dhcp_snooping': And(str, Or('trusted', 'untrusted')),
                            'edge_port': And(str, Or('enable', 'disable')),
                            'fortiswitch_name': And(str),
                            'lldp_profile': Or(str, None),
                            'lldp_status': And(str, Or('disable', 'tx', 'rx', 'tx-rx')),
                            'loop_guard': And(str, Or('enable', 'disable')),
                            'nac_profile': Or(str, None),
                            'native_vlan': Or(str, None),
                            'port': Or(int, str),
                            'qos_policy': Or(str, None),
                            'stp': And(str, Or('enable', 'disable')),
                            'stp_bpdu_guard': And(str, Or('enable', 'disable')),
                            'stp_root_guard': And(str, Or('enable', 'disable')),
                            # 'upstream_fortigate_name': And(str)

                        }
                    ]
                }
            ],
            'ha': [
                {
                    'fortigate_name': And(str),
                    'ha_mode': And(str, Or("a-a", "a-p", "standalone")),
                    'ha_ports': And(list),
                    'monitor_ports': Or(list, None),
                    'group_name': And(str),
                    'session_pickup': Or(str, None),
                    'session_pickup_connectionless': Or(str, None),
                    'priority': Or(int, None),

                }
            ],
            'ipsec': [
                {
                    'admin_access': Or(list, str, None),
                    'comments': Or(str, None),
                    'fortigate_name': And(str),
                    'ike_version': And(int),
                    'local_subnet': And(str),
                    'overlay_id': And(int),
                    'phase1_authentication': And(str),
                    'phase1_dh_group': And(int),
                    'phase1_encryption': And(str),
                    'phase1_key_lifetime': And(int),
                    'phase2_authentication': And(str),
                    'phase2_dh_group': And(int),
                    'phase2_encryption': And(str),
                    'phase2_key_lifetime': And(int),
                    'psk': And(str),
                    'remote_subnet': And(str),
                    'vpn_interface_ip': Or(str, None),
                    'vpn_name': And(str),
                    'vpn_type': And(str),
                    'vrf_id': And(int),
                    'wan_gateway': And(str),
                    'wan_interface': And(str),
                }
            ],
            'policy_packages': [
                {
                    'fortigate_name': And(str),
                    'policy_package': And(str),
                    'policies': [
                        {
                            'action': And(str),
                            'antivirus': Or(str, None),
                            'appcontrol': Or(str, None),
                            'comments': Or(str, None),
                            'destination_addr': Or(list, str),
                            'destination_int': And(str),
                            'dns_filter': Or(str, None),
                            'file_filter': Or(str, None),
                            'ips': Or(str, None),
                            'log': And(str),
                            'name': And(str),
                            'nat': And(str, Or('enable', 'disable')),
                            'policy_package': And(str),
                            'schedule': And(str),
                            'sequence': And(int),
                            'service': Or(list, str),
                            'source_addr': Or(list, str),
                            'source_int': And(str),
                            'ssl_inspection': Or(str, None),
                            'voip': Or(str, None),
                            'web_filter': Or(str, None)
                        }
                    ]
                }
            ],
            'sdwan_interfaces': [
                {
                    'cost': And(int),
                    'fortigate_name': And(str),
                    'gateway': Or(str, None),
                    'id': And(int),
                    'interface': And(str),
                    'type': And(str),
                    'zone': Or(str, None)
                }
            ],
            'sdwan_rules': [
                {
                    'destination_address_object': Or(str, list, None),
                    'destination_internet_service': Or(str, list, None),
                    'fortigate_name': And(str),
                    'forward_dscp': And(str, Or('enable', 'disable')),
                    'measured_sla_name': And(str),
                    'mode': And(str),
                    'name': And(str),
                    'priority': And(int),
                    'reverse_dscp': And(str, Or('enable', 'disable')),
                    'sdwan_member_ids': Or(str, int),
                    'service': Or(str, list, None),
                    'source_address_object': Or(str, list, None),
                    'source_user_group':  Or(str, list, None)
                }
            ],
            'sdwan_slas': [
                {
                    'check_failures': And(int),
                    'check_successes': And(int),
                    'fortigate_name': And(str),
                    'interval_ms': And(int),
                    'protocol': And(str),
                    'sdwan_member_ids': Or(str, int),
                    'server': And(str),
                    'sla_jitter_ms': And(int),
                    'sla_latency_ms': And(int),
                    'sla_name': And(str),
                    'sla_packet_loss_percent': And(int)
                }
            ],
            'sdwan_zones': And(list),
            'service_groups': [
                {
                    'name': And(str),
                    'adom': And(str),
                    'ports': And(list)
                }
            ],
            'templates': [
                {
                    'fortiap': Or(str, None),
                    'fortigate_name': And(str),
                    'fortiswitch':  Or(str, None),
                    'provisioning':  Or(str, None),
                    'sdwan':  Or(str, None),
                }
            ],
            'zones': [
                {
                    'members': And(list),
                    'name': And(str)
                }
            ]
        }]
    )

    return schema

