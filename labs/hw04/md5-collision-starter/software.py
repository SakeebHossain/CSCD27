# -*- coding: utf-8 -*-
bits = """
                             R�D ���]�rO:�g ���0j<�@��,�a1���n����n���l���rG%�^#׆iE����� /R�
�����[��ǒ�B��wҍA�y����2b�Z�B��z��pE?�ãq���߈��"""
from hashlib import sha256
if sha256(bits).hexdigest() == "573552f4af6cf2c1a5903a33e511750b306633cc6475efede9623bb6fb61c327":
    print "I am good!"
else:
    print "I am evil!" 
