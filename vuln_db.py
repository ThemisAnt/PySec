VULN_DB = {
    "OpenSSH_6.6.1": {
        "cve": "CVE-2015-5600",
        "description": "Keyboard-interactive authentication flaw allows attackers to bypass MaxAuthTries via multiple ChallengeResponseAuthentication devices, enabling brute-force attacks.",
        "severity": "Medium"
    },
    "OpenSSH_7.2": {
        "cve": "CVE-2016-6210",
        "description": "Allows remote attackers to enumerate valid usernames via timing differences during authentication.",
        "severity": "Low"
    },
    "Apache/2.4.7": {
        "cve": "CVE-2014-0226",
        "description": "Race condition in the mod_status module allows remote attackers to cause a denial of service or execute arbitrary code.",
        "severity": "High"
    },
    "vsftpd 2.3.4": {
        "cve": "CVE-2011-2523",
        "description": "Contains a backdoor that can give an attacker a remote root shell.",
        "severity": "Critical"
    },
}


def check_vulnerabilities(banner):
    matches = []

    for version_string, info in VULN_DB.items():
        if version_string in banner:
            matches.append({
                "matched_version": version_string,
                "cve": info["cve"],
                "description": info["description"],
                "severity": info["severity"]
            })

    return matches