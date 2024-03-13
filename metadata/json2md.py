#!/usr/bin/env python3

import json
import copy
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("json_filename", type=str)
parser.add_argument("-t", "--title", type=str)
parser.add_argument("-a", "--analysis", action="store_true")
parser.add_argument(
    "-d", "--depth", type=int, default=1, help="header depth of title (default=1)"
)
args = parser.parse_args()


with open(args.json_filename, "r") as f:
    j = json.load(f)


def uploader_spec(
    fields,
    required,
    optional,
    at_least_one_required,
    at_least_one_required_headers,
    prefix="",
):

    for k, v in fields.items():
        restrictions = []
        at_least_one_required_keys = []

        if v.get("default") is not None:
            restrictions.append("• Default: " + f"`{v['default']}`")

        if v.get("restrictions"):
            for restriction in v["restrictions"]:
                condition, _, value = restriction.partition(": ")

                if "at least one required" in condition.lower():
                    at_least_one_required_keys.append(
                        tuple(
                            sorted(
                                [x.strip() for x in value.strip().split(",")],
                                key=str.lower,
                            )
                        )
                    )
                else:
                    restrictions.append("• " + ": ".join([condition, f"`{value}`"]))

        if v.get("values"):
            restrictions.append(
                "• Choices: " + ", ".join([f"`{val}`" for val in v["values"]])
            )

        row = [
            f"`{prefix}{k}`",
            f"`{v['type']}`",
            v["description"],
            "<br>".join(restrictions),
        ]

        if v["required"]:
            required.append(row)

        elif at_least_one_required_keys:
            for key in at_least_one_required_keys:
                at_least_one_required.setdefault(
                    key, copy.deepcopy(at_least_one_required_headers)
                ).append(row)

        else:
            optional.append(row)

        if v["type"] == "relation":
            uploader_spec(
                v["fields"],
                required,
                optional,
                at_least_one_required,
                at_least_one_required_headers,
                prefix=k + ".",
            )

    return required, at_least_one_required, optional


def analysis_spec(fields, spec, prefix=""):
    for k, v in fields.items():
        restrictions = []

        if v.get("values"):
            restrictions.append(
                "• Choices: " + ", ".join([f"`{val}`" for val in v["values"]])
            )

        row = [
            f"`{prefix}{k}`",
            f"`{v['type']}`",
            v["description"],
            "<br>".join(restrictions),
        ]

        spec.append(row)

        if v["type"] == "relation":
            analysis_spec(v["fields"], spec, prefix=k + ".")

    return spec


if args.title:
    print("#" * args.depth + " " + args.title)
    print()


if not args.analysis:
    required = [
        [
            "Field name" + "&nbsp;" * 40,
            "Data type",
            "Description",
            "Restrictions",
        ],
        ["-----"] * 4,
    ]
    optional = copy.deepcopy(required)
    at_least_one_required = {}
    at_least_one_required_headers = copy.deepcopy(required)

    uploader_spec(
        j["fields"],
        required,
        optional,
        at_least_one_required,
        at_least_one_required_headers,
    )

    print("#" * args.depth + "# Required fields\n")
    print("".join(["| " + " | ".join(row) + " |\n" for row in required]))

    for x, table in at_least_one_required.items():
        print("At least one of the following fields are required:\n")
        print("".join(["| " + " | ".join(row) + " |\n" for row in table]))

    print("#" * args.depth + "# Optional fields\n")
    print("".join(["| " + " | ".join(row) + " |\n" for row in optional]))
else:
    spec = [
        [
            "Field name" + "&nbsp;" * 40,
            "Data type",
            "Description",
            "Restrictions",
        ],
        ["-----"] * 4,
    ]
    analysis_spec(j["fields"], spec)

    print("#" * args.depth + "# Analysis fields\n")
    print("".join(["| " + " | ".join(row) + " |\n" for row in spec]))
