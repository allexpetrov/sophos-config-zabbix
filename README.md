# sophos-config-zabbix
Template to monitor the configuration of Sophos UTM v.9.6 by Zabbix > 4.0

Disclaimer:
This is 0.1apha version of template and script
This isn't an official template by Sophos Company or Zabbix SIA
Tested against Sophos v9.6 with 1.3 release of API engine
Tested on Zabbix 4.0.2

User macro list:
{$T_SOPHOS_API_PASSWORD} - #your user password
{$T_SOPHOS_API_USER} - # your admin username
{$T_SOPHOS_HISTORY_DATA} - # for how long to store the history* data
{$T_SOPHOS_HISTORY_MASTER} -  # for how long to keep master item data. Configured to 1h for proper debugging, but during the prodcution rollout better to have this configured to 0
{$T_SOPHOS_KEEP_LOST_PERIOD} - # for how long to keep the non-discovered resources
{$T_SOPHOS_PORT} - # Sophos Web GUI TCP port. Usually 4444
{$T_SOPHOS_TRENDS_DATA} - # For how long to keep trends* table data
{$T_SOPHOS_UPDATE_INTERVAL_DISCOVERY} - #How often to run LLD rule. Configured to 5 minutes for test purposes. For production it's better not to have this < 1h 
{$T_SOPHOS_UPDATE_INTERVAL_MASTER} - # How often to poll the API by master item. Configured to 5 minutes

