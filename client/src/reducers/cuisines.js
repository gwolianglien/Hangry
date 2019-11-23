import {
    ADD_CUISINE,
    REMOVE_CUISINE,
    CLEAR
} from '../actions/constants';

const initialState = [];

export default (state=initialState, action) => {
    const curr = action.payload;
    const idx = state.indexOf(curr);
    switch (action.type) {
        case ADD_CUISINE:
            if (idx === -1) {
                return [...state, curr];
            }
            return state;
        case REMOVE_CUISINE:
            if (idx !== -1) {
                state.splice(idx, 1);
                return state;
            }
            return state;
        case CLEAR:
            return [];
        default:
            return state;
    }
}