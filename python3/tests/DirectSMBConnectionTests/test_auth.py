
from nose2.tools.decorators import with_teardown
from smb.SMBConnection import SMBConnection
from smb import smb_structs
from .util import getConnectionInfo

conn, conn2, conn3 = None, None, None

def teardown_func():
    global conn, conn2, conn3
    if conn:
        conn.close()
    if conn2:
        conn2.close()
    if conn3:
        conn3.close();

@with_teardown(teardown_func)
def test_NTLMv1_auth_SMB1():
    global conn, conn2, conn3
    smb_structs.SUPPORT_SMB2 = False
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert conn.connect(info['server_ip'], info['server_port'])

    conn2 = SMBConnection(info['user'], 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert not conn2.connect(info['server_ip'], info['server_port'])

    conn3 = SMBConnection('INVALIDUSER', 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert not conn3.connect(info['server_ip'], info['server_port'])

@with_teardown(teardown_func)
def test_NTLMv1_auth_SMB1_callable_password():
    global conn, conn2, conn3
    smb_structs.SUPPORT_SMB2 = False
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], lambda: info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert conn.connect(info['server_ip'], info['server_port'])

    conn2 = SMBConnection(info['user'], lambda: 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert not conn2.connect(info['server_ip'], info['server_port'])

    conn3 = SMBConnection('INVALIDUSER', lambda: 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert not conn3.connect(info['server_ip'], info['server_port'])

@with_teardown(teardown_func)
def test_NTLMv2_auth_SMB1():
    global conn, conn2, conn3
    smb_structs.SUPPORT_SMB2 = False
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert conn.connect(info['server_ip'], info['server_port'])

    conn2 = SMBConnection(info['user'], 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert not conn2.connect(info['server_ip'], info['server_port'])

    conn3 = SMBConnection('INVALIDUSER', 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert not conn3.connect(info['server_ip'], info['server_port'])

@with_teardown(teardown_func)
def test_NTLMv1_auth_SMB2():
    global conn, conn2, conn3
    smb_structs.SUPPORT_SMB2 = True
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert conn.connect(info['server_ip'], info['server_port'])

    conn2 = SMBConnection(info['user'], 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert not conn2.connect(info['server_ip'], info['server_port'])

    conn3 = SMBConnection('INVALIDUSER', 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = False, is_direct_tcp = True)
    assert not conn3.connect(info['server_ip'], info['server_port'])

@with_teardown(teardown_func)
def test_NTLMv2_auth_SMB2():
    global conn, conn2, conn3
    smb_structs.SUPPORT_SMB2 = True
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert conn.connect(info['server_ip'], info['server_port'])

    conn2 = SMBConnection(info['user'], 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert not conn2.connect(info['server_ip'], info['server_port'])

    conn3 = SMBConnection('INVALIDUSER', 'wrongPass', info['client_name'], info['server_name'], use_ntlm_v2 = True, is_direct_tcp = True)
    assert not conn3.connect(info['server_ip'], info['server_port'])
