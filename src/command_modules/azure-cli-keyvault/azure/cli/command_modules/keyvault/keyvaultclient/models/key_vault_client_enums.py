#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
#pylint: skip-file
from enum import Enum


class JsonWebKeyType(Enum):

    ec = "EC"
    rsa = "RSA"
    rsa_hsm = "RSA-HSM"
    oct = "oct"


class KeyUsageType(Enum):

    digital_signature = "digitalSignature"
    non_repudiation = "nonRepudiation"
    key_encipherment = "keyEncipherment"
    data_encipherment = "dataEncipherment"
    key_agreement = "keyAgreement"
    key_cert_sign = "keyCertSign"
    c_rl_sign = "cRLSign"
    encipher_only = "encipherOnly"
    decipher_only = "decipherOnly"


class ActionType(Enum):

    email_contacts = "EmailContacts"
    auto_renew = "AutoRenew"


class JsonWebKeyOperation(Enum):

    encrypt = "encrypt"
    decrypt = "decrypt"
    sign = "sign"
    verify = "verify"
    wrap_key = "wrapKey"
    unwrap_key = "unwrapKey"


class JsonWebKeyEncryptionAlgorithm(Enum):

    rsa_oaep = "RSA-OAEP"
    rsa1_5 = "RSA1_5"


class JsonWebKeySignatureAlgorithm(Enum):

    rs256 = "RS256"
    rs384 = "RS384"
    rs512 = "RS512"
    rsnull = "RSNULL"
