const initialState = {
    recommendations: []
}
  
const recommendations = (state=initialState, action) => {
    switch(action.type) {
        case 'RECOMMENDATION':
            return {
                ...state,
                location: action.data
            }
        case 'CLEAR':
            return {
                recommendations: [],
            }
        default:
            return state;
    }
}

export default recommendations;
  