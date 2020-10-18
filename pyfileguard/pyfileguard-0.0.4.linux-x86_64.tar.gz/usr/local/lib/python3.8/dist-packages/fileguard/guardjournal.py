
import os

from . largefileguard import LargeFileGuard


class GuardJournal(object):
    
    def __init__(self, fnam=None, debug=False):
        self.debug = debug
        if fnam==None:
            fnam="journal.bim.sum"
        self.fnam = fnam
        self.bim_files = []
        
        try:
            fs = os.stat(self.fnam)
            # if guard summery exists do a rollback
            self.rollback( self._read() )
            #self.close()
            
        except:
            pass
                
    def _print_d(self,*args):
        if self.debug:
            print(self.__class__.__name__,*args)
            
    def _read(self):
        "read journal summary information"
        cont = self.fd.read()
        lines = cont.splitlines()
        #lines = list(filter( lambda x : len(x)>0 and x[0]!="#", lines ))
        bim_files = list(map( lambda x : l.split("\t"), lines ))
        self._print_d( "found", bim_files )
        return bim_files

    def _cleanup(self):        
        self._cleanup_others()
        try:
            self._print_d("remove",self.fnam)
            os.remove(self.fnam)
        except:
            pass
        
    def _cleanup_others(self):
        for fnam, bim_file in self.bim_files:
            try:
                self._print_d("remove",fnam,bim_file)
                os.remove( bim_file )
            except:
                pass
        self.bim_files = []
        
    def rollback(self,bim_files=None,debug=True):
        if bim_files==None:
            bim_files, self.bim_files = self.bim_files, []
        for fnam, bim_file in bim_files:
            try:
                with LargeFileGuard(fnam,"r+",
                                    bimfile = bim_file,
                                    keep_bim=False,
                                    debug=debug,                                   
                                   ) as f:
                   self._print_d("rollback",fnam,bim_file)
                   f.rollback()
            except Exception as ex:
                self._print_d( ex )
               
        self._cleanup()
        
    def add(self, fileguard):
        self._print_d( "adding", fileguard.fnam )
        self.bim_files.append( (fileguard.fnam, fileguard.bimfile ) )
        with open(self.fnam,"w+") as fd:
            for fnam, bimfile in self.bim_files:
                fd.write(fileguard.fnam+"\t"+fileguard.bimfile+"\n")
            # write all buffers
            fd.flush()
            os.fsync(fd.fileno())
                   
    def close(self):
        self._cleanup()
        
    def commit(self):
        self._cleanup()

    def __enter__(self):
        self._print_d("__enter__")
        return self
    
    def __exit__( self, exception_type, exception_value, traceback ):
        self._print_d("__exit__", exception_type, exception_value, traceback)
        if exception_type is not None:
            self.rollback()
        self.close()

