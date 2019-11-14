import sys

from pycvesearch import CVESearch

from conanfile import *name of class*


def search_vulnerability(package_name, package_version):
    cve = CVESearch()
    ret = 0

    print("search vulnerabilities for package: " + package_name + " version: " + package_version)
    resp = cve.search(package_name)

    for entry in resp["data"]:
        vulnerable_product_list = entry["vulnerable_product"]
        vulnerable_configuration_list = entry["vulnerable_configuration"]
        vulnerabilities = set(vulnerable_product_list + vulnerable_configuration_list)

        for product in vulnerabilities:
            product_info = product.split(':')
            product_name = product_info[4]
            product_version = product_info[5]

            if package_name == product_name and package_version == product_version:
                print("found vulnerability: " + entry["summary"])
                ret = 1

    return ret


def main():
    ret = 0

    for package in *name of class*.requires:
        package_info = package.split("/")
        package_name = package_info[0]
        package_version = package_info[1].split("@")[0]

        if search_vulnerability(package_name, package_version) != 0:
            ret = 1

    sys.exit(ret)


if __name__ == '__main__':
    main()
