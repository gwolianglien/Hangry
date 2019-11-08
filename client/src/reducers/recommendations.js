
const initialState = {
    recommendations: []
}

export default (currentState=initialState, action) => {
    switch(action.type) {
        case 'RECOMMENDATION':
            return {
                ...currentState,
                location: action.data
            }
        case 'CLEAR':
            return {
                recommendations: [],
            }
        default:
            return currentState;
    }
}
