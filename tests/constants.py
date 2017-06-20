import json
from app.common.constants import NEW_CERTIFICATE_EVENT_NAME, TRANSFER_CERTIFICATE_EVENT_NAME, \
    CLAIM_CERTIFICATE_EVENT_NAME, ADMIN_CLEANING_EVENT_NAME


CONTRACT_ADDRESS = '0x57a0526fbce4183d146be2ef31e16969dacf51bf'
CONTRACT_FAKE_ADDRESS = '0x343deaf9453bcfde30323237abdde4343dff2323'


with open('solidity/%s/abi.json' % CONTRACT_ADDRESS, 'rb') as json_abi:
    CONTRACT_ABI = json_abi.read()


EVENT_NAMES = [
    NEW_CERTIFICATE_EVENT_NAME,
    TRANSFER_CERTIFICATE_EVENT_NAME,
    CLAIM_CERTIFICATE_EVENT_NAME,
    ADMIN_CLEANING_EVENT_NAME,
]


EVENT_ABIS = [
    json.dumps(abi, separators=(',', ':')).encode()
    for abi in json.loads(CONTRACT_ABI.decode()) if abi['type'] == 'event'
]


BLOCK_NUMBER = 1264783
BLOCK = {
    'author': '0x00e6d2b931f55a3f1701c7389d592a7778897879',
    'difficulty': 340282366920938463463374607431768211454,
    'extraData': '0xd5830106068650617269747986312e31362e30826c69',
    'gasLimit': 5000000,
    'gasUsed': 0,
    'hash': '0x640703624778047e2f6877a64cab68609e8f1f35b67465b81e71f54aadf53fd3',
    'logsBloom': '0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                 '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                 '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                 '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                 '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
                 '000000000',
    'miner': '0x00e6d2b931f55a3f1701c7389d592a7778897879',
    'number': 1264783,
    'parentHash': '0xf1219f9b8289737bc1e98fe6d02b5cac63d26392d85dbf6b7f036036a06649c7',
    'receiptsRoot': '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421',
    'sealFields': [
        '0x8416431117',
        '0xb84157ce6dbc568ad64abc500993aa405908375d69259f713e22a22148bf34cf987a0328c5cedb32ee726358ce7ebfa401d674376789'
        'c1479a259ce12af8695244c101'],
    'sha3Uncles': '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
    'signature': '57ce6dbc568ad64abc500993aa405908375d69259f713e22a22148bf34cf987a0328c5cedb32ee726358ce7ebfa401d674376'
                 '789c1479a259ce12af8695244c101',
    'size': 579,
    'stateRoot': '0xfb5f08926783d8c538ac6ef36059195f323f99ae0457a6f1ba4e6b976ed89880',
    'step': '373494039',
    'timestamp': 1493976156,
    'totalDifficulty': 379940235091372315749250137680296225319808256,
    'transactions': [],
    'transactionsRoot': '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421',
    'uncles': []
}

OWNER_ADDRESS = '0x13377b14b615fff59c8e66288c32365d38181cdb'