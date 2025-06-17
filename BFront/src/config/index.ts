export const BASE_URL = 'http://localhost:8000'

export const API_URL = `${BASE_URL}/api`

export const GAMES_URL = `${API_URL}/games`

export const GAMES_LIST_URL = `${GAMES_URL}/list/`

export const GAME_SEARCH_URL = `${GAMES_URL}/search/`

export const GET_GAME_BY_ID_URL = `${GAMES_URL}/` // req params: id

export const GET_CAT_BY_ID = `${GAMES_URL}/cat/` // req params: id

export const GET_LEN_GAMES = `${GAMES_URL}/len/`

export const POST_LIKE = `${GAMES_URL}/like/`

export const POST_DISLIKE = `${GAMES_URL}/dislike/`

export const GET_CATS = `${GAMES_URL}/cats/`