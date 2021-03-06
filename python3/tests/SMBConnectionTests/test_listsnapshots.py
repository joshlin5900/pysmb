
from nose2.tools.decorators import with_setup, with_teardown
from smb.SMBConnection import SMBConnection
from smb import smb_structs
from .util import getConnectionInfo

conn = None

def setup_func_SMB1():
    global conn
    smb_structs.SUPPORT_SMB2 = False
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = True)
    assert conn.connect(info['server_ip'], info['server_port'])

def setup_func_SMB2():
    global conn
    smb_structs.SUPPORT_SMB2 = True
    info = getConnectionInfo()
    conn = SMBConnection(info['user'], info['password'], info['client_name'], info['server_name'], use_ntlm_v2 = True)
    assert conn.connect(info['server_ip'], info['server_port'])

def teardown_func():
    global conn
    conn.close()

@with_setup(setup_func_SMB1)
@with_teardown(teardown_func)
def test_listsnapshots_SMB1():
    global conn
    results = conn.listSnapshots('smbtest', '/rfc1001.txt')
    assert len(results) > 0

@with_setup(setup_func_SMB2)
@with_teardown(teardown_func)
def test_listsnapshots_SMB2():
    global conn
    results = conn.listSnapshots('smbtest', '/rfc1001.txt')
    assert len(results) > 0
