import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from snmp_cmds import Session

from dotenv import load_dotenv


load_dotenv()
TFTP_SERVER = os.environ.get('TFTP_SERVER')


def snr_upload_config(sw):
    """
    Function to upload config to tftp server
    for SNR-S2995G model

    :param sw: snmp_cmds.api.Session object
    :return: None
    """
    sw.set(oid='.1.3.6.1.4.1.40418.7.100.1.10.3.0', value_type='s', value=TFTP_SERVER)
    sw.set(oid='.1.3.6.1.4.1.40418.7.100.1.10.4.0', value_type='s', value='startup.cfg')
    sw.set(oid='.1.3.6.1.4.1.40418.7.100.1.10.5.0', value_type='s', value=sw.ipaddress)
    sw.set(oid='.1.3.6.1.4.1.40418.7.100.1.10.7.0', value_type='i', value='2')
    sw.set(oid='.1.3.6.1.4.1.40418.7.100.1.10.8.0', value_type='i', value='1')
    sw.get(oid='.1.3.6.1.4.1.40418.7.100.1.10.9.0')


def tplink_upload_config(sw):
    """
    Function to upload config to tftp server
    for JetStream models

    :param sw: snmp_cmds.api.Session object
    :return: None
    """
    sw.set(oid='.1.3.6.1.4.1.11863.6.3.1.7.1.0', value_type='s', value=TFTP_SERVER)
    sw.set(oid='.1.3.6.1.4.1.11863.6.3.1.7.2.0', value_type='s', value=sw.ipaddress)
    sw.set(oid='.1.3.6.1.4.1.11863.6.3.1.7.4.0', value_type='i', value='1')


def dgs_upload_config(sw):
    """
    Function to upload config to tftp server
    for DGS-3120/3420 models

    :param sw: snmp_cmds.api.Session object
    :return: None
    """
    sw.set(oid='.1.3.6.1.4.1.171.12.1.2.18.1.1.3.3', value_type='a', value=TFTP_SERVER)
    time.sleep(0.1)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.18.1.1.5.3', value_type='s', value=sw.ipaddress)
    time.sleep(0.1)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.18.1.1.7.3', value_type='s', value='config.cfg')
    time.sleep(0.1)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.18.1.1.8.3', value_type='i', value='2')
    time.sleep(0.1)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.18.1.1.12.3', value_type='i', value='3')


def des1210_upload_config(sw):
    """
    Function to upload config to tftp server
    for DES1210-28ME model

    :param sw: snmp_cmds.api.Session object
    :return: None
    """
    sw.set(oid='1.3.6.1.4.1.171.10.75.15.2.3.5.0', value_type='a', value=TFTP_SERVER)
    sw.set(oid='1.3.6.1.4.1.171.10.75.15.2.3.6.0', value_type='s', value=sw.ipaddress)
    sw.set(oid='1.3.6.1.4.1.171.10.75.15.2.3.7.0', value_type='i', value='2')


def des3526_upload_config(sw):
    """
    Function to upload config to tftp server
    for DES-3526 model

    :param sw: snmp_cmds.api.Session object
    :return: None
    """
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.3.3', value_type='a', value='10.1.2.68')
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.4.3', value_type='i', value='2')
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.5.3', value_type='s', value=sw.ipaddress)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.7.3', value_type='i', value='2')
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.8.3', value_type='i', value='3')


def des30xx_upload_config(sw):
    """
    Function to upload config to tftp server
    for DES-30xx models

    :param sw: snmp_cmds.api.Session object
    :return: None
    """
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.3.3', value_type='a', value=TFTP_SERVER)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.4.3', value_type='i', value='2')
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.5.3', value_type='s', value=sw.ipaddress)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.7.3', value_type='i', value='2')
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.8.3', value_type='i', value='3')


def des_upload_config(sw):
    """
    Function to upload config to tftp server
    for other DES series models

    :param sw: snmp_cmds.api.Session object
    :return: None
    """
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.6.3', value_type='i', value='3')
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.4.3', value_type='i', value='2')
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.5.3', value_type='s', value=sw.ipaddress)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.7.3', value_type='i', value='2')
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.3.3', value_type='a', value=TFTP_SERVER)
    sw.set(oid='1.3.6.1.4.1.171.12.1.2.1.1.8.3', value_type='i', value='3')


def mes_upload_config(ip):
    """
    Function to upload config to tftp
    uses subprocess module

    :param ip: str
    :return: None
    """
    command = f'''
    snmpset -v2c -c private {ip} 1.3.6.1.4.1.89.87.2.1.3.1 i 1 \
    1.3.6.1.4.1.89.87.2.1.7.1 i 2 \
    1.3.6.1.4.1.89.87.2.1.8.1 i 3 \
    1.3.6.1.4.1.89.87.2.1.9.1 a 10.1.2.68 \
    1.3.6.1.4.1.89.87.2.1.11.1 s {ip} \
    1.3.6.1.4.1.89.87.2.1.17.1 i 4
    '''
    subprocess.run(command, shell=True)


def download_sw_config(ip_tuple):
    ip, model = ip_tuple
    sw_obj = Session(ipaddress=ip, write_community='private', read_community='private')

    if model.startswith('DES-1210'):
        des1210_upload_config(sw_obj)
    elif model.startswith('DGS-3120') or model.startswith('DGS-3420'):
        dgs_upload_config(sw_obj)
    elif model.startswith('SNR'):
        snr_upload_config(sw_obj)
    elif model.startswith('MES'):
        mes_upload_config(ip)
    elif model.startswith('JetStream'):
        tplink_upload_config(sw_obj)
    else:
        des_upload_config(sw_obj)


def concurrent_exe(function, devices, limit=50):
    """
    Function that use multithreading to execute another function
    :param function: func
    :param devices: ip address list
    :param limit: int limit of workers
    :return:
    """
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [executor.submit(function, device) for device in devices]
        for f in as_completed(futures):
            result = f.result()
            print(f'Future done {f}')


if __name__ == '__main__':
    sw_list = 'INSERT YOUR IP ADDRESS LIST HERE'

    concurrent_exe(download_sw_config, sw_list)



