# -*- coding: utf-8 -*-
import logging
import math
import random
import time
from collections.abc import Iterator, Sized

import apistar
import requests

logger = logging.getLogger(__name__)


class ResponsePaginator(Sized, Iterator):
    """
    A lazy generator to handle paginated Arkindex API endpoints.
    Does not perform any requests to the API until it is required.
    """

    def __init__(self, client, *request_args, **request_kwargs):
        r"""
        :param client apistar.Client: An API client to use to perform requests for each page.
        :param \*request_args: Arguments to send to :meth:`apistar.Client.request`.
        :param \**request_kwargs: Keyword arguments to send to :meth:`apistar.Client.request`.
        """
        self.client = client
        """The APIStar client used to perform requests on each page."""

        self.data = {}
        """Stored data from the last performed request."""

        self.results = []
        """Stored results from the last performed request."""

        self.request_args = request_args
        """Arguments to send to :meth:`apistar.Client.request` with each request."""

        self.request_kwargs = request_kwargs
        """
        Keyword arguments to send to :meth:`apistar.Client.request` with each request.
        """

        self.current_page = self.request_kwargs.get("page", 0)
        """The current page number. 0 or ``page`` from :meth:`apistar.Client.request` keyword arguments
        if no pages have been requested."""

        self._started = False
        """Has any request been sent"""

        self.retries = request_kwargs.pop("retries", 5)
        assert (
            isinstance(self.retries, int) and self.retries > 0
        ), "retries must be a positive integer"
        """Max number of retries per API request"""

        # Add initial page to pages
        self.initial_page = self.current_page or 1
        self.pages = {self.initial_page: self.retries}

        # Store missing page indexes
        self.missing = set()
        self.allow_missing_data = request_kwargs.pop("allow_missing_data", False)
        assert isinstance(
            self.allow_missing_data, bool
        ), "allow_missing_data must be a boolean"

    def _fetch_page(self):
        # Filter out pages with no retries
        # Transform as a list of tuples for simpler output
        remaining = sorted([(m, v) for m, v in self.pages.items() if v > 0])

        # No remaining pages, end of iteration
        if not remaining:
            raise StopIteration

        # Get next page to load
        page, retry = remaining[0]
        self.request_kwargs["page"] = page

        try:
            logger.info(
                f"Loading page {page} on try {self.retries - retry + 1}/{self.retries} - remains {len(self.pages)} pages to load."
            )
            self.data = self.client.request(*self.request_args, **self.request_kwargs)
            self.results = self.data.get("results", [])
            self.current_page = page
            self._started = True

            if page == self.initial_page and self.results:
                # On first successful page load, populate pages to load
                nb_pages = math.ceil(self.data["count"] / len(self.results))
                self.pages = {
                    i: self.retries for i in range(self.initial_page + 1, nb_pages + 1)
                }
                if self.pages:
                    logger.info(f"Pagination will load {nb_pages} pages.")
            else:
                # Mark page as loaded on other pages
                del self.pages[page]

            # Stop happy path here, we don't need to process errors
            return self.data

        except apistar.exceptions.ErrorResponse as e:
            logger.warning(f"API Error {e.status_code} on pagination: {e.content}")

            # Decrement pages counter
            self.pages[page] -= 1

            # Sleep a bit (less than a second)
            time.sleep(random.random())

        except requests.exceptions.ConnectionError as e:
            logger.error(f"Server connection error, will retry in a few seconds: {e}")

            # Decrement pages counter
            self.pages[page] -= 1

            # Sleep a few seconds
            time.sleep(random.randint(1, 10))

        # Detect and store references to missing pages
        # when a page has no retries left
        if self.pages[page] <= 0:
            logger.warning(f"No more retries left for page {page}")
            if self.allow_missing_data:
                self.missing.add(page)
            else:
                raise Exception("Stopping pagination as data will be incomplete")

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.results) < 1:
            if self.data and self.data.get("next") is None:
                raise StopIteration

            # Continuously try to fetch a page until there are some retries left
            # This will still yield as soon as some data is fetched
            while self._fetch_page() is None:
                pass

        # Even after fetching a new page, if the new page is empty, just fail
        if len(self.results) < 1:
            raise StopIteration

        return self.results.pop(0)

    def __len__(self):
        # Handle calls to len when no requests have been made yet
        if not self.data and self.current_page < 1:
            self._fetch_page()
        elif not self._started:
            self._fetch_page()
        return self.data["count"]

    def __repr__(self):
        return "<{} via {!r}: {!r} {!r}>".format(
            self.__class__.__name__,
            self.client,
            self.request_args,
            self.request_kwargs,
        )
