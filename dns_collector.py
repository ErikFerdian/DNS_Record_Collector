import dns.resolver
import json
import sys
import argparse

def get_records(domain, record_type):
    """Ambil record DNS berdasarkan type (A, MX, TXT, NS) dengan fallback resolver."""
    resolvers_list = [
        ["8.8.8.8", "8.8.4.4"],        # Google DNS
        ["1.1.1.1", "1.0.0.1"],        # Cloudflare DNS
        ["9.9.9.9", "149.112.112.112"],# Quad9
        None                           # Default (bawaan OS/ISP)
    ]

    for nameservers in resolvers_list:
        try:
            resolver = dns.resolver.Resolver()
            resolver.timeout = 5
            resolver.lifetime = 5

            if nameservers:  
                resolver.nameservers = nameservers

            answers = resolver.resolve(domain, record_type)

            if record_type == "MX":
                return [str(r.exchange) + " (priority=" + str(r.preference) + ")" for r in answers]
            else:
                return [str(r.to_text()) for r in answers]

        except Exception as e:
            # Coba resolver berikutnya
            last_error = str(e)
            continue

    return [f"Timeout/Error: {last_error}"]

def main():
    parser = argparse.ArgumentParser(description="DNS Record Collector")
    parser.add_argument("domain", help="Domain yang ingin dicek (contoh: google.com)")
    parser.add_argument("--type", help="Tipe record (A, MX, TXT, NS). Default = semua", choices=["A", "MX", "TXT", "NS"])
    args = parser.parse_args()

    domain = args.domain

    print(f"\n🔍 Mengumpulkan DNS Records untuk: {domain}\n")

    if args.type:
        records = {args.type: get_records(domain, args.type)}
    else:
        records = {
            "A": get_records(domain, "A"),
            "MX": get_records(domain, "MX"),
            "TXT": get_records(domain, "TXT"),
            "NS": get_records(domain, "NS"),
        }

    # Tampilkan hasil di terminal
    for rtype, values in records.items():
        print(f"[{rtype}]")
        for v in values:
            print(f" - {v}")
        print("")

    # Simpan ke file JSON
    with open("dns_report.json", "w") as f:
        json.dump(records, f, indent=4)

    print("✅ Hasil sudah disimpan ke dns_report.json\n")

if __name__ == "__main__":
    main()
