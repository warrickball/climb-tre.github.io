#!/usr/bin/env python3

import json
import copy
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("json_filename", type=str)
parser.add_argument("-t", "--title", type=str)
parser.add_argument(
    "-d", "--depth", type=int, default=1, help="header depth of title (default=1)"
)
args = parser.parse_args()


with open(args.json_filename, "r") as f:
    j = json.load(f)

required = [
    ["Field name", "Data type", "Description", "Restrictions"],
    ["-----"] * 4,
]
optional = copy.deepcopy(required)
at_least_one_required = {}
at_least_one_required_headers = copy.deepcopy(required)

for k, v in j["fields"].items():
    restrictions = []
    at_least_one_required_keys = []

    if v.get("values"):
        restrictions.append(
            "• Choices: " + ", ".join([f"`{val}`" for val in v["values"]])
        )

    if v.get("default") is not None:
        restrictions.append("• Default: " + f"`{v['default']}`")

    if v.get("restrictions"):
        for restriction in v["restrictions"]:
            condition, _, value = restriction.partition(": ")

            if "at least one required" in condition.lower():
                at_least_one_required_keys.append(
                    tuple(
                        sorted(
                            [x.strip() for x in value.strip().split(",")], key=str.lower
                        )
                    )
                )
            else:
                restrictions.append("• " + ": ".join([condition, f"`{value}`"]))

    row = [f"`{k}`", f"`{v['type']}`", v["description"], "\n".join(restrictions)]

    if v["required"]:
        required.append(row)

    elif at_least_one_required_keys:
        for key in at_least_one_required_keys:
            at_least_one_required.setdefault(
                key, copy.deepcopy(at_least_one_required_headers)
            ).append(row)

    else:
        optional.append(row)

if args.title:
    print("#" * args.depth + " " + args.title)
    print()

print("#" * args.depth + "# Required\n")
print("".join(["| " + " | ".join(row) + " |\n" for row in required]))

for x, table in at_least_one_required.items():
    print("#" * args.depth + "### At least one of the following are required:\n")
    print("".join(["| " + " | ".join(row) + " |\n" for row in table]))

print("#" * args.depth + "# Optional\n")
print("".join(["| " + " | ".join(row) + " |\n" for row in optional]))
