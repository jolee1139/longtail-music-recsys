"""Load Last.fm 360K and build the user x artist interaction matrix.

TODO:
- load_raw(path) -> DataFrame with columns user_id, artist_id, artist_name, plays
- filter_sparse(df, min_users_per_artist, min_artists_per_user)
- to_sparse_matrix(df) -> (scipy.sparse.csr_matrix, user_index, artist_index)
- train_test_split_by_user(matrix, test_frac, seed)
"""
