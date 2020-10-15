class GetCategoriesForUniverse:
    def get_categories_for_universe(self, universe_id: int):
        request_params = {
            'method': 'get',
            'path': f'/api/signals/universes/{universe_id}/categories'
        }

        response = self.request(**request_params)

        return response