from sqlalchemy import Boolean, Column, VARCHAR, NVARCHAR, DateTime, ForeignKey, Integer, String, Text, Float, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class Locations(Base):
    """Location Data"""
    __tablename__ = "locations"
    location_name = Column(String, primary_key=True)
    full_street_address = Column(VARCHAR(500), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class DeviceLocations(Base):
    """Device Location Data"""
    __tablename__ = "deviceLocations"
    __table_args__ = (
        PrimaryKeyConstraint('location_name'),
    )
    location_name = Column(String, ForeignKey("locations.location_name"))
    device_type = Column(String)
    device_serial_number = Column(VARCHAR(500), nullable=False)
    device_model = Column(String, nullable=False)
    device_name = Column(String, nullable=False)
    upstream_fortigate_name = Column(String)

    # Relationships
    locations = relationship("Locations")


class FortiGates(Base):
    """ FortiGate Data """
    __tablename__ = "fortigates"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )
    fortigate_name = Column(String, ForeignKey("deviceLocations.device_name"))
    fgt_vdom = Column(String)
    fmgr_adom = Column(String)
    mgmt_port = Column(String)
    mgmt_ip = Column(String)
    mgmt_vrf = Column(String)
    wan1_port = Column(String)
    wan1_ip = Column(String)
    wan1_ul_kbps = Column(String)
    wan1_dl_kbps = Column(String)
    wan2_port = Column(String)
    wan2_ip = Column(String)
    wan2_ul_kbps = Column(String)
    wan2_dl_kbps = Column(String)
    wan3_port = Column(String)
    wan3_ip = Column(String)
    wan3_ul_kbps = Column(String)
    wan3_dl_kbps = Column(String)
    fortilink_trunk_interfaces = Column(String)
    fortilink_stack_ip = Column(String)
    fmgr_device_group = Column(String)

    device_locations = relationship("DeviceLocations")


class HA(Base):
    """ High Availability data"""
    __tablename__ = "ha"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    ha_mode = Column(String)
    ha_ports = Column(String)
    group_name = Column(String)
    session_pickup = Column(String)
    session_pickup_connectionless = Column(String)
    priority = Column(String)
    monitor_ports = Column(String)


class TemplateAssignments(Base):
    """ Template Assignment Data"""
    __tablename__ = "template_assignments"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )
    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    provisioning = Column(String)
    sdwan = Column(String)
    fortiswitch = Column(String)
    fortiap = Column(String)


class StaticRoutes(Base):
    """ StaticRoute Data """
    __tablename__ = "staticroutes"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    destination = Column(String)
    gateway = Column(String)
    interface = Column(String)
    distance = Column(String)
    comment = Column(String)

    fortigates = relationship("FortiGates")


class Networks(Base):
    """ Network Data """
    __tablename__ = "networks"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    network_alias = Column(String)
    role = Column(String)
    vlan_id = Column(Integer)
    ipv4_subnet = Column(String)
    ipv4_gateway = Column(String)
    zone = Column(String)
    physical_interface = Column(String)
    dhcp_server = Column(String)
    bgp_network = Column(String)
    ipv6_subnet = Column(String)
    ipv6_gateway = Column(String)
    device_detection = Column(String)
    allow_access = Column(String)

    fortigates = relationship("FortiGates")


class FortiSwitchPorts(Base):
    """ FortiSwitchPort Data """
    __tablename__ = "fortiswitchPorts"
    __table_args__ = (
        PrimaryKeyConstraint('fortiswitch_name'),
    )
    fortiswitch_name = Column(String, ForeignKey("deviceLocations.device_name"))
    port = Column(String)
    description = Column(String)
    native_vlan = Column(String)
    allowed_vlans = Column(String)
    stp = Column(String)
    loop_guard = Column(String)
    edge_port = Column(String)
    stp_bpdu_guard = Column(String)
    stp_root_guard = Column(String)
    dhcp_snooping = Column(String)
    qos_policy = Column(String)
    lldp_status = Column(String)
    lldp_profile = Column(String)
    nac_profile = Column(String)

    fortigates = relationship("DeviceLocations")


class SSIDs(Base):
    """ SSID Data """
    __tablename__ = "ssids"
    __table_args__ = (
        PrimaryKeyConstraint('upstream_fortigate_name'),
    )

    upstream_fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    ssid = Column(String)
    traffic_mode = Column(String)
    broadcast_ssid = Column(String)
    security_mode = Column(String)
    passphrase = Column(String)
    authentication = Column(String)
    bridge_vlan = Column(String)
    tunnel_ipv4_gateway = Column(String)
    captive_portal_url = Column(String)
    captive_user_groups = Column(String)
    captive_exempt_cidrs = Column(String)

    fortigates = relationship("FortiGates")


class APProfiles(Base):
    """ FortiAP Profile Data """
    __tablename__ = "apProfiles"
    __table_args__ = (
        PrimaryKeyConstraint('location_name'),
    )

    location_name = Column(String, ForeignKey("locations.location_name"))
    profile_name = Column(String)
    fortiap_platform = Column(String, ForeignKey("deviceLocations.device_model"))
    radio_1_mode = Column(String)
    radio_2_mode = Column(String)
    radio_1_band = Column(String)
    radio_2_band = Column(String)
    radio_1_channel_width = Column(String)
    radio_2_channel_width = Column(String)
    radio_1_channels = Column(String)
    radio_2_channels = Column(String)

    locations = relationship("Locations")


class RadiusServers(Base):
    """ Radius Server Data -- includes a dummy password in the role you have to change it later"""
    __tablename__ = "radius_servers"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )
    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    name = Column(String)
    radius_server_ip = Column(String)
    radius_coa = Column(String)
    timeout = Column(String)
    source_ip = Column(String)


class IPSec(Base):
    """ IPSec Data """
    __tablename__ = "ipsec"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    vpn_name = Column(String)
    vpn_type = Column(String)
    wan_gateway = Column(String)
    vpn_interface_ip = Column(String)
    remote_interface_ip = Column(String)
    wan_interface = Column(String)
    psk = Column(String)
    ike_version = Column(Integer)
    phase1_encryption = Column(String)
    phase1_authentication = Column(String)
    phase1_dh_group = Column(String)
    phase1_key_lifetime = Column(String)
    phase2_encryption = Column(String)
    phase2_authentication = Column(String)
    phase2_dh_group = Column(String)
    phase2_key_lifetime = Column(String)
    vrf_id = Column(String)
    overlay_id = Column(String)
    local_subnet = Column(String)
    remote_subnet = Column(String)
    allow_access = Column(String)
    ul_speed_kbps = Column(String)
    dl_speed_kbps = Column(String)
    comments = Column(String)

    fortigates = relationship("FortiGates")


class SDWANInterfaces(Base):
    """ SDWAN Interface Data """
    __tablename__ = "sdwanInterfaces"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    id = Column(String)
    zone = Column(String)
    interface = Column(String)
    gateway = Column(String)
    cost = Column(String)
    type = Column(String)

    fortigates = relationship("FortiGates")


class SDWANSLAs(Base):
    """ SDWAN SLA Data """
    __tablename__ = "sdwanSLAs"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    sla_name = Column(String)
    sdwan_member_ids = Column(String, ForeignKey("sdwanInterfaces.id"))
    protocol = Column(String)
    server = Column(String)
    sla_latency_ms = Column(String)
    sla_jitter_ms = Column(String)
    sla_packet_loss_percent = Column(String)
    interval_ms = Column(String)
    check_failures = Column(String)
    check_successes = Column(String)

    fortigates = relationship("FortiGates")
    sdwan_interfaces = relationship("SDWANInterfaces")


class SDWANRules(Base):
    """ SDWAN Rule Data """
    __tablename__ = "sdwanRules"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name', 'measured_sla_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    priority = Column(String)
    name = Column(String)
    source_address_object = Column(String, ForeignKey("addressGroups.name"))
    source_user_group = Column(String)
    destination_address_object = Column(String, ForeignKey("addressGroups.name"))
    service = Column(String, ForeignKey("serviceGroups.name"))
    destination_internet_service = Column(String)
    mode = Column(String)
    sdwan_member_ids = Column(String, ForeignKey("sdwanInterfaces.id"))
    measured_sla_name = Column(String, ForeignKey("sdwanSLAs.sla_name"))

    fortigates = relationship("FortiGates")
    slas = relationship("SDWANSLAs")
    sdwan_interfaces = relationship("SDWANInterfaces")


class BGPCommunityLists(Base):
    """ BGP Route Community List Data """
    __tablename__ = "bgpCommunityLists"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    name = Column(String)
    match = Column(String)
    action = Column(String)

    fortigates = relationship("FortiGates")


class BGPRouteMaps(Base):
    """ BGP Route Map Data """
    __tablename__ = "bgpRouteMaps"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name', 'match_community_list'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    name = Column(String)
    set_community = Column(String)
    match_community_list = Column(String, ForeignKey("bgpCommunityLists.name"))
    set_route_tag = Column(String)
    match_as_path = Column(String)
    set_local_preference = Column(String)
    match_ip_address = Column(String)

    fortigates = relationship("FortiGates")
    community_lists = relationship("BGPCommunityLists")


class BGPNeighbors(Base):
    """ BGPNeighbor Data """
    __tablename__ = "bgpNeighbors"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    local_as = Column(String)
    local_interface = Column(String)
    neighbor_ip = Column(String)
    remote_as = Column(String)
    route_map_in = Column(String, ForeignKey("bgpRouteMaps.name"))
    route_map_out = Column(String, ForeignKey("bgpRouteMaps.name"))
    route_map_out_preferable = Column(String, ForeignKey("bgpRouteMaps.name"))
    link_failover = Column(String)
    connect_timer = Column(String)
    advertisement_interval = Column(String)
    update_source = Column(String)
    graceful_restart = Column(String)
    soft_recognition = Column(String)
    comments = Column(String)

    fortigates = relationship("FortiGates")
    # route_maps = relationship("BGPRouteMaps", foreign_keys=[route_map_in, route_map_out, route_map_out_preferable])


class BGPNeighborGroups(Base):
    """ BGPNeighborGroup Data """
    __tablename__ = "bgpNeighborGroups"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    neighbor_group_name = Column(String)
    prefix = Column(String)
    remote_as = Column(String)
    route_map_in = Column(String, ForeignKey("bgpRouteMaps.name"))
    route_map_out = Column(String, ForeignKey("bgpRouteMaps.name"))
    route_map_out_preferable = Column(String, ForeignKey("bgpRouteMaps.name"))
    link_failover = Column(String)
    connect_timer = Column(String)
    advertisement_interval = Column(String)
    update_source = Column(String)
    graceful_restart = Column(String)
    soft_recognition = Column(String)
    comments = Column(String)

    fortigates = relationship("FortiGates")
    # route_maps = relationship("BGPRouteMaps", foreign_keys=[route_map_in, route_map_out, route_map_out_preferable])


class ASPathLists(Base):
    """ AS Path Lists"""
    __tablename__ = "as_path_lists"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    name = Column(String)
    rule = Column(String)
    regexp = Column(String)
    action = Column(String)


class PrefixLists(Base):
    """ Prefix Lists"""
    __tablename__ = "prefix_lists"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    name = Column(String)
    rule = Column(String)
    prefix = Column(String)


class AddressGroups(Base):
    """ Address Group Data """
    __tablename__ = "addressGroups"

    name = Column(String, primary_key=True)
    subnets = Column(String)


class ServiceGroups(Base):
    """ Service Group Data """
    __tablename__ = "serviceGroups"

    name = Column(String, primary_key=True)
    ports = Column(String)


class PolicyPackages(Base):
    """ Policy Package Data """
    __tablename__ = "policyPackages"
    __table_args__ = (
        PrimaryKeyConstraint('fortigate_name'),
    )

    fortigate_name = Column(String, ForeignKey("fortigates.fortigate_name"))
    policy_package = Column(String)

    fortigates = relationship("FortiGates")


class ADOMPolicies(Base):
    """ ADOM Policy Rule Data """
    __tablename__ = "adomPolicies"
    __table_args__ = (
        PrimaryKeyConstraint('policy_package'),
    )

    policy_package = Column(String, ForeignKey("policyPackages.policy_package"))
    sequence = Column(Integer)
    name = Column(String)
    source_int = Column(String)
    destination_int = Column(String)
    source_addr = Column(String, ForeignKey("addressGroups.name"))
    destination_addr = Column(String, ForeignKey("addressGroups.name"))
    schedule = Column(String)
    service = Column(String, ForeignKey("serviceGroups.name"))
    action = Column(String)
    log = Column(String)
    nat = Column(String)
    comments = Column(String)
    antivirus = Column(String)
    web_filter = Column(String)
    dns_filter = Column(String)
    appcontrol = Column(String)
    ips = Column(String)
    file_filter = Column(String)
    voip = Column(String)
    ssl_inspect = Column(String)

    policy_packages = relationship("PolicyPackages")



