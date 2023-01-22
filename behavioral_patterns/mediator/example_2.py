class Job:
    def __init__(self, name):
        self.name = name

class JobMediator:
    def __init__(self):
        self.jobs = []
        self.workers = []

    def add_job(self, job):
        self.jobs.append(job)

    def add_worker(self, worker):
        self.workers.append(worker)

    def dispatch_job(self):
        if self.jobs and self.workers:
            job = self.jobs.pop()
            worker = self.workers.pop()
            worker.do_job(job)

class Worker:
    def __init__(self, mediator):
        self.mediator = mediator

    def do_job(self, job):
        print(f"Worker is working on {job.name}")
        self.mediator.dispatch_job()

def main():
    # Usage
    mediator = JobMediator()
    worker1 = Worker(mediator)
    worker2 = Worker(mediator)

    mediator.add_job(Job("Job 1"))
    mediator.add_job(Job("Job 2"))
    mediator.add_job(Job("Job 3"))

    mediator.add_worker(worker1)
    mediator.add_worker(worker2)

    mediator.dispatch_job()
    # Output: "Worker is working on Job 1"
    #         "Worker is working on Job 2"
    #         "Worker is working on Job 3"


if __name__ == '__main__':
    main()
