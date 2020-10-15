class ListMarketsForSignal:
    def list_markets_for_signal(self, signal_id: int):
        request_params = {
            'method': 'get',
            'path': f'/api/signals/{signal_id}/markets'
        }

        response = self.request(**request_params)

        return response