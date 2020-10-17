"""
Miva Merchant

This file and the source codes contained herein are the property of
Miva, Inc.  Use of this file is restricted to the specific terms and
conditions in the License Agreement associated with this file.  Distribution
of this file or portions of this file for uses not covered by the License
Agreement is not allowed without a written agreement signed by an officer of
Miva, Inc.

Copyright 1998-2020 Miva, Inc.  All rights reserved.
https://www.miva.com

Prefix         : MMT-COMMAND-BRANCH-
Next Error Code: 5
"""

import abc

import merchantapi.request
import merchantapi.model

from mmt.exceptions import Error
from mmt.commands import Command


class BranchRequestCommand( Command, abc.ABC ):
	def __init__( self, *args, **kwargs ):
		super().__init__( *args, **kwargs )

		self._request_client = None

	def validate( self ):
		if self.configmanager.credential_lookup( self.args.get( 'credential_key' ) ) is None:
			raise Error( 'MMT-COMMAND-BRANCH-00001', f'Credential key \'{self.args.get( "credential_key" )}\' does not exist' )

		if self.args.get( 'store_code' ) is None or len( self.args.get( 'store_code' ) ) == 0:
			raise Error( 'MMT-COMMAND-BRANCH-00002', 'A Store Code is required' )

	def initialize( self ):
		self._request_client = self.build_request_client( self.args.get( 'credential_key' ) )
		self._request_client.set_option( 'default_store_code', self.args.get( 'store_code' ) )

	@abc.abstractmethod
	def run( self ):
		raise NotImplementedError


class BranchListCommand( BranchRequestCommand ):
	def run( self ):
		request = merchantapi.request.BranchListLoadQuery( self._request_client )
		request.set_sort( 'name' )

		response = self.send_request( request )

		for i, branch in enumerate( response.get_branches() ):
			if i > 0:
				print( '' )

			print( f'Branch: {branch.get_name()}' )
			print( f'\tIs Primary: {branch.get_is_primary()}' )
			print( f'\tIs Working: {branch.get_is_working()}' )
			print( f'\tPreview URL: {branch.get_preview_url()}' )


class BranchCreateCommand( BranchRequestCommand ):
	def run( self ):
		parent_branch_id = self._load_branch( self.args.get( 'from' ) ).get_id()

		request = merchantapi.request.BranchCreate( self._request_client )
		request.set_parent_branch_id( parent_branch_id )
		request.set_name( self.args.get( 'name' ) )
		request.set_color( self.args.get( 'color' ) )

		response	= self.send_request( request )
		branch		= response.get_branch()

		print( f'Branch \'{branch.get_name()}\' created' )

	def _load_branch( self, branch_name: str ) -> merchantapi.model.Branch:
		request	= merchantapi.request.BranchListLoadQuery( self._request_client )
		request.set_count( 1 )
		request.set_filters( request.filter_expression().equal( 'name', branch_name ) )

		response = self.send_request( request )

		if len( response.get_branches() ) != 1:
			raise Error( 'MMT-COMMAND-BRANCH-00003', f'Branch \'{branch_name}\' does not exist' )

		return response.get_branches()[ 0 ]


class BranchDeleteCommand( BranchRequestCommand ):
	def run( self ):
		request = merchantapi.request.BranchDelete()
		request.set_branch_name( self.args.get( 'name' ) )
		request.set_client( self._request_client )

		self.send_request( request )

		print( f'Branch \'{self.args.get( "name" )}\' deleted' )
