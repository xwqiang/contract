#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vobject


def create_vcard(last_name=None, first_name=None, mobile_number=None, org=None, email=None):
    j = vobject.vCard()

    if first_name and last_name:
        j.add('n')
        j.n.value = vobject.vcard.Name(family=last_name, given=first_name)
        j.add('fn')
        j.fn.value = last_name + " " + first_name
    else:
        # vCard limitation - must be at least one fn element
        raise RuntimeError("First name and last name must be given")

    if org:
        j.add('ORG')
        j.org.value = org

    if mobile_number:
        tel = j.add("tel")
        tel.type_param = ["WORK", "MOBILE"]
        tel.value = mobile_number

    if email:
        j.add('email')
        j.email.value = email
        j.email.type_param = 'INTERNET'

    return j.serialize()


def main():
    f = open('contacts.txt', 'r')
    index = 1
    vcardfile = open('mycontract' + '.vcf', 'w')
    for line in f.readlines():
        contact = line.split()
        org = contact[0]
        fullname = contact[1]
        mobile_number = contact[2]

        last_name = fullname[:index]
        first_name = fullname[index:]

        print(last_name, first_name, mobile_number, org)
        vcardfile.write(create_vcard(last_name, first_name, mobile_number, [org]))
    vcardfile.close
    f.close


if __name__ == '__main__':
    main()
