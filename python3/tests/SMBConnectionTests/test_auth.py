
from nose2.tools.decorators import with_teardown
from smb.SMBConnection import SMBConnection
from smb import smb_structs
from .util import getConnectionInfo

conn = None

def teardown_func():
    global conn
    conn.close()

@with_teardown(teardown_func)
def test_NTLMv1_auth_SMB1():
    global conn
    smb_structs.SUPPORT_SMB2 = False
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], domain = info['domain'], use_ntlm_v2 = False)
    assert conn.connect(info['server_ip'], info['server_port'])

@with_teardown(teardown_func)
def test_NTLMv2_auth_SMB1():
    global conn
    smb_structs.SUPPORT_SMB2 = False
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], domain = info['domain'], use_ntlm_v2 = True)
    assert conn.connect(info['server_ip'], info['server_port'])

@with_teardown(teardown_func)
def test_NTLMv1_auth_SMB2():
    global conn
    smb_structs.SUPPORT_SMB2 = True
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], domain = info['domain'], use_ntlm_v2 = False)
    assert conn.connect(info['server_ip'], info['server_port'])

@with_teardown(teardown_func)
def test_NTLMv2_auth_SMB2():
    global conn
    smb_structs.SUPPORT_SMB2 = True
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], domain = info['domain'], use_ntlm_v2 = True)
    assert conn.connect(info['server_ip'], info['server_port'])
