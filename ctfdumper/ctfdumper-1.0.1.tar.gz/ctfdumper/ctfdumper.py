import requests, queue, re, urllib.parse, json, threading, tqdm, time
import pandas as pd

class CTFDumper:

    def __init__(self, url, threads=10):
        self.url = url
        self.threads_num = threads
        self.tasks = queue.Queue()
        self.results_submissions = queue.Queue()
        self.results_users = queue.Queue()

    def _worker(self):
        def get_submission_data(submission_task):
            page_num = submission_task['page_num']
            r = self._s.get(self.url + '/api/v1/submissions?page={}'.format(page_num))
            try:
                results = json.loads(r.text)
            except:
                return
            data = results['data']

            parsed_submissions = []
            for entry_data in data:
                parsed_submissions.append({
                    'user_id' : entry_data['user_id'],
                    'challenge_name' : entry_data['challenge']['name'],
                    'challenge_category' : entry_data['challenge']['category'],
                    'type' : entry_data['type'],
                    'provided': entry_data['provided'],
                    'date' : entry_data['date']
                })

            self.results_submissions.put((parsed_submissions))

        def get_username(userid_task):
            user_page = userid_task['user_page']
            r = self._s.get(self.url + '/api/v1/users?page={}'.format(user_page))
            try:
                results = json.loads(r.text)
            except:
                return

            for user_data in results['data']:
                self.results_users.put((user_data['id'], user_data['name']))

        while True:
            task = self.tasks.get()
            if task == None:
                break
            if "page_num" in task:
                get_submission_data(task)
            else:
                get_username(task)

            self.tasks.task_done()

    def get_submissions(self, username, password):
        self._s = requests.session()
        r = self._s.get(self.url + "/login")
        nonce = re.search(r'<input id="nonce" name="nonce" type="hidden" value="(.*?)">', r.text).group(1)

        payload = {
            "name" : username,
            "password" : password,
            "_submit" : "Submit",
            "nonce" : nonce
        }

        r = self._s.post(self.url + "/login",
                    params={'next' : '/challenges'},
                    data=payload)

        if not r.ok or urllib.parse.urlparse(r.url).path != '/challenges':
            raise Exception("Could not login to the CTFD site: {}".format(self.url))

        r = self._s.get(self.url + "/api/v1/submissions")
        if r.status_code != 200:
            raise Exception("Could not access submission api endpoint! You probably do not have access.")

        total_pages = json.loads(r.text)['meta']['pagination']['pages']

        r = self._s.get(self.url + "/api/v1/users")
        if r.status_code != 200:
            raise Exception("Could not access submission users endpoint! You probably do not have access.")

        total_user_pages = json.loads(r.text)['meta']['pagination']['pages']

        total_tasks = total_pages + total_user_pages
        prog_bar = tqdm.tqdm(total=total_tasks)

        threads = [threading.Thread(target=self._worker, daemon=True) for _i in range(self.threads_num)]
        [t.start() for t in threads]

        for page_num in range(1, total_pages+1):
            self.tasks.put(({'page_num' : page_num}))

        for user_page in range(1, total_user_pages+1):
            self.tasks.put(({'user_page' : user_page}))

        prev_tasks_done = total_tasks

        while True:
            curr_tasks_left = self.tasks.qsize()
            prog_bar.update(prev_tasks_done - curr_tasks_left)
            prog_bar.refresh()
            if curr_tasks_left == 0:
                break
            prev_tasks_done = curr_tasks_left
            time.sleep(0.0001)

        self.tasks.join()

        [self.tasks.put((None)) for _t in threads]
        [t.join() for t in threads]

        user_map = {}

        while self.results_users.qsize() > 0:
            id_to_name = self.results_users.get()
            user_map[id_to_name[0]] = id_to_name[1]
            self.results_users.task_done()

        if self.results_submissions.qsize() <= 0:
            [t.join() for t in threads]
            return None

        pre_submission_list = self.results_submissions.get()
        post_submission_list = []

        for submission_data in pre_submission_list:
            try:
                submission_data['username'] = user_map[submission_data['user_id']]
                post_submission_list.append(submission_data)
            except:
                pass

        result_df = pd.DataFrame(post_submission_list)
        self.results_submissions.task_done()

        while self.results_submissions.qsize() > 0:
            pre_submission_list = self.results_submissions.get()
            post_submission_list = []

            for submission_data in pre_submission_list:
                try:
                    submission_data['username'] = user_map[submission_data['user_id']]
                    post_submission_list.append(submission_data)
                except:
                    pass

            df = pd.DataFrame(post_submission_list)
            result_df = result_df.append(df, ignore_index=True)
            self.results_submissions.task_done()

        return result_df
