#!/usr/bin/env python3

import json
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
optional = [row[:] for row in required]  # deep copy

for k, v in j["fields"].items():
    restrictions = []
    if v.get("values"):
        restrictions.append(
            "• Choices: " + ", ".join([f"`{val}`" for val in v["values"]])
        )
    if v.get("default") is not None:
        restrictions.append("• Default: " + f"`{v['default']}`")
    if v.get("restrictions"):
        partitions = [restriction.partition(":") for restriction in v["restrictions"]]
        restrictions.extend(
            [
                "• " + ":".join([condition, f"`{value}`"])
                for condition, _, value in partitions
            ]
        )

    row = [f"`{k}`", f"`{v['type']}`", v["description"], "\n".join(restrictions)]
    if v["required"]:
        required.append(row)
    else:
        optional.append(row)

if args.title:
    print("#" * args.depth + " " + args.title)
    print()

print("#" * args.depth + "# Required\n")
print("".join(["| " + " | ".join(row) + " |\n" for row in required]))
print("#" * args.depth + "# Optional\n")
print("".join(["| " + " | ".join(row) + " |\n" for row in optional]))
