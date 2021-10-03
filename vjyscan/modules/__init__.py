from vjyscan.modules.fingerprints import commons


def handle_modules(client, target):
    cms = commons.do_finger(client, target)
    if not cms:
        pass  # we have to do all enumeration here
    else:
        pass  # Convert value to modules to call here
