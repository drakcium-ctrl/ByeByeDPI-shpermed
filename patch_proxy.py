with open('app/src/main/cpp/byedpi/proxy.c', 'r') as f:
    content = f.read()

needle = '                if (params.baddr.sa.sa_family != addr.sa.sa_family) {\n                    return -1;\n                }\n                LOG(LOG_S, "udp addr:'

replacement = '                if (params.baddr.sa.sa_family != addr.sa.sa_family) {\n                    return -1;\n                }\n                /* Drop UDP to blocked ports (QUIC on 443, etc.) */\n                uint16_t _dport = ntohs(addr.in.sin_port);\n                for (int _i = 0; _i < params.udp_drop_ports_n; _i++) {\n                    if (params.udp_drop_ports[_i] == _dport) {\n                        LOG(LOG_S, "udp drop: port=%d\\n", (int)_dport);\n                        buff_ppush(pool, buff);\n                        return 0;\n                    }\n                }\n                LOG(LOG_S, "udp addr:'

if needle in content:
    content = content.replace(needle, replacement, 1)
    with open('app/src/main/cpp/byedpi/proxy.c', 'w') as f:
        f.write(content)
    print("proxy.c patched successfully")
else:
    print("ERROR: context not found in proxy.c")
    exit(1)
