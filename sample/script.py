from . import tasks


def run_workflow():
    result = tasks.do_work.apply_async()
    print(result.get())
