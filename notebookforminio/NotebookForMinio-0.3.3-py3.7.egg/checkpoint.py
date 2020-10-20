from NoteBookForMinio.manager import MinioManagerMixin
from notebook.services.contents.checkpoints import Checkpoints, GenericCheckpointsMixin


class MinioCheckpoints(MinioManagerMixin,
                          GenericCheckpointsMixin,
                          Checkpoints):
    def create_file_checkpoint(self, content, format, path):pass
    def create_notebook_checkpoint(self, nb, path):pass
    def get_file_checkpoint(self, checkpoint_id, path):pass
    def get_notebook_checkpoint(self, checkpoint_id, path):pass
    def delete_checkpoint(self, checkpoint_id, path):pass
    def list_checkpoints(self, path):pass
    def rename_checkpoint(self, checkpoint_id, old_path, new_path):pass
    def rename_all_checkpoints(self,old_path, new_path):pass
    def delete_all_checkpoints(self,path):pass