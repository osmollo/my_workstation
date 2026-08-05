#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import pexpect


def main():
    module = AnsibleModule(
        argument_spec={
            "database": {"type": "str", "required": True},
            "pkcs12_file": {"type": "str", "required": True},
            "nssdb_password": {"type": "str", "required": True, "no_log": True},
            "pkcs12_password": {"type": "str", "required": True, "no_log": True},
        },
        supports_check_mode=True,
    )

    if module.check_mode:
        module.exit_json(changed=True)

    command = [
        "pk12util",
        "-i",
        module.params["pkcs12_file"],
        "-d",
        "sql:" + module.params["database"],
    ]

    process = pexpect.spawn(command[0], command[1:], encoding="utf-8", timeout=30)
    try:
        process.expect("Enter new password:")
        process.sendline(module.params["nssdb_password"])
        process.expect("Re-enter password:")
        process.sendline(module.params["nssdb_password"])
        process.expect("Enter password for PKCS12 file:")
        process.sendline(module.params["pkcs12_password"])
        process.expect(pexpect.EOF)
    except (pexpect.EOF, pexpect.TIMEOUT) as error:
        module.fail_json(
            msg="pk12util import failed before completing its password prompts",
            output=process.before,
            error=str(error),
        )

    process.close()
    if process.exitstatus != 0:
        module.fail_json(
            msg="pk12util import failed",
            output=process.before,
            rc=process.exitstatus,
        )

    module.exit_json(changed=True)


if __name__ == "__main__":
    main()
