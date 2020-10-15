import json
from collections import Counter
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Dict, Iterator, List
from zipfile import ZipFile, ZIP_BZIP2

from .kubuntypes import (KubunLink, KubunSelector, KubunString, KubunType,
						 Schema, TypeName)
from .misc import KubunIdentifier, KubunJSONEncoder


class KubunNode():
	def __init__(self, title: str, coverImages: List[str] = []):
		self.title = title
		self.coverImages = coverImages
		self.props: Dict[KubunIdentifier, KubunType] = {}

	def toDict(self):
		return {
			'title': self.title,
			'coverImages': self.coverImages,
			** {
				i.toDict(): v for i, v in self.props.items()
			}
		}

	def __repr__(self):
		return f"<KubunNode: { self.title }, Props: { ', '.join(sorted(map(str, self.props.keys()))) }>"


class Confector():
	def __init__(self, archivePath: Path):
		self.schemata: Dict[str, Schema] = {}
		self.archivePath = archivePath
		self.archiveZip = ZipFile(archivePath, 'w', ZIP_BZIP2)
		self.tempfiles: Dict[str, NamedTemporaryFile] = {}
		self.nodeCounter: Counter = Counter()
		self.schemataChecked = False

	def isReady(self, ignoreSchemataCheck=False):
		assert self.archiveZip is not None, "Confector is finalized already."
		if not ignoreSchemataCheck:
			assert self.schemataChecked, "Please call confector.checkSchemata() after adding all of your schemata."

	def registerSchema(self, tagName: str, schema: Schema):
		self.isReady(True)

		assert type(schema) is Schema
		self.schemata.update({tagName: schema})
		self.archiveZip.writestr(f"schemata/{tagName}.json", json.dumps(schema, cls=KubunJSONEncoder))
		self.schemataChecked = False

	def checkSchemata(self):
		# Collect outgoing links
		linkProps: Dict[KubunIdentifier, TypeName] = {}
		linkToTargetTypeName = {}

		for s in self.schemata.values():
			outboundLinks = filter(lambda p: p.isOutboundLink(), s.main.collect())
			linkProps.update({
				p.ident: (p.config['target']['target_ident'], p.config['target']['target_tag'])
				for p in outboundLinks
			})

		# Gather expected target-types
		for propertyIdent, (targetIdent, targetTag) in linkProps.items():
			errorMessage = f"Property {propertyIdent} targets invalid foreign property {targetIdent} in tag: {targetTag}"
			assert targetTag in self.schemata, errorMessage
			s = self.schemata[targetTag]
			if targetIdent == 'title':
				linkToTargetTypeName.update({propertyIdent: KubunString})
			else:
				targetProp = s.getProperty(targetIdent)
				assert targetProp is not None, errorMessage
				linkToTargetTypeName.update({propertyIdent: targetProp.kubunType})

		self.linkToTargetTypeName = linkToTargetTypeName
		self.schemataChecked = True

	def addNode(self, tagName: str, node: KubunNode):
		self.isReady()

		if tagName not in self.tempfiles.keys():
			tempfile = NamedTemporaryFile(mode='w+')
			self.tempfiles.update({tagName: tempfile})

		self.nodeCounter.update({tagName: 1})
		self.tempfiles[tagName].write(
			json.dumps(node, cls=KubunJSONEncoder) + "\n")

	def addNodes(self, tagName: str, nodes: Iterator[KubunNode]):
		self.isReady()

		for node in nodes:
			self.addNode(tagName, node)

	def addMultiplePropertiesToNode(self, tagName: str, node: KubunNode, values: Dict[str, any], noNone: bool = False):
		self.isReady()

		for propertyIdent, value in values.items():
			self.addPropertyToNode(tagName, propertyIdent, node, value, noNone)

	def addPropertyToNode(self, tagName: str, propertyIdent: str, node: KubunNode, value: any, noNone: bool = False):
		self.isReady()

		if value is None:
			if noNone:
				raise Exception(f"Got None as value but noNone is set: Property: {propertyIdent}")
			else:
				return

		schema = self.schemata.get(tagName)
		assert schema is not None, f"Unknown Tag: { tagName }"

		propertyIdentCasted = KubunIdentifier(propertyIdent)
		prop = schema.getProperty(propertyIdentCasted)
		expectedType = prop.kubunType.expectedPropValue()

		try:
			if expectedType is KubunSelector:
				if not type(value) is list:
					value = [value]  # KubunSelectors are lists.
				if len(value) == 0:
					return  # Empty selectors will never be resolved anyway.
				valueCasted = KubunSelector(value, self.linkToTargetTypeName[propertyIdentCasted])
			else:
				if not isinstance(value, expectedType):  # Auto-Cast
					valueCasted = expectedType(value)
				else:
					valueCasted = value
		except ValueError:
			raise Exception(f"Auto-Casting failed: PropertyIdent: { propertyIdent }, Value: { value }, Casting to: { expectedType }")

		assert type(valueCasted) is expectedType, f"Value has incorrect Type: { type(valueCasted) }; PropertyIdent: { propertyIdent }, Value: { value }, Should be: { expectedType }"
		assert propertyIdentCasted not in node.props.keys(), f"Nodes can't have duplicate Properties: PropertyIdent: { propertyIdent }"
		node.props.update({propertyIdentCasted: valueCasted})

	def finalize(self, metaData: dict):
		self.isReady()

		print("Confector is creating your archive...")
		print("-" * 25)

		for tagName, count in self.nodeCounter.most_common():
			print(f"{ tagName.ljust(40) } -> wrote { count } nodes.")

		for tagName, datafile in self.tempfiles.items():
			datafile.seek(0)
			self.archiveZip.writestr(f"data/{tagName}.json", datafile.read())
			datafile.close()

		self.archiveZip.writestr("meta.json", json.dumps(metaData))  # TODO: Attribution as class

		print("\nArchive Contents:")
		self.archiveZip.printdir()
		print("\n")

		self.archiveZip.close()
		self.archiveZip = None

		print(f"Confector done. Archive at {self.archivePath}")
