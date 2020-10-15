"""Combine multiple popular python security tools and generate reports or output
into different formats
"""
from __future__ import annotations
import argparse
from typing import Any
from sys import exit as sysexit, stdout
from simplesecurity.types import Finding

stdout.reconfigure(encoding="utf-8")

import simplesecurity.formatter as formatter
import simplesecurity.plugins as plugins
import simplesecurity.filter as secfilter

FORMAT_HELP = "Output format. One of ansi, json, markdown, csv. default=ansi"
PLUGIN_HELP = "Plugin to use. One of bandit, safety, dodgy, dlint, all, default=all"


def runAllPlugins(pluginMap: dict[str, Any], severity: int,
confidence: int) -> list[Finding]:
	"""Run each plugin

	Args:
		pluginMap (dict[str, Any]): the plugin map
		severity (int): the minimum severity to report on
		confidence (int): the minimum confidence to report on

	Returns:
		list[Finding]: list of findings
	"""
	findings: list[Finding] = []
	for plugin in pluginMap:
		if (pluginMap[plugin]["max_severity"] >= severity and
		pluginMap[plugin]["max_confidence"] >= confidence):
			try:
				findings.extend(pluginMap[plugin]["func"]())
			except RuntimeError as error:
				print(error)
	return findings


def cli():
	""" cli entry point """
	# yapf: disable
	parser = argparse.ArgumentParser(description=__doc__ ,
	formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("--format", "-f", help=FORMAT_HELP)
	parser.add_argument("--plugin", "-p", help=PLUGIN_HELP)
	parser.add_argument("--file", "-o", help="Filename to write to (omit for stdout)")
	parser.add_argument("--level", "-l", help="Minimum level/ severity to show", type=int, default=0)
	parser.add_argument("--confidence", "-c", help="Minimum confidence to show", type=int, default=0)
	parser.add_argument("--no-colour", "-z", help="No ANSI colours", action="store_true")
	parser.add_argument("--high-contrast", "-Z", help="High contrast colours", action="store_true")
	# yapf: enable
	args = parser.parse_args()
	# File
	filename = stdout if args.file is None else open(args.file, "w",
	encoding="utf-8")
	# Colour Mode
	colourMode = 1
	if args.no_colour:
		colourMode = 0
	if args.high_contrast:
		colourMode = 2
	# Format
	formatMap = {
	"json": formatter.json, "markdown": formatter.markdown, "csv": formatter.csv,
	"ansi": formatter.ansi}
	if args.format is None:
		formatt = formatter.ansi
	elif args.format in formatMap:
		formatt = formatMap[args.format]
	else:
		print(FORMAT_HELP)
		sysexit(1)

	# Plugin
	pluginMap: dict[str, Any] = {
	"bandit": {"func": plugins.bandit, "max_severity": 3, "max_confidence": 3},
	"safety": {"func": plugins.safety, "max_severity": 2, "max_confidence": 3},
	"dodgy": {"func": plugins.dodgy, "max_severity": 2, "max_confidence": 2},
	"dlint": {"func": plugins.dlint, "max_severity": 2, "max_confidence": 2}
	} # yapf: disable
	if args.plugin is None or args.plugin == "all" or args.plugin in pluginMap:
		findings = []
		if args.plugin is None or args.plugin == "all":
			findings = runAllPlugins(pluginMap, args.level, args.confidence)
		elif (pluginMap[args.plugin]["max_severity"] >= args.level and
		pluginMap[args.plugin]["max_confidence"] >= args.confidence):
			findings = pluginMap[args.plugin]["func"]()
		print(formatt(secfilter.filterSeverityAndConfidence(
			secfilter.deduplicate(findings), args.level, args.confidence),
		colourMode=colourMode), file=filename) # yapf: disable
	else:
		print(PLUGIN_HELP)
		sysexit(1)
