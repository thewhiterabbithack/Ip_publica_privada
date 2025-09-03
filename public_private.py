#!/usr/bin/env python3

import ipaddress
import argparse

parser = argparse.ArgumentParser(description="Verifica si una IP es pública o privada")
parser.add_argument("--ip", "-i", help="Host objetivo para escaneo")
args = parser.parse_args()

if args.ip:
    try:
        ip = ipaddress.ip_address(args.ip)
        if ip.is_private:
            print(f"La IP {args.ip} es privada.")
        else:
            print(f"La IP {args.ip} es pública.")
    except ValueError:
        print(f"{args.ip} no es una IP válida.")
else:
    print("No se proporcionó ninguna IP.")







 
