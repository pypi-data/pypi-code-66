#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import sys

from ..util_core.v2ray import restart
from ..util_core.writer import NodeWriter, GroupWriter
from ..util_core.group import Vmess, Socks, Mtproto, SS, Vless, Trojan
from ..util_core.selector import GroupSelector, ClientSelector
from ..util_core.utils import StreamType, stream_list, is_email, clean_iptables, random_email, ColorStr, readchar, random_port, port_is_use

@restart(True)
def new_port(new_stream=None):
    info = dict()
    if new_stream:
        correct_list = stream_list()
        if new_stream not in [x.value for x in correct_list]:
            print(_("input error! input -h or --help to get help"))
            exit(-1)
        
        stream = list(filter(lambda stream:stream.value == new_stream, correct_list))[0]

        if stream == StreamType.SOCKS:
            user = input(_("please input socks user: "))
            password = input(_("please input socks password: "))
            if user == "" or password == "":
                print(_("socks user or password is null!!"))
                exit(-1)
            info = {"user":user, "pass": password}
        elif stream == StreamType.SS:
            from .ss import SSFactory
            sf = SSFactory()
            info = {"method": sf.get_method(), "password": sf.get_password()}
    else:
        salt_stream = [StreamType.KCP_DTLS, StreamType.KCP_WECHAT, StreamType.KCP_UTP, StreamType.KCP_SRTP, StreamType.KCP_WG]
        random.shuffle(salt_stream)
        stream = salt_stream[0]
        print("{}: {} \n".format(_("random generate (srtp | wechat-video | utp | dtls | wireguard) fake header, new protocol"), ColorStr.green(stream.value)))

    new_port = ""
    while True:
        new_random_port = random_port(1000, 65535)
        new_port = input("{0} {1}, {2}: ".format(_("random generate port"), ColorStr.green(str(new_random_port)), _("enter to use, or input customize port")))

        if not new_port:
            new_port = str(new_random_port)
        else:
            if not new_port.isnumeric():
                print(_("input error, please input again"))
                continue
            elif port_is_use(new_port):
                print(_("port is use, please input other port!"))
                continue
        break

    print("")
    print("{}: {}".format(_("new port"), new_port))
    print("")
    nw = NodeWriter()
    nw.create_new_port(int(new_port), stream, **info)
    return True

@restart()
def new_user():
    gs = GroupSelector(_('add user'))
    group = gs.group
    group_list = gs.group_list

    if group == None:
        pass
    else:
        email = ""
        if type(group.node_list[0]) in (Vmess, Vless, Trojan): 
            while True:
                is_duplicate_email=False
                remail = random_email()
                tip = _("create random email:") + ColorStr.cyan(remail) + _(", enter to use it or input new email: ")
                email = input(tip)
                if email == "":
                    email = remail
                if not is_email(email):
                    print(_("not email, please input again"))
                    continue
                
                for loop_group in group_list:
                    for node in loop_group.node_list:
                        if node.user_info == None or node.user_info == '':
                            continue
                        elif node.user_info == email:
                            print(_("have same email, please input other"))
                            is_duplicate_email = True
                            break              
                if not is_duplicate_email:
                    break

            nw = NodeWriter(group.tag, group.index)
            info = {'email': email}
            if type(group.node_list[0]) == Trojan:
                password = input(_("please input trojan user password: "))
                if password == "":
                    print(_("password is null!!"))
                    exit(-1)
                info['password'] = password
            nw.create_new_user(**info)
            return True

        elif type(group.node_list[0]) == Socks:
            print(_("local group is socks, please input user and password to create user"))
            print("")
            user = input(_("please input socks user: "))
            password = input(_("please input socks password: "))
            if user == "" or password == "":
                print(_("socks user or password is null!!"))
                exit(-1)
            info = {"user":user, "pass": password}
            nw = NodeWriter(group.tag, group.index)
            nw.create_new_user(**info)
            return True

        elif type(group.node_list[0]) == Mtproto:
            print("")
            print(_("Mtproto protocol only support one user!!"))

        elif type(group.node_list[0]) == SS:
            print("")
            print(_("Shadowsocks protocol only support one user, u can add new port to multiple SS!"))

@restart()
def del_port():
    gs = GroupSelector(_('del port'))
    group = gs.group

    if group == None:
        pass
    else:
        print(_("del group info: "))
        print(group)
        choice = readchar(_("delete?(y/n): ")).lower()
        if choice == 'y':
            nw = NodeWriter()
            nw.del_port(group)
            clean_iptables(group.port)
            return True
        else:
            print(_("undo delete"))

@restart()
def del_user():
    cs = ClientSelector(_('del user'))
    group = cs.group

    if group == None:
        pass
    else:
        client_index = cs.client_index
        print(_("del user info:"))
        print(group.show_node(client_index))
        choice = readchar(_("delete?(y/n): ")).lower()
        if choice == 'y':
            if len(group.node_list) == 1:
                clean_iptables(group.port)
            nw = NodeWriter()
            nw.del_user(group, client_index)
            return True
        else:
            print(_("undo delete"))