"""
lock:
  # XXX Pipfile.lock
  # .tool-versions
  runtime:
    digest:
  spec:
    digest:
  repositories:
     - name:
       digest:
  artifacts:
    - name:
      instance:
      digest:
      changeId:
  ensembles:
    name: # e.g. localhost
      uri:
      changeId:
"""


def saveLock(task, lock):
    instance = task.target
    artifact = instance.artifacts.get("image")
    if artifact:
        name = task.outputs.get("image_path")
        docker_container = task.outputs.get("docker_container")
        if docker_container:
            digest = docker_container["Image"]
            lock.artifacts[instance.name]["image"] = dict(
                name=name, digest=digest, changeId=task.changeId
            )
