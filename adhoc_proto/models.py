# -*- coding: utf-8 -*-

import suitcase.fields
import suitcase.structure

PROTOCOL_NAME = 'MPS7'


class Header(suitcase.structure.Structure):

    protocol = suitcase.fields.Magic(expected_sequence=PROTOCOL_NAME)
    version = suitcase.fields.UBInt8()
    record_count = suitcase.fields.UBInt32()
