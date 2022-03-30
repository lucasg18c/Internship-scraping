from time import time
from constants import FETCH_INTERVAL
from internships_crowler import fetchInternships


class InternshipComponent:
    def __init__(self) -> None:
        self.internships = []
        self.next_query = time()

    def get_newer(self, than_id: int) -> list:
        self.refresh()

        if not len(self.internships) or self.internships[0]['iid'] <= than_id < 0:
            return []

        send = []

        # Internships list is already reversed
        for i in self.internships:
            if i["iid"] == than_id:
                break

            send.append(i)

        return send

    def get_all(self) -> list:
        self.refresh()
        return self.internships

    def refresh(self) -> None:
        if self.next_query <= time():
            self.internships = fetchInternships(debug=False)
            self.next_query = time() + FETCH_INTERVAL
