from builtins import str
from builtins import object
import logging
import copy
from elasticsearch import Elasticsearch


class BmajIndex(object):
    """
    ElasticSearch indexation and search
    """

    """
    ElasticSearch server
    """
    es = None

    """
    Index name
    """
    index = 'biomaj'

    """
    Do indexing
    """
    do_index = False

    """
    Skip if failure (tests)
    """
    skip_if_failure = False

    @staticmethod
    def load(hosts=None, index='biomaj', do_index=True):
        """
        Initialize index

        :param hosts: List of elastic search nodes to connect to
        :type hosts: list
        :param do_index: index data or not
        :type do_index: bool
        """
        if hosts is None:
            hosts = ['localhost']
        if not do_index:
            return
        BmajIndex.index = index
        BmajIndex.do_index = do_index
        if BmajIndex.es is None:
            BmajIndex.es = Elasticsearch(hosts)

            mapping = {
                "mappings": {
                    "production": {
                        "date_detection": False
                    },
                    "releasestats": {
                        "date_detection": False,
                    }
                }
            }
            try:
                if not BmajIndex.es.indices.exists(index=BmajIndex.index):
                    BmajIndex.es.indices.create(index=BmajIndex.index, body=mapping)
            except Exception as e:
                logging.error('ElasticSearch connection error, check server is running and configuration: ' + str(e))

    @staticmethod
    def _bulk_delete(query, flush=True):
        try:
            page = BmajIndex.es.search(
                index=BmajIndex.index,
                doc_type='production',
                search_type="query_then_fetch",
                size=1000,
                body={
                    'query': {
                        'match': {
                            'bank': query['bank']
                        }
                    }
                })

            if page is None:
                return
            bulk_delete = ''
            for del_hit in page['hits']['hits']:
                if ('release' in query and query['release'] == del_hit['_source']['release']) or 'release' not in query:
                    bulk_delete += "{ \"delete\" : {\"_index\":\"" + BmajIndex.index + "\",\"_type\":\"production\", \"_id\" : \"" + del_hit['_id'] + "\" } }\n"
            if bulk_delete:
                BmajIndex.es.bulk(body=bulk_delete)
                if flush:
                    BmajIndex.es.indices.flush(index=BmajIndex.index, force=True)
        except Exception as e:
            if BmajIndex.skip_if_failure:
                BmajIndex.do_index = False
            else:
                logging.error('Failed to delete bank index: ' + str(e))

    @staticmethod
    def delete_all_bank(bank_name):
        """
        Delete complete index for a bank
        """
        if not BmajIndex.do_index:
            return
        BmajIndex._bulk_delete({"bank": bank_name}, True)

    @staticmethod
    def remove(bank_name, release):
        """
        Remove a production release

        :param bank_name: Name of the bank
        :type bank_name: str
        :param release: production release
        :type release: str
        """
        if not BmajIndex.do_index:
            return
        BmajIndex._bulk_delete({"release": release, "bank": bank_name})
        """
        try:
            query = {
              "query" : {
                "term" : {"release" : release, "bank": bank_name}
                }
              }
            BmajIndex.es.delete_by_query(index=BmajIndex.index, body=query)
        except Exception as e:
            logging.error('Index:Remove:'+bank_name+'_'+str(release)+':Exception:'+str(e))
            if BmajIndex.skip_if_failure:
                BmajIndex.do_index = False
        """

    @staticmethod
    def search(query):
        if not BmajIndex.do_index:
            return None
        res = BmajIndex.es.search(index=BmajIndex.index,
                                  doc_type='production',
                                  search_type="query_then_fetch",
                                  body=query)
        return res['hits']['hits']

    @staticmethod
    def searchq(query, size=1000):
        """
        Lucene syntax search

        :param query: Lucene search string
        :type query: str
        :param size: number of results
        :type size: int
        :return: list of matches
        """
        if not BmajIndex.do_index:
            return None
        res = BmajIndex.es.search(index=BmajIndex.index, doc_type='production', q=query, size=size)
        return res['hits']['hits']

    @staticmethod
    def add_stat(stat_id, stat):
        """
        Add some statistics, must contain release and bank properties.
        """
        if not BmajIndex.do_index:
            return
        if stat['release'] is None or stat['bank'] is None:
            return False
        try:
            BmajIndex.es.index(index=BmajIndex.index, doc_type='releasestats', id=stat_id, body=stat)
        except Exception:
            if BmajIndex.skip_if_failure:
                BmajIndex.do_index = False
            else:
                return False
        return True

    @staticmethod
    def add(bank_name, prod, flush=False):
        """
        Index a production release

        :param bank_name: Name of the bank
        :type bank_name: str
        :param prod: session release object
        :type prod: dict
        :param flush: Force flushing
        :type flush: bool
        """
        if not BmajIndex.do_index:
            return
        obj = copy.deepcopy(prod)
        if obj['release'] is None:
            return
        obj['bank'] = bank_name
        formats = obj['formats']
        try:
            for fkey, fvalue in formats.items():
                for elt in fvalue:
                    elt['format'] = fkey
                    elt['bank'] = bank_name
                    elt['release'] = obj['release']
                    if 'status' in obj:
                        elt['status'] = obj['status']
                    BmajIndex.es.index(index=BmajIndex.index, doc_type='production', body=elt)
            if flush:
                BmajIndex.es.indices.flush(index=BmajIndex.index, force=True)
        except Exception as e:
            logging.error('Index:Add:' + bank_name + '_' + str(obj['release']) + ':Exception:' + str(e))
            if BmajIndex.skip_if_failure:
                BmajIndex.do_index = False
